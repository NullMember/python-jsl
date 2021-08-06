# python-jsl
Python Wrapper for JoyShockLibrary using ctypes

# How to use

Just `import JoyShockLibrary` in your project or use `from JoyShockLibrary import *` if you prefer. For API documentation please
refer to [JoyShockLibrary project page](https://github.com/JibbSmart/JoyShockLibrary#functions). Since this is pure ctypes wrapper, there is slight usage differences.  

1. To use `JslGetConnectedDeviceHandles` function you need to pass int array. You can create int array using `(ctypes.c_int * arrayLength)()`
2. To use `JslGetCalibrationOffset` function you need to pass three C float pointers. You can create C floats using `variableName = ctypes.c_float()`. They can be used directly to pass pointers of them. For example `JslGetCalibrationOffset(deviceID, variableName1, variableName2, variableName3)`
3. To create C compatible callback function pointer you need to pass your callback function to `JslCallback` or `JslTouchCallback` functions. They will return C compatible pointer of your functions. You can pass them directly to `JslSetCallback` or `JslSetTouchCallback` functions.

You can find examples for these differences above in [JoyShockLibrary wrapper source](src/JoyShockLibrary/__init__.py).

# Requirements

You need to copy JoyShockLibrary.dll (for Windows) to one of your PATH folders or where your script is running.  
Both JoyShockLibrary and this python wrapper tested on Windows. They might work on other OSes.