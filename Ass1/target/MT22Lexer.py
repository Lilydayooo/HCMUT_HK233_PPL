# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\7\35\u00c7\n\35\f\35\16\35\u00ca")
        buf.write("\13\35\3\35\3\35\6\35\u00ce\n\35\r\35\16\35\u00cf\7\35")
        buf.write("\u00d2\n\35\f\35\16\35\u00d5\13\35\3\35\5\35\u00d8\n\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\5\36\u00df\n\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u00e7\n\36\3\36\3\36\3\37\3\37")
        buf.write("\5\37\u00ed\n\37\3 \3 \3 \7 \u00f2\n \f \16 \u00f5\13")
        buf.write(" \3 \3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u010e\n\"\3#\3")
        buf.write("#\3#\3#\5#\u0114\n#\3$\3$\7$\u0118\n$\f$\16$\u011b\13")
        buf.write("$\3%\3%\5%\u011f\n%\3%\6%\u0122\n%\r%\16%\u0123\3&\3&")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*")
        buf.write("\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\39\39\39\39\39\39\39\39\39\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\6=\u01a9\n=\r=\16=\u01aa\3=\3=\3=\3=\3=\3>\3>\3>")
        buf.write("\3>\7>\u01b6\n>\f>\16>\u01b9\13>\3>\3>\3?\3?\7?\u01bf")
        buf.write("\n?\f?\16?\u01c2\13?\3@\6@\u01c5\n@\r@\16@\u01c6\3@\3")
        buf.write("@\3A\3A\3A\7A\u01ce\nA\fA\16A\u01d1\13A\3A\5A\u01d4\n")
        buf.write("A\3A\3A\3B\3B\3B\7B\u01db\nB\fB\16B\u01de\13B\3B\3B\3")
        buf.write("B\3C\3C\3C\3\u01aa\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\2C\2E\2G\2I\2K\2M\2O\"Q#S$U%W&Y\'[(])_*a+c,e-g.")
        buf.write("i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081;\u0083")
        buf.write("<\u0085=\3\2\16\5\2\f\f$$^^\t\2))^^ddhhppttvv\3\2$$\4")
        buf.write("\2GGgg\4\2--//\3\2\63;\3\2\62;\4\2\f\f\17\17\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\3\3\f\f\2\u01fb\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\3\u0087\3\2\2\2\5\u0089\3\2\2\2\7\u008b\3\2\2\2\t\u008d")
        buf.write("\3\2\2\2\13\u008f\3\2\2\2\r\u0091\3\2\2\2\17\u0093\3\2")
        buf.write("\2\2\21\u0096\3\2\2\2\23\u0099\3\2\2\2\25\u009c\3\2\2")
        buf.write("\2\27\u009f\3\2\2\2\31\u00a1\3\2\2\2\33\u00a4\3\2\2\2")
        buf.write("\35\u00a6\3\2\2\2\37\u00a9\3\2\2\2!\u00ac\3\2\2\2#\u00ae")
        buf.write("\3\2\2\2%\u00b0\3\2\2\2\'\u00b2\3\2\2\2)\u00b4\3\2\2\2")
        buf.write("+\u00b6\3\2\2\2-\u00b8\3\2\2\2/\u00ba\3\2\2\2\61\u00bc")
        buf.write("\3\2\2\2\63\u00be\3\2\2\2\65\u00c0\3\2\2\2\67\u00c2\3")
        buf.write("\2\2\29\u00d7\3\2\2\2;\u00e6\3\2\2\2=\u00ec\3\2\2\2?\u00ee")
        buf.write("\3\2\2\2A\u00f9\3\2\2\2C\u010d\3\2\2\2E\u0113\3\2\2\2")
        buf.write("G\u0115\3\2\2\2I\u011c\3\2\2\2K\u0125\3\2\2\2M\u0127\3")
        buf.write("\2\2\2O\u0129\3\2\2\2Q\u012e\3\2\2\2S\u0134\3\2\2\2U\u013c")
        buf.write("\3\2\2\2W\u013f\3\2\2\2Y\u0144\3\2\2\2[\u014a\3\2\2\2")
        buf.write("]\u0150\3\2\2\2_\u0154\3\2\2\2a\u015d\3\2\2\2c\u0160\3")
        buf.write("\2\2\2e\u0168\3\2\2\2g\u016f\3\2\2\2i\u0176\3\2\2\2k\u017b")
        buf.write("\3\2\2\2m\u0181\3\2\2\2o\u0186\3\2\2\2q\u018a\3\2\2\2")
        buf.write("s\u0193\3\2\2\2u\u0196\3\2\2\2w\u019e\3\2\2\2y\u01a4\3")
        buf.write("\2\2\2{\u01b1\3\2\2\2}\u01bc\3\2\2\2\177\u01c4\3\2\2\2")
        buf.write("\u0081\u01ca\3\2\2\2\u0083\u01d7\3\2\2\2\u0085\u01e2\3")
        buf.write("\2\2\2\u0087\u0088\7-\2\2\u0088\4\3\2\2\2\u0089\u008a")
        buf.write("\7/\2\2\u008a\6\3\2\2\2\u008b\u008c\7,\2\2\u008c\b\3\2")
        buf.write("\2\2\u008d\u008e\7\61\2\2\u008e\n\3\2\2\2\u008f\u0090")
        buf.write("\7\'\2\2\u0090\f\3\2\2\2\u0091\u0092\7#\2\2\u0092\16\3")
        buf.write("\2\2\2\u0093\u0094\7(\2\2\u0094\u0095\7(\2\2\u0095\20")
        buf.write("\3\2\2\2\u0096\u0097\7~\2\2\u0097\u0098\7~\2\2\u0098\22")
        buf.write("\3\2\2\2\u0099\u009a\7?\2\2\u009a\u009b\7?\2\2\u009b\24")
        buf.write("\3\2\2\2\u009c\u009d\7#\2\2\u009d\u009e\7?\2\2\u009e\26")
        buf.write("\3\2\2\2\u009f\u00a0\7>\2\2\u00a0\30\3\2\2\2\u00a1\u00a2")
        buf.write("\7>\2\2\u00a2\u00a3\7?\2\2\u00a3\32\3\2\2\2\u00a4\u00a5")
        buf.write("\7@\2\2\u00a5\34\3\2\2\2\u00a6\u00a7\7@\2\2\u00a7\u00a8")
        buf.write("\7?\2\2\u00a8\36\3\2\2\2\u00a9\u00aa\7<\2\2\u00aa\u00ab")
        buf.write("\7<\2\2\u00ab \3\2\2\2\u00ac\u00ad\7*\2\2\u00ad\"\3\2")
        buf.write("\2\2\u00ae\u00af\7+\2\2\u00af$\3\2\2\2\u00b0\u00b1\7]")
        buf.write("\2\2\u00b1&\3\2\2\2\u00b2\u00b3\7_\2\2\u00b3(\3\2\2\2")
        buf.write("\u00b4\u00b5\7}\2\2\u00b5*\3\2\2\2\u00b6\u00b7\7\177\2")
        buf.write("\2\u00b7,\3\2\2\2\u00b8\u00b9\7.\2\2\u00b9.\3\2\2\2\u00ba")
        buf.write("\u00bb\7\60\2\2\u00bb\60\3\2\2\2\u00bc\u00bd\7=\2\2\u00bd")
        buf.write("\62\3\2\2\2\u00be\u00bf\7<\2\2\u00bf\64\3\2\2\2\u00c0")
        buf.write("\u00c1\7?\2\2\u00c1\66\3\2\2\2\u00c2\u00c3\7a\2\2\u00c3")
        buf.write("8\3\2\2\2\u00c4\u00c8\5K&\2\u00c5\u00c7\5M\'\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00d3\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00cb\u00cd\5\67\34\2\u00cc\u00ce\5M\'\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cb\3\2\2\2")
        buf.write("\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3")
        buf.write("\2\2\2\u00d4\u00d8\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d8")
        buf.write("\7\62\2\2\u00d7\u00c4\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00da\b\35\2\2\u00da:\3\2\2\2\u00db")
        buf.write("\u00dc\59\35\2\u00dc\u00de\5G$\2\u00dd\u00df\5I%\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e7\3\2\2\2")
        buf.write("\u00e0\u00e1\5G$\2\u00e1\u00e2\5I%\2\u00e2\u00e7\3\2\2")
        buf.write("\2\u00e3\u00e4\59\35\2\u00e4\u00e5\5I%\2\u00e5\u00e7\3")
        buf.write("\2\2\2\u00e6\u00db\3\2\2\2\u00e6\u00e0\3\2\2\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\b\36\3\2\u00e9")
        buf.write("<\3\2\2\2\u00ea\u00ed\5i\65\2\u00eb\u00ed\5Y-\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed>\3\2\2\2\u00ee")
        buf.write("\u00f3\7$\2\2\u00ef\u00f2\5A!\2\u00f0\u00f2\5C\"\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3")
        buf.write("\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\7$\2\2\u00f7\u00f8")
        buf.write("\b \4\2\u00f8@\3\2\2\2\u00f9\u00fa\n\2\2\2\u00faB\3\2")
        buf.write("\2\2\u00fb\u00fc\7^\2\2\u00fc\u010e\7d\2\2\u00fd\u00fe")
        buf.write("\7^\2\2\u00fe\u010e\7h\2\2\u00ff\u0100\7^\2\2\u0100\u010e")
        buf.write("\7t\2\2\u0101\u0102\7^\2\2\u0102\u010e\7p\2\2\u0103\u0104")
        buf.write("\7^\2\2\u0104\u010e\7^\2\2\u0105\u0106\7^\2\2\u0106\u010e")
        buf.write("\7)\2\2\u0107\u0108\7^\2\2\u0108\u010e\7v\2\2\u0109\u010a")
        buf.write("\7^\2\2\u010a\u010e\7$\2\2\u010b\u010c\7)\2\2\u010c\u010e")
        buf.write("\7$\2\2\u010d\u00fb\3\2\2\2\u010d\u00fd\3\2\2\2\u010d")
        buf.write("\u00ff\3\2\2\2\u010d\u0101\3\2\2\2\u010d\u0103\3\2\2\2")
        buf.write("\u010d\u0105\3\2\2\2\u010d\u0107\3\2\2\2\u010d\u0109\3")
        buf.write("\2\2\2\u010d\u010b\3\2\2\2\u010eD\3\2\2\2\u010f\u0110")
        buf.write("\7^\2\2\u0110\u0114\n\3\2\2\u0111\u0112\7)\2\2\u0112\u0114")
        buf.write("\n\4\2\2\u0113\u010f\3\2\2\2\u0113\u0111\3\2\2\2\u0114")
        buf.write("F\3\2\2\2\u0115\u0119\7\60\2\2\u0116\u0118\5M\'\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u0119\u011a\3\2\2\2\u011aH\3\2\2\2\u011b\u0119\3\2\2")
        buf.write("\2\u011c\u011e\t\5\2\2\u011d\u011f\t\6\2\2\u011e\u011d")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u0122\5M\'\2\u0121\u0120\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124J\3\2\2")
        buf.write("\2\u0125\u0126\t\7\2\2\u0126L\3\2\2\2\u0127\u0128\t\b")
        buf.write("\2\2\u0128N\3\2\2\2\u0129\u012a\7c\2\2\u012a\u012b\7w")
        buf.write("\2\2\u012b\u012c\7v\2\2\u012c\u012d\7q\2\2\u012dP\3\2")
        buf.write("\2\2\u012e\u012f\7d\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7c\2\2\u0132\u0133\7m\2\2\u0133R\3")
        buf.write("\2\2\2\u0134\u0135\7d\2\2\u0135\u0136\7q\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7n\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7c\2\2\u013a\u013b\7p\2\2\u013bT\3\2\2\2\u013c\u013d")
        buf.write("\7f\2\2\u013d\u013e\7q\2\2\u013eV\3\2\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7n\2\2\u0141\u0142\7u\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143X\3\2\2\2\u0144\u0145\7h\2\2\u0145\u0146")
        buf.write("\7c\2\2\u0146\u0147\7n\2\2\u0147\u0148\7u\2\2\u0148\u0149")
        buf.write("\7g\2\2\u0149Z\3\2\2\2\u014a\u014b\7h\2\2\u014b\u014c")
        buf.write("\7n\2\2\u014c\u014d\7q\2\2\u014d\u014e\7c\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014f\\\3\2\2\2\u0150\u0151\7h\2\2\u0151\u0152")
        buf.write("\7q\2\2\u0152\u0153\7t\2\2\u0153^\3\2\2\2\u0154\u0155")
        buf.write("\7h\2\2\u0155\u0156\7w\2\2\u0156\u0157\7p\2\2\u0157\u0158")
        buf.write("\7e\2\2\u0158\u0159\7v\2\2\u0159\u015a\7k\2\2\u015a\u015b")
        buf.write("\7q\2\2\u015b\u015c\7p\2\2\u015c`\3\2\2\2\u015d\u015e")
        buf.write("\7k\2\2\u015e\u015f\7h\2\2\u015fb\3\2\2\2\u0160\u0161")
        buf.write("\7k\2\2\u0161\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7g\2\2\u0164\u0165\7i\2\2\u0165\u0166\7g\2\2\u0166\u0167")
        buf.write("\7t\2\2\u0167d\3\2\2\2\u0168\u0169\7t\2\2\u0169\u016a")
        buf.write("\7g\2\2\u016a\u016b\7v\2\2\u016b\u016c\7w\2\2\u016c\u016d")
        buf.write("\7t\2\2\u016d\u016e\7p\2\2\u016ef\3\2\2\2\u016f\u0170")
        buf.write("\7u\2\2\u0170\u0171\7v\2\2\u0171\u0172\7t\2\2\u0172\u0173")
        buf.write("\7k\2\2\u0173\u0174\7p\2\2\u0174\u0175\7i\2\2\u0175h\3")
        buf.write("\2\2\2\u0176\u0177\7v\2\2\u0177\u0178\7t\2\2\u0178\u0179")
        buf.write("\7w\2\2\u0179\u017a\7g\2\2\u017aj\3\2\2\2\u017b\u017c")
        buf.write("\7y\2\2\u017c\u017d\7j\2\2\u017d\u017e\7k\2\2\u017e\u017f")
        buf.write("\7n\2\2\u017f\u0180\7g\2\2\u0180l\3\2\2\2\u0181\u0182")
        buf.write("\7x\2\2\u0182\u0183\7q\2\2\u0183\u0184\7k\2\2\u0184\u0185")
        buf.write("\7f\2\2\u0185n\3\2\2\2\u0186\u0187\7q\2\2\u0187\u0188")
        buf.write("\7w\2\2\u0188\u0189\7v\2\2\u0189p\3\2\2\2\u018a\u018b")
        buf.write("\7e\2\2\u018b\u018c\7q\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7v\2\2\u018e\u018f\7k\2\2\u018f\u0190\7p\2\2\u0190\u0191")
        buf.write("\7w\2\2\u0191\u0192\7g\2\2\u0192r\3\2\2\2\u0193\u0194")
        buf.write("\7q\2\2\u0194\u0195\7h\2\2\u0195t\3\2\2\2\u0196\u0197")
        buf.write("\7k\2\2\u0197\u0198\7p\2\2\u0198\u0199\7j\2\2\u0199\u019a")
        buf.write("\7g\2\2\u019a\u019b\7t\2\2\u019b\u019c\7k\2\2\u019c\u019d")
        buf.write("\7v\2\2\u019dv\3\2\2\2\u019e\u019f\7c\2\2\u019f\u01a0")
        buf.write("\7t\2\2\u01a0\u01a1\7t\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3")
        buf.write("\7{\2\2\u01a3x\3\2\2\2\u01a4\u01a5\7\61\2\2\u01a5\u01a6")
        buf.write("\7,\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a9\13\2\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\7")
        buf.write(",\2\2\u01ad\u01ae\7\61\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0")
        buf.write("\b=\5\2\u01b0z\3\2\2\2\u01b1\u01b2\7\61\2\2\u01b2\u01b3")
        buf.write("\7\61\2\2\u01b3\u01b7\3\2\2\2\u01b4\u01b6\n\t\2\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01ba\u01bb\b>\5\2\u01bb|\3\2\2\2\u01bc\u01c0\t")
        buf.write("\n\2\2\u01bd\u01bf\t\13\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1~\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5\t\f\2")
        buf.write("\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01c9\b@\5\2\u01c9\u0080\3\2\2\2\u01ca\u01cf\7$\2\2\u01cb")
        buf.write("\u01ce\5A!\2\u01cc\u01ce\5C\"\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01cf\u01d0\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d2\u01d4\t\r\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d6\bA\6\2\u01d6\u0082\3\2\2\2\u01d7")
        buf.write("\u01dc\7$\2\2\u01d8\u01db\5A!\2\u01d9\u01db\5C\"\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3")
        buf.write("\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\5E#\2\u01e0\u01e1")
        buf.write("\bB\7\2\u01e1\u0084\3\2\2\2\u01e2\u01e3\13\2\2\2\u01e3")
        buf.write("\u01e4\bC\b\2\u01e4\u0086\3\2\2\2\32\2\u00c8\u00cf\u00d3")
        buf.write("\u00d7\u00de\u00e6\u00ec\u00f1\u00f3\u010d\u0113\u0119")
        buf.write("\u011e\u0123\u01aa\u01b7\u01c0\u01c6\u01cd\u01cf\u01d3")
        buf.write("\u01da\u01dc\t\3\35\2\3\36\3\3 \4\b\2\2\3A\5\3B\6\3C\7")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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
            esc = '\n'
            if cont[-1] in esc: raise UncloseString(cont[1:-1])
            else: raise UncloseString(content[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            raise ErrorToken(self.text)

     


