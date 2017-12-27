import msvcrt

def getch_windows():
    while msvcrt.kbhit():
        msvcrt.getch()
    ch = msvcrt.getch()
    while ch.decode() in '\x00\xe0':
        msvcrt.getch()
        ch = msvcrt.getch()
    return ch.decode()
