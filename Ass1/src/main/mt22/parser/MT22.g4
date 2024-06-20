grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

//---------------------LEXER----------------------//	 
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
MORE: '>';
MORE_EQ: '>=';
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
STRING_LIT: '"' (STR_CHAR | ESC_SEQ)* '"' {self.text = str(self.text[1:-1])};
array_lit: LEFT_BRACE /*WAIT FOR SYNTAX*/ RIGHT_BRACE;

fragment STR_CHAR: ~[\\\n];
fragment ESC_SEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\\\' | '\\\'' | '\\t' | '\\"' | '\'"';
fragment ESC_ERR: '\\' ~[bfrnt\\'] | '\'' ~'"';
fragment DECI: '.'DIGIT*;
fragment EXPO: [eE][+-]?DIGIT+;
fragment NON_0_DIGIT: [1-9];
fragment DIGIT: [0-9];

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

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
ERROR_CHAR: . {
	raise ErrorToken(self.text)
};