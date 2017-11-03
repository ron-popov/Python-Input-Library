# Python Input Library
A library that allowes to simulate windows key presses

## Structure & Documantation
The library consists of 3 sections, each one has different methods that do different things.


### utils
The utils file contains random methods that are useful but don't belong to a certain catagory.

#### GetMonitorRes
__Description__ : Returns the resolution of your monitor. Not tested for multiple monitor setups.
__Parameters__ : None
__Return value__ : Tuple of length 2, first element represents width and second element represents height.

#### Delay
__Description__ : Delays the program for a certain amount of time.
__Parameters__ : The number of seconds to delay the program. Doesn't have to be a whole number.
__Return value__ : None


### keyboard
The keyboard file contains methods that interact with the keyboard.

#### HoldKey
__Description__ : Starts pressing a certain key.
__Parameters__ : A hexadecimal key code of the wanted key. A list of key hexadecimal key codes can be found [here](https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx?f=255).
__Return value__ : None

#### ReleaseKey
__Description__ : Releases a certain key.
__Parameters__ : A hexadecimal key code of the wanted key. A list of key hexadecimal key codes can be found [here](https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx?f=255).
__Return value__ : None


# mouse
The mouse file contains method that interact with the mouse.

# GetMousePos
__Description__- : Returns the position of the mouse
__Parameters__ : None
__Return value__ : Tuple of length 2, the first elements represents the x location and the second element represents y location.

# SetMousePos
__Description__ : Changes the mouse location
__Parameters__ : 
* The desired x location.
* The desired y location.
__Return value__ : none
