import sys, tty, termios
import fcntl, os

def getch_unix(NONBLOCK=False, encoding=None, raw=True):
    fd = sys.stdin.fileno()
    if raw:
        settings = termios.tcgetattr(fd)
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    ch = ''
    try:
        if raw:
            tty.setraw(fd)
        if NONBLOCK:
            fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        if encoding:
            ch = sys.stdin.buffer.read(1)
            if ch:
                ch = ch.decode(encoding)
            else:
                ch = ''
        else:
            ch = sys.stdin.read(1)
    finally:
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)
        if raw:
            termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    return ch
