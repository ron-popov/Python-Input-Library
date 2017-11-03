# Python Input Library
A library that allowes to simulate windows key presses

## Structure & Documantation
The library consists of 3 sections, each one has different methods that do different things.


### utils
The utils file contains random methods that are useful but don't belong to a certain catagory.

#### GetMonitorRes
Description : Returns the resolution of your monitor. Not tested for multiple monitor setups.  
Parameters : None.  
Return value : Tuple of length 2, first element represents width and second element represents height.  

#### Delay
Description : Delays the program for a certain amount of time.  
Parameters : The number of seconds to delay the program. Doesn't have to be a whole number.  
Return value : None.  


### keyboard
The keyboard file contains methods that interact with the keyboard.

#### HoldKey
Description : Starts pressing a certain key.  
Parameters : A hexadecimal key code of the wanted key. A list of key hexadecimal key codes can be found [here](https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx?f=255).  
Return value : None.  

#### ReleaseKey
Description : Releases a certain key.  
Parameters : A hexadecimal key code of the wanted key. A list of key hexadecimal key codes can be found [here](https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx?f=255).  
Return value : None.  


# mouse
The mouse file contains method that interact with the mouse.

# GetMousePos
Description : Returns the position of the mouse.  
Parameters : None.  
Return value :
* The mouse x location.
* The mouse y location.

# SetMousePos
Description : Changes the mouse location  
Parameters : 
* The desired x location.  
* The desired y location.  

Return value: None.  
