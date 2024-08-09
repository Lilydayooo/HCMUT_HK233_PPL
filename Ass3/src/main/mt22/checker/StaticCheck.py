from AST import *
from Utils import Utils
from Visitor import *
from StaticError import *
from functools import reduce

class MTyp:
    def __init__(self, ptype, rtype):
        self.ptype = ptype
        self.rtype = rtype

class Sym:
    def __init__(self, name, mtyp, val = None):
        self.name = name
        self.mtyp = mtyp
        self.val = val

class Array(Type):
    def __init__(self, value: int, element: Type) -> None:
        self.value = value
        self.element = element
    def __s__(self):
        return "Array({}, {})".format(str(self.value), str(self.element))
    @staticmethod
    def getDi(array):
        if not TUtils.isArray(array):
            return [array]
        return [array.val, *Array.getDi(array.el)]
    @staticmethod
    def isDiMatch(di1, di2, f):
        if (len(di1) != len(di2)):
            f()
        return True

class TUtils:
    @staticmethod
    def inList(ret, lt):
        return type(ret) in lt
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
    def arrayCheck(ret):
        return type(ret) is Array
    @staticmethod
    def arrayLit(ret):
        return type(ret) is ArrayLit
    @staticmethod
    def arrayCell(ret):
        return type(ret) is ArrayCell
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
        return type(type1) is type(type2)
    @staticmethod
    def interType(name, t, x, y = Variable):
        for envi in x:
            if name in envi and isinstance(envi[name]["kind"], y):
                envi[name]["type"] = t
                return {"type": t}
        return {"type": None}
    
class LookUp:
    @staticmethod
    def lookup(name, lst, f, k = Variable):
        for x in lst:
            if name in x and isinstance(x[name]["kind"], k):
                return x[name]
        return f()
    @staticmethod
    def check(name, dict, f) -> None:
        if name in dict: f()

class StaticChecker(Visitor):
    global_env = [
        Sym("readInteger", MTyp([], IntegerType())),
        Sym("printInteger", MTyp([IntegerType()],VoidType())),
        Sym("readFloat", MTyp([], FloatType())),
        Sym("writeFloat", MTyp([FloatType()], VoidType())),
        Sym("readBoolean", MTyp([], BooleanType())),
        Sym("printBoolean", MTyp([BooleanType()], VoidType())),
        Sym("readString", MTyp([], StringType())),
        Sym("printString", MTyp([StringType()], VoidType())),
        Sym("super", MTyp([[Expr()]], VoidType())),
        Sym("preventDefault", MTyp([], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast
        self.env = [{}]
        self.il_arr_lit = None
        self.f_decl = {"flag": False, "return_type": None, "name": None, "inherit": {"func": None, "super_or_preventDefault": None}, "has_first_stmt_return": False}
        self.loop = {"flag": False, "ast": None}
        self.ifstmt = []
        self.forstmt = []
        self.whilestmt = []
        self.do_whilestmt = []

    def addIfEle(self, el): self.ifstmt.append(el)
    def addForEle(self, el): self.forstmt.append(el)
    def addWhileEle(self, el): self.whilestmt.append(el)
    def addDoWhileEle(self, el): self.do_whilestmt.append(el)

    def removeIfEle(self): self.ifstmt.pop()
    def removeForEle(self): self.forstmt.pop()
    def removeWhileEle(self): self.whilestmt.pop()
    def removeDoWhileEle(self): self.do_whilestmt.pop()

    def getIfSize(self): return len(self.forstmt)
    def getForSize(self): return len(self.forstmt)
    def getWhileSize(self): return len(self.whilestmt)
    def getDoWhileSize(self): return len(self.do_whilestmt)

    def set_loop(self, flag, ast):
        self.loop["flag"] = flag
        self.loop["ast"] = ast

    def reset_loop(self):
        self.loop["flag"] = False
        self.loop["ast"] = None

    def setFunctionDecl(self, flag, return_type, name):
        self.f_decl["flag"] = flag
        self.f_decl["return_type"] = return_type
        self.f_decl["name"] = name

    def resetFunctionDecl(self):
        self.f_decl = {"flag": False, "return_type": None, "name": None, "inherit": {"func": None, "super_or_preventDefault": None}, "has_first_stmt_return": False}

    def checking(self): return self.visit(self.ast, StaticChecker.global_env)

    def raise_(self, err): raise err

    def checkInherit(self, name, o, typ):
        if not TUtils.noneCheck(self.f_decl["inherit"]["func"]) and self.f_decl["inherit"]["super_or_preventDefault"] == "super":
            f = LookUp.lookup(
                self.f_decl["inherit"]["func"]["name"], o, None, Function
            )
            par = self.lookup(
                name, f["params_inherit"], lambda par:par["name"]
            )
            if not TUtils.noneCheck(par) and par["inherit"]:
                self.raise_(Invalid(Parameter(), name))
    
    def visitProgram(self, ast: Program, c):
        print(a)