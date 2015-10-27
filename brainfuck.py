import sys

commands = ['>','<','+','-','.',',','[',']']

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
        elif c == '[':
            if cells[p] == 0:
                paren = 0
                for k in range(i+1,len(source)):
                    if source[k]=='[':
                        paren += 1
                    elif source[k]==']':
                        if paren == 0:
                            i = k
                            break
                        paren -= 1
        elif c == ']':
            if cells[p] != 0:
                paren = 0
                for k in range(i-1,0,-1):
                    if source[k]==']':
                        paren += 1
                    elif source[k]=='[':
                        if paren == 0:
                            i = k
                            break
                        paren -= 1
        i += 1
            
            
def main():
    source = ''
    while 1:
        line = raw_input("brainfuck>> ")
        if line == '':break
        source += line
    source = ''.join([c for c in source if c in commands])
    eval(source)

if __name__ == "__main__":
    main()
