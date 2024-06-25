/*2053114*/
grammar MT22;

@lexer::header {
from lexererr import *
}

@parser::members {
@property
def ids_size(self):
    try:
        return self._ids_size
    except AttributeError: 
        self._ids_size = -1
        return self._ids_size

@property
def exprs_size(self):
    try:
        return self._exprs_size
    except AttributeError:
        self._exprs_size = -1
        return self._exprs_size

@ids_size.setter
def ids_size(self, value):
    self._ids_size = value

@exprs_size.setter
def exprs_size(self, value):
    self._exprs_size = value


def check(self, flag):
    if flag: 
        if self.exprs_size != -1 and self.exprs_size != self.ids_size: 
            raise NoViableAltException(self)
        else:
            self.ids_size = -1
            self.exprs_size = -1
    else:
        if self.exprs_size + 2 >= self.ids_size:
            raise NoViableAltException(self)
        else:
            self.exprs_size += 1
    
}


options{
	language=Python3;
}

program: decls EOF;

decls: decl decls | decl;

decl: var_decl | func_decl;

//--------------------LEXER---------------------//	 
	/*______________OPERATORS______________*/

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
SAME: '==';
NOTSAME: '!=';
LESS: '<';
LESS_EQ: '<=';
MOR: '>';
MOR_EQ: '>=';
SCOPE: '::';

	/*_____________SEPERATORS_____________*/

LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACK: '[';
RIGHT_BRACK: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
COMMA: ',';
DOT: '.';
SEMI_COLON: ';';
COLON: ':';
ASSIGN: '=';
UNDERSCORE: '_';

	/*________________LITERALS________________*/

INT_LIT: ((NON_0_DIGIT DIGIT* (UNDERSCORE DIGIT+)*) | '0') {self.text = self.text.replace('_','')};
FLOAT_LIT: ((INT_LIT DECI EXPO?) | (DECI EXPO) | (INT_LIT EXPO)) {self.text = self.text.replace('_','')};
BOOL_LIT: TRUE | FALSE;
STRING_LIT: '"' (STR_CHAR | ESC_SEQ)* '"' 
{self.text = str(self.text[1:-1])};
array_lit: LEFT_BRACE exprs_list? RIGHT_BRACE;

fragment STR_CHAR: ~[\\\n"];
fragment ESC_SEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\\\' | '\\\'' | '\\t' | '\\"' | '\'"';
fragment ESC_ERR: '\\' ~[bfrnt\\'] | '\'' ~'"';
fragment DECI: '.'DIGIT*;
fragment EXPO: [eE][+-]?DIGIT+;
fragment NON_0_DIGIT: [1-9];
fragment DIGIT: [0-9];

	/*______________DECLARATIONS______________*/

var_decl: ids_list COLON (atomic_type | array_type | auto_type) (ASSIGN exprs_var_list)?
{
self.check(True)
}
SEMI_COLON;
ids_list: ID {self.ids_size +=2} (COMMA ID {self.ids_size+=1})*;
exprs_var_list: expr
{
self.check(False)
}
COMMA exprs_var_list | expr {self.exprs_size+=2};

func_decl: ID COLON FUNCTION (atomic_type | void_type | auto_type | array_type) LEFT_PAREN params_list? RIGHT_PAREN (INHERIT ID)? body;

params_list: param COMMA params_list | param;

param: INHERIT? OUT? ID COLON (atomic_type | array_type | auto_type);

body: block_stmt;

	/*_______________EXPRESSIONS_______________*/

expr: string_expr;

string_expr: relat_expr SCOPE relat_expr | relat_expr; //String Expressions (Scope)

relat_expr: expr1 (SAME | NOTSAME | MOR | MOR_EQ | LESS | LESS_EQ) expr1 | expr1; //Relational Expressions

expr1: expr1 (AND | OR) expr2 | expr2; //AND - OR Expressions

expr2: expr2 (ADD | SUB) expr3 | expr3; //ADD - SUBTRACT Expressions

expr3: expr3 (MUL | DIV | MOD) expr4 | expr4; //MULTIPLICATION - DIVISION - MODULAR Expressions

expr4: NOT expr4 | expr5; //NOT Expressions

expr5: SUB expr5 | expr6; //SIGN Expressions (i.e: -174)

expr6: ID indexes | expr7; //INDEX OPERATOR
indexes: LEFT_BRACK exprs_list RIGHT_BRACK;

expr7: operand | LEFT_PAREN expr RIGHT_PAREN; //OPERANDS Expressions

operand: literal | func_call | ID;

func_call: ID LEFT_PAREN exprs_list? RIGHT_PAREN;

literal: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT | array_lit;

exprs_list: expr COMMA exprs_list | expr;

	/*_______________STATEMENTS_______________*/

stmt_list: (stmt | var_decl) stmt_list | (stmt | var_decl);

stmt: assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt;

assign_stmt: assign_left ASSIGN assign_right SEMI_COLON;
assign_left: scalar_var | ID indexes;
assign_right: expr;

if_stmt: IF LEFT_PAREN expr RIGHT_PAREN stmt (ELSE stmt)?;

for_stmt: FOR LEFT_PAREN initial_expr COMMA condition_expr COMMA upd8_expr RIGHT_PAREN stmt;
initial_expr: scalar_var ASSIGN expr;
condition_expr: expr;
upd8_expr: expr;

while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;

do_while_stmt: DO block_stmt WHILE LEFT_PAREN expr RIGHT_PAREN SEMI_COLON;

break_stmt: BREAK SEMI_COLON;

continue_stmt: CONTINUE SEMI_COLON;

return_stmt: RETURN expr? SEMI_COLON;

call_stmt: func_call SEMI_COLON;

block_stmt: LEFT_BRACE stmt_list? RIGHT_BRACE;

scalar_var: ID;

	/*_________________TYPES_________________*/

bool_type: BOOLEAN;

int_type: INTEGER;

float_type: FLOAT;

string_type: STRING;

void_type: VOID;

auto_type: AUTO;

array_type: ARRAY LEFT_BRACK dimensions RIGHT_BRACK OF atomic_type;
dimensions: INT_LIT (COMMA INT_LIT)*;

atomic_type: bool_type | int_type | float_type | string_type;

	/*________________KEYWORDS________________*/

AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

	/*________________COMMENT________________*/

BLOCK_CMT: '/*' (.)+? '*/' -> skip;
LINE_CMT: '//' ~[\n\r]* -> skip;

	/*______________IDENTIFIERS______________*/
ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \b\f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: 
'"' (STR_CHAR | ESC_SEQ)* EOF {
cont = str(self.text) 
raise UncloseString(cont[1:])
};

ILLEGAL_ESCAPE: 
'"' (STR_CHAR | ESC_SEQ)* ESC_ERR {
raise IllegalEscape(str(self.text[1:]))
};

ERROR_CHAR: . {
raise ErrorToken(self.text)
};