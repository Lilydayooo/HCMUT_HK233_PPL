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
    
    def visitProgram(self, ctx: Program, c):
        for declares in ctx.decls:
            if type(declares) is FuncDecl:
                return_type = declares.return_type
                param = []
                LookUp.check(declares.name, self.env[0], lambda: self.raise_(
                    Redeclared(Function(), declares.name)
                ))
                for ele in declares.params:
                    for x in param:
                        if x["name"] == ele.name: self.raise_(Redeclared(Parameter(), ele.name))
                    
                    p = {"type": ele.typ, "kind": Variable(), "inherit": ele.inherit, "out": ele.out, "name": ele.name}
                    param.append(p)

                self.env[0][declares.name] = {"type": return_type, "kind": Function(), "params": param}
        
        entry = False
        for declares in ctx.decls:
            if type(declares) is FuncDecl:
                return_type = declares.return_type
                par = declares.params
                if type(declares) is FuncDecl and declares.name == "main" and TUtils.voidType(return_type) and lens(par) == 0:
                    entry = True
            self.visit(declares, (self.env, None))
        
        if not entry: self.raise_(NoEntryPoint())

        return ""
    
    def visitVarDecl(self, ctx: VarDecl, cont):
        (o, _) = cont
        name = ctx.name
        LookUp.check(name, o[0], lambda: self.raise_(Redeclared(Variable(), name)))
        typ = ctx.typ

        if not TUtils.noneCheck(ctx.init):
            if TUtils.arrayLit(ctx.init):
                self.il_arr_lit = {"type": typ, "ast": ctx, "astInit": ctx.init}
            
            if TUtils.arrayType(typ):
                a_dimen = typ.dimensions
                a_type = typ.typ
                self.il_arr_lit = {"type": a_type, "ast": ctx, "astInit": ctx.init}

                if not TUtils.arrayLit(ctx.init) and not TUtils.arrayCell(ctx.init): self.raise_(TypeMismatchInVarDecl(ctx))

                init = self.visit(ctx.init, (o, a_type))
                dimen_lst = Array.getDi(init["type"])
                dimen_lst = dimen_lst[:-1]

                if Array.isDiMatch(a_dimen, dimen_lst, lambda: self.raise_(TypeMismatchInVarDecl(ctx))):
                    o[0][name] = {"type": typ, "kind": Variable(), "dimensions": dimen_lst}
                self.il_arr_lit = None
            else:
                ini = self.visit(ctx.init, (o, typ))
                ini_typ = ini["type"]
                
                if TUtils.autoType(ini_typ):
                    ini["type"] = typ
                    o[0][name] = {"type": ini_typ, "kind": Variable()}
                    return
                
                if TUtils.autoType(typ):
                    if TUtils.arrayCheck(ini_typ):
                        ini_typ = Array.getDi(ini_typ)[-1]
                    o[0][name] = {"type": ini_typ, "kind": Variable()}
                    return
                
                if TUtils.arrayLit(ctx.init): self.raise_(TypeMismatchInVarDecl(ctx))

                if TUtils.intType(ini_typ) and TUtils.floatType(typ):
                    o[0][name] = {"type": FloatType(), "kind": Variable()}
                    return
                
                if not TUtils.sameTypeCheck(typ, ini_typ): self.raise_(TypeMismatchInVarDecl(ctx))

                o[0][name] = {"type": ini_typ, "kind": Variable()}
                self.il_arr_lit = None
        else:
            if TUtils.autoType(typ): self.raise_(Invalid(Variable(), name))
            o[0][name] = {"type": ini_typ, "kind": Variable()}
            self.il_arr_lit = None

    def visitParamDecl(self, ctx: ParamDecl, cont):
        (o, _) = cont
        name = ctx.name
        if name in o[0]: 
            if o[0][name]["inherit"]: self.raise_(Invalid(Parameter(), name))
        
        typ = ctx.name
        inh = ctx.inherit
        out = ctx.out

        result = {"type": typ, "kind": Variable(), "inherit": inh, "out": out}
        o[0][name] = result
        result["name"] = name
        return result
    
    def visitFuncDecl(self, ctx: FuncDecl, cont):
        (o, _) = cont
        name = ctx.name
        sym = self.lookup(name, StaticChecker.global_env, lambda symbol: symbol.name)

        if not TUtils.noneCheck(sym): self.raise_(Redeclared(Function(), name))

        type_return = ctx.return_type
        inher = ctx.inherit
        b = ctx.body
        new_o = [{}] + o
        self.setFunctionDecl(True, {"type": type_return}, name)

        if not TUtils.noneCheck(inher):
            inherit_funct = LookUp.lookup(inher, new_o, lambda: self.raise_(Undeclared(Function(), inher)), Function)

            if len(inherit_funct["params"]) != 0:
                for par in inherit_funct["params"]:
                    if par["inherit"]: new_o[0][par["name"]] = par
                
                for ele in ctx.params:
                    p = self.visit(ele, (new_o, None))

                if len(b.body) == 0: self.raise_(InvalidStatementInFunction(name))

                first = b.body[0]
                if not isinstance(first, CallStmt): self.raise_(InvalidStatementInFunction(name))

                first_name = first.name
                if first_name != "super" and first_name != "preventDefault": self.raise_(InvalidStatementInFunction(name))

                self.f_decl["inherit"]["super_or_preventDefault"] = "preventDefault" if first_name == "preventDefault" else "super" if first_name == "super" else None
            else:
                for ele in ctx.params:
                    p = self.visit(ele, (new_o, None))

                if len(b.body) != 0:
                    first = b.body[0]
                    if isinstance(first, CallStmt):
                        first_name = first.name
                        self.f_decl["inherit"]["super_or_preventDefault"] = "preventDefault" if first_name == "preventDefault" else "super" if first_name == "super" else None
                    else:
                        self.f_decl["inherit"]["super_or_preventDefault"] = "super"
        
            self.f_decl["inherit"]["func"] = {**inherit_funct, **{"name": inher}}
        else:
            for ele in ctx.params:
                p = self.visit(ele, (new_o, None))
        self.visit(b, (new_o, None))
        self.resetFunctionDecl()