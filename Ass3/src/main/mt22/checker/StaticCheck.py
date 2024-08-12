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
        (obj, _) = cont
        name = ctx.name
        LookUp.check(name, obj[0], lambda: self.raise_(Redeclared(Variable(), name)))
        typ = ctx.typ

        if not TUtils.noneCheck(ctx.init):
            if TUtils.arrayLit(ctx.init):
                self.il_arr_lit = {"type": typ, "ast": ctx, "astInit": ctx.init}
            
            if TUtils.arrayType(typ):
                a_dimen = typ.dimensions
                a_type = typ.typ
                self.il_arr_lit = {"type": a_type, "ast": ctx, "astInit": ctx.init}

                if not TUtils.arrayLit(ctx.init) and not TUtils.arrayCell(ctx.init): self.raise_(TypeMismatchInVarDecl(ctx))

                init = self.visit(ctx.init, (obj, a_type))
                dimen_lst = Array.getDi(init["type"])
                dimen_lst = dimen_lst[:-1]

                if Array.isDiMatch(a_dimen, dimen_lst, lambda: self.raise_(TypeMismatchInVarDecl(ctx))):
                    obj[0][name] = {"type": typ, "kind": Variable(), "dimensions": dimen_lst}
                self.il_arr_lit = None
            else:
                ini = self.visit(ctx.init, (obj, typ))
                ini_typ = ini["type"]
                
                if TUtils.autoType(ini_typ):
                    ini["type"] = typ
                    obj[0][name] = {"type": ini_typ, "kind": Variable()}
                    return
                
                if TUtils.autoType(typ):
                    if TUtils.arrayCheck(ini_typ):
                        ini_typ = Array.getDi(ini_typ)[-1]
                    obj[0][name] = {"type": ini_typ, "kind": Variable()}
                    return
                
                if TUtils.arrayLit(ctx.init): self.raise_(TypeMismatchInVarDecl(ctx))

                if TUtils.intType(ini_typ) and TUtils.floatType(typ):
                    obj[0][name] = {"type": FloatType(), "kind": Variable()}
                    return
                
                if not TUtils.sameTypeCheck(typ, ini_typ): self.raise_(TypeMismatchInVarDecl(ctx))

                obj[0][name] = {"type": ini_typ, "kind": Variable()}
                self.il_arr_lit = None
        else:
            if TUtils.autoType(typ): self.raise_(Invalid(Variable(), name))
            obj[0][name] = {"type": ini_typ, "kind": Variable()}
            self.il_arr_lit = None

    def visitParamDecl(self, ctx: ParamDecl, cont):
        (obj, _) = cont
        name = ctx.name
        if name in obj[0]: 
            if obj[0][name]["inherit"]: self.raise_(Invalid(Parameter(), name))
        
        typ = ctx.name
        inh = ctx.inherit
        out = ctx.out

        result = {"type": typ, "kind": Variable(), "inherit": inh, "out": out}
        obj[0][name] = result
        result["name"] = name
        return result
    
    def visitFuncDecl(self, ctx: FuncDecl, cont):
        (obj, _) = cont
        name = ctx.name
        sym = self.lookup(name, StaticChecker.global_env, lambda symbol: symbol.name)

        if not TUtils.noneCheck(sym): self.raise_(Redeclared(Function(), name))

        type_return = ctx.return_type
        inher = ctx.inherit
        b = ctx.body
        new_o = [{}] + obj
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

    def visitAssignStmt(self, ctx: AssignStmt, cont):
        (obj, _) = cont
        left_type = None
        left_expr = None
        if self.loop["flag"]:
            name = ctx.lhs.name
            id = LookUp.lookup(name, obj, lambda: None, Variable)
            if TUtils.noneCheck(id):
                obj[0][name] = {"type": IntegerType(), "kind": Variable()}
                left_type = IntegerType()
            else:
                if TUtils.autoType(id["type"]): id["type"] = IntegerType()
                else:
                    if not TUtils.intType(id["type"]): self.raise_(TypeMismatchInStatement(self.loop["ast"]))
                left_type = id["type"]
        else:
            left_expr = self.visit(ctx.lhs, cont)
            left_type = left_expr["type"]
            if TUtils.arrayType(left_type) or TUtils.voidType(left_type): self.raise_(TypeMismatchInStatement(ctx))
        
        right_expr = self.visit(ctx.rhs, cont)
        right_type = right_expr["type"]
        if TUtils.autoType(left_type):
            left_expr["type"] = left_type = right_type
        elif TUtils.autoType(right_type):
            right_expr["type"] = right_type = left_type

        if not (TUtils.floatType(left_type) and TUtils.intType(right_type)):
            if not TUtils.sameTypeCheck(left_type, right_type):
                self.raise_(TypeMismatchInStatement(ctx if not self.loop["flag"] else self.loop["ast"]))

    def visitBlockStmt(self, ctx: BlockStmt, cont):
        (obj, t) = cont
        reduce(lambda _, ele: self.visit(ele, (obj if self.f_decl["flag"] or self.loop["flag"] else [{}] + obj, t)), ctx.body, [])

    def visitIfStmt(self, ctx: IfStmt, cont):
        self.addIfEle(True)
        cond = self.visit(ctx.cond, cont)
        if not TUtils.boolType(cond["type"]): self.raise_(TypeMismatchInStatement(ctx))

        self.visit(ctx.tstmt, cont)
        if not TUtils.noneCheck(ast.fstmt): self.visit(ctx.fstmt, cont)

        self.removeIfEle()

    def visitForStmt(self, ctx: ForStmt, cont):
        (obj, t) = cont
        self.set_loop(True, ctx)
        self.addForEle(True)
        o_new = [{}] + obj

        self.visit(ctx.init, {o_new, t})
        self.reset_loop()

        cond_expr = self.visit(ctx.cond, (o_new, t))
        cond_type = cond_expr["type"]
        if TUtils.autoType(cond_type): cond_type = cond_expr["type"] = BooleanType()
        if not TUtils.boolType(cond_type): self.raise_(TypeMismatchInStatement(ctx))
        
        up8_type = self.visit(ctx.upd, (o_new, t))["type"]
        if not TUtils.intType(up8_type): self.raise_(TypeMismatchInStatement(ctx))

        self.visit(ctx.stmt, (o_new, t))
        self.removeForEle()

    def visitWhileStmt(self, ctx: WhileStmt, cont):
        self.addWhileEle(True)

        cond_expr = self.visit(ctx.cond, cont)
        cond_type = cond_expr["type"]
        if TUtils.autoType(cond_type): cond_type = cond_expr["type"] = BooleanType()
        if not TUtils.boolType(cond_type): self.raise_(TypeMismatchInStatement(ctx))

        self.visit(ctx.stmt, cont)
        self.removeWhileEle

    def visitDoWhileStmt(self, ctx: DoWhileStmt, cont):
        self.addDoWhileEle(True)
        self.visit(ctx.stmt, cont)

        cond_expr = self.visit(ctx.cond, cont)
        cond_type = cond_expr["type"]
        if TUtils.autoType(cond_type): cond_type = cond_expr["type"] = BooleanType()
        if TUtils.boolType(cond_type): self.raise_(TypeMismatchInStatement(ctx))
        self.removeDoWhileEle()

    def visitBreakStmt(self, ctx: BreakStmt, cont):
        if self.getForSize() == 0 and self.getWhileSize() == 0 and self.getDoWhileSize() == 0: self.raise_(MustInLoop(ctx))
    
    def visitContinueStmt(self, ctx: ContinueStmt, cont):
        if self.getForSize() == 0 and self.getWhileSize() == 0 and self.getDoWhileSize() == 0: self.raise_(MustInLoop(ctx))

    def visitReturnStmt(self, ctx: ReturnStmt, cont):
        (obj, _) = cont

        if self.f_decl["flag"]:
            f_type = self.f_decl["return_type"]["type"]

            exp = None
            exp_type = VoidType()

            if not TUtils.noneCheck(ctx.expr):
                exp = self.visit(ctx.expr, cont)
                exp_type = exp["type"]

            if TUtils.autoType(f_type):
                self.f_decl["return_type"] = TUtils.interType(
                    self.f_decl["name"], exp_type, obj, Function
                )
                f_type = self.f_decl["return_type"]["type"]

            elif TUtils.autoType(exp_type):
                exp_type = exp["type"] = f_type

            if self.getForSize() != 0 or self.getWhileSize() != 0 or self.getDoWhileSize() != 0 or self.getIfSize() != 0:
                if not (TUtils.floatType(f_type) and TUtils.intType(exp_type)):
                    if not TUtils.sameTypeCheck(exp_type, f_type):
                        self.raise_(TypeMismatchInStatement(ctx))
            
            else:
                if not self.f_decl["has_first_stmt_return"]:
                    if not (TUtils.floatType(f_type) and TUtils.intType(exp_type)):
                        if not TUtils.sameTypeCheck(exp_type, f_type):
                            self.raise_(TypeMismatchInStatement(ctx))
                    self.f_decl["has_first_stmt_return"] = True
    
    def visitCallStmt(self, ctx: CallStmt, cont):
        (obj, _) = cont
        name = ctx.name
        sym = self.lookup(name, StaticChecker.global_env, lambda symbol: symbol.name)
        par = None
        f_type = None
        funct = dict()

        if TUtils.noneCheck(sym):
            funct = LookUp.lookup(name, obj, lambda: self.raise_(Undeclared(Function(), name)), Function)
            f_type = funct["type"]
            par = funct["params"]

        else:
            if name == "super" or name== "preventDefault":
                if (self.f_decl["flag"] and TUtils.noneCheck(self.f_decl["inherit"]["func"])) or TUtils.noneCheck(self.f_decl["inherit"]["super_or_preventDefault"]):
                    self.raise_(InvalidStatementInFunction(self.f_decl["name"]))
                par = self.f_decl["inherit"]["func"]["params"] if name == "super" else sym.mtyp.ptype
            else:
                par = list(map(lambda p: self.visit(p, cont), sym.mtyp.ptype))
            f_type = sym.mtyp.rtype
        
        if name!= "super":
            if len(ctx.args) != len(par): self.raise_(TypeMismatchInStatement(ctx))
        else:
            if len(par) < len(ctx.args): self.raise_(TypeMismatchInExpression(ctx.args[len(par)]))
            if len(par) > len(ctx.args): self.raise_(TypeMismatchInExpression(None))

        for ele in zip(par, ctx.args):
            ele0_type = ele[0]["type"]
            ele_type = self.visit(ele[1], (obj, ele0_type))["type"]

            if TUtils.arrayCheck(ele_type): ele_type = Array.getDi(ele_type)[-1]
            if TUtils.autoType(ele0_type): ele0_type = ele[0]["type"] = ele_type

            if not (TUtils.floatType(ele0_type) and TUtils.intType(ele_type)):
                if not TUtils.autoType(ele0_type):
                    if not TUtils.sameTypeCheck(ele0_type, ele_type):
                        self.raise_(TypeMismatchInExpression(ele[1]) if name == "super" else TypeMismatchInStatement(ctx))
        return {"type": f_type}