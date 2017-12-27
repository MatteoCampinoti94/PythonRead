import msvcrt

def getch_windows(NONBLOCK=False):
    if NONBLOCK:
		if msvcrt.kbhit():
			return msvcrt.getch().decode()
	else:
		return msvcrt.getch().decode()
