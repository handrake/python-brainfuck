import sys

commands = '><+-.,[]'

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

def eval(source):
    i = 0
    p = 0
    cells = [0]
    while i != len(source):
        c = source[i]
        #print 'i =', i, 'cells =', cells, 'p =', p, 'c =', c, '*p =', cells[p]
        if c == '>':
            if p == len(cells)-1:
                cells.append(0)
            p += 1
        elif c == '<':
            if p != 0:
                p -= 1
        elif c == '+':
            cells[p] += 1
        elif c == '-':
            cells[p] -= 1
        elif c == '.':
            sys.stdout.write(chr(cells[p]))
            sys.stdout.flush()
        elif c == ',':
            cells[p] = sys.stdin.read(1)
        elif c == '[' and cells[p] == 0:
            i += find_matching_paren(source[i+1:], c)
        elif c == ']' and cells[p] != 0:
            i -= find_matching_paren(source[i-1::-1], c) + 1
        i += 1

def main():
    source = ''
    while 1:
        line = input("brainfuck>> ")
        if line == '':break
        source += line
    source = ''.join([c for c in source if c in commands])
    eval(source)

if __name__ == "__main__":
    main()
