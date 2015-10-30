import unittest
import brainfuck

test_cases = [("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.", "Hello World!\n")]

class InterpreterTestCase(unittest.TestCase):
    def setUp(self):
        self.interpreter = brainfuck.BrainfuckInterpreter()
    def runTest(self):
        for case in test_cases:
            self.assertEqual(case[1], self.interpreter.eval(case[0]))
