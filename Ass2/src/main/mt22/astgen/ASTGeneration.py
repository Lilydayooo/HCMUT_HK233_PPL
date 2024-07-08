from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #program: decls EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))
    
        #______________DECLARATIONS______________
    
    #decls: decl decls | decl;
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.decl()) + self.visit(ctx.decls())
        else:
            return self.visit(ctx.decl())
    
    #decl: var_decl | func_decl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.getChild(0))
    
    #var_decl: idlist COLON (atomic_type | array_type | auto_type) (ASSIGN exprs_list_var_decl)? {self.check(True)} SEMI_COLON;
    def visitVar_decl(self, ctx: MT22Parser.Var_declContext):
        if ctx.exprs_list_var_decl():
            return [VarDecl(id, self.visit(ctx.getChild(2)), expr) for id, expr in zip(self.visit(ctx.idlist()), self.visit(ctx.exprs_list_var_decl()))]
        else:
            return [VarDecl(id, self.visit(ctx.getChild(2)), None) for id in self.visit(ctx.idlist())]
    
    #idlist: ID (COMMA ID)*;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        return [x.getText() for x in ctx.ID()]
    
    #exprs_list_var_decl: expr COMMA exprs_list_var_decl | expr;
    def visitExprs_list_var_decl(self, ctx: MT22Parser.Exprs_list_var_declContext):
        return [self.visit(ctx.expr()) + self.visit(ctx.exprs_list_var_decl())] if ctx.getChildCount() == 3 else [self.visit(ctx.expr())]

    #func_decl: ID COLON FUNCTION (atomic_type | void_type | auto_type | array_type) LEFT_PAREN params_list? RIGHT_PAREN (INHERIT ID)? body;
    def visitFunc_decl(self, ctx: MT22Parser.Func_declContext):
        return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.getChild(3)), self.visit(ctx.params_list()) if ctx.params_list() else [], ctx.ID(1).getText() if ctx.INHERIT() else None, self.visit(ctx.body()))]
    
    #params_list: param COMMA params_list | param;
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        return [self.visit(ctx.param()) + self.visit(ctx.params_list())] if ctx.getChildCount() == 3 else [self.visit(ctx.param())]
    
    #param: INHERIT? OUT? ID COLON (atomic_type | array_type | auto_type);
    def visitParam(self, ctx: MT22Parser.ParamContext):
        return [ParamDecl(ctx.ID().getText(), self.visit(ctx.getChild(ctx.getChildCount() - 1)), True if ctx.OUT() else False, True if ctx.INHERIT() else False)]
    
    #body: block_stmt;
    def visitBody(self, ctx: MT22Parser.BodyContext):
        return self.visit(ctx.block_stmt())
    
        #_______________EXPRESSIONS_______________

    #expr: string_expr;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        return self.visit(ctx.string_expr())
    
    #string_expr: relat_expr SCOPE relat_expr | relat_expr;
    def visitString_expr(self, ctx: MT22Parser.String_exprContext):
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.relat_expr(0)), self.visit(ctx.relat_expr(1))) if ctx.getChildCount() == 3 else self.visit(ctx.relat_expr(0))
    
    #relat_expr: expr1 (SAME | NOTSAME | MOR | MOR_EQ | LESS | LESS_EQ) expr1 | expr1;
    def visitRelat_expr(self, ctx: MT22Parser.Relat_exprContext):
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1))) if ctx.getChildCount() == 3 else self.visit(ctx.expr1(0))
    
    #expr1: expr1 (AND | OR) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr1()), self.visit(ctx.expr2())) if ctx.getChildCount() == 3 else self.visit(ctx.expr2())
    
    #expr2: expr2 (ADD | SUB) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3())) if ctx.getChildCount() == 3 else self.visit(ctx.expr3())
    
    #expr3: expr3 (MUL | DIV | MOD) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4())) if ctx.getChildCount() == 3 else self.visit(ctx.expr4())
    
    #expr4: NOT expr4 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr4())) if ctx.getChildCount() == 2 else self.visit(ctx.expr5())
    
    #expr5: SUB expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr5())) if ctx.getChildCount() == 2 else self.visit(ctx.expr6())
    
    #expr6: ID indexes | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.indexes())) if ctx.getChildCount() == 2 else self.visit(ctx.expr7())
    
    #indexes: LEFT_BRACK exprs_list RIGHT_BRACK;
    def visitIndexes(self, ctx: MT22Parser.IndexesContext):
        return self.visit(ctx.exprs_list())
    
    #expr7: operand | LEFT_PAREN expr RIGHT_PAREN;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        return self.visit(ctx.expr()) if ctx.getChildCount() == 3 else self.visit(ctx.operand())
    
    #operand: literal | func_call | ID;
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.func_call():
            return self.visit(ctx.func_call(0))
        else:
            return self.visit(ctx.literal())
    
    #func_call: ID LEFT_PAREN exprs_list? RIGHT_PAREN;
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        id = ctx.ID().getText()
        exprlist = self.visit(ctx.exprs_list()) if ctx.exprs_list() else []
        return [FuncCall(id, exprlist), id, exprlist]
    
    #literal: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | array_lit;
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            flt = ctx.FLOAT_LIT().getText()
            return FloatLit(float("0" + flt) if flt[0] == "." else float(flt))
        elif ctx.BOOL_LIT():
            return BooleanLit(self.toBool(ctx.BOOL_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLit(str(ctx.STRING_LIT().getText()))
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
    
    #exprs_list: expr COMMA exprs_list | expr;
    def visitExprs_list(self, ctx: MT22Parser.Exprs_listContext):
        if ctx.exprs_list():
            return (self.visit(ctx.expr()) + self.visit(ctx.exprs_list())) 
        else: self.visit(ctx.expr())
    
        #_______________STATEMENTS_______________

    #stmt_list: (stmt | var_decl) stmt_list | (stmt | var_decl);
    def visitStmt_list(self, ctx: MT22Parser.Stmt_listContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl()) + self.visit(ctx.stmt_list()) if ctx.getChildCount() == 2 else self.visit(ctx.stmt_list())
        
        return self.visit(ctx.stmt()) + self.visit(ctx.stmt_list()) if ctx.getChildCount() == 2 else self.visit(ctx.stmt_list())
    
    #stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    #assign_stmt: assign_left ASSIGN assign_right SEMI_COLON;
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        return None
    
    #assign_left: scalar_var | ID indexes;
    def visitAssign_left(self, ctx: MT22Parser.Assign_leftContext):
        return None
    
    #assign_right: expr;
    def visitAssign_right(self, ctx: MT22Parser.Assign_rightContext):
        return None
    
    #if_stmt: IF LEFT_PAREN expr RIGHT_PAREN stmt (ELSE stmt)?;
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        if ctx.getChildCount() == 2:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.getChild(1)), None)
        else:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.getChild(1)), self.visit(ctx.getChild(2)))
    
    #for_stmt: FOR LEFT_PAREN initial_expr COMMA condition_expr COMMA upd8_expr RIGHT_PAREN stmt;
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        return None
    
    #initial_expr: scalar_var ASSIGN expr;
    def visitInitial_expr(self, ctx: MT22Parser.Initial_exprContext):
        return None
    
    #condition_expr: expr;
    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return self.visit(ctx.expr())
    
    #upd8_expr: expr;
    def visitUpd8(self, ctx: MT22Parser.Upd8Context):
        return self.visit(ctx.expr())
    
    #while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return None
    
    #do_while_stmt: DO block_stmt WHILE LEFT_PAREN expr RIGHT_PAREN SEMI_COLON;
    def visitDo_while_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        return None
    
    #break_stmt: BREAK SEMI_COLON;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return None
    
    #continue_stmt: CONTINUE SEMI_COLON;
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return None
    
    #return_stmt: RETURN expr? SEMI_COLON;
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)
    
    #call_stmt: func_call SEMI_COLON;
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        return None
    
    #block_stmt: LEFT_BRACE stmt_list? RIGHT_BRACE;
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
    
    #scalar_var: ID;
    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        return Id(ctx.ID().getText())
    
        #_________________TYPES_________________

    #bool_type: BOOLEAN;
    def visitBool_type(self, ctx: MT22Parser.Bool_typeContext):
        return BooleanType()

    #int_type: INTEGER;
    def visitInt_type(self, ctx: MT22Parser.Int_typeContext):
        return IntegerType()

    #float_type: FLOAT;
    def visitFloat_type(self, ctx: MT22Parser.Float_typeContext):
        return FloatType()

    #string_type: STRING;
    def visitString_type(self, ctx: MT22Parser.String_typeContext):
        return StringType()

    #void_type: VOID;
    def visitVoid_type(self, ctx: MT22Parser.Void_typeContext):
        return VoidType()

    #auto_type: AUTO;
    def visitAuto_type(self, ctx: MT22Parser.Auto_typeContext):
        return AutoType()
    
    #array_type: ARRAY LEFT_BRACK dimensions RIGHT_BRACK OF atomic_type;
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomic_type()))

    #dimensions: INT_LIT (COMMA INT_LIT)*;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        return [int(x.getText()) for x in ctx.INT_LIT()]

    #atomic_type: bool_type | int_type | float_type | string_type;
    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        return self.visit(ctx.getChild(0))