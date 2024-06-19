grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
ERROR_CHAR: . {
	raise ErrorToken(self.text)
};