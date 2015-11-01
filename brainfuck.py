import sys
from getch import getch

commands = '><+-.,[]'

class BrainfuckInterpreter:
    def __init__(self):
        self.i = 0
        self.p = 0
        self.cells = [0]

    @staticmethod
    def find_matching_paren(source, c):
        paren = 0
        d = {'[':']', ']':'['}
        for k in range(len(source)):
            if source[k]==c:
                paren += 1
            elif source[k]==d[c]:
                if paren == 0:
                    return k
                paren -= 1
        return -1

    def show_cells(self):
        print("Cell pointer is at", self.p)
        for i in range(len(self.cells)):
            print(i, self.cells[i],end=" ")
            if self.p == i:
                print("<-")
            else:
                print("")

    def eval(self, source):
        s = ''
        while self.i != len(source):
            c = source[self.i]
            if c == '>':
                if self.p == len(self.cells)-1:
                    self.cells.append(0)
                self.p += 1
            elif c == '<':
                if self.p != 0:
                    self.p -= 1
            elif c == '+':
                self.cells[self.p] += 1
            elif c == '-':
                self.cells[self.p] -= 1
            elif c == '.':
                sys.stdout.write(chr(self.cells[self.p]))
                sys.stdout.flush()
                s += chr(self.cells[self.p])
            elif c == ',':
                self.cells[self.p] = ord(getch())
            elif c == '[' and self.cells[self.p] == 0:
                self.i += self.find_matching_paren(source[self.i+1:], c)
            elif c == ']' and self.cells[self.p] != 0:
                self.i -= self.find_matching_paren(source[self.i-1::-1], c) + 1
            self.i += 1
        return s

def usage():
    print("", file=sys.stderr)
    print("Usage: {0} <filename>".format(__file__), file=sys.stderr)
    print("", file=sys.stderr)
    print("For more information, please visit https://github.com/handrake/brainfuck", file=sys.stderr)
    print("", file=sys.stderr)

def shell():
    source = ''
    while 1:
        line = input("brainfuck>> ")
        if line == '':break
        source += line
    source = ''.join([c for c in source if c in commands])
    return source

def main():
    import getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", [])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
    filename = args[0] if args[0] else None
    if filename:
        source = open(filename).read()
    else:
        source = shell()
    interpreter = BrainfuckInterpreter()
    interpreter.eval(source)
    interpreter.show_cells()

if __name__ == "__main__":
    main()
