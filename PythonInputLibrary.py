import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize


# Functions

def PrintString(to_print):
    for c in to_print:
        PressKey(GetKeyCode(c))
        

def ChangeLanguage():
    RawPressKey(GetKeyCode('shift'))
    RawPressKey(GetKeyCode('alt'))
    RawReleaseKey(GetKeyCode('alt'))
    RawReleaseKey(GetKeyCode('shift'))

def PressKey(KeyCode):
    RawPressKey(KeyCode)
    RawReleaseKey(KeyCode)

def RawPressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def RawReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def delay(length):
    time.sleep(length)

def GetKeyCode(char):
    special_keys = {
        'enter' : 0x0D , 
        'delete' : 0x2E , 
        'shift' : 0xA0, 
        'ctrl' : 0x11, 
        'up' : 0x26, 
        'down' : 0x28, 
        'left' : 0x25,
        'right' : 0x27,
        'space' : 0x20,
        'alt' : 0x12
    }
    if char in special_keys:
        return special_keys[char]
    elif(ord(char) <= 57 and ord(char) >= 48):
        return 0x30 + (ord(char) - ord('0'))
    else :
        char = char.upper()
        return 0x41 + (ord(char) - ord('A'))

def SinglePress(char):
    PressKey(char)
    ReleaseKey(char)
    
def CominePress(listy):
    for x in listy:
        PressKey(x)
    for x in listy:
        ReleaseKey(x)

'''
if __name__ == "__main__":
    print("Before")
    time.sleep(5)
    print("After")
    for i in range(20):
        PressKey(0x11)
        PressKey(0x56)
        delay(0.01)
        ReleaseKey(0x11)
        ReleaseKey(0x56)
        delay(0.01)
        PressKey(0x0D)
        delay(0.01)
        ReleaseKey(0x0D)
        delay(0.01)
'''
