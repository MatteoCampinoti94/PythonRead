import subprocess, sys

python_v = '.'.join([str(v) for v in sys.version_info[0:3]])
sys.stdout.write('Testing with python version %s\n\n' % python_v)

proc = subprocess.Popen(['python%s' % python_v[0], 'test.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

keys = {
    'LF': '\x0d',
    'CR': '\x0a',
    'ENTER': '\x0d',
    'BACKSPACE': '\x7f',
    'SPACE': '\x20',
    'ESC': '\x1b',
    'CTRL_A': '\x01',
    'CTRL_B': '\x02',
    'CTRL_C': '\x03',
    'CTRL_D': '\x04',
    'CTRL_E': '\x05',
    'CTRL_F': '\x06',
    'CTRL_Z': '\x1a',
    'ALT_A': '\x1b\x61',
    'CTRL_ALT_A': '\x1b\x01',
    'UP': '\x1b\x5b\x41',
    'DOWN': '\x1b\x5b\x42',
    'LEFT': '\x1b\x5b\x44',
    'RIGHT': '\x1b\x5b\x43',
    'CTRL_ALT_SUPR': '\x1b\x5b\x33\x5e',
    'F1': '\x1b\x4f\x50',
    'F2': '\x1b\x4f\x51',
    'F3': '\x1b\x4f\x52',
    'F4': '\x1b\x4f\x53',
    'F5': '\x1b\x4f\x31\x35\x7e',
    'F6': '\x1b\x4f\x31\x37\x7e',
    'F7': '\x1b\x4f\x31\x38\x7e',
    'F8': '\x1b\x4f\x31\x39\x7e',
    'F9': '\x1b\x4f\x32\x30\x7e',
    'F10': '\x1b\x4f\x32\x31\x7e',
    'F11': '\x1b\x4f\x32\x33\x7e',
    'F12': '\x1b\x4f\x32\x34\x7e',
    'PAGE_UP': '\x1b\x5b\x35\x7e',
    'PAGE_DOWN': '\x1b\x5b\x36\x7e',
    'HOME': '\x1b\x5b\x48',
    'END': '\x1b\x5b\x46',
    'INSERT': '\x1b\x5b\x32\x7e',
    'SUPR': '\x1b\x5b\x33\x7e',
    'ENDTEST': '$'
    }

for i in keys :
    sin = str(keys[i])
    sys.stdout.write('Test: %s %s ' % (i, sin.encode()))
    proc.stdin.write(sin.encode())
    proc.stdin.flush()
    c, sout = '', ''
    while c != '#':
        sout += c
        c = proc.stdout.read(1).decode()
    if sin == sout:
        sys.stdout.write('Okay\n')
    else:
        sys.stdout.write('Failed\n')
