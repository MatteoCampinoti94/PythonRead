import sys

if sys.platform.startswith('linux'):
    from .getch_unix import getch_unix as getch
elif sys.platform == 'darwin':
    from .getch_unix import getch_unix as getch
elif sys.platform in ('win32', 'cygwin'):
    from .getch_windows import getch_windows as getch
else:
    raise NotImplemented('Platform "%s" not implemented' % sys.platform)

def getkey(getch_fn=None, encoding=None, raw=True):
    if getch_fn:
        # if an external function is given then assume NONBLOCK flag is not set
        #  keep reading and check for escape sequences
        c1 = getch_fn()
        if ord(c1) != 0x1b:
            return c1
        c2 = getch_fn()
        if ord(c2) != 0x5b:
            return c1 + c2
        c3 = getch_fn()
        if ord(c3) != 0x33:
            return c1 + c2 + c3
        c4 = getch_fn()
        return c1 + c2 + c3 + c4
    else:
        # read first character from stdin
        c = getch(NONBLOCK=False, encoding=encoding, raw=raw)
        ct = None
        # keep reading from stdin with NONBLOCK flag until it returns empty
        #  meaning stdin has no more characters stored
        while ct != '':
            ct = getch(NONBLOCK=True, encoding=encoding, raw=raw)
            c += ct
        if raw:
            c = c[0:-1]
        return c

def getline(getch_fn=None, encoding=None):
    if getch_fn:
        l, lt = '', ''
        # keep reading till a return or newline entered
        while lt not in ('\r', '\n'):
            l += lt
            lt = getch_fn()
        return l
    else:
        l, lt = '', ''
        # keep reading till a return or newline entered
        while lt not in ('\r', '\n'):
            l += lt
            lt = getch(NONBLOCK=False, encoding=encoding, raw=raw)
        return l

def flush():
    c = None
    while c != '':
        c = getch(NONBLOCK=True, raw=False)