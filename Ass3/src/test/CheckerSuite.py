import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = """
        x: integer = 3;
        x: string;
        main: function void(){}
    """

        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_1(self):
        input = """
        x: integer = 3;
        y: auto;
        main: function void(){}
    """

        expect = "Invalid Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """
        x: integer = 3;
        y: auto = x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """
        x: integer = 3;
        y: float = 3.100;
        z: auto = y + x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """
        x: boolean;
        y: auto = 3.100;
        z: auto = y + x;
        main: function void(){}
    """

        expect = "Type mismatch in expression: BinExpr(+, Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """
        x: string = "hello";
        y: auto = x == "Hiiii";
        main: function void(){}
    """

        expect = "Type mismatch in expression: BinExpr(==, Id(x), StringLit(Hiiii))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """
        x: boolean = false;
        y: auto = x == true;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """
        x: integer = 100;
        y: auto = x == true;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """
        x: integer = 100;
        y: auto = x != 5;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """
        x: integer = 100;
        y: integer = x != 5;
        main: function void(){}
    """

        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BinExpr(!=, Id(x), IntegerLit(5)))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """
        x: integer = -100;
        y: integer = -x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
        y: integer =  true || (true && false);
        main: function void(){}
    """

        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BinExpr(||, BooleanLit(True), BinExpr(&&, BooleanLit(True), BooleanLit(False))))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """
        x: integer = -100_999;
        y: float = x;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
        x: float = -100_999.123;
        y: integer = x;
        main: function void(){}
    """

        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """
        a : array [2] of integer;
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """
        a : array [2] of integer = {-1.0, 3.0};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(3.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 415))

        def test_16(self):
            input = """
        a : array [2] of integer = {-1, 3};
        main: function void(){}
    """

            expect = "[]"
            self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        a: array [2] of integer = {1, 2};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
        b: array [2, 3] of integer = {{}, {}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        c: array [2, 3] of integer = {{1}, {1, 2, 3}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        d: array [2, 3, 5] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        e: array [2, 3] of integer = {{1.0}, {1, 2, 3}};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(e, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
        f: array [2, 3] of integer = {{1, 1}, {1.0, 2, 3}};
        main: function void(){}
    """

        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([FloatLit(1.0), IntegerLit(2), IntegerLit(3)])])"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
            x, y, z: integer = 1, 2, 3;
            a: array [3, 2] of integer = {{x + z}, {y, z}};
            main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
        // c : integer = 1;
        c : array [1] of integer = {1};
        b : integer = 10;
        // a : array [2, 2] of integer = {{3, c[0.1 + 3]}, {b, 199}};
        a : array [2, 2] of integer = {{3, c[1 + 3, 3 + 4]}, {b, 199}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
        a3 : array [2, 2] of boolean = {{3.3, 3.5}, {123.1, 199.10}};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a3, ArrayType([2, 2], BooleanType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
        a2 : array [2, 2] of integer = {{3.3, 3.5}, {123.1, 199.10}};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a2, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.1)])]))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
        a : array [2, 2] of float = {{3, 3}, {123, 199}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        a : array [2, 2] of float = {{3, 3}, {123, 199, 123}, {123}};
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
        a : array [2, 2] of float = {false};
        main: function void(){}
    """

        expect = "Type mismatch in statement: VarDecl(a, ArrayType([2, 2], FloatType), ArrayLit([BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
        fact : function integer (n : integer) {}
    """

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """
        fact : function integer (n : integer) {}
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """
        fact : function integer (n : integer, n : float) {}
        main: function void(){}
    """

        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """
        fact : function integer (n : integer) {}
        fact : function float () {}
        main: function void(){}
    """

        expect = "Redeclared Function: fact"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            x: integer = 3;
            x: boolean = false;
        }
        main: function void(){}
    """

        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            x: integer = 3;
            y: float = 3.100;
            z: auto = y + x;

            c : array [1] of integer = {1};
            b : integer = 10;
            a : array [2, 2] of integer = {{3, c[1 + 3]}, {b, 199}};
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            if (n == 10) {}
            else {
            }
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
        x: float = 3.0;
        fact : function integer (n : integer) {
            if (n + 10) {}
            else {
            }
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(n), IntegerLit(10)), BlockStmt([]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
        x: float = 3.0;
        a : array [2] of integer;
        fact : function integer (n : integer) {
            n = n + 10;
            a[0] = 1239;
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """
        x: float = 3.0;
        a : array [2] of integer;
        foo: function auto(){}
        fact : function integer (n : integer) {
            b: float;
            n = b + 1;
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """
        a : array [2] of integer;
        // foo: function auto(){}
        foo: function auto(x: integer){}
        // foo1: function auto(y: float){}
        fact : function integer (n : integer) {
            foo: float = 3.0;
            b: integer;
            // n1: float = foo(foo(1)); // foo(int)
            // n1: float = foo(1) + foo1(foo(100)); // foo: float foo1: float
            // n1: float = foo(1) + 1; // foo: int
            //n1: float = !foo(1) + 1; // TypeMisMatch
            n1: boolean = -foo(1) == true;
            // n1: float = -foo(1) + 1; // foo: float
        }
        main: function void(){}
    """

        expect = "Type mismatch in expression: UnExpr(-, FuncCall(foo, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """
        foo: function auto(x: integer){}
        foo1: function auto(x: float){}
        fact : function integer (n : integer) {
            // b: integer = 99;
            // b = foo(100); // foo: int
            // foo(19) = b // don't have this

            a : array [2] of integer;
            a[1] = (foo1(foo(1900)) + 1);
            // a[0] = 19;
            // a[2] = 10.1231;
            // a[2] = false;

            // foo: float = 3.0;
            // foo = foo(100);

            // n1: float = foo(foo(1)); // foo(int)
            // n1: float = foo(1) + foo1(foo(100)); // foo: float foo1: float
            // n1: float = foo(1) + 1; // foo: int
            //n1: float = !foo(1) + 1; // TypeMisMatch
            // n1: boolean = -foo(1) == true;
            // n1: float = -foo(1) + 1; // foo: float
        }
        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        // foo: function auto(){}
        foo1: function auto(y: boolean){}
        foo2: function boolean(){}
        fact : function integer (n : integer) {
            // if (foo1(foo()) == true){}
            a : array [2] of integer;
            // if (8 < 5){}
            // if (8.0 < 5){}
            // if (a[1, 2, 3] > 100){}
            // if (a[1, 2, 3] > foo()){}
            // if (!foo()){}
            // if (!foo2()){}
            i: float = 3;
            // i: integer = 3;
            for (i = 123, 9 > 8, i + 1){}
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, IntegerLit(9), IntegerLit(8)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        // foo: function auto(){}
        // foo1: function auto(y: boolean){}
        foo2: function boolean(i: integer){}
        /*fact : function integer () {
            // a : array [2] of integer;
            // i: float = 3;
        }*/
        main: function void(){

            // i: integer = 3;
            // for (i = 123, i > 8, i + 1){}

            for (i = 123, i > 8, foo2(1)){}
            // for (i = 123, i > 8, i + 1.4){}
        }
    """

        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, Id(i), IntegerLit(8)), FuncCall(foo2, [IntegerLit(1)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
        foo2: function auto(i: integer){
            return 1;
        }

        main: function void(){}
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """
        foo1: function integer(){}
        foo2: function float(inherit x: boolean){
            return 1;
        }
        foo3: function float() inherit foo1{
            printInteger(1);
            preventDefault();
            return 1.123;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo3"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """

        x: integer;
        foo1: function integer(inherit x: float){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10);
            z: float = 10.1;
            return 1;
        }
        foo3: function float(out z: float) inherit foo2{
            preventDefault();
            y: integer = 10;
            printInteger(1);
            return 1.123;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """

        x: integer;
        foo1: function integer(inherit x: float){}
        foo2: function float(inherit y: float){
            super(10);
            z: float = 10.1;
            return 1;
        }
        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """

        x: integer;
        foo1: function integer(){}

        foo2: function float(inherit y: float) inherit foo1{
            // super();
            // preventDefault();
            z: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        x: integer;
        foo1: function integer(y: integer){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10, 1.0);
            z: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Type mismatch in expression: FloatLit(1.0)"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """

        x: integer;
        foo1: function integer(inherit y: integer){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10);
            z: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """

            x: integer;
            foo1: function integer(inherit y: integer){}

            foo2: function float(inherit z: float) inherit foo1{
                super(10);
                y: float = 10.1;
                return 1;
            }

            main: function void(){
                x: integer = readInteger();
            }
        """

        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """

        x: integer;

        foo2: function float(inherit z: float) inherit foo1{
            preventDefault();
            y: float = 10.1;
            return 1;
        }

        foo1: function integer(inherit y: integer){}

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """

        x: integer;
        foo1: function integer(inherit y: integer){}

        foo2: function float(inherit z: float) inherit foo1{
            preventDefault(1, 2, 3);
            y: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Type mismatch in statement: CallStmt(preventDefault, IntegerLit(1), IntegerLit(2), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_55(self):
        input = """

        x: integer;
        foo1: function auto(){}

        foo2: function float(inherit z: float) inherit foo1{
            super(1);
            y: float = 10.1;
            return 1;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """
            x: integer = 65;
            fact: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * fact(n - 1);
            }
            inc: function void(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = fact(3);
                inc(x, delta);
                printInteger(x);
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """

        foo1: function auto(inherit x: boolean){}
        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """
        main: function void() {
            x: array[4, 10, 10] of integer;
            for (i = 1, i < 100, i+1) {
                if (i % 2 == 0) {
                    while(true){
                        x[i, 0, 1] = i;
                        break;
                    }
                    do{
                        continue;
                    }while(true);
                    continue;
                    break;
                } else {
                    x[0, i, i] = i + 1;
                }
                break;
            }
            break;
        }
    """

        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """
        main: function void(argc: integer, argv: array[100] of string) {}
    """

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = r"""
        isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of string = {"hello", "world", "!!!", "", "test\n"};

            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """

        expect = "Type mismatch in expression: BinExpr(!=, ArrayCell(strs, [Id(i)]), ArrayCell(strs, [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))]))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = r"""
        isPalindrome: function boolean(strs: array[100] of integer, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of integer = {1, 2, 3, 4 ,5};

            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = r"""
        isPalindrome: function boolean(strs: array[100] of integer, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return 10.123;
        }
        main: function void() {}
    """

        expect = "Type mismatch in statement: ReturnStmt(FloatLit(10.123))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = r"""
        gcdIteration: function integer(p: integer, q: integer) {
          while (p * q != 0) {
            if (p > q) {
              p = p % q;
            } else {
              q = q % p;
            }
          }
          return p + q;
        }
        gcdRecursion: function integer(p: integer, q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
        main: function void() {}
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = r"""
        n : integer = 10;
        recursiveSearch: function integer(out n: integer, m: integer, arr: array[100] of integer, index: integer) {
          index = index + 1;
          if (index > n) {
            return -1;
          }
          if (arr[index - 1] == m) {
            for (i = index - 1, i < n - 1, i+1) {
              arr[i] = arr[i + 1];
            }
            n = n - 1;
            return index - 1;
          }
          return recursiveSearch(n, m, arr, index);
        }
        main: function void() {
            arr   : array [5] of integer = {1, 91, 0, -100, 100};
            printInteger(recursiveSearch(n, 10, arr, 0));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = r"""
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size / 2, i+1) {
            if (head[i] != tail[i])
              return false;
          }
          return true;
        }
        main: function void() {
            head, tail: array [5] of integer = {1, 91, 0, -100, 100}, {10, 1, 1000, -100, 100};
            printBoolean(isSymmetry(head, tail, 5));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = r"""
        checkElements: function boolean (arr: array[100] of integer, n: integer) {
          if ((n > 1000) || (n < 0))
            return false;
          for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j]/*)*/)
                return false;
            }
          }
          return true;
        }
        main: function void() {
            arr   : array [5] of integer = {1, 91, 0, -100, 100};
            printBoolean(checkElements(arr, 0));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = r"""
        binarySearch: function integer(arr: array[100] of integer, left: integer, right: integer, x: integer) {
          if (right >= left) {
            mid:integer = left + (right - left) / 2;
            if (arr[mid] == x)
              return mid;
            if (arr[mid] > x)
              return binarySearch(arr, left, mid - 1, x);
            return binarySearch(arr, mid + 1, right, x);
          }
          return -1;
        }
        main: function void() {
            arr   : array [5] of integer = {1, 91, 0, -100, 100};
            binarySearch(arr, 0, 4, 0);
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = r"""
            main: function void() {
                j: boolean = false;
                for (i = 1, i < 100, i+1) {
                    j : integer = 0;
                    j = true;
                }
            }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(j), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = r"""
        main: function void() {
            for (i = 1, i < 100, i+1) {
                j : integer = 0;
                while (j < 200) {
                    if (i + j >= 20) {
                        break;
                    } else {
                     j = j + 1;
                    }
                }
            }
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = r"""
        x :  integer = 1;
        main: function void(out x: integer) {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = r"""
        x :  integer = 1;
        foo: function auto(x: integer, y: float){}
        main: function void(out x: integer) {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = r"""
        x :  integer = 1;
        foo: function auto(x: integer, y: float){}
        main: function void() {
            for (i = 1, i < 100, i+1) {
                for (j = 1, j < 200, j+1) {
                    if (i + j >= 2) {
                        foo(2, x + 1);
                    }
                }
            }
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = r"""
            checkElementsUniqueness: function auto (arr: array[100] of integer, n: integer) {
              if ((n > 1000) || (n < 0))
                return 1;
              for (i = 0, i < n - 1, i+1) {
                for (j = i + 1, j < n, j+1) {
                  if (arr[i] == arr[j])
                    return false;
                }
              }
              return true;
            }

            main: function void() {
                arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
                if (checkElementsUniqueness(arr, 6)) printString("Correct!");
                else printString("Wrong!");
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = r"""
        checkElementsUniqueness: function auto (arr: array[100] of integer, n: integer) {
          if ((n > 1000) || (n < 0))
            return true;
          for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j])
                return false;
            }
          }
          return true;
        }

        main: function void() {
            arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
            if (checkElementsUniqueness(arr, 6)) printString("Correct!");
            else printString("Wrong!");
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = r"""
        a : integer = 2;
        main: function void() {
            do{
                c = c + 1;
            }
            while (a==c);
        }
    """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = r"""
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            f[1] = d + 2.5;
            return f[1];
        }
        main: function void() {}
    """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(f, [IntegerLit(1)]), BinExpr(+, Id(d), FloatLit(2.5)))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = r"""
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            else
                break;
        }
        main: function void() {}
    """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = r"""
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            printString(foo("Hello", 1.2312));
        }
        main: function void() {}
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = r"""
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            return a;
            do
            {
                a = b + 1;
            }
            while (a==true);
        }
        main: function void() {
        }
    """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(b), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = r"""
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return b;
            }
            while (a==true);

            return a;
        }
        main: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = r"""
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return b;
            }
            while (a==102);

            return a;
        }
        main: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = r"""
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return a;
            }
            while (a==102);
            return b;
        }
        main: function void() {
        }
    """
        expect = "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = r"""
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else
                return false;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            readInteger(n);
            if (count(n) == true)
                print("n is prime number");
            else
                print("n is not prime number");
        }
    """
        expect = "Type mismatch in statement: CallStmt(readInteger, Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = r"""
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else
                return false;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            if (count(n) == true)
                printString("n is prime number");
            else
                printString("n is not prime number");
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + randomChar();
            return s;
        }
        main: function void() {}
    """
        expect = "Undeclared Function: randomChar"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + readString();
            return s;
        }
        main: function void() {}
    """
        expect = "Type mismatch in expression: BinExpr(+, Id(s), FuncCall(readString, []))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s::readString();
            return s;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            printString("The random string length n is "::random(n));
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = r"""
        a,b: array[10] of integer;
        swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
        {
            if (n>10)
                return;
            else
            {
                temp,i : integer;
                for (i=0,i<n,i+1)
                {
                    temp=a[i];
                    a[i]=b[i];
                    b[i]=temp;
                }
            }
        }
        main: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
            foo3: function auto(inherit i: integer, a: float) {}
            foo2: function auto(inherit b: float, a: float) inherit foo3 {
                super(true, 1.0);
            }
            main: function void(){
                foo2(foo1(1.0), 1);
            }
            """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit b: float, a: float) inherit foo3 {
            super(1, 1.0);
            c: integer = 1;
        }
        foo1: function integer(inherit c: float) inherit foo2 {
            super(1, 1.0);
            i: integer = 2;
            return 1;
        }

        main: function void(){
            foo2(foo1(1.0), 1);
        }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
            foo2: function auto() {}
            foo1: function integer(inherit c: float) inherit foo2 {
                printInteger(super(1.0, 1.0));
                i: integer = 2;
                return 1;
            }

            main: function void(){
                foo2(foo1(1.0), 1);
            }
            """
        expect = "Type mismatch in expression: FloatLit(1.0)"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """
            main: function void() {
                x: array[4, 10, 10] of integer;
                for (i = 1, i < 100, i+1) {
                    if (i % 2 == 0) {
                        x[i, 0, 1] = i;
                    } else {
                        x[0, i] = i + 1;
                    }
                    for(j = 1, j < 100, j+1) {
                        continue;
                    }
                    while(true) {continue;}
                    break;
                }
            }
            """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(x, [IntegerLit(0), Id(i)]), BinExpr(+, Id(i), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """
            foo: function auto(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                x: integer = 2;
                for (i = 1, i < 100, i+1) {
                    foo(x + 1, foo(i + 1, foo(x + 2, 1)));
                }
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
            x: array[0, 100] of integer;
            inc: function auto(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = 1;
                i: integer = 1;
                if (x[i, 0] > inc(x[0, i])) {
                    x[i, 0] = i;
                } else {
                    x[0, i] = i + 1;
                }
            }
            """
        expect = "Type mismatch in expression: FuncCall(inc, [ArrayCell(x, [IntegerLit(0), Id(i)])])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    # Need to test
    # def test_95(self):
    #     input = """
    #         x: integer;
    #         inc: function auto(out n: integer, delta: integer) {
    #             n = n + delta;
    #             return 1;
    #         }
    #         main: function void() {
    #             delta: integer = 1;
    #             n1: float = -inc(x, delta) + 1; // inc: integer
    #         }
    #         """
    #     expect = "Need to test"
    #     self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
            x: integer;
            a: array [10] of integer;
            inc: function auto(out n: integer, delta: integer) {
                n = n + delta;
            }
            main: function void() {
                delta: integer = 1;
                delta = inc(delta, x);
            }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """
            x: integer;
            jump: function integer(inherit nums: array[100] of integer, size: integer){
              minjump: integer = size - 1;
              return minjump;
            }

            jump_: function float(inherit z: float) inherit jump {
                preventDefault();
                y: float = 10.1;
                return nums[0];
            }

            main: function void(){
            }
        """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
            x: integer = foo(1); // Correct
            y: integer = 1;
            foo: function integer(x: integer){
                return x;
            }
            main: function void(){}
        """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 498))

    # Need to Test
    # def test_99(self):
    #     input = """

    #     foo1: function integer(){}

    #     foo2: function float(inherit x: boolean) inherit foo1{
    #         return 1;
    #     }
    #     foo3: function float() inherit foo2{
    #         super(false);
    #         preventDefault();
    #         x: float = 10.2;
    #         return 1.123;
    #     }

    #     main: function void(){
    #         x: integer = readInteger();
    #     }
    # """
    #     expect = "Need To Test"
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    def test_100(self):
        input = r"""
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            return f[1];
        }

        bar: function void (inherit out a: float, inherit out b: string) inherit foo {
            super("Hello", 123);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            else
                break;
        }
        main: function void() {}
    """
        expect = "Type mismatch in expression: BinExpr(==, Id(a), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_101(self):
        input = """
            x: integer;
            jump: function integer(inherit nums: array[100] of integer, size: integer){
              minjump: integer = size - 1;
              return minjump;
            }

            jump_: function float(ns: array[100] of integer, inherit z: float) inherit jump {
                super(ns, 10);
                y: float = 10.1;
                return nums[0];
            }

            main: function void(){
            }
        """

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test_102(self):
        input = """
            x: integer = y; // Undeclared y
            y: integer = 1;
            foo: function integer(x: integer){
                return 1;
            }
            main: function void(){}
        """

        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test_103(self):
        input = r"""
        max_two_nums: function auto (a: integer, b: integer) {
            if (a > b) {
                return a;
            }
            return b;
        }

        main: function void(){
            // max_two_nums(1, 1, 2.3); //-> Type mismatch in statement: CallStmt(max_two_nums, IntegerLit(1), IntegerLit(1), FloatLit(2.3))
            //max_two_nums(1.0, 1); // -> Type mismatch in statement: CallStmt(max_two_nums, FloatLit(1.0), IntegerLit(1))
            // max_two_nums(1.0); // -> Type mismatch in statement: CallStmt(max_two_nums, FloatLit(1.0))
            // max_two_nums(); // -> Type mismatch in statement: CallStmt(max_two_nums, )
            // a: integer = max_two_nums(1, 1, 2.3); // -> Type mismatch in expression: FuncCall(max_two_nums, [IntegerLit(1), IntegerLit(1), FloatLit(2.3)])
            // a: integer = max_two_nums(1.0, 1); // -> Type mismatch in expression: FuncCall(max_two_nums, [FloatLit(1.0), IntegerLit(1)])
            // a: integer = max_two_nums(1.0); // -> Type mismatch in expression: FuncCall(max_two_nums, [FloatLit(1.0)])
            a: integer = max_two_nums(); // -> Type mismatch in expression: FuncCall(max_two_nums, [])
        }
    """
        expect = "Type mismatch in expression: FuncCall(max_two_nums, [])"
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test_104(self):
        input = r"""
        a: array[2, 2, 3] of integer;
        //a: array[2, 2] of integer = {{1, 2}, {3, 4}};
        //b: array[2] of integer = 0; // incorrect
        // b: array[2] of integer = a[0]; // incorrect
        //b: array[2] of integer = a[0, 1]; // correct
        c: array[2, 2] of integer = a[0]; // correct
        main: function void() {
            //c: integer = b[0];
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 504))

    def test_105(self):
        input = r"""
        x: integer = inc1(2);
        main: function void() {
            y: integer = inc1(1);
        }
        inc1: function integer(a: integer) {
            return 1;
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 505))

    def test_106(self):
        input = r"""
        main: function void() inherit inc1 {
        }
        inc1: function void() {
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 506))

    def test_107(self):
        input = r"""
        a: array[2, 2, 3] of integer;
        b: array[2] of integer = a[1, 1];
        main: function void() {
            c: integer = b[0];
        }
    """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 507))

    def test_108(self):
        input = r"""
        main: function void() {
            x(1, 2);
        }
        x: function void(a: integer) {

        }
    """
        expect = "Type mismatch in statement: CallStmt(x, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 508))

    def test_109(self):
        input = r"""
        foo: function integer(){}

        main: function void(){
            m: integer;
            m = foo + 1;
        }
    """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 509))

    def test_110(self):
        input = r"""
        foo: function void(){}

        bar: function integer(){return foo();}

        foo: function integer(){return 1;}
    """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 510))

    def test_111(self):
        input = r"""
        max_two_nums: function auto (a: integer, b: integer) {
            if (a > b) {
                return a;
            }
            return b;
        }

        main: function void(){
            a: integer = max_two_nums(1.0, 1);
        }
    """
        expect = "Type mismatch in expression: FuncCall(max_two_nums, [FloatLit(1.0), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 511))

    def test_112(self):
        input = r"""
        max_two_nums: function auto (a: integer, a: integer) inherit foo {
        }

        main: function void(){
            a: integer = max_two_nums(1, 1);
        }
    """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 512))

    def test_113(self):
        input = r"""
        M: function void (a: integer) inherit N {}

        N: function void (inherit a: integer) {}
    """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 513))

    def test_114(self):
        input = r"""
        max_two_nums: function auto (a: integer, b: integer) {
            if (a > b) {
                return a;
            }
            return b;
        }

        foo: function void () inherit max_two_nums{
            //super(1, 1, 2.3); //-> Type mismatch in expression: FloatLit(2.3)
            // super(1.0, 1); // -> Type mismatch in expression: FloatLit(1.0)
            // super(1.0); // -> Type mismatch in expression: None
            super(); // -> Type mismatch in expression: None
        }

        main: function void(){
        }
    """
        expect = "Type mismatch in expression: None"
        self.assertTrue(TestChecker.test(input, expect, 514))
