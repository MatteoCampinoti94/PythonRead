import sys, readkeys

c = None
while c != '$':
    c = readkeys.getkey(raw=False)
    sys.stdout.write(c + '#')
    sys.stdout.flush()

c = None
while c != '$':
    c = readkeys.getkey(raw=False)
    sys.stdout.write(c + '#')
    sys.stdout.flush()

c = None
while c != '$':
    c = readkeys.getkey(raw=False)
    sys.stdout.write(c + '#')
    sys.stdout.flush()

c = None
while c != '$':
    c = readkeys.getch(raw=False)
    sys.stdout.write(c + '#')
    sys.stdout.flush()
