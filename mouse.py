import win32api, win32con

# returns the current position of the mouse
def GetMousePos():
    x, y = win32api.GetCursorPos()
    return x,y

# moves the mouse cursur to the given coordinates
def SetMousePos(x,y):
    win32api.SetCursorPos((x, y))

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
