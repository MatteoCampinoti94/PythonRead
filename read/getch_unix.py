import sys, tty, termios
import fcntl, os

def getch_unix(NONBLOCK=False):
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr(fd)
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    ch = ''
    try:
        tty.setraw(fd)
        if NONBLOCK:
            fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        ch = sys.stdin.read(1)
    finally:
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    return ch
