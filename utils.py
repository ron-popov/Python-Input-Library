import time
import ctypes

def GetMonitorRes():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize

def Delay(seconds):
    time.sleep(seconds)
