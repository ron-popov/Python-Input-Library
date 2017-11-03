import ctypes
from ctypes import wintypes
import time
import win32api, win32con
import time
import pyautogui

class Utils:
     
    def Delay(seconds):
        time.sleep(seconds)

class Mouse:

    # returns the current position of the mouse
    def GetMousePos():
        x, y = win32api.GetCursorPos()
        return x,y

    # starts holding the right mouse button
    def HoldRightButton():
        x, y = GetMousePos()
        win32api.mouse_event(win32con.MOUSEEVETF_RIGHTDOWN,x,y,0,0)

    # releases the right mouse button
    def ReleaseRightButton():
        x, y = getmousepos()
        win32api.mouse_event(win32con.MOUSEEVETF_RIGHTUP,x,y,0,0)

    # starts holding the left mouse button
    def HoldLeftButton():
        x, y = getmousepos()
        win32api.mouse_event(win32con.MOUSEEVETF_LEFTDOWN,x,y,0,0)

    # releases the left mouse button
    def ReleaseLeftButton():
        x, y = getmousepos()
        win32api.mouse_event(win32con.MOUSEEVETF_LEFTUP,x,y,0,0)
    
    # moves the mouse cursur to the given coordinates
    def MoveCursor(x,y):
        win32api.SetCursorPos((x, y))

# class Keyboard:

#     # ------------ Computer Magic Start -----------------
#     user32 = ctypes.WinDLL('user32', use_last_error=True)

#     INPUT_MOUSE    = 0
#     INPUT_KEYBOARD = 1
#     INPUT_HARDWARE = 2

#     KEYEVENTF_EXTENDEDKEY = 0x0001
#     KEYEVENTF_KEYUP       = 0x0002
#     KEYEVENTF_UNICODE     = 0x0004
#     KEYEVENTF_SCANCODE    = 0x0008

#     MAPVK_VK_TO_VSC = 0

#     # msdn.microsoft.com/en-us/library/dd375731
#     VK_TAB  = 0x09
#     VK_MENU = 0x12

#     # C struct definitions

#     wintypes.ULONG_PTR = wintypes.WPARAM

#     class MOUSEINPUT(ctypes.Structure):
#         _fields_ = (("dx",          wintypes.LONG),
#                     ("dy",          wintypes.LONG),
#                     ("mouseData",   wintypes.DWORD),
#                     ("dwFlags",     wintypes.DWORD),
#                     ("time",        wintypes.DWORD),
#                     ("dwExtraInfo", wintypes.ULONG_PTR))

#     class KEYBDINPUT(ctypes.Structure):
#         _fields_ = (("wVk",         wintypes.WORD),
#                     ("wScan",       wintypes.WORD),
#                     ("dwFlags",     wintypes.DWORD),
#                     ("time",        wintypes.DWORD),
#                     ("dwExtraInfo", wintypes.ULONG_PTR))

#         def __init__(self, *args, **kwds):
#             super(KEYBDINPUT, self).__init__(*args, **kwds)
#             # some programs use the scan code even if KEYEVENTF_SCANCODE
#             # isn't set in dwFflags, so attempt to map the correct code.
#             if not self.dwFlags & KEYEVENTF_UNICODE:
#                 self.wScan = user32.MapVirtualKeyExW(self.wVk,
#                                                      MAPVK_VK_TO_VSC, 0)

#     class HARDWAREINPUT(ctypes.Structure):
#         _fields_ = (("uMsg",    wintypes.DWORD),
#                     ("wParamL", wintypes.WORD),
#                     ("wParamH", wintypes.WORD))

#     class INPUT(ctypes.Structure):
#         class _INPUT(ctypes.Union):
#             _fields_ = (("ki", KEYBDINPUT),
#                         ("mi", MOUSEINPUT),
#                         ("hi", HARDWAREINPUT))
#         _anonymous_ = ("_input",)
#         _fields_ = (("type",   wintypes.DWORD),
#                     ("_input", _INPUT))

#     LPINPUT = ctypes.POINTER(INPUT)

#     def _check_count(result, func, args):
#         if result == 0:
#             raise ctypes.WinError(ctypes.get_last_error())
#         return args

#     user32.SendInput.errcheck = _check_count
#     user32.SendInput.argtypes = (wintypes.UINT, # nInputs
#                                  LPINPUT,       # pInputs
#                                  ctypes.c_int)  # cbSize

#     # ------------ Computer Magic End -----------------


#     # starts holding the given key
#     def HoldKey(hexCodeKey):
#         x = INPUT(type=INPUT_KEYBOARD,
#                   ki=KEYBDINPUT(wVk=hexKeyCode))
#         user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    
#     # releases the given key
#     def ReleaseKey(hexCodeKey):
#         x = INPUT(type=INPUT_KEYBOARD,
#                   ki=KEYBDINPUT(wVk=hexKeyCode,
#                                 dwFlags=KEYEVENTF_KEYUP))
#         user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
