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
        4,1,59,441,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,116,8,1,1,2,1,2,3,2,120,
        8,2,1,3,1,3,3,3,124,8,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,3,5,133,8,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,146,8,6,1,6,1,6,
        1,6,3,6,151,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,161,8,7,3,7,
        163,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,172,8,8,1,8,1,8,3,8,176,
        8,8,1,8,1,8,1,8,3,8,181,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,190,
        8,9,1,10,3,10,193,8,10,1,10,3,10,196,8,10,1,10,1,10,1,10,1,10,1,
        10,3,10,203,8,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,
        13,214,8,13,1,14,1,14,1,14,1,14,1,14,3,14,221,8,14,1,15,1,15,1,15,
        1,15,1,15,1,15,5,15,229,8,15,10,15,12,15,232,9,15,1,16,1,16,1,16,
        1,16,1,16,1,16,5,16,240,8,16,10,16,12,16,243,9,16,1,17,1,17,1,17,
        1,17,1,17,1,17,5,17,251,8,17,10,17,12,17,254,9,17,1,18,1,18,1,18,
        3,18,259,8,18,1,19,1,19,1,19,3,19,264,8,19,1,20,1,20,1,20,3,20,269,
        8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,280,8,22,
        1,23,1,23,1,23,3,23,285,8,23,1,24,1,24,1,24,3,24,290,8,24,1,24,1,
        24,1,25,1,25,1,25,1,25,1,25,3,25,299,8,25,1,26,1,26,1,26,1,26,1,
        26,3,26,306,8,26,1,27,1,27,3,27,310,8,27,1,27,1,27,1,27,1,27,3,27,
        316,8,27,3,27,318,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,3,28,330,8,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,3,
        30,340,8,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,351,
        8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,
        1,41,1,41,3,41,393,8,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,3,43,
        402,8,43,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,
        1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,52,
        1,52,1,52,5,52,430,8,52,10,52,12,52,433,9,52,1,53,1,53,1,53,1,53,
        3,53,439,8,53,1,53,0,3,30,32,34,54,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,
        0,4,1,0,9,14,1,0,7,8,1,0,1,2,1,0,3,5,443,0,108,1,0,0,0,2,115,1,0,
        0,0,4,119,1,0,0,0,6,121,1,0,0,0,8,127,1,0,0,0,10,132,1,0,0,0,12,
        150,1,0,0,0,14,162,1,0,0,0,16,164,1,0,0,0,18,189,1,0,0,0,20,192,
        1,0,0,0,22,204,1,0,0,0,24,206,1,0,0,0,26,213,1,0,0,0,28,220,1,0,
        0,0,30,222,1,0,0,0,32,233,1,0,0,0,34,244,1,0,0,0,36,258,1,0,0,0,
        38,263,1,0,0,0,40,268,1,0,0,0,42,270,1,0,0,0,44,279,1,0,0,0,46,284,
        1,0,0,0,48,286,1,0,0,0,50,298,1,0,0,0,52,305,1,0,0,0,54,317,1,0,
        0,0,56,329,1,0,0,0,58,331,1,0,0,0,60,339,1,0,0,0,62,341,1,0,0,0,
        64,343,1,0,0,0,66,352,1,0,0,0,68,362,1,0,0,0,70,366,1,0,0,0,72,368,
        1,0,0,0,74,370,1,0,0,0,76,376,1,0,0,0,78,384,1,0,0,0,80,387,1,0,
        0,0,82,390,1,0,0,0,84,396,1,0,0,0,86,399,1,0,0,0,88,405,1,0,0,0,
        90,407,1,0,0,0,92,409,1,0,0,0,94,411,1,0,0,0,96,413,1,0,0,0,98,415,
        1,0,0,0,100,417,1,0,0,0,102,419,1,0,0,0,104,426,1,0,0,0,106,438,
        1,0,0,0,108,109,3,2,1,0,109,110,5,0,0,1,110,1,1,0,0,0,111,112,3,
        4,2,0,112,113,3,2,1,0,113,116,1,0,0,0,114,116,3,4,2,0,115,111,1,
        0,0,0,115,114,1,0,0,0,116,3,1,0,0,0,117,120,3,8,4,0,118,120,3,16,
        8,0,119,117,1,0,0,0,119,118,1,0,0,0,120,5,1,0,0,0,121,123,5,20,0,
        0,122,124,3,52,26,0,123,122,1,0,0,0,123,124,1,0,0,0,124,125,1,0,
        0,0,125,126,5,21,0,0,126,7,1,0,0,0,127,128,3,10,5,0,128,129,5,24,
        0,0,129,9,1,0,0,0,130,133,3,12,6,0,131,133,3,14,7,0,132,130,1,0,
        0,0,132,131,1,0,0,0,133,11,1,0,0,0,134,135,5,55,0,0,135,136,5,22,
        0,0,136,137,3,12,6,0,137,138,5,22,0,0,138,139,3,24,12,0,139,151,
        1,0,0,0,140,141,5,55,0,0,141,145,5,25,0,0,142,146,3,100,50,0,143,
        146,3,106,53,0,144,146,3,102,51,0,145,142,1,0,0,0,145,143,1,0,0,
        0,145,144,1,0,0,0,146,147,1,0,0,0,147,148,5,26,0,0,148,149,3,24,
        12,0,149,151,1,0,0,0,150,134,1,0,0,0,150,140,1,0,0,0,151,13,1,0,
        0,0,152,153,5,55,0,0,153,154,5,22,0,0,154,163,3,14,7,0,155,156,5,
        55,0,0,156,160,5,25,0,0,157,161,3,100,50,0,158,161,3,106,53,0,159,
        161,3,102,51,0,160,157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,
        163,1,0,0,0,162,152,1,0,0,0,162,155,1,0,0,0,163,15,1,0,0,0,164,165,
        5,55,0,0,165,166,5,25,0,0,166,171,5,40,0,0,167,172,3,106,53,0,168,
        172,3,98,49,0,169,172,3,100,50,0,170,172,3,102,51,0,171,167,1,0,
        0,0,171,168,1,0,0,0,171,169,1,0,0,0,171,170,1,0,0,0,172,173,1,0,
        0,0,173,175,5,16,0,0,174,176,3,18,9,0,175,174,1,0,0,0,175,176,1,
        0,0,0,176,177,1,0,0,0,177,180,5,17,0,0,178,179,5,51,0,0,179,181,
        5,55,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,
        3,22,11,0,183,17,1,0,0,0,184,185,3,20,10,0,185,186,5,22,0,0,186,
        187,3,18,9,0,187,190,1,0,0,0,188,190,3,20,10,0,189,184,1,0,0,0,189,
        188,1,0,0,0,190,19,1,0,0,0,191,193,5,51,0,0,192,191,1,0,0,0,192,
        193,1,0,0,0,193,195,1,0,0,0,194,196,5,48,0,0,195,194,1,0,0,0,195,
        196,1,0,0,0,196,197,1,0,0,0,197,198,5,55,0,0,198,202,5,25,0,0,199,
        203,3,106,53,0,200,203,3,102,51,0,201,203,3,100,50,0,202,199,1,0,
        0,0,202,200,1,0,0,0,202,201,1,0,0,0,203,21,1,0,0,0,204,205,3,86,
        43,0,205,23,1,0,0,0,206,207,3,26,13,0,207,25,1,0,0,0,208,209,3,28,
        14,0,209,210,5,15,0,0,210,211,3,28,14,0,211,214,1,0,0,0,212,214,
        3,28,14,0,213,208,1,0,0,0,213,212,1,0,0,0,214,27,1,0,0,0,215,216,
        3,30,15,0,216,217,7,0,0,0,217,218,3,30,15,0,218,221,1,0,0,0,219,
        221,3,30,15,0,220,215,1,0,0,0,220,219,1,0,0,0,221,29,1,0,0,0,222,
        223,6,15,-1,0,223,224,3,32,16,0,224,230,1,0,0,0,225,226,10,2,0,0,
        226,227,7,1,0,0,227,229,3,32,16,0,228,225,1,0,0,0,229,232,1,0,0,
        0,230,228,1,0,0,0,230,231,1,0,0,0,231,31,1,0,0,0,232,230,1,0,0,0,
        233,234,6,16,-1,0,234,235,3,34,17,0,235,241,1,0,0,0,236,237,10,2,
        0,0,237,238,7,2,0,0,238,240,3,34,17,0,239,236,1,0,0,0,240,243,1,
        0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,33,1,0,0,0,243,241,1,0,
        0,0,244,245,6,17,-1,0,245,246,3,36,18,0,246,252,1,0,0,0,247,248,
        10,2,0,0,248,249,7,3,0,0,249,251,3,36,18,0,250,247,1,0,0,0,251,254,
        1,0,0,0,252,250,1,0,0,0,252,253,1,0,0,0,253,35,1,0,0,0,254,252,1,
        0,0,0,255,256,5,6,0,0,256,259,3,36,18,0,257,259,3,38,19,0,258,255,
        1,0,0,0,258,257,1,0,0,0,259,37,1,0,0,0,260,261,5,2,0,0,261,264,3,
        38,19,0,262,264,3,40,20,0,263,260,1,0,0,0,263,262,1,0,0,0,264,39,
        1,0,0,0,265,266,5,55,0,0,266,269,3,42,21,0,267,269,3,44,22,0,268,
        265,1,0,0,0,268,267,1,0,0,0,269,41,1,0,0,0,270,271,5,18,0,0,271,
        272,3,52,26,0,272,273,5,19,0,0,273,43,1,0,0,0,274,280,3,46,23,0,
        275,276,5,16,0,0,276,277,3,24,12,0,277,278,5,17,0,0,278,280,1,0,
        0,0,279,274,1,0,0,0,279,275,1,0,0,0,280,45,1,0,0,0,281,285,3,50,
        25,0,282,285,3,48,24,0,283,285,5,55,0,0,284,281,1,0,0,0,284,282,
        1,0,0,0,284,283,1,0,0,0,285,47,1,0,0,0,286,287,5,55,0,0,287,289,
        5,16,0,0,288,290,3,52,26,0,289,288,1,0,0,0,289,290,1,0,0,0,290,291,
        1,0,0,0,291,292,5,17,0,0,292,49,1,0,0,0,293,299,5,28,0,0,294,299,
        5,29,0,0,295,299,5,30,0,0,296,299,5,31,0,0,297,299,3,6,3,0,298,293,
        1,0,0,0,298,294,1,0,0,0,298,295,1,0,0,0,298,296,1,0,0,0,298,297,
        1,0,0,0,299,51,1,0,0,0,300,301,3,24,12,0,301,302,5,22,0,0,302,303,
        3,52,26,0,303,306,1,0,0,0,304,306,3,24,12,0,305,300,1,0,0,0,305,
        304,1,0,0,0,306,53,1,0,0,0,307,310,3,56,28,0,308,310,3,8,4,0,309,
        307,1,0,0,0,309,308,1,0,0,0,310,311,1,0,0,0,311,312,3,54,27,0,312,
        318,1,0,0,0,313,316,3,56,28,0,314,316,3,8,4,0,315,313,1,0,0,0,315,
        314,1,0,0,0,316,318,1,0,0,0,317,309,1,0,0,0,317,315,1,0,0,0,318,
        55,1,0,0,0,319,330,3,58,29,0,320,330,3,64,32,0,321,330,3,66,33,0,
        322,330,3,74,37,0,323,330,3,76,38,0,324,330,3,78,39,0,325,330,3,
        80,40,0,326,330,3,82,41,0,327,330,3,84,42,0,328,330,3,86,43,0,329,
        319,1,0,0,0,329,320,1,0,0,0,329,321,1,0,0,0,329,322,1,0,0,0,329,
        323,1,0,0,0,329,324,1,0,0,0,329,325,1,0,0,0,329,326,1,0,0,0,329,
        327,1,0,0,0,329,328,1,0,0,0,330,57,1,0,0,0,331,332,3,60,30,0,332,
        333,5,26,0,0,333,334,3,62,31,0,334,335,5,24,0,0,335,59,1,0,0,0,336,
        340,3,88,44,0,337,338,5,55,0,0,338,340,3,42,21,0,339,336,1,0,0,0,
        339,337,1,0,0,0,340,61,1,0,0,0,341,342,3,24,12,0,342,63,1,0,0,0,
        343,344,5,41,0,0,344,345,5,16,0,0,345,346,3,24,12,0,346,347,5,17,
        0,0,347,350,3,56,28,0,348,349,5,36,0,0,349,351,3,56,28,0,350,348,
        1,0,0,0,350,351,1,0,0,0,351,65,1,0,0,0,352,353,5,39,0,0,353,354,
        5,16,0,0,354,355,3,68,34,0,355,356,5,22,0,0,356,357,3,70,35,0,357,
        358,5,22,0,0,358,359,3,72,36,0,359,360,5,17,0,0,360,361,3,56,28,
        0,361,67,1,0,0,0,362,363,3,88,44,0,363,364,5,26,0,0,364,365,3,24,
        12,0,365,69,1,0,0,0,366,367,3,24,12,0,367,71,1,0,0,0,368,369,3,24,
        12,0,369,73,1,0,0,0,370,371,5,46,0,0,371,372,5,16,0,0,372,373,3,
        24,12,0,373,374,5,17,0,0,374,375,3,56,28,0,375,75,1,0,0,0,376,377,
        5,35,0,0,377,378,3,86,43,0,378,379,5,46,0,0,379,380,5,16,0,0,380,
        381,3,24,12,0,381,382,5,17,0,0,382,383,5,24,0,0,383,77,1,0,0,0,384,
        385,5,33,0,0,385,386,5,24,0,0,386,79,1,0,0,0,387,388,5,49,0,0,388,
        389,5,24,0,0,389,81,1,0,0,0,390,392,5,43,0,0,391,393,3,24,12,0,392,
        391,1,0,0,0,392,393,1,0,0,0,393,394,1,0,0,0,394,395,5,24,0,0,395,
        83,1,0,0,0,396,397,3,48,24,0,397,398,5,24,0,0,398,85,1,0,0,0,399,
        401,5,20,0,0,400,402,3,54,27,0,401,400,1,0,0,0,401,402,1,0,0,0,402,
        403,1,0,0,0,403,404,5,21,0,0,404,87,1,0,0,0,405,406,5,55,0,0,406,
        89,1,0,0,0,407,408,5,34,0,0,408,91,1,0,0,0,409,410,5,42,0,0,410,
        93,1,0,0,0,411,412,5,38,0,0,412,95,1,0,0,0,413,414,5,44,0,0,414,
        97,1,0,0,0,415,416,5,47,0,0,416,99,1,0,0,0,417,418,5,32,0,0,418,
        101,1,0,0,0,419,420,5,52,0,0,420,421,5,18,0,0,421,422,3,104,52,0,
        422,423,5,19,0,0,423,424,5,50,0,0,424,425,3,106,53,0,425,103,1,0,
        0,0,426,431,5,28,0,0,427,428,5,22,0,0,428,430,5,28,0,0,429,427,1,
        0,0,0,430,433,1,0,0,0,431,429,1,0,0,0,431,432,1,0,0,0,432,105,1,
        0,0,0,433,431,1,0,0,0,434,439,3,90,45,0,435,439,3,92,46,0,436,439,
        3,94,47,0,437,439,3,96,48,0,438,434,1,0,0,0,438,435,1,0,0,0,438,
        436,1,0,0,0,438,437,1,0,0,0,439,107,1,0,0,0,38,115,119,123,132,145,
        150,160,162,171,175,180,189,192,195,202,213,220,230,241,252,258,
        263,268,279,284,289,298,305,309,315,317,329,339,350,392,401,431,
        438
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
    RULE_varDecl = 5
    RULE_varAssign = 6
    RULE_varNonAssign = 7
    RULE_func_decl = 8
    RULE_params_list = 9
    RULE_param = 10
    RULE_body = 11
    RULE_expr = 12
    RULE_string_expr = 13
    RULE_relat_expr = 14
    RULE_expr1 = 15
    RULE_expr2 = 16
    RULE_expr3 = 17
    RULE_expr4 = 18
    RULE_expr5 = 19
    RULE_expr6 = 20
    RULE_indexes = 21
    RULE_expr7 = 22
    RULE_operand = 23
    RULE_func_call = 24
    RULE_literal = 25
    RULE_exprs_list = 26
    RULE_stmt_list = 27
    RULE_stmt = 28
    RULE_assign_stmt = 29
    RULE_assign_left = 30
    RULE_assign_right = 31
    RULE_if_stmt = 32
    RULE_for_stmt = 33
    RULE_initial_expr = 34
    RULE_condition_expr = 35
    RULE_upd8_expr = 36
    RULE_while_stmt = 37
    RULE_do_while_stmt = 38
    RULE_break_stmt = 39
    RULE_continue_stmt = 40
    RULE_return_stmt = 41
    RULE_call_stmt = 42
    RULE_block_stmt = 43
    RULE_scalar_var = 44
    RULE_bool_type = 45
    RULE_int_type = 46
    RULE_float_type = 47
    RULE_string_type = 48
    RULE_void_type = 49
    RULE_auto_type = 50
    RULE_array_type = 51
    RULE_dimensions = 52
    RULE_atomic_type = 53

    ruleNames =  [ "program", "decls", "decl", "array_lit", "var_decl", 
                   "varDecl", "varAssign", "varNonAssign", "func_decl", 
                   "params_list", "param", "body", "expr", "string_expr", 
                   "relat_expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "indexes", "expr7", "operand", "func_call", 
                   "literal", "exprs_list", "stmt_list", "stmt", "assign_stmt", 
                   "assign_left", "assign_right", "if_stmt", "for_stmt", 
                   "initial_expr", "condition_expr", "upd8_expr", "while_stmt", 
                   "do_while_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "block_stmt", "scalar_var", "bool_type", 
                   "int_type", "float_type", "string_type", "void_type", 
                   "auto_type", "array_type", "dimensions", "atomic_type" ]

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
            self.state = 108
            self.decls()
            self.state = 109
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.decl()
                self.state = 112
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
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




    def array_lit(self):

        localctx = MT22Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 122
                self.exprs_list()


            self.state = 125
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

        def varDecl(self):
            return self.getTypedRuleContext(MT22Parser.VarDeclContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_var_decl




    def var_decl(self):

        localctx = MT22Parser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.varDecl()
            self.state = 128
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varAssign(self):
            return self.getTypedRuleContext(MT22Parser.VarAssignContext,0)


        def varNonAssign(self):
            return self.getTypedRuleContext(MT22Parser.VarNonAssignContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_varDecl




    def varDecl(self):

        localctx = MT22Parser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDecl)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.varAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.varNonAssign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):
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

        def varAssign(self):
            return self.getTypedRuleContext(MT22Parser.VarAssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_varAssign




    def varAssign(self):

        localctx = MT22Parser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varAssign)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(MT22Parser.ID)
                self.state = 135
                self.match(MT22Parser.COMMA)
                self.state = 136
                self.varAssign()
                self.state = 137
                self.match(MT22Parser.COMMA)
                self.state = 138
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(MT22Parser.ID)
                self.state = 141
                self.match(MT22Parser.COLON)
                self.state = 145
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 142
                    self.auto_type()
                    pass
                elif token in [34, 38, 42, 44]:
                    self.state = 143
                    self.atomic_type()
                    pass
                elif token in [52]:
                    self.state = 144
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 147
                self.match(MT22Parser.ASSIGN)
                self.state = 148
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarNonAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def varNonAssign(self):
            return self.getTypedRuleContext(MT22Parser.VarNonAssignContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_varNonAssign




    def varNonAssign(self):

        localctx = MT22Parser.VarNonAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varNonAssign)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(MT22Parser.ID)
                self.state = 153
                self.match(MT22Parser.COMMA)
                self.state = 154
                self.varNonAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(MT22Parser.ID)
                self.state = 156
                self.match(MT22Parser.COLON)
                self.state = 160
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 157
                    self.auto_type()
                    pass
                elif token in [34, 38, 42, 44]:
                    self.state = 158
                    self.atomic_type()
                    pass
                elif token in [52]:
                    self.state = 159
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

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




    def func_decl(self):

        localctx = MT22Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MT22Parser.ID)
            self.state = 165
            self.match(MT22Parser.COLON)
            self.state = 166
            self.match(MT22Parser.FUNCTION)
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 167
                self.atomic_type()
                pass
            elif token in [47]:
                self.state = 168
                self.void_type()
                pass
            elif token in [32]:
                self.state = 169
                self.auto_type()
                pass
            elif token in [52]:
                self.state = 170
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 173
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 38562071809359872) != 0):
                self.state = 174
                self.params_list()


            self.state = 177
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 178
                self.match(MT22Parser.INHERIT)
                self.state = 179
                self.match(MT22Parser.ID)


            self.state = 182
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
        self.enterRule(localctx, 18, self.RULE_params_list)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.param()
                self.state = 185
                self.match(MT22Parser.COMMA)
                self.state = 186
                self.params_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
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
        self.enterRule(localctx, 20, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 191
                self.match(MT22Parser.INHERIT)


            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 194
                self.match(MT22Parser.OUT)


            self.state = 197
            self.match(MT22Parser.ID)
            self.state = 198
            self.match(MT22Parser.COLON)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 199
                self.atomic_type()
                pass
            elif token in [52]:
                self.state = 200
                self.array_type()
                pass
            elif token in [32]:
                self.state = 201
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
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
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
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
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
        self.enterRule(localctx, 26, self.RULE_string_expr)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.relat_expr()
                self.state = 209
                self.match(MT22Parser.SCOPE)
                self.state = 210
                self.relat_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
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
        self.enterRule(localctx, 28, self.RULE_relat_expr)
        self._la = 0 # Token type
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.expr1(0)
                self.state = 216
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 217
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.expr2(0) 
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 238
                    self.expr3(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 249
                    self.expr4() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_expr4)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(MT22Parser.NOT)
                self.state = 256
                self.expr4()
                pass
            elif token in [2, 16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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
        self.enterRule(localctx, 38, self.RULE_expr5)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(MT22Parser.SUB)
                self.state = 261
                self.expr5()
                pass
            elif token in [16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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
        self.enterRule(localctx, 40, self.RULE_expr6)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(MT22Parser.ID)
                self.state = 266
                self.indexes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
        self.enterRule(localctx, 42, self.RULE_indexes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 271
            self.exprs_list()
            self.state = 272
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
        self.enterRule(localctx, 44, self.RULE_expr7)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.operand()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(MT22Parser.LEFT_PAREN)
                self.state = 276
                self.expr()
                self.state = 277
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
        self.enterRule(localctx, 46, self.RULE_operand)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
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
        self.enterRule(localctx, 48, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MT22Parser.ID)
            self.state = 287
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 288
                self.exprs_list()


            self.state = 291
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
        self.enterRule(localctx, 50, self.RULE_literal)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(MT22Parser.INT_LIT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(MT22Parser.FLOAT_LIT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(MT22Parser.BOOL_LIT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.match(MT22Parser.STRING_LIT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
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
        self.enterRule(localctx, 52, self.RULE_exprs_list)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.expr()
                self.state = 301
                self.match(MT22Parser.COMMA)
                self.state = 302
                self.exprs_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
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
        self.enterRule(localctx, 54, self.RULE_stmt_list)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 307
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 308
                    self.var_decl()
                    pass


                self.state = 311
                self.stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 313
                    self.stmt()
                    pass

                elif la_ == 2:
                    self.state = 314
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
        self.enterRule(localctx, 56, self.RULE_stmt)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 324
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 325
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 326
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 327
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 328
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
        self.enterRule(localctx, 58, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.assign_left()
            self.state = 332
            self.match(MT22Parser.ASSIGN)
            self.state = 333
            self.assign_right()
            self.state = 334
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
        self.enterRule(localctx, 60, self.RULE_assign_left)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.match(MT22Parser.ID)
                self.state = 338
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
        self.enterRule(localctx, 62, self.RULE_assign_right)
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
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MT22Parser.IF)
            self.state = 344
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 345
            self.expr()
            self.state = 346
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 347
            self.stmt()
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 348
                self.match(MT22Parser.ELSE)
                self.state = 349
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
        self.enterRule(localctx, 66, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(MT22Parser.FOR)
            self.state = 353
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 354
            self.initial_expr()
            self.state = 355
            self.match(MT22Parser.COMMA)
            self.state = 356
            self.condition_expr()
            self.state = 357
            self.match(MT22Parser.COMMA)
            self.state = 358
            self.upd8_expr()
            self.state = 359
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 360
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
        self.enterRule(localctx, 68, self.RULE_initial_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.scalar_var()
            self.state = 363
            self.match(MT22Parser.ASSIGN)
            self.state = 364
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
        self.enterRule(localctx, 70, self.RULE_condition_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
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
        self.enterRule(localctx, 72, self.RULE_upd8_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
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
        self.enterRule(localctx, 74, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MT22Parser.WHILE)
            self.state = 371
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 372
            self.expr()
            self.state = 373
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 374
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
        self.enterRule(localctx, 76, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MT22Parser.DO)
            self.state = 377
            self.block_stmt()
            self.state = 378
            self.match(MT22Parser.WHILE)
            self.state = 379
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 380
            self.expr()
            self.state = 381
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 382
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
        self.enterRule(localctx, 78, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MT22Parser.BREAK)
            self.state = 385
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
        self.enterRule(localctx, 80, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(MT22Parser.CONTINUE)
            self.state = 388
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
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(MT22Parser.RETURN)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0):
                self.state = 391
                self.expr()


            self.state = 394
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
        self.enterRule(localctx, 84, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.func_call()
            self.state = 397
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
        self.enterRule(localctx, 86, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36673703539376128) != 0):
                self.state = 400
                self.stmt_list()


            self.state = 403
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
        self.enterRule(localctx, 88, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
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
        self.enterRule(localctx, 90, self.RULE_bool_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
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
        self.enterRule(localctx, 92, self.RULE_int_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
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
        self.enterRule(localctx, 94, self.RULE_float_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
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
        self.enterRule(localctx, 96, self.RULE_string_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
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
        self.enterRule(localctx, 98, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
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
        self.enterRule(localctx, 100, self.RULE_auto_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
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
        self.enterRule(localctx, 102, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(MT22Parser.ARRAY)
            self.state = 420
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 421
            self.dimensions()
            self.state = 422
            self.match(MT22Parser.RIGHT_BRACK)
            self.state = 423
            self.match(MT22Parser.OF)
            self.state = 424
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
        self.enterRule(localctx, 104, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MT22Parser.INT_LIT)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 427
                self.match(MT22Parser.COMMA)
                self.state = 428
                self.match(MT22Parser.INT_LIT)
                self.state = 433
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
        self.enterRule(localctx, 106, self.RULE_atomic_type)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.bool_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.int_type()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.float_type()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 437
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
        self._predicates[15] = self.expr1_sempred
        self._predicates[16] = self.expr2_sempred
        self._predicates[17] = self.expr3_sempred
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
         




