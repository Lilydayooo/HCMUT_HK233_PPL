# Generated from d:/DHBK/233/PPL_Assignments/Ass1/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,59,481,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,
        1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,
        1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,5,27,197,8,27,10,27,12,27,
        200,9,27,1,27,1,27,4,27,204,8,27,11,27,12,27,205,5,27,208,8,27,10,
        27,12,27,211,9,27,1,27,3,27,214,8,27,1,27,1,27,1,28,1,28,1,28,3,
        28,221,8,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,229,8,28,1,28,1,28,
        1,29,1,29,3,29,235,8,29,1,30,1,30,1,30,5,30,240,8,30,10,30,12,30,
        243,9,30,1,30,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,
        268,8,32,1,33,1,33,1,33,1,33,3,33,274,8,33,1,34,1,34,5,34,278,8,
        34,10,34,12,34,281,9,34,1,35,1,35,3,35,285,8,35,1,35,4,35,288,8,
        35,11,35,12,35,289,1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,38,1,38,
        1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,
        1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,46,
        1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,52,
        1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,54,1,54,1,54,
        1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,
        1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,
        1,58,1,59,1,59,1,59,1,59,4,59,423,8,59,11,59,12,59,424,1,59,1,59,
        1,59,1,59,1,59,1,60,1,60,1,60,1,60,5,60,436,8,60,10,60,12,60,439,
        9,60,1,60,1,60,1,61,1,61,5,61,445,8,61,10,61,12,61,448,9,61,1,62,
        4,62,451,8,62,11,62,12,62,452,1,62,1,62,1,63,1,63,1,63,5,63,460,
        8,63,10,63,12,63,463,9,63,1,63,1,63,1,63,1,64,1,64,1,64,5,64,471,
        8,64,10,64,12,64,474,9,64,1,64,1,64,1,64,1,65,1,65,1,65,1,424,0,
        66,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,0,65,0,67,0,69,0,
        71,0,73,0,75,0,77,32,79,33,81,34,83,35,85,36,87,37,89,38,91,39,93,
        40,95,41,97,42,99,43,101,44,103,45,105,46,107,47,109,48,111,49,113,
        50,115,51,117,52,119,53,121,54,123,55,125,56,127,57,129,58,131,59,
        1,0,11,3,0,10,10,34,34,92,92,7,0,39,39,92,92,98,98,102,102,110,110,
        114,114,116,116,1,0,34,34,2,0,69,69,101,101,2,0,43,43,45,45,1,0,
        49,57,1,0,48,57,2,0,10,10,13,13,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,3,0,8,10,12,13,32,32,503,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,
        0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,
        0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,
        0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,77,1,0,0,
        0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,
        0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,
        0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,
        0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,
        117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,
        0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,1,133,1,0,0,0,3,135,
        1,0,0,0,5,137,1,0,0,0,7,139,1,0,0,0,9,141,1,0,0,0,11,143,1,0,0,0,
        13,145,1,0,0,0,15,148,1,0,0,0,17,151,1,0,0,0,19,154,1,0,0,0,21,157,
        1,0,0,0,23,159,1,0,0,0,25,162,1,0,0,0,27,164,1,0,0,0,29,167,1,0,
        0,0,31,170,1,0,0,0,33,172,1,0,0,0,35,174,1,0,0,0,37,176,1,0,0,0,
        39,178,1,0,0,0,41,180,1,0,0,0,43,182,1,0,0,0,45,184,1,0,0,0,47,186,
        1,0,0,0,49,188,1,0,0,0,51,190,1,0,0,0,53,192,1,0,0,0,55,213,1,0,
        0,0,57,228,1,0,0,0,59,234,1,0,0,0,61,236,1,0,0,0,63,247,1,0,0,0,
        65,267,1,0,0,0,67,273,1,0,0,0,69,275,1,0,0,0,71,282,1,0,0,0,73,291,
        1,0,0,0,75,293,1,0,0,0,77,295,1,0,0,0,79,300,1,0,0,0,81,306,1,0,
        0,0,83,314,1,0,0,0,85,317,1,0,0,0,87,322,1,0,0,0,89,328,1,0,0,0,
        91,334,1,0,0,0,93,338,1,0,0,0,95,347,1,0,0,0,97,350,1,0,0,0,99,358,
        1,0,0,0,101,365,1,0,0,0,103,372,1,0,0,0,105,377,1,0,0,0,107,383,
        1,0,0,0,109,388,1,0,0,0,111,392,1,0,0,0,113,401,1,0,0,0,115,404,
        1,0,0,0,117,412,1,0,0,0,119,418,1,0,0,0,121,431,1,0,0,0,123,442,
        1,0,0,0,125,450,1,0,0,0,127,456,1,0,0,0,129,467,1,0,0,0,131,478,
        1,0,0,0,133,134,5,43,0,0,134,2,1,0,0,0,135,136,5,45,0,0,136,4,1,
        0,0,0,137,138,5,42,0,0,138,6,1,0,0,0,139,140,5,47,0,0,140,8,1,0,
        0,0,141,142,5,37,0,0,142,10,1,0,0,0,143,144,5,33,0,0,144,12,1,0,
        0,0,145,146,5,38,0,0,146,147,5,38,0,0,147,14,1,0,0,0,148,149,5,124,
        0,0,149,150,5,124,0,0,150,16,1,0,0,0,151,152,5,61,0,0,152,153,5,
        61,0,0,153,18,1,0,0,0,154,155,5,33,0,0,155,156,5,61,0,0,156,20,1,
        0,0,0,157,158,5,60,0,0,158,22,1,0,0,0,159,160,5,60,0,0,160,161,5,
        61,0,0,161,24,1,0,0,0,162,163,5,62,0,0,163,26,1,0,0,0,164,165,5,
        62,0,0,165,166,5,61,0,0,166,28,1,0,0,0,167,168,5,58,0,0,168,169,
        5,58,0,0,169,30,1,0,0,0,170,171,5,40,0,0,171,32,1,0,0,0,172,173,
        5,41,0,0,173,34,1,0,0,0,174,175,5,91,0,0,175,36,1,0,0,0,176,177,
        5,93,0,0,177,38,1,0,0,0,178,179,5,123,0,0,179,40,1,0,0,0,180,181,
        5,125,0,0,181,42,1,0,0,0,182,183,5,44,0,0,183,44,1,0,0,0,184,185,
        5,46,0,0,185,46,1,0,0,0,186,187,5,59,0,0,187,48,1,0,0,0,188,189,
        5,58,0,0,189,50,1,0,0,0,190,191,5,61,0,0,191,52,1,0,0,0,192,193,
        5,95,0,0,193,54,1,0,0,0,194,198,3,73,36,0,195,197,3,75,37,0,196,
        195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,
        209,1,0,0,0,200,198,1,0,0,0,201,203,3,53,26,0,202,204,3,75,37,0,
        203,202,1,0,0,0,204,205,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,
        206,208,1,0,0,0,207,201,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,
        209,210,1,0,0,0,210,214,1,0,0,0,211,209,1,0,0,0,212,214,5,48,0,0,
        213,194,1,0,0,0,213,212,1,0,0,0,214,215,1,0,0,0,215,216,6,27,0,0,
        216,56,1,0,0,0,217,218,3,55,27,0,218,220,3,69,34,0,219,221,3,71,
        35,0,220,219,1,0,0,0,220,221,1,0,0,0,221,229,1,0,0,0,222,223,3,69,
        34,0,223,224,3,71,35,0,224,229,1,0,0,0,225,226,3,55,27,0,226,227,
        3,71,35,0,227,229,1,0,0,0,228,217,1,0,0,0,228,222,1,0,0,0,228,225,
        1,0,0,0,229,230,1,0,0,0,230,231,6,28,1,0,231,58,1,0,0,0,232,235,
        3,103,51,0,233,235,3,87,43,0,234,232,1,0,0,0,234,233,1,0,0,0,235,
        60,1,0,0,0,236,241,5,34,0,0,237,240,3,63,31,0,238,240,3,65,32,0,
        239,237,1,0,0,0,239,238,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,
        241,242,1,0,0,0,242,244,1,0,0,0,243,241,1,0,0,0,244,245,5,34,0,0,
        245,246,6,30,2,0,246,62,1,0,0,0,247,248,8,0,0,0,248,64,1,0,0,0,249,
        250,5,92,0,0,250,268,5,98,0,0,251,252,5,92,0,0,252,268,5,102,0,0,
        253,254,5,92,0,0,254,268,5,114,0,0,255,256,5,92,0,0,256,268,5,110,
        0,0,257,258,5,92,0,0,258,268,5,92,0,0,259,260,5,92,0,0,260,268,5,
        39,0,0,261,262,5,92,0,0,262,268,5,116,0,0,263,264,5,92,0,0,264,268,
        5,34,0,0,265,266,5,39,0,0,266,268,5,34,0,0,267,249,1,0,0,0,267,251,
        1,0,0,0,267,253,1,0,0,0,267,255,1,0,0,0,267,257,1,0,0,0,267,259,
        1,0,0,0,267,261,1,0,0,0,267,263,1,0,0,0,267,265,1,0,0,0,268,66,1,
        0,0,0,269,270,5,92,0,0,270,274,8,1,0,0,271,272,5,39,0,0,272,274,
        8,2,0,0,273,269,1,0,0,0,273,271,1,0,0,0,274,68,1,0,0,0,275,279,5,
        46,0,0,276,278,3,75,37,0,277,276,1,0,0,0,278,281,1,0,0,0,279,277,
        1,0,0,0,279,280,1,0,0,0,280,70,1,0,0,0,281,279,1,0,0,0,282,284,7,
        3,0,0,283,285,7,4,0,0,284,283,1,0,0,0,284,285,1,0,0,0,285,287,1,
        0,0,0,286,288,3,75,37,0,287,286,1,0,0,0,288,289,1,0,0,0,289,287,
        1,0,0,0,289,290,1,0,0,0,290,72,1,0,0,0,291,292,7,5,0,0,292,74,1,
        0,0,0,293,294,7,6,0,0,294,76,1,0,0,0,295,296,5,97,0,0,296,297,5,
        117,0,0,297,298,5,116,0,0,298,299,5,111,0,0,299,78,1,0,0,0,300,301,
        5,98,0,0,301,302,5,114,0,0,302,303,5,101,0,0,303,304,5,97,0,0,304,
        305,5,107,0,0,305,80,1,0,0,0,306,307,5,98,0,0,307,308,5,111,0,0,
        308,309,5,111,0,0,309,310,5,108,0,0,310,311,5,101,0,0,311,312,5,
        97,0,0,312,313,5,110,0,0,313,82,1,0,0,0,314,315,5,100,0,0,315,316,
        5,111,0,0,316,84,1,0,0,0,317,318,5,101,0,0,318,319,5,108,0,0,319,
        320,5,115,0,0,320,321,5,101,0,0,321,86,1,0,0,0,322,323,5,102,0,0,
        323,324,5,97,0,0,324,325,5,108,0,0,325,326,5,115,0,0,326,327,5,101,
        0,0,327,88,1,0,0,0,328,329,5,102,0,0,329,330,5,108,0,0,330,331,5,
        111,0,0,331,332,5,97,0,0,332,333,5,116,0,0,333,90,1,0,0,0,334,335,
        5,102,0,0,335,336,5,111,0,0,336,337,5,114,0,0,337,92,1,0,0,0,338,
        339,5,102,0,0,339,340,5,117,0,0,340,341,5,110,0,0,341,342,5,99,0,
        0,342,343,5,116,0,0,343,344,5,105,0,0,344,345,5,111,0,0,345,346,
        5,110,0,0,346,94,1,0,0,0,347,348,5,105,0,0,348,349,5,102,0,0,349,
        96,1,0,0,0,350,351,5,105,0,0,351,352,5,110,0,0,352,353,5,116,0,0,
        353,354,5,101,0,0,354,355,5,103,0,0,355,356,5,101,0,0,356,357,5,
        114,0,0,357,98,1,0,0,0,358,359,5,114,0,0,359,360,5,101,0,0,360,361,
        5,116,0,0,361,362,5,117,0,0,362,363,5,114,0,0,363,364,5,110,0,0,
        364,100,1,0,0,0,365,366,5,115,0,0,366,367,5,116,0,0,367,368,5,114,
        0,0,368,369,5,105,0,0,369,370,5,110,0,0,370,371,5,103,0,0,371,102,
        1,0,0,0,372,373,5,116,0,0,373,374,5,114,0,0,374,375,5,117,0,0,375,
        376,5,101,0,0,376,104,1,0,0,0,377,378,5,119,0,0,378,379,5,104,0,
        0,379,380,5,105,0,0,380,381,5,108,0,0,381,382,5,101,0,0,382,106,
        1,0,0,0,383,384,5,118,0,0,384,385,5,111,0,0,385,386,5,105,0,0,386,
        387,5,100,0,0,387,108,1,0,0,0,388,389,5,111,0,0,389,390,5,117,0,
        0,390,391,5,116,0,0,391,110,1,0,0,0,392,393,5,99,0,0,393,394,5,111,
        0,0,394,395,5,110,0,0,395,396,5,116,0,0,396,397,5,105,0,0,397,398,
        5,110,0,0,398,399,5,117,0,0,399,400,5,101,0,0,400,112,1,0,0,0,401,
        402,5,111,0,0,402,403,5,102,0,0,403,114,1,0,0,0,404,405,5,105,0,
        0,405,406,5,110,0,0,406,407,5,104,0,0,407,408,5,101,0,0,408,409,
        5,114,0,0,409,410,5,105,0,0,410,411,5,116,0,0,411,116,1,0,0,0,412,
        413,5,97,0,0,413,414,5,114,0,0,414,415,5,114,0,0,415,416,5,97,0,
        0,416,417,5,121,0,0,417,118,1,0,0,0,418,419,5,47,0,0,419,420,5,42,
        0,0,420,422,1,0,0,0,421,423,9,0,0,0,422,421,1,0,0,0,423,424,1,0,
        0,0,424,425,1,0,0,0,424,422,1,0,0,0,425,426,1,0,0,0,426,427,5,42,
        0,0,427,428,5,47,0,0,428,429,1,0,0,0,429,430,6,59,3,0,430,120,1,
        0,0,0,431,432,5,47,0,0,432,433,5,47,0,0,433,437,1,0,0,0,434,436,
        8,7,0,0,435,434,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,
        1,0,0,0,438,440,1,0,0,0,439,437,1,0,0,0,440,441,6,60,3,0,441,122,
        1,0,0,0,442,446,7,8,0,0,443,445,7,9,0,0,444,443,1,0,0,0,445,448,
        1,0,0,0,446,444,1,0,0,0,446,447,1,0,0,0,447,124,1,0,0,0,448,446,
        1,0,0,0,449,451,7,10,0,0,450,449,1,0,0,0,451,452,1,0,0,0,452,450,
        1,0,0,0,452,453,1,0,0,0,453,454,1,0,0,0,454,455,6,62,3,0,455,126,
        1,0,0,0,456,461,5,34,0,0,457,460,3,63,31,0,458,460,3,65,32,0,459,
        457,1,0,0,0,459,458,1,0,0,0,460,463,1,0,0,0,461,459,1,0,0,0,461,
        462,1,0,0,0,462,464,1,0,0,0,463,461,1,0,0,0,464,465,5,0,0,1,465,
        466,6,63,4,0,466,128,1,0,0,0,467,472,5,34,0,0,468,471,3,63,31,0,
        469,471,3,65,32,0,470,468,1,0,0,0,470,469,1,0,0,0,471,474,1,0,0,
        0,472,470,1,0,0,0,472,473,1,0,0,0,473,475,1,0,0,0,474,472,1,0,0,
        0,475,476,3,67,33,0,476,477,6,64,5,0,477,130,1,0,0,0,478,479,9,0,
        0,0,479,480,6,65,6,0,480,132,1,0,0,0,23,0,198,205,209,213,220,228,
        234,239,241,267,273,279,284,289,424,437,446,452,459,461,470,472,
        7,1,27,0,1,28,1,1,30,2,6,0,0,1,63,3,1,64,4,1,65,5
    ]

class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    NOT = 6
    AND = 7
    OR = 8
    SAME = 9
    NOTSAME = 10
    LESS = 11
    LESS_EQ = 12
    MOR = 13
    MOR_EQ = 14
    SCOPE = 15
    LEFT_PAREN = 16
    RIGHT_PAREN = 17
    LEFT_BRACK = 18
    RIGHT_BRACK = 19
    LEFT_BRACE = 20
    RIGHT_BRACE = 21
    COMMA = 22
    DOT = 23
    SEMI_COLON = 24
    COLON = 25
    ASSIGN = 26
    UNDERSCORE = 27
    INT_LIT = 28
    FLOAT_LIT = 29
    BOOL_LIT = 30
    STRING_LIT = 31
    AUTO = 32
    BREAK = 33
    BOOLEAN = 34
    DO = 35
    ELSE = 36
    FALSE = 37
    FLOAT = 38
    FOR = 39
    FUNCTION = 40
    IF = 41
    INTEGER = 42
    RETURN = 43
    STRING = 44
    TRUE = 45
    WHILE = 46
    VOID = 47
    OUT = 48
    CONTINUE = 49
    OF = 50
    INHERIT = 51
    ARRAY = 52
    BLOCK_CMT = 53
    LINE_CMT = 54
    ID = 55
    WS = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "','", "'.'", "';'", "':'", "'='", 
            "'_'", "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "SAME", 
            "NOTSAME", "LESS", "LESS_EQ", "MOR", "MOR_EQ", "SCOPE", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_BRACK", "RIGHT_BRACK", "LEFT_BRACE", "RIGHT_BRACE", 
            "COMMA", "DOT", "SEMI_COLON", "COLON", "ASSIGN", "UNDERSCORE", 
            "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "AUTO", "BREAK", 
            "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "BLOCK_CMT", "LINE_CMT", 
            "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "SAME", "NOTSAME", "LESS", "LESS_EQ", "MOR", "MOR_EQ", 
                  "SCOPE", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACK", "RIGHT_BRACK", 
                  "LEFT_BRACE", "RIGHT_BRACE", "COMMA", "DOT", "SEMI_COLON", 
                  "COLON", "ASSIGN", "UNDERSCORE", "INT_LIT", "FLOAT_LIT", 
                  "BOOL_LIT", "STRING_LIT", "STR_CHAR", "ESC_SEQ", "ESC_ERR", 
                  "DECI", "EXPO", "NON_0_DIGIT", "DIGIT", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "BLOCK_CMT", 
                  "LINE_CMT", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[27] = self.INT_LIT_action 
            actions[28] = self.FLOAT_LIT_action 
            actions[30] = self.STRING_LIT_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = str(self.text[1:-1])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            cont = str(self.text) 
            raise UncloseString(cont[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            raise ErrorToken(self.text)

     


