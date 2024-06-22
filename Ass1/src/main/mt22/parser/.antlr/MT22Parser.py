# Generated from d:/DHBK/233/PPL_Assignments/Ass1/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,59,10,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,6,1,0,0,0,4,5,5,0,0,1,5,1,1,0,0,0,6,7,5,20,0,0,7,
        8,5,21,0,0,8,3,1,0,0,0,0
    ]

class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "'.'", "';'", "':'", "'='", "'_'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'boolean'", "'do'", "'else'", "'false'", "'float'", 
                     "'for'", "'function'", "'if'", "'integer'", "'return'", 
                     "'string'", "'true'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                      "AND", "OR", "SAME", "NOTSAME", "LESS", "LESS_EQ", 
                      "MOR", "MOR_EQ", "SCOPE", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_BRACK", "RIGHT_BRACK", "LEFT_BRACE", "RIGHT_BRACE", 
                      "COMMA", "DOT", "SEMI_COLON", "COLON", "ASSIGN", "UNDERSCORE", 
                      "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
                      "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
                      "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                      "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                      "OF", "INHERIT", "ARRAY", "BLOCK_CMT", "LINE_CMT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_array_lit = 1

    ruleNames =  [ "program", "array_lit" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MUL=3
    DIV=4
    MOD=5
    NOT=6
    AND=7
    OR=8
    SAME=9
    NOTSAME=10
    LESS=11
    LESS_EQ=12
    MOR=13
    MOR_EQ=14
    SCOPE=15
    LEFT_PAREN=16
    RIGHT_PAREN=17
    LEFT_BRACK=18
    RIGHT_BRACK=19
    LEFT_BRACE=20
    RIGHT_BRACE=21
    COMMA=22
    DOT=23
    SEMI_COLON=24
    COLON=25
    ASSIGN=26
    UNDERSCORE=27
    INT_LIT=28
    FLOAT_LIT=29
    BOOL_LIT=30
    STRING_LIT=31
    AUTO=32
    BREAK=33
    BOOLEAN=34
    DO=35
    ELSE=36
    FALSE=37
    FLOAT=38
    FOR=39
    FUNCTION=40
    IF=41
    INTEGER=42
    RETURN=43
    STRING=44
    TRUE=45
    WHILE=46
    VOID=47
    OUT=48
    CONTINUE=49
    OF=50
    INHERIT=51
    ARRAY=52
    BLOCK_CMT=53
    LINE_CMT=54
    ID=55
    WS=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    ERROR_CHAR=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(MT22Parser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MT22Parser.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array_lit




    def array_lit(self):

        localctx = MT22Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 7
            self.match(MT22Parser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





