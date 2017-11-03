import keyboard # imports all of the keyboard commands
import mouse # imports all of the mouse commands
import utils # imports random utility commands

# hold and releases the key with hex code 0x48
# basicly a single press
keyboard.HoldKey(0x48)
keyboard.ReleaseKey(0x48)

# or we can wrap those 2 lines in a method !
def PressKey(hexKeyCode):
    keyboard.HoldKey(hexKeyCode)
    keyboard.ReleaseKey(hexKeyCode)

# and call it a bunch of times
PressKey(0x45)
PressKey(0x4C)
PressKey(0x4C)
PressKey(0x4F)
PressKey(0x20)
PressKey(0x57)
PressKey(0x4F)
PressKey(0x52)
PressKey(0x4C)
PressKey(0x44)

# saves the x,y coordinates of the mouse position
# in a list of length 2, where the first element represents
# x location and the second element the y location
# then it print it
currentMousePos = mouse.GetMousePos()
print("Calculating Mouse Position")
utils.Delay(1)
print("Your mouse is at X:" + str(currentMousePos[0]) + " Y:" + str(currentMousePos[1]))
utils.Delay(3)

print("Now the fun part begins...")
utils.Delay(3)

# this is just for fun and doesn't serve any purpose
# NOTE : this might not work on a multiple displays setup
monitorWidth,monitorHeight = utils.GetMonitorRes()
counter = 0
while True:
    mouse.SetMousePos(counter % monitorWidth, counter % monitorHeight)
    counter += 1
    utils.Delay(0.005)
