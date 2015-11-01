import unittest
import brainfuck

hello_case = ("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.", "Hello World!\n")

class InterpreterTestCase(unittest.TestCase):
    def setUp(self):
        self.interpreter = brainfuck.BrainfuckInterpreter()
    def test_hello_world(self):
        self.assertEqual(hello_case[1], self.interpreter.eval(hello_case[0]))
    def test_missing_parenthesis(self):
        self.assertRaises(SyntaxError, self.interpreter.eval, '[++]+]')
