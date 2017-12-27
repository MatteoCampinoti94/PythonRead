import sys, tty, termios
import fcntl, os

def getch_unix(NONBLOCK=False, encoding='utf-8'):
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr(fd)
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    ch = ''
    try:
        tty.setraw(fd)
        if NONBLOCK:
            fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        ch = sys.stdin.buffer.read(1).decode(encoding)
    finally:
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    return ch
