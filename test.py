import sys, readkeys

c = None
while c != '$':
    c = readkeys.getkey(raw=False)
    sys.stdout.write(c + '#')
    sys.stdout.flush()
