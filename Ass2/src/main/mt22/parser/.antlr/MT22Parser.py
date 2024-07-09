# Generated from d:/DHBK/233/PPL_Assignments/Ass2/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
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
        4,1,59,436,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,114,8,1,1,2,1,2,3,2,118,8,2,1,3,
        1,3,3,3,122,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,131,8,4,1,4,1,4,
        3,4,135,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,145,8,5,10,5,12,
        5,148,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,158,8,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,3,7,167,8,7,1,7,1,7,3,7,171,8,7,1,7,1,7,1,7,3,
        7,176,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,185,8,8,1,9,3,9,188,8,
        9,1,9,3,9,191,8,9,1,9,1,9,1,9,1,9,1,9,3,9,198,8,9,1,10,1,10,1,11,
        1,11,1,12,1,12,1,12,1,12,1,12,3,12,209,8,12,1,13,1,13,1,13,1,13,
        1,13,3,13,216,8,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,224,8,14,10,
        14,12,14,227,9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,235,8,15,10,
        15,12,15,238,9,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,246,8,16,10,
        16,12,16,249,9,16,1,17,1,17,1,17,3,17,254,8,17,1,18,1,18,1,18,3,
        18,259,8,18,1,19,1,19,1,19,3,19,264,8,19,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,3,21,275,8,21,1,22,1,22,1,22,3,22,280,8,22,1,
        23,1,23,1,23,3,23,285,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,
        24,294,8,24,1,25,1,25,1,25,1,25,1,25,3,25,301,8,25,1,26,1,26,3,26,
        305,8,26,1,26,1,26,1,26,1,26,3,26,311,8,26,3,26,313,8,26,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,325,8,27,1,28,1,
        28,1,28,1,28,1,28,1,29,1,29,1,29,3,29,335,8,29,1,30,1,30,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,3,31,346,8,31,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,35,1,
        35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,
        37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,3,40,388,8,40,1,
        40,1,40,1,41,1,41,1,41,1,42,1,42,3,42,397,8,42,1,42,1,42,1,43,1,
        43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,
        50,1,50,1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,51,5,51,425,8,51,10,
        51,12,51,428,9,51,1,52,1,52,1,52,1,52,3,52,434,8,52,1,52,0,3,28,
        30,32,53,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,90,92,94,96,98,100,102,104,0,4,1,0,9,14,1,0,7,8,1,0,1,2,
        1,0,3,5,437,0,106,1,0,0,0,2,113,1,0,0,0,4,117,1,0,0,0,6,119,1,0,
        0,0,8,125,1,0,0,0,10,139,1,0,0,0,12,157,1,0,0,0,14,159,1,0,0,0,16,
        184,1,0,0,0,18,187,1,0,0,0,20,199,1,0,0,0,22,201,1,0,0,0,24,208,
        1,0,0,0,26,215,1,0,0,0,28,217,1,0,0,0,30,228,1,0,0,0,32,239,1,0,
        0,0,34,253,1,0,0,0,36,258,1,0,0,0,38,263,1,0,0,0,40,265,1,0,0,0,
        42,274,1,0,0,0,44,279,1,0,0,0,46,281,1,0,0,0,48,293,1,0,0,0,50,300,
        1,0,0,0,52,312,1,0,0,0,54,324,1,0,0,0,56,326,1,0,0,0,58,334,1,0,
        0,0,60,336,1,0,0,0,62,338,1,0,0,0,64,347,1,0,0,0,66,357,1,0,0,0,
        68,361,1,0,0,0,70,363,1,0,0,0,72,365,1,0,0,0,74,371,1,0,0,0,76,379,
        1,0,0,0,78,382,1,0,0,0,80,385,1,0,0,0,82,391,1,0,0,0,84,394,1,0,
        0,0,86,400,1,0,0,0,88,402,1,0,0,0,90,404,1,0,0,0,92,406,1,0,0,0,
        94,408,1,0,0,0,96,410,1,0,0,0,98,412,1,0,0,0,100,414,1,0,0,0,102,
        421,1,0,0,0,104,433,1,0,0,0,106,107,3,2,1,0,107,108,5,0,0,1,108,
        1,1,0,0,0,109,110,3,4,2,0,110,111,3,2,1,0,111,114,1,0,0,0,112,114,
        3,4,2,0,113,109,1,0,0,0,113,112,1,0,0,0,114,3,1,0,0,0,115,118,3,
        8,4,0,116,118,3,14,7,0,117,115,1,0,0,0,117,116,1,0,0,0,118,5,1,0,
        0,0,119,121,5,20,0,0,120,122,3,50,25,0,121,120,1,0,0,0,121,122,1,
        0,0,0,122,123,1,0,0,0,123,124,5,21,0,0,124,7,1,0,0,0,125,126,3,10,
        5,0,126,130,5,25,0,0,127,131,3,104,52,0,128,131,3,100,50,0,129,131,
        3,98,49,0,130,127,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,134,
        1,0,0,0,132,133,5,26,0,0,133,135,3,12,6,0,134,132,1,0,0,0,134,135,
        1,0,0,0,135,136,1,0,0,0,136,137,6,4,-1,0,137,138,5,24,0,0,138,9,
        1,0,0,0,139,140,5,55,0,0,140,146,6,5,-1,0,141,142,5,22,0,0,142,143,
        5,55,0,0,143,145,6,5,-1,0,144,141,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,146,147,1,0,0,0,147,11,1,0,0,0,148,146,1,0,0,0,149,150,3,
        22,11,0,150,151,6,6,-1,0,151,152,5,22,0,0,152,153,3,12,6,0,153,158,
        1,0,0,0,154,155,3,22,11,0,155,156,6,6,-1,0,156,158,1,0,0,0,157,149,
        1,0,0,0,157,154,1,0,0,0,158,13,1,0,0,0,159,160,5,55,0,0,160,161,
        5,25,0,0,161,166,5,40,0,0,162,167,3,104,52,0,163,167,3,96,48,0,164,
        167,3,98,49,0,165,167,3,100,50,0,166,162,1,0,0,0,166,163,1,0,0,0,
        166,164,1,0,0,0,166,165,1,0,0,0,167,168,1,0,0,0,168,170,5,16,0,0,
        169,171,3,16,8,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,
        172,175,5,17,0,0,173,174,5,51,0,0,174,176,5,55,0,0,175,173,1,0,0,
        0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,3,20,10,0,178,15,1,0,0,
        0,179,180,3,18,9,0,180,181,5,22,0,0,181,182,3,16,8,0,182,185,1,0,
        0,0,183,185,3,18,9,0,184,179,1,0,0,0,184,183,1,0,0,0,185,17,1,0,
        0,0,186,188,5,51,0,0,187,186,1,0,0,0,187,188,1,0,0,0,188,190,1,0,
        0,0,189,191,5,48,0,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,
        0,0,192,193,5,55,0,0,193,197,5,25,0,0,194,198,3,104,52,0,195,198,
        3,100,50,0,196,198,3,98,49,0,197,194,1,0,0,0,197,195,1,0,0,0,197,
        196,1,0,0,0,198,19,1,0,0,0,199,200,3,84,42,0,200,21,1,0,0,0,201,
        202,3,24,12,0,202,23,1,0,0,0,203,204,3,26,13,0,204,205,5,15,0,0,
        205,206,3,26,13,0,206,209,1,0,0,0,207,209,3,26,13,0,208,203,1,0,
        0,0,208,207,1,0,0,0,209,25,1,0,0,0,210,211,3,28,14,0,211,212,7,0,
        0,0,212,213,3,28,14,0,213,216,1,0,0,0,214,216,3,28,14,0,215,210,
        1,0,0,0,215,214,1,0,0,0,216,27,1,0,0,0,217,218,6,14,-1,0,218,219,
        3,30,15,0,219,225,1,0,0,0,220,221,10,2,0,0,221,222,7,1,0,0,222,224,
        3,30,15,0,223,220,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,
        1,0,0,0,226,29,1,0,0,0,227,225,1,0,0,0,228,229,6,15,-1,0,229,230,
        3,32,16,0,230,236,1,0,0,0,231,232,10,2,0,0,232,233,7,2,0,0,233,235,
        3,32,16,0,234,231,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,
        1,0,0,0,237,31,1,0,0,0,238,236,1,0,0,0,239,240,6,16,-1,0,240,241,
        3,34,17,0,241,247,1,0,0,0,242,243,10,2,0,0,243,244,7,3,0,0,244,246,
        3,34,17,0,245,242,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,248,
        1,0,0,0,248,33,1,0,0,0,249,247,1,0,0,0,250,251,5,6,0,0,251,254,3,
        34,17,0,252,254,3,36,18,0,253,250,1,0,0,0,253,252,1,0,0,0,254,35,
        1,0,0,0,255,256,5,2,0,0,256,259,3,36,18,0,257,259,3,38,19,0,258,
        255,1,0,0,0,258,257,1,0,0,0,259,37,1,0,0,0,260,261,5,55,0,0,261,
        264,3,40,20,0,262,264,3,42,21,0,263,260,1,0,0,0,263,262,1,0,0,0,
        264,39,1,0,0,0,265,266,5,18,0,0,266,267,3,50,25,0,267,268,5,19,0,
        0,268,41,1,0,0,0,269,275,3,44,22,0,270,271,5,16,0,0,271,272,3,22,
        11,0,272,273,5,17,0,0,273,275,1,0,0,0,274,269,1,0,0,0,274,270,1,
        0,0,0,275,43,1,0,0,0,276,280,3,48,24,0,277,280,3,46,23,0,278,280,
        5,55,0,0,279,276,1,0,0,0,279,277,1,0,0,0,279,278,1,0,0,0,280,45,
        1,0,0,0,281,282,5,55,0,0,282,284,5,16,0,0,283,285,3,50,25,0,284,
        283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,5,17,0,0,287,
        47,1,0,0,0,288,294,5,28,0,0,289,294,5,29,0,0,290,294,5,30,0,0,291,
        294,5,31,0,0,292,294,3,6,3,0,293,288,1,0,0,0,293,289,1,0,0,0,293,
        290,1,0,0,0,293,291,1,0,0,0,293,292,1,0,0,0,294,49,1,0,0,0,295,296,
        3,22,11,0,296,297,5,22,0,0,297,298,3,50,25,0,298,301,1,0,0,0,299,
        301,3,22,11,0,300,295,1,0,0,0,300,299,1,0,0,0,301,51,1,0,0,0,302,
        305,3,54,27,0,303,305,3,8,4,0,304,302,1,0,0,0,304,303,1,0,0,0,305,
        306,1,0,0,0,306,307,3,52,26,0,307,313,1,0,0,0,308,311,3,54,27,0,
        309,311,3,8,4,0,310,308,1,0,0,0,310,309,1,0,0,0,311,313,1,0,0,0,
        312,304,1,0,0,0,312,310,1,0,0,0,313,53,1,0,0,0,314,325,3,56,28,0,
        315,325,3,62,31,0,316,325,3,64,32,0,317,325,3,72,36,0,318,325,3,
        74,37,0,319,325,3,76,38,0,320,325,3,78,39,0,321,325,3,80,40,0,322,
        325,3,82,41,0,323,325,3,84,42,0,324,314,1,0,0,0,324,315,1,0,0,0,
        324,316,1,0,0,0,324,317,1,0,0,0,324,318,1,0,0,0,324,319,1,0,0,0,
        324,320,1,0,0,0,324,321,1,0,0,0,324,322,1,0,0,0,324,323,1,0,0,0,
        325,55,1,0,0,0,326,327,3,58,29,0,327,328,5,26,0,0,328,329,3,60,30,
        0,329,330,5,24,0,0,330,57,1,0,0,0,331,335,3,86,43,0,332,333,5,55,
        0,0,333,335,3,40,20,0,334,331,1,0,0,0,334,332,1,0,0,0,335,59,1,0,
        0,0,336,337,3,22,11,0,337,61,1,0,0,0,338,339,5,41,0,0,339,340,5,
        16,0,0,340,341,3,22,11,0,341,342,5,17,0,0,342,345,3,54,27,0,343,
        344,5,36,0,0,344,346,3,54,27,0,345,343,1,0,0,0,345,346,1,0,0,0,346,
        63,1,0,0,0,347,348,5,39,0,0,348,349,5,16,0,0,349,350,3,66,33,0,350,
        351,5,22,0,0,351,352,3,68,34,0,352,353,5,22,0,0,353,354,3,70,35,
        0,354,355,5,17,0,0,355,356,3,54,27,0,356,65,1,0,0,0,357,358,3,86,
        43,0,358,359,5,26,0,0,359,360,3,22,11,0,360,67,1,0,0,0,361,362,3,
        22,11,0,362,69,1,0,0,0,363,364,3,22,11,0,364,71,1,0,0,0,365,366,
        5,46,0,0,366,367,5,16,0,0,367,368,3,22,11,0,368,369,5,17,0,0,369,
        370,3,54,27,0,370,73,1,0,0,0,371,372,5,35,0,0,372,373,3,84,42,0,
        373,374,5,46,0,0,374,375,5,16,0,0,375,376,3,22,11,0,376,377,5,17,
        0,0,377,378,5,24,0,0,378,75,1,0,0,0,379,380,5,33,0,0,380,381,5,24,
        0,0,381,77,1,0,0,0,382,383,5,49,0,0,383,384,5,24,0,0,384,79,1,0,
        0,0,385,387,5,43,0,0,386,388,3,22,11,0,387,386,1,0,0,0,387,388,1,
        0,0,0,388,389,1,0,0,0,389,390,5,24,0,0,390,81,1,0,0,0,391,392,3,
        46,23,0,392,393,5,24,0,0,393,83,1,0,0,0,394,396,5,20,0,0,395,397,
        3,52,26,0,396,395,1,0,0,0,396,397,1,0,0,0,397,398,1,0,0,0,398,399,
        5,21,0,0,399,85,1,0,0,0,400,401,5,55,0,0,401,87,1,0,0,0,402,403,
        5,34,0,0,403,89,1,0,0,0,404,405,5,42,0,0,405,91,1,0,0,0,406,407,
        5,38,0,0,407,93,1,0,0,0,408,409,5,44,0,0,409,95,1,0,0,0,410,411,
        5,47,0,0,411,97,1,0,0,0,412,413,5,32,0,0,413,99,1,0,0,0,414,415,
        5,52,0,0,415,416,5,18,0,0,416,417,3,102,51,0,417,418,5,19,0,0,418,
        419,5,50,0,0,419,420,3,104,52,0,420,101,1,0,0,0,421,426,5,28,0,0,
        422,423,5,22,0,0,423,425,5,28,0,0,424,422,1,0,0,0,425,428,1,0,0,
        0,426,424,1,0,0,0,426,427,1,0,0,0,427,103,1,0,0,0,428,426,1,0,0,
        0,429,434,3,88,44,0,430,434,3,90,45,0,431,434,3,92,46,0,432,434,
        3,94,47,0,433,429,1,0,0,0,433,430,1,0,0,0,433,431,1,0,0,0,433,432,
        1,0,0,0,434,105,1,0,0,0,37,113,117,121,130,134,146,157,166,170,175,
        184,187,190,197,208,215,225,236,247,253,258,263,274,279,284,293,
        300,304,310,312,324,334,345,387,396,426,433
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
    RULE_idlist = 5
    RULE_exprs_list_var_decl = 6
    RULE_func_decl = 7
    RULE_params_list = 8
    RULE_param = 9
    RULE_body = 10
    RULE_expr = 11
    RULE_string_expr = 12
    RULE_relat_expr = 13
    RULE_expr1 = 14
    RULE_expr2 = 15
    RULE_expr3 = 16
    RULE_expr4 = 17
    RULE_expr5 = 18
    RULE_expr6 = 19
    RULE_indexes = 20
    RULE_expr7 = 21
    RULE_operand = 22
    RULE_func_call = 23
    RULE_literal = 24
    RULE_exprs_list = 25
    RULE_stmt_list = 26
    RULE_stmt = 27
    RULE_assign_stmt = 28
    RULE_assign_left = 29
    RULE_assign_right = 30
    RULE_if_stmt = 31
    RULE_for_stmt = 32
    RULE_initial_expr = 33
    RULE_condition_expr = 34
    RULE_upd8_expr = 35
    RULE_while_stmt = 36
    RULE_do_while_stmt = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_return_stmt = 40
    RULE_call_stmt = 41
    RULE_block_stmt = 42
    RULE_scalar_var = 43
    RULE_bool_type = 44
    RULE_int_type = 45
    RULE_float_type = 46
    RULE_string_type = 47
    RULE_void_type = 48
    RULE_auto_type = 49
    RULE_array_type = 50
    RULE_dimensions = 51
    RULE_atomic_type = 52

    ruleNames =  [ "program", "decls", "decl", "array_lit", "var_decl", 
                   "idlist", "exprs_list_var_decl", "func_decl", "params_list", 
                   "param", "body", "expr", "string_expr", "relat_expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "indexes", "expr7", "operand", "func_call", "literal", 
                   "exprs_list", "stmt_list", "stmt", "assign_stmt", "assign_left", 
                   "assign_right", "if_stmt", "for_stmt", "initial_expr", 
                   "condition_expr", "upd8_expr", "while_stmt", "do_while_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "call_stmt", 
                   "block_stmt", "scalar_var", "bool_type", "int_type", 
                   "float_type", "string_type", "void_type", "auto_type", 
                   "array_type", "dimensions", "atomic_type" ]

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.decls()
            self.state = 107
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.decl()
                self.state = 110
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
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

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_lit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_lit" ):
                listener.enterArray_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_lit" ):
                listener.exitArray_lit(self)




    def array_lit(self):

        localctx = MT22Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 120
                self.exprs_list()


            self.state = 123
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

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def exprs_list_var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_list_var_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = MT22Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.idlist()
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
                self.exprs_list_var_decl()


            self.check(True)
            self.state = 137
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlist" ):
                listener.enterIdlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlist" ):
                listener.exitIdlist(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MT22Parser.ID)
            self.ids_size += 2
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 141
                self.match(MT22Parser.COMMA)
                self.state = 142
                self.match(MT22Parser.ID)
                self.ids_size += 1
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exprs_list_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprs_list_var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_list_var_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprs_list_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs_list_var_decl" ):
                listener.enterExprs_list_var_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs_list_var_decl" ):
                listener.exitExprs_list_var_decl(self)




    def exprs_list_var_decl(self):

        localctx = MT22Parser.Exprs_list_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprs_list_var_decl)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.expr()
                self.check(False)
                self.state = 151
                self.match(MT22Parser.COMMA)
                self.state = 152
                self.exprs_list_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.expr()
                self.exprs_size += 2
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


        def params_list(self):
            return self.getTypedRuleContext(MT22Parser.Params_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)




    def func_decl(self):

        localctx = MT22Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(MT22Parser.ID)
            self.state = 160
            self.match(MT22Parser.COLON)
            self.state = 161
            self.match(MT22Parser.FUNCTION)
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 162
                self.atomic_type()
                pass
            elif token in [47]:
                self.state = 163
                self.void_type()
                pass
            elif token in [32]:
                self.state = 164
                self.auto_type()
                pass
            elif token in [52]:
                self.state = 165
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 168
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 38562071809359872) != 0):
                self.state = 169
                self.params_list()


            self.state = 172
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 173
                self.match(MT22Parser.INHERIT)
                self.state = 174
                self.match(MT22Parser.ID)


            self.state = 177
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_list" ):
                listener.enterParams_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_list" ):
                listener.exitParams_list(self)




    def params_list(self):

        localctx = MT22Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params_list)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.param()
                self.state = 180
                self.match(MT22Parser.COMMA)
                self.state = 181
                self.params_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 186
                self.match(MT22Parser.INHERIT)


            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 189
                self.match(MT22Parser.OUT)


            self.state = 192
            self.match(MT22Parser.ID)
            self.state = 193
            self.match(MT22Parser.COLON)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 194
                self.atomic_type()
                pass
            elif token in [52]:
                self.state = 195
                self.array_type()
                pass
            elif token in [32]:
                self.state = 196
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_expr" ):
                listener.enterString_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_expr" ):
                listener.exitString_expr(self)




    def string_expr(self):

        localctx = MT22Parser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_string_expr)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.relat_expr()
                self.state = 204
                self.match(MT22Parser.SCOPE)
                self.state = 205
                self.relat_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelat_expr" ):
                listener.enterRelat_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelat_expr" ):
                listener.exitRelat_expr(self)




    def relat_expr(self):

        localctx = MT22Parser.Relat_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relat_expr)
        self._la = 0 # Token type
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.expr1(0)
                self.state = 211
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 220
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 221
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 222
                    self.expr2(0) 
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 233
                    self.expr3(0) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr3" ):
                listener.enterExpr3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr3" ):
                listener.exitExpr3(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.expr4() 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr4" ):
                listener.enterExpr4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr4" ):
                listener.exitExpr4(self)




    def expr4(self):

        localctx = MT22Parser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr4)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(MT22Parser.NOT)
                self.state = 251
                self.expr4()
                pass
            elif token in [2, 16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr5" ):
                listener.enterExpr5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr5" ):
                listener.exitExpr5(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr5)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(MT22Parser.SUB)
                self.state = 256
                self.expr5()
                pass
            elif token in [16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr6" ):
                listener.enterExpr6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr6" ):
                listener.exitExpr6(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr6)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(MT22Parser.ID)
                self.state = 261
                self.indexes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexes" ):
                listener.enterIndexes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexes" ):
                listener.exitIndexes(self)




    def indexes(self):

        localctx = MT22Parser.IndexesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_indexes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 266
            self.exprs_list()
            self.state = 267
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr7" ):
                listener.enterExpr7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr7" ):
                listener.exitExpr7(self)




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr7)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.operand()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(MT22Parser.LEFT_PAREN)
                self.state = 271
                self.expr()
                self.state = 272
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MT22Parser.ID)
            self.state = 282
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 283
                self.exprs_list()


            self.state = 286
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(MT22Parser.INT_LIT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(MT22Parser.FLOAT_LIT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
                self.match(MT22Parser.BOOL_LIT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.match(MT22Parser.STRING_LIT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs_list" ):
                listener.enterExprs_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs_list" ):
                listener.exitExprs_list(self)




    def exprs_list(self):

        localctx = MT22Parser.Exprs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprs_list)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.expr()
                self.state = 296
                self.match(MT22Parser.COMMA)
                self.state = 297
                self.exprs_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)




    def stmt_list(self):

        localctx = MT22Parser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_list)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 302
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 303
                    self.var_decl()
                    pass


                self.state = 306
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 308
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 309
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 317
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 318
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 319
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 320
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 321
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 322
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 323
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = MT22Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.assign_left()
            self.state = 327
            self.match(MT22Parser.ASSIGN)
            self.state = 328
            self.assign_right()
            self.state = 329
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_left" ):
                listener.enterAssign_left(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_left" ):
                listener.exitAssign_left(self)




    def assign_left(self):

        localctx = MT22Parser.Assign_leftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assign_left)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(MT22Parser.ID)
                self.state = 333
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_right" ):
                listener.enterAssign_right(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_right" ):
                listener.exitAssign_right(self)




    def assign_right(self):

        localctx = MT22Parser.Assign_rightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign_right)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = MT22Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MT22Parser.IF)
            self.state = 339
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 340
            self.expr()
            self.state = 341
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 342
            self.stmt()
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 343
                self.match(MT22Parser.ELSE)
                self.state = 344
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)




    def for_stmt(self):

        localctx = MT22Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(MT22Parser.FOR)
            self.state = 348
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 349
            self.initial_expr()
            self.state = 350
            self.match(MT22Parser.COMMA)
            self.state = 351
            self.condition_expr()
            self.state = 352
            self.match(MT22Parser.COMMA)
            self.state = 353
            self.upd8_expr()
            self.state = 354
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 355
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitial_expr" ):
                listener.enterInitial_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitial_expr" ):
                listener.exitInitial_expr(self)




    def initial_expr(self):

        localctx = MT22Parser.Initial_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_initial_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.scalar_var()
            self.state = 358
            self.match(MT22Parser.ASSIGN)
            self.state = 359
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_expr" ):
                listener.enterCondition_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_expr" ):
                listener.exitCondition_expr(self)




    def condition_expr(self):

        localctx = MT22Parser.Condition_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_condition_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpd8_expr" ):
                listener.enterUpd8_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpd8_expr" ):
                listener.exitUpd8_expr(self)




    def upd8_expr(self):

        localctx = MT22Parser.Upd8_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_upd8_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = MT22Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MT22Parser.WHILE)
            self.state = 366
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 367
            self.expr()
            self.state = 368
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 369
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while_stmt" ):
                listener.enterDo_while_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while_stmt" ):
                listener.exitDo_while_stmt(self)




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(MT22Parser.DO)
            self.state = 372
            self.block_stmt()
            self.state = 373
            self.match(MT22Parser.WHILE)
            self.state = 374
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 375
            self.expr()
            self.state = 376
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 377
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)




    def break_stmt(self):

        localctx = MT22Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(MT22Parser.BREAK)
            self.state = 380
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_stmt" ):
                listener.enterContinue_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_stmt" ):
                listener.exitContinue_stmt(self)




    def continue_stmt(self):

        localctx = MT22Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MT22Parser.CONTINUE)
            self.state = 383
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MT22Parser.RETURN)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 386
                self.expr()


            self.state = 389
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_stmt" ):
                listener.enterCall_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_stmt" ):
                listener.exitCall_stmt(self)




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.func_call()
            self.state = 392
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stmt" ):
                listener.enterBlock_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stmt" ):
                listener.exitBlock_stmt(self)




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36673703539376128) != 0):
                self.state = 395
                self.stmt_list()


            self.state = 398
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalar_var" ):
                listener.enterScalar_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalar_var" ):
                listener.exitScalar_var(self)




    def scalar_var(self):

        localctx = MT22Parser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_type" ):
                listener.enterBool_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_type" ):
                listener.exitBool_type(self)




    def bool_type(self):

        localctx = MT22Parser.Bool_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_bool_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_type" ):
                listener.enterInt_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_type" ):
                listener.exitInt_type(self)




    def int_type(self):

        localctx = MT22Parser.Int_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_int_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_type" ):
                listener.enterFloat_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_type" ):
                listener.exitFloat_type(self)




    def float_type(self):

        localctx = MT22Parser.Float_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_float_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_type" ):
                listener.enterString_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_type" ):
                listener.exitString_type(self)




    def string_type(self):

        localctx = MT22Parser.String_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_string_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid_type" ):
                listener.enterVoid_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid_type" ):
                listener.exitVoid_type(self)




    def void_type(self):

        localctx = MT22Parser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAuto_type" ):
                listener.enterAuto_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAuto_type" ):
                listener.exitAuto_type(self)




    def auto_type(self):

        localctx = MT22Parser.Auto_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_auto_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(MT22Parser.ARRAY)
            self.state = 415
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 416
            self.dimensions()
            self.state = 417
            self.match(MT22Parser.RIGHT_BRACK)
            self.state = 418
            self.match(MT22Parser.OF)
            self.state = 419
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensions" ):
                listener.enterDimensions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensions" ):
                listener.exitDimensions(self)




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MT22Parser.INT_LIT)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 422
                self.match(MT22Parser.COMMA)
                self.state = 423
                self.match(MT22Parser.INT_LIT)
                self.state = 428
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic_type" ):
                listener.enterAtomic_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic_type" ):
                listener.exitAtomic_type(self)




    def atomic_type(self):

        localctx = MT22Parser.Atomic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_atomic_type)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.bool_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.int_type()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.float_type()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
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
        self._predicates[14] = self.expr1_sempred
        self._predicates[15] = self.expr2_sempred
        self._predicates[16] = self.expr3_sempred
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
         




