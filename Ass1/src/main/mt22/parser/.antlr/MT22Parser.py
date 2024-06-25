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
        4,1,59,416,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,3,1,110,8,1,1,2,1,2,3,2,114,8,2,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,131,8,4,1,4,1,4,3,4,135,
        8,4,1,4,1,4,1,4,3,4,140,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,149,
        8,5,1,5,1,5,1,5,1,5,1,5,3,5,156,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        3,6,165,8,6,1,7,3,7,168,8,7,1,7,3,7,171,8,7,1,7,1,7,1,7,1,7,1,7,
        3,7,178,8,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,189,8,
        10,1,11,1,11,1,11,1,11,1,11,3,11,196,8,11,1,12,1,12,1,12,1,12,1,
        12,1,12,5,12,204,8,12,10,12,12,12,207,9,12,1,13,1,13,1,13,1,13,1,
        13,1,13,5,13,215,8,13,10,13,12,13,218,9,13,1,14,1,14,1,14,1,14,1,
        14,1,14,5,14,226,8,14,10,14,12,14,229,9,14,1,15,1,15,1,15,3,15,234,
        8,15,1,16,1,16,1,16,3,16,239,8,16,1,17,1,17,1,17,3,17,244,8,17,1,
        18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,255,8,19,1,20,1,
        20,1,20,3,20,260,8,20,1,21,1,21,1,21,3,21,265,8,21,1,21,1,21,1,22,
        1,22,1,22,1,22,1,22,3,22,274,8,22,1,23,1,23,1,23,1,23,1,23,3,23,
        281,8,23,1,24,1,24,3,24,285,8,24,1,24,1,24,1,24,1,24,3,24,291,8,
        24,3,24,293,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,3,25,305,8,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,3,27,315,
        8,27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,326,8,29,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,
        1,38,3,38,368,8,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,3,40,377,8,
        40,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,
        46,1,46,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,
        49,5,49,405,8,49,10,49,12,49,408,9,49,1,50,1,50,1,50,1,50,3,50,414,
        8,50,1,50,0,3,24,26,28,51,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,88,90,92,94,96,98,100,0,4,1,0,9,14,1,0,7,8,
        1,0,1,2,1,0,3,5,416,0,102,1,0,0,0,2,109,1,0,0,0,4,113,1,0,0,0,6,
        115,1,0,0,0,8,139,1,0,0,0,10,141,1,0,0,0,12,164,1,0,0,0,14,167,1,
        0,0,0,16,179,1,0,0,0,18,181,1,0,0,0,20,188,1,0,0,0,22,195,1,0,0,
        0,24,197,1,0,0,0,26,208,1,0,0,0,28,219,1,0,0,0,30,233,1,0,0,0,32,
        238,1,0,0,0,34,243,1,0,0,0,36,245,1,0,0,0,38,254,1,0,0,0,40,259,
        1,0,0,0,42,261,1,0,0,0,44,273,1,0,0,0,46,280,1,0,0,0,48,292,1,0,
        0,0,50,304,1,0,0,0,52,306,1,0,0,0,54,314,1,0,0,0,56,316,1,0,0,0,
        58,318,1,0,0,0,60,327,1,0,0,0,62,337,1,0,0,0,64,341,1,0,0,0,66,343,
        1,0,0,0,68,345,1,0,0,0,70,351,1,0,0,0,72,359,1,0,0,0,74,362,1,0,
        0,0,76,365,1,0,0,0,78,371,1,0,0,0,80,374,1,0,0,0,82,380,1,0,0,0,
        84,382,1,0,0,0,86,384,1,0,0,0,88,386,1,0,0,0,90,388,1,0,0,0,92,390,
        1,0,0,0,94,392,1,0,0,0,96,394,1,0,0,0,98,401,1,0,0,0,100,413,1,0,
        0,0,102,103,3,2,1,0,103,104,5,0,0,1,104,1,1,0,0,0,105,106,3,4,2,
        0,106,107,3,2,1,0,107,110,1,0,0,0,108,110,3,4,2,0,109,105,1,0,0,
        0,109,108,1,0,0,0,110,3,1,0,0,0,111,114,3,8,4,0,112,114,3,10,5,0,
        113,111,1,0,0,0,113,112,1,0,0,0,114,5,1,0,0,0,115,116,5,20,0,0,116,
        117,5,21,0,0,117,7,1,0,0,0,118,119,5,55,0,0,119,120,5,22,0,0,120,
        121,3,8,4,0,121,122,5,22,0,0,122,123,3,18,9,0,123,124,5,24,0,0,124,
        140,1,0,0,0,125,126,5,55,0,0,126,130,5,25,0,0,127,131,3,100,50,0,
        128,131,3,96,48,0,129,131,3,94,47,0,130,127,1,0,0,0,130,128,1,0,
        0,0,130,129,1,0,0,0,131,134,1,0,0,0,132,133,5,26,0,0,133,135,3,18,
        9,0,134,132,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,6,4,
        -1,0,137,138,5,24,0,0,138,140,1,0,0,0,139,118,1,0,0,0,139,125,1,
        0,0,0,140,9,1,0,0,0,141,142,5,55,0,0,142,143,5,25,0,0,143,148,5,
        40,0,0,144,149,3,100,50,0,145,149,3,92,46,0,146,149,3,94,47,0,147,
        149,3,96,48,0,148,144,1,0,0,0,148,145,1,0,0,0,148,146,1,0,0,0,148,
        147,1,0,0,0,149,150,1,0,0,0,150,151,5,16,0,0,151,152,3,12,6,0,152,
        155,5,17,0,0,153,154,5,51,0,0,154,156,5,55,0,0,155,153,1,0,0,0,155,
        156,1,0,0,0,156,157,1,0,0,0,157,158,3,16,8,0,158,11,1,0,0,0,159,
        160,3,14,7,0,160,161,5,22,0,0,161,162,3,12,6,0,162,165,1,0,0,0,163,
        165,3,14,7,0,164,159,1,0,0,0,164,163,1,0,0,0,165,13,1,0,0,0,166,
        168,5,51,0,0,167,166,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,
        171,5,48,0,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,
        173,5,55,0,0,173,177,5,25,0,0,174,178,3,100,50,0,175,178,3,96,48,
        0,176,178,3,94,47,0,177,174,1,0,0,0,177,175,1,0,0,0,177,176,1,0,
        0,0,178,15,1,0,0,0,179,180,3,80,40,0,180,17,1,0,0,0,181,182,3,20,
        10,0,182,19,1,0,0,0,183,184,3,22,11,0,184,185,5,15,0,0,185,186,3,
        22,11,0,186,189,1,0,0,0,187,189,3,22,11,0,188,183,1,0,0,0,188,187,
        1,0,0,0,189,21,1,0,0,0,190,191,3,24,12,0,191,192,7,0,0,0,192,193,
        3,24,12,0,193,196,1,0,0,0,194,196,3,24,12,0,195,190,1,0,0,0,195,
        194,1,0,0,0,196,23,1,0,0,0,197,198,6,12,-1,0,198,199,3,26,13,0,199,
        205,1,0,0,0,200,201,10,2,0,0,201,202,7,1,0,0,202,204,3,26,13,0,203,
        200,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,
        25,1,0,0,0,207,205,1,0,0,0,208,209,6,13,-1,0,209,210,3,28,14,0,210,
        216,1,0,0,0,211,212,10,2,0,0,212,213,7,2,0,0,213,215,3,28,14,0,214,
        211,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        27,1,0,0,0,218,216,1,0,0,0,219,220,6,14,-1,0,220,221,3,30,15,0,221,
        227,1,0,0,0,222,223,10,2,0,0,223,224,7,3,0,0,224,226,3,30,15,0,225,
        222,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        29,1,0,0,0,229,227,1,0,0,0,230,231,5,6,0,0,231,234,3,30,15,0,232,
        234,3,32,16,0,233,230,1,0,0,0,233,232,1,0,0,0,234,31,1,0,0,0,235,
        236,5,2,0,0,236,239,3,32,16,0,237,239,3,34,17,0,238,235,1,0,0,0,
        238,237,1,0,0,0,239,33,1,0,0,0,240,241,5,55,0,0,241,244,3,36,18,
        0,242,244,3,38,19,0,243,240,1,0,0,0,243,242,1,0,0,0,244,35,1,0,0,
        0,245,246,5,18,0,0,246,247,3,46,23,0,247,248,5,19,0,0,248,37,1,0,
        0,0,249,255,3,40,20,0,250,251,5,16,0,0,251,252,3,18,9,0,252,253,
        5,17,0,0,253,255,1,0,0,0,254,249,1,0,0,0,254,250,1,0,0,0,255,39,
        1,0,0,0,256,260,3,44,22,0,257,260,3,42,21,0,258,260,5,55,0,0,259,
        256,1,0,0,0,259,257,1,0,0,0,259,258,1,0,0,0,260,41,1,0,0,0,261,262,
        5,55,0,0,262,264,5,16,0,0,263,265,3,46,23,0,264,263,1,0,0,0,264,
        265,1,0,0,0,265,266,1,0,0,0,266,267,5,17,0,0,267,43,1,0,0,0,268,
        274,5,28,0,0,269,274,5,29,0,0,270,274,5,30,0,0,271,274,5,31,0,0,
        272,274,3,6,3,0,273,268,1,0,0,0,273,269,1,0,0,0,273,270,1,0,0,0,
        273,271,1,0,0,0,273,272,1,0,0,0,274,45,1,0,0,0,275,276,3,18,9,0,
        276,277,5,22,0,0,277,278,3,46,23,0,278,281,1,0,0,0,279,281,3,18,
        9,0,280,275,1,0,0,0,280,279,1,0,0,0,281,47,1,0,0,0,282,285,3,50,
        25,0,283,285,3,8,4,0,284,282,1,0,0,0,284,283,1,0,0,0,285,286,1,0,
        0,0,286,287,3,48,24,0,287,293,1,0,0,0,288,291,3,50,25,0,289,291,
        3,8,4,0,290,288,1,0,0,0,290,289,1,0,0,0,291,293,1,0,0,0,292,284,
        1,0,0,0,292,290,1,0,0,0,293,49,1,0,0,0,294,305,3,52,26,0,295,305,
        3,58,29,0,296,305,3,60,30,0,297,305,3,68,34,0,298,305,3,70,35,0,
        299,305,3,72,36,0,300,305,3,74,37,0,301,305,3,76,38,0,302,305,3,
        78,39,0,303,305,3,80,40,0,304,294,1,0,0,0,304,295,1,0,0,0,304,296,
        1,0,0,0,304,297,1,0,0,0,304,298,1,0,0,0,304,299,1,0,0,0,304,300,
        1,0,0,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,51,1,
        0,0,0,306,307,3,54,27,0,307,308,5,26,0,0,308,309,3,56,28,0,309,310,
        5,24,0,0,310,53,1,0,0,0,311,315,3,82,41,0,312,313,5,55,0,0,313,315,
        3,36,18,0,314,311,1,0,0,0,314,312,1,0,0,0,315,55,1,0,0,0,316,317,
        3,18,9,0,317,57,1,0,0,0,318,319,5,41,0,0,319,320,5,16,0,0,320,321,
        3,18,9,0,321,322,5,17,0,0,322,325,3,50,25,0,323,324,5,36,0,0,324,
        326,3,50,25,0,325,323,1,0,0,0,325,326,1,0,0,0,326,59,1,0,0,0,327,
        328,5,39,0,0,328,329,5,16,0,0,329,330,3,62,31,0,330,331,5,22,0,0,
        331,332,3,64,32,0,332,333,5,22,0,0,333,334,3,66,33,0,334,335,5,17,
        0,0,335,336,3,50,25,0,336,61,1,0,0,0,337,338,3,82,41,0,338,339,5,
        26,0,0,339,340,3,18,9,0,340,63,1,0,0,0,341,342,3,18,9,0,342,65,1,
        0,0,0,343,344,3,18,9,0,344,67,1,0,0,0,345,346,5,46,0,0,346,347,5,
        16,0,0,347,348,3,18,9,0,348,349,5,17,0,0,349,350,3,50,25,0,350,69,
        1,0,0,0,351,352,5,35,0,0,352,353,3,80,40,0,353,354,5,46,0,0,354,
        355,5,16,0,0,355,356,3,18,9,0,356,357,5,17,0,0,357,358,5,24,0,0,
        358,71,1,0,0,0,359,360,5,33,0,0,360,361,5,24,0,0,361,73,1,0,0,0,
        362,363,5,49,0,0,363,364,5,24,0,0,364,75,1,0,0,0,365,367,5,43,0,
        0,366,368,3,18,9,0,367,366,1,0,0,0,367,368,1,0,0,0,368,369,1,0,0,
        0,369,370,5,24,0,0,370,77,1,0,0,0,371,372,3,42,21,0,372,373,5,24,
        0,0,373,79,1,0,0,0,374,376,5,20,0,0,375,377,3,48,24,0,376,375,1,
        0,0,0,376,377,1,0,0,0,377,378,1,0,0,0,378,379,5,21,0,0,379,81,1,
        0,0,0,380,381,5,55,0,0,381,83,1,0,0,0,382,383,5,34,0,0,383,85,1,
        0,0,0,384,385,5,42,0,0,385,87,1,0,0,0,386,387,5,38,0,0,387,89,1,
        0,0,0,388,389,5,44,0,0,389,91,1,0,0,0,390,391,5,47,0,0,391,93,1,
        0,0,0,392,393,5,32,0,0,393,95,1,0,0,0,394,395,5,52,0,0,395,396,5,
        18,0,0,396,397,3,98,49,0,397,398,5,19,0,0,398,399,5,50,0,0,399,400,
        3,100,50,0,400,97,1,0,0,0,401,406,5,28,0,0,402,403,5,22,0,0,403,
        405,5,28,0,0,404,402,1,0,0,0,405,408,1,0,0,0,406,404,1,0,0,0,406,
        407,1,0,0,0,407,99,1,0,0,0,408,406,1,0,0,0,409,414,3,84,42,0,410,
        414,3,86,43,0,411,414,3,88,44,0,412,414,3,90,45,0,413,409,1,0,0,
        0,413,410,1,0,0,0,413,411,1,0,0,0,413,412,1,0,0,0,414,101,1,0,0,
        0,34,109,113,130,134,139,148,155,164,167,170,177,188,195,205,216,
        227,233,238,243,254,259,264,273,280,284,290,292,304,314,325,367,
        376,406,413
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
    RULE_decls = 1
    RULE_decl = 2
    RULE_array_lit = 3
    RULE_var_decl = 4
    RULE_func_decl = 5
    RULE_params_list = 6
    RULE_param = 7
    RULE_body = 8
    RULE_expr = 9
    RULE_string_expr = 10
    RULE_relat_expr = 11
    RULE_expr1 = 12
    RULE_expr2 = 13
    RULE_expr3 = 14
    RULE_expr4 = 15
    RULE_expr5 = 16
    RULE_expr6 = 17
    RULE_indexes = 18
    RULE_expr7 = 19
    RULE_operand = 20
    RULE_func_call = 21
    RULE_literal = 22
    RULE_exprs_list = 23
    RULE_stmt_list = 24
    RULE_stmt = 25
    RULE_assign_stmt = 26
    RULE_assign_left = 27
    RULE_assign_right = 28
    RULE_if_stmt = 29
    RULE_for_stmt = 30
    RULE_initial_expr = 31
    RULE_condition_expr = 32
    RULE_upd8_expr = 33
    RULE_while_stmt = 34
    RULE_do_while_stmt = 35
    RULE_break_stmt = 36
    RULE_continue_stmt = 37
    RULE_return_stmt = 38
    RULE_call_stmt = 39
    RULE_block_stmt = 40
    RULE_scalar_var = 41
    RULE_bool_type = 42
    RULE_int_type = 43
    RULE_float_type = 44
    RULE_string_type = 45
    RULE_void_type = 46
    RULE_auto_type = 47
    RULE_array_type = 48
    RULE_dimensions = 49
    RULE_atomic_type = 50

    ruleNames =  [ "program", "decls", "decl", "array_lit", "var_decl", 
                   "func_decl", "params_list", "param", "body", "expr", 
                   "string_expr", "relat_expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "indexes", "expr7", "operand", 
                   "func_call", "literal", "exprs_list", "stmt_list", "stmt", 
                   "assign_stmt", "assign_left", "assign_right", "if_stmt", 
                   "for_stmt", "initial_expr", "condition_expr", "upd8_expr", 
                   "while_stmt", "do_while_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "call_stmt", "block_stmt", "scalar_var", 
                   "bool_type", "int_type", "float_type", "string_type", 
                   "void_type", "auto_type", "array_type", "dimensions", 
                   "atomic_type" ]

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

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.decls()
            self.state = 103
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.decl()
                self.state = 106
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MT22Parser.Func_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.func_decl()
                pass


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
        self.enterRule(localctx, 6, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 116
            self.match(MT22Parser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Var_declContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_var_decl




    def var_decl(self):

        localctx = MT22Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(MT22Parser.ID)
                self.state = 119
                self.match(MT22Parser.COMMA)
                self.state = 120
                self.var_decl()
                self.state = 121
                self.match(MT22Parser.COMMA)
                self.state = 122
                self.expr()
                self.state = 123
                self.match(MT22Parser.SEMI_COLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(MT22Parser.ID)
                self.state = 126
                self.match(MT22Parser.COLON)
                self.state = 130
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 38, 42, 44]:
                    self.state = 127
                    self.atomic_type()
                    pass
                elif token in [52]:
                    self.state = 128
                    self.array_type()
                    pass
                elif token in [32]:
                    self.state = 129
                    self.auto_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 132
                    self.match(MT22Parser.ASSIGN)
                    self.state = 133
                    self.expr()



                self.check(True)

                self.state = 137
                self.match(MT22Parser.SEMI_COLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def params_list(self):
            return self.getTypedRuleContext(MT22Parser.Params_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def body(self):
            return self.getTypedRuleContext(MT22Parser.BodyContext,0)


        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def void_type(self):
            return self.getTypedRuleContext(MT22Parser.Void_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_decl




    def func_decl(self):

        localctx = MT22Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MT22Parser.ID)
            self.state = 142
            self.match(MT22Parser.COLON)
            self.state = 143
            self.match(MT22Parser.FUNCTION)
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 144
                self.atomic_type()
                pass
            elif token in [47]:
                self.state = 145
                self.void_type()
                pass
            elif token in [32]:
                self.state = 146
                self.auto_type()
                pass
            elif token in [52]:
                self.state = 147
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 150
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 151
            self.params_list()
            self.state = 152
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 153
                self.match(MT22Parser.INHERIT)
                self.state = 154
                self.match(MT22Parser.ID)


            self.state = 157
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def params_list(self):
            return self.getTypedRuleContext(MT22Parser.Params_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_params_list




    def params_list(self):

        localctx = MT22Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params_list)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.param()
                self.state = 160
                self.match(MT22Parser.COMMA)
                self.state = 161
                self.params_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_param




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 166
                self.match(MT22Parser.INHERIT)


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 169
                self.match(MT22Parser.OUT)


            self.state = 172
            self.match(MT22Parser.ID)
            self.state = 173
            self.match(MT22Parser.COLON)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 174
                self.atomic_type()
                pass
            elif token in [52]:
                self.state = 175
                self.array_type()
                pass
            elif token in [32]:
                self.state = 176
                self.auto_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_body




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self):
            return self.getTypedRuleContext(MT22Parser.String_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.string_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relat_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Relat_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Relat_exprContext,i)


        def SCOPE(self):
            return self.getToken(MT22Parser.SCOPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_expr




    def string_expr(self):

        localctx = MT22Parser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_string_expr)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.relat_expr()
                self.state = 184
                self.match(MT22Parser.SCOPE)
                self.state = 185
                self.relat_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.relat_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relat_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def SAME(self):
            return self.getToken(MT22Parser.SAME, 0)

        def NOTSAME(self):
            return self.getToken(MT22Parser.NOTSAME, 0)

        def MOR(self):
            return self.getToken(MT22Parser.MOR, 0)

        def MOR_EQ(self):
            return self.getToken(MT22Parser.MOR_EQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def LESS_EQ(self):
            return self.getToken(MT22Parser.LESS_EQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relat_expr




    def relat_expr(self):

        localctx = MT22Parser.Relat_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relat_expr)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.expr1(0)
                self.state = 191
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MT22Parser.Expr1Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 200
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 201
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 202
                    self.expr2(0) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 211
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 212
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 213
                    self.expr3(0) 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 224
                    self.expr4() 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr4




    def expr4(self):

        localctx = MT22Parser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr4)
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(MT22Parser.NOT)
                self.state = 231
                self.expr4()
                pass
            elif token in [2, 16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.expr5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr5)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MT22Parser.SUB)
                self.state = 236
                self.expr5()
                pass
            elif token in [16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexes(self):
            return self.getTypedRuleContext(MT22Parser.IndexesContext,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr6)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(MT22Parser.ID)
                self.state = 241
                self.indexes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expr7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACK(self):
            return self.getToken(MT22Parser.LEFT_BRACK, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def RIGHT_BRACK(self):
            return self.getToken(MT22Parser.RIGHT_BRACK, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexes




    def indexes(self):

        localctx = MT22Parser.IndexesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_indexes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 246
            self.exprs_list()
            self.state = 247
            self.match(MT22Parser.RIGHT_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr7




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr7)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.operand()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MT22Parser.LEFT_PAREN)
                self.state = 251
                self.expr()
                self.state = 252
                self.match(MT22Parser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operand




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operand)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_call




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MT22Parser.ID)
            self.state = 262
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 263
                self.exprs_list()


            self.state = 266
            self.match(MT22Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MT22Parser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MT22Parser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(MT22Parser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MT22Parser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(MT22Parser.Array_litContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(MT22Parser.INT_LIT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(MT22Parser.FLOAT_LIT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.match(MT22Parser.BOOL_LIT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.match(MT22Parser.STRING_LIT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 272
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exprs_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprs_list




    def exprs_list(self):

        localctx = MT22Parser.Exprs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exprs_list)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.expr()
                self.state = 276
                self.match(MT22Parser.COMMA)
                self.state = 277
                self.exprs_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(MT22Parser.Stmt_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Var_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt_list




    def stmt_list(self):

        localctx = MT22Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt_list)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 283
                    self.var_decl()
                    pass


                self.state = 286
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 288
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 289
                    self.var_decl()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MT22Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MT22Parser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 298
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 299
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 300
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 301
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 302
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 303
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_left(self):
            return self.getTypedRuleContext(MT22Parser.Assign_leftContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def assign_right(self):
            return self.getTypedRuleContext(MT22Parser.Assign_rightContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = MT22Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.assign_left()
            self.state = 307
            self.match(MT22Parser.ASSIGN)
            self.state = 308
            self.assign_right()
            self.state = 309
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_leftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(MT22Parser.Scalar_varContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexes(self):
            return self.getTypedRuleContext(MT22Parser.IndexesContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign_left




    def assign_left(self):

        localctx = MT22Parser.Assign_leftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assign_left)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(MT22Parser.ID)
                self.state = 313
                self.indexes()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_rightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign_right




    def assign_right(self):

        localctx = MT22Parser.Assign_rightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign_right)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_stmt




    def if_stmt(self):

        localctx = MT22Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(MT22Parser.IF)
            self.state = 319
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 320
            self.expr()
            self.state = 321
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 322
            self.stmt()
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 323
                self.match(MT22Parser.ELSE)
                self.state = 324
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def initial_expr(self):
            return self.getTypedRuleContext(MT22Parser.Initial_exprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def condition_expr(self):
            return self.getTypedRuleContext(MT22Parser.Condition_exprContext,0)


        def upd8_expr(self):
            return self.getTypedRuleContext(MT22Parser.Upd8_exprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_stmt




    def for_stmt(self):

        localctx = MT22Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MT22Parser.FOR)
            self.state = 328
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 329
            self.initial_expr()
            self.state = 330
            self.match(MT22Parser.COMMA)
            self.state = 331
            self.condition_expr()
            self.state = 332
            self.match(MT22Parser.COMMA)
            self.state = 333
            self.upd8_expr()
            self.state = 334
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 335
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initial_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(MT22Parser.Scalar_varContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_initial_expr




    def initial_expr(self):

        localctx = MT22Parser.Initial_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_initial_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.scalar_var()
            self.state = 338
            self.match(MT22Parser.ASSIGN)
            self.state = 339
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_condition_expr




    def condition_expr(self):

        localctx = MT22Parser.Condition_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_condition_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Upd8_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_upd8_expr




    def upd8_expr(self):

        localctx = MT22Parser.Upd8_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_upd8_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_stmt




    def while_stmt(self):

        localctx = MT22Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MT22Parser.WHILE)
            self.state = 346
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 347
            self.expr()
            self.state = 348
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 349
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MT22Parser.DO)
            self.state = 352
            self.block_stmt()
            self.state = 353
            self.match(MT22Parser.WHILE)
            self.state = 354
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 355
            self.expr()
            self.state = 356
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 357
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = MT22Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MT22Parser.BREAK)
            self.state = 360
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MT22Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MT22Parser.CONTINUE)
            self.state = 363
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MT22Parser.RETURN)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 366
                self.expr()


            self.state = 369
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call_stmt




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.func_call()
            self.state = 372
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(MT22Parser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MT22Parser.RIGHT_BRACE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(MT22Parser.Stmt_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_stmt




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36673703539376128) != 0):
                self.state = 375
                self.stmt_list()


            self.state = 378
            self.match(MT22Parser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalar_var




    def scalar_var(self):

        localctx = MT22Parser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_bool_type




    def bool_type(self):

        localctx = MT22Parser.Bool_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_bool_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MT22Parser.BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_int_type




    def int_type(self):

        localctx = MT22Parser.Int_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_int_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MT22Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_float_type




    def float_type(self):

        localctx = MT22Parser.Float_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_float_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MT22Parser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_type




    def string_type(self):

        localctx = MT22Parser.String_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_string_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MT22Parser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_void_type




    def void_type(self):

        localctx = MT22Parser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MT22Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Auto_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_auto_type




    def auto_type(self):

        localctx = MT22Parser.Auto_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_auto_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MT22Parser.AUTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LEFT_BRACK(self):
            return self.getToken(MT22Parser.LEFT_BRACK, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RIGHT_BRACK(self):
            return self.getToken(MT22Parser.RIGHT_BRACK, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MT22Parser.ARRAY)
            self.state = 395
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 396
            self.dimensions()
            self.state = 397
            self.match(MT22Parser.RIGHT_BRACK)
            self.state = 398
            self.match(MT22Parser.OF)
            self.state = 399
            self.atomic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INT_LIT)
            else:
                return self.getToken(MT22Parser.INT_LIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MT22Parser.INT_LIT)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 402
                self.match(MT22Parser.COMMA)
                self.state = 403
                self.match(MT22Parser.INT_LIT)
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_type(self):
            return self.getTypedRuleContext(MT22Parser.Bool_typeContext,0)


        def int_type(self):
            return self.getTypedRuleContext(MT22Parser.Int_typeContext,0)


        def float_type(self):
            return self.getTypedRuleContext(MT22Parser.Float_typeContext,0)


        def string_type(self):
            return self.getTypedRuleContext(MT22Parser.String_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_type




    def atomic_type(self):

        localctx = MT22Parser.Atomic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_atomic_type)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.bool_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.int_type()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.float_type()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.string_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr1_sempred
        self._predicates[13] = self.expr2_sempred
        self._predicates[14] = self.expr3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




