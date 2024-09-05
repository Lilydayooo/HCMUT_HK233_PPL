from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC, abstractmethod

from Utils import *
from StaticChecker import *
from StaticError import *

class TUtils:
    @staticmethod
    def boolType(ret):
        return type(ret) is BooleanType
    @staticmethod
    def intType(ret):
        return type(ret) is IntegerType
    @staticmethod
    def floatType(ret):
        return type(ret) is FloatType
    @staticmethod
    def autoType(ret):
        return type(ret) is AutoType
    @staticmethod
    def arrayType(ret):
        return type(ret) is ArrayType
    @staticmethod
    def stringType(ret):
        return type(ret) is StringType
    @staticmethod
    def voidType(ret):
        return type(ret) is VoidType
    @staticmethod
    def noneCheck(ret):
        return type(ret) is type(None)
    @staticmethod
    def sameTypeCheck(type1, type2):
        return type(type1) is type2
    @staticmethod
    def isMergeType(left_type, right_type):
        return FloatType() if FloatType in [type(x) for x in [left_type, right_type]] else IntegerType()
    @staticmethod
    def isRetrieveType(origin, lst=[]):
        if TUtils.arrayType(origin): return ArrayPointerType(origin.typ, lst)
        return origin
    
class OperUtils:
    @staticmethod
    def arithmeticOp(oper):
        return str(oper).lower() in ["+", "-", "*", "/", "%"]
    @staticmethod
    def relationalOp(oper):
        return str(oper).lower() in ["!=", "==", ">", "<", ">=", "<="]
    @staticmethod
    def booleanOp(oper):
        return str(oper).lower() in ["&&", "||"]
    
class CodeGenerator(Utils):
    def __init__(self): self.libName = "io"

    def initial(self):
        return [
            Symbol("readInteger", MType([], IntegerType()), CName(self.libName)),
            Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
            Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
            Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),
            Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName)),
            Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
        ]
    
    def gen(self, ast, directory):
        glo = self.initial()
        gloc = CodeGenVisitor(ast, glo, directory)
        gloc.visit(ast, None)

class MType:
    def __init__(self, partype, rettype, par = [], par_inherit = []):
        self.partype = partype
        self.rettype = rettype
        self.params = par
        self.params_inherit = par_inherit


class Symbol:
    def __init__(self, name, mtype, val=None, inh = None):
        self.name = name
        self.mtype = mtype
        self.value = val
        self.inherit = inh


class SubBody():
    def __init__(self, frame, sym, glob = False, blockStmt = False, inh = False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = glob
        self.isBlockStmt = blockStmt
        self.inherit = inh


class Access():
    def __init__(self, frame, sym, isLeft, isFirst, arr=list()):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.arr = arr

class CType(Type):
    def __init__(self, classname):
        self.cname = classname

    def __str__(self): return "Class({0})".format(str(self.cname))

class ArrayPointerType(Type):
    def __init__(self, classType, lst = []):
        self.eleType = classType
        self.lst = lst

    def __str__(self): return "Class({0}, [{1}])".format(str(self.eleType),",",join(str(element) for element in self.lst))


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emitter = Emitter(self.path + "/MT22Class.j")
        self.array_index_glb = 0

    def genMETHOD(self, declare: FuncDecl, symbol, frm: Frame, glb_vardecl: list or None):
        f_name = declare.name
        f_type = declare.return_type
        inh = declare.inherit
        blk = declare.body

        initial = TUtils.noneCheck(f_type) and f_name == "<init>"
        classInitial = TUtils.noneCheck(f_type) and f_name == "<clinit>"
        main = f_name == "main" and len(declare.params) == 0 and TUtils.voidType(f_type)
        r_type = VoidType() if initial or classInitial else TUtils.isRetrieveType(f_type)
        ifProc = TUtils.voidType(r_type)

        i_type = [ArrayPointerType(StringType())] if main else [TUtils.isRetrieveType(param.typ) for param in declare.params]
        m_type = MTyp(i_type, r_type, list(map(lambda par: [par.name, par.typ, par.inherit], declare.params)), [list(map(lambda par: [par.name, par.typ, par.inherit, None], declare.params))])

        self.emit.printout(self.emit.emitMETHOD(f_name, m_type, not initial, frm))

    def visitProgram(self, ast, c):
        [self.visit(i, c)for i in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
