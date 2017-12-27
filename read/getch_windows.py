import msvcrt

def getch_windows(NONBLOCK=False, encoding='utf-8'):
	if NONBLOCK:
		if msvcrt.kbhit():
			return msvcrt.getch().decode(encoding)
		else:
			return ''
	else:
		return msvcrt.getch().decode(encoding)
