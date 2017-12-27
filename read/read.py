import sys

if sys.platform.startswith('linux'):
    from .getch_unix import getch_unix as getch
elif sys.platform == 'darwin':
    from .getch_unix import getch_unix as getch
elif sys.platform in ('win32', 'cygwin'):
    from .getch_windows import getch_windows as getch
else:
    raise NotImplemented('Platform "%s" not implemented' % sys.platform)

def getkey(getch_fn=None):
    if not getch_fn:
        # read first character from stdin
        c = getch()
        ct = None
        # keep reading from stdin with NONBLOCK flag until it returns empty
        #  meaning stdin has no more characters stored
        while ct != '':
            ct = getch(NONBLOCK=True)
            c += ct
        return c
    else:
        c1 = getchar_fn()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar_fn()
        if ord(c2) != 0x5b:
            return c1 + c2
        c3 = getchar_fn()
        if ord(c3) != 0x33:
            return c1 + c2 + c3
        c4 = getchar_fn()
        return c1 + c2 + c3 + c4