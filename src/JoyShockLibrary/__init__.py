import ctypes
import ctypes.util
import os

_jsl = None

# This will search JoyShockLibrary.dll in your PATH or
# directory of your script.
DLLPATH = ctypes.util.find_library('JoyShockLibrary.dll')
if DLLPATH != None:
    _jsl = ctypes.cdll.LoadLibrary(DLLPATH)
else:
    DLLPATH = './JoyShockLibrary.dll'
    if os.path.exists(DLLPATH):
        try:
            _jsl = ctypes.cdll.LoadLibrary(DLLPATH)
        except:
            raise Exception('JoyShockLibrary.dll Not Found')

JS_TYPE_JOYCON_LEFT = 1
JS_TYPE_JOYCON_RIGHT = 2
JS_TYPE_PRO_CONTROLLER = 3
JS_TYPE_DS4 = 4
JS_TYPE_DS = 5

JS_SPLIT_TYPE_LEFT = 1
JS_SPLIT_TYPE_RIGHT = 2
JS_SPLIT_TYPE_FULL = 3

JSMASK_UP = 0x00001
JSMASK_DOWN = 0x00002
JSMASK_LEFT = 0x00004
JSMASK_RIGHT = 0x00008
JSMASK_PLUS = 0x00010
JSMASK_OPTIONS = 0x00010
JSMASK_MINUS = 0x00020
JSMASK_SHARE = 0x00020
JSMASK_LCLICK = 0x00040
JSMASK_RCLICK = 0x00080
JSMASK_L = 0x00100
JSMASK_R = 0x00200
JSMASK_ZL = 0x00400
JSMASK_ZR = 0x00800
JSMASK_S = 0x01000
JSMASK_E = 0x02000
JSMASK_W = 0x04000
JSMASK_N = 0x08000
JSMASK_HOME = 0x10000
JSMASK_PS = 0x10000
JSMASK_CAPTURE = 0x20000
JSMASK_TOUCHPAD_CLICK = 0x20000
JSMASK_MIC = 0x40000
JSMASK_SL = 0x40000
JSMASK_SR = 0x80000

JSOFFSET_UP = 0
JSOFFSET_DOWN = 1
JSOFFSET_LEFT = 2
JSOFFSET_RIGHT = 3
JSOFFSET_PLUS = 4
JSOFFSET_OPTIONS = 4
JSOFFSET_MINUS = 5
JSOFFSET_SHARE = 5
JSOFFSET_LCLICK = 6
JSOFFSET_RCLICK = 7
JSOFFSET_L = 8
JSOFFSET_R = 9
JSOFFSET_ZL = 10
JSOFFSET_ZR = 11
JSOFFSET_S = 12
JSOFFSET_E = 13
JSOFFSET_W = 14
JSOFFSET_N = 15
JSOFFSET_HOME = 16
JSOFFSET_PS = 16
JSOFFSET_CAPTURE = 17
JSOFFSET_TOUCHPAD_CLICK = 17
JSOFFSET_MIC = 18
JSOFFSET_SL = 18
JSOFFSET_SR = 19

DS5_PLAYER_1 = 4
DS5_PLAYER_2 = 10
DS5_PLAYER_3 = 21

# You can access those values with the name of fields
# Example:
#     result = JslGetSimpleState(deviceHandle)
#     print(result.lTrigger, result.rTrigger)
class JOY_SHOCK_STATE(ctypes.Structure):
    _fields_ = [('buttons', ctypes.c_int),
                ('lTrigger', ctypes.c_float),
                ('rTrigger', ctypes.c_float),
                ('stickLX', ctypes.c_float),
                ('stickLY', ctypes.c_float),
                ('stickRX', ctypes.c_float),
                ('stickRY', ctypes.c_float)]

class IMU_STATE(ctypes.Structure):
    _fields_ = [('accelX', ctypes.c_float),
                ('accelY', ctypes.c_float),
                ('accelZ', ctypes.c_float),
                ('gyroX', ctypes.c_float),
                ('gyroY', ctypes.c_float),
                ('gyroZ', ctypes.c_float)]

class MOTION_STATE(ctypes.Structure):
    _fields_ = [('quatW', ctypes.c_float),
                ('quatX', ctypes.c_float),
                ('quatY', ctypes.c_float),
                ('quatZ', ctypes.c_float),
                ('accelX', ctypes.c_float),
                ('accelY', ctypes.c_float),
                ('accelZ', ctypes.c_float),
                ('gravX', ctypes.c_float),
                ('gravY', ctypes.c_float),
                ('gravZ', ctypes.c_float)]

class TOUCH_STATE(ctypes.Structure):
    _fields_ = [('t0Id', ctypes.c_int),
                ('t1Id', ctypes.c_int),
                ('t0Down', ctypes.c_bool),
                ('t1Down', ctypes.c_bool),
                ('t0X', ctypes.c_float),
                ('t0Y', ctypes.c_float),
                ('t1X', ctypes.c_float),
                ('t1Y', ctypes.c_float)]

JslConnectDevices = _jsl.JslConnectDevices
JslConnectDevices.restype = ctypes.c_int

# to create num long int array "(ctypes.c_int * num)()"
# Example:
#     size = JslConnectDevices()
#     handles = (ctypes.c_int * size)()
#     deviceCount = JslGetConnectedDeviceHandles(handles, size)
JslGetConnectedDeviceHandles = _jsl.JslGetConnectedDeviceHandles
JslGetConnectedDeviceHandles.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
JslGetConnectedDeviceHandles.restype = ctypes.c_int

JslDisconnectAndDisposeAll = _jsl.JslDisconnectAndDisposeAll
JslDisconnectAndDisposeAll.restype = None

# get buttons as bits in the following order, using North South East West to name face buttons to avoid ambiguity between Xbox and Nintendo layouts:
# 0x00001: up
# 0x00002: down
# 0x00004: left
# 0x00008: right
# 0x00010: plus
# 0x00020: minus
# 0x00040: left stick click
# 0x00080: right stick click
# 0x00100: L
# 0x00200: R
# ZL and ZR are reported as analogue inputs (GetLeftTrigger, GetRightTrigger), because DS4 and XBox controllers use analogue triggers, but we also have them as raw buttons
# 0x00400: ZL
# 0x00800: ZR
# 0x01000: S
# 0x02000: E
# 0x04000: W
# 0x08000: N
# 0x10000: home / PS
# 0x20000: capture / touchpad-click
# 0x40000: SL
# 0x80000: SR
# These are the best way to get all the buttons/triggers/sticks, gyro/accelerometer (IMU), orientation/acceleration/gravity (Motion), or touchpad

JslGetSimpleState = _jsl.JslGetSimpleState
JslGetSimpleState.argtypes = [ctypes.c_int]
JslGetSimpleState.restype = JOY_SHOCK_STATE

JslGetIMUState = _jsl.JslGetIMUState
JslGetIMUState.argtypes = [ctypes.c_int]
JslGetIMUState.restype = IMU_STATE

JslGetMotionState = _jsl.JslGetMotionState
JslGetMotionState.argtypes = [ctypes.c_int]
JslGetMotionState.restype = MOTION_STATE

JslGetTouchState = _jsl.JslGetTouchState
JslGetTouchState.argtypes = [ctypes.c_int]
JslGetTouchState.restype = TOUCH_STATE

JslGetButtons = _jsl.JslGetButtons
JslGetButtons.argtypes = [ctypes.c_int]
JslGetButtons.restype = ctypes.c_int

# get thumbsticks
JslGetLeftX = _jsl.JslGetLeftX
JslGetLeftX.argtypes = [ctypes.c_int]
JslGetLeftX.restype = ctypes.c_float

JslGetLeftY = _jsl.JslGetLeftY
JslGetLeftY.argtypes = [ctypes.c_int]
JslGetLeftY.restype = ctypes.c_float

JslGetRightX = _jsl.JslGetRightX
JslGetRightX.argtypes = [ctypes.c_int]
JslGetRightX.restype = ctypes.c_float

JslGetRightY = _jsl.JslGetRightY
JslGetRightY.argtypes = [ctypes.c_int]
JslGetRightY.restype = ctypes.c_float

# get triggers. Switch controllers don't have analogue triggers, but will report 0.0 or 1.0 so they can be used in the same way as others
JslGetLeftTrigger = _jsl.JslGetLeftTrigger
JslGetLeftTrigger.argtypes = [ctypes.c_int]
JslGetLeftTrigger.restype = ctypes.c_float

JslGetRightTrigger = _jsl.JslGetRightTrigger
JslGetRightTrigger.argtypes = [ctypes.c_int]
JslGetRightTrigger.restype = ctypes.c_float

# get gyro
JslGetGyroX = _jsl.JslGetGyroX
JslGetGyroX.argtypes = [ctypes.c_int]
JslGetGyroX.restype = ctypes.c_float

JslGetGyroY = _jsl.JslGetGyroY
JslGetGyroY.argtypes = [ctypes.c_int]
JslGetGyroY.restype = ctypes.c_float

JslGetGyroZ = _jsl.JslGetGyroZ
JslGetGyroZ.argtypes = [ctypes.c_int]
JslGetGyroZ.restype = ctypes.c_float

# get accelerometor
JslGetAccelX = _jsl.JslGetAccelX
JslGetAccelX.argtypes = [ctypes.c_int]
JslGetAccelX.restype = ctypes.c_float

JslGetAccelY = _jsl.JslGetAccelY
JslGetAccelY.argtypes = [ctypes.c_int]
JslGetAccelY.restype = ctypes.c_float

JslGetAccelZ = _jsl.JslGetAccelZ
JslGetAccelZ.argtypes = [ctypes.c_int]
JslGetAccelZ.restype = ctypes.c_float

# get touchpad
JslGetTouchId = _jsl.JslGetTouchId
JslGetTouchId.argtypes = [ctypes.c_int, ctypes.c_bool]
JslGetTouchId.restype = ctypes.c_int

JslGetTouchDown = _jsl.JslGetTouchDown
JslGetTouchDown.argtypes = [ctypes.c_int, ctypes.c_bool]
JslGetTouchDown.restype = ctypes.c_bool

JslGetTouchX = _jsl.JslGetTouchX
JslGetTouchX.argtypes = [ctypes.c_int, ctypes.c_bool]
JslGetTouchX.restype = ctypes.c_float

JslGetTouchY = _jsl.JslGetTouchY
JslGetTouchY.argtypes = [ctypes.c_int, ctypes.c_bool]
JslGetTouchY.restype = ctypes.c_float

# analog parameters have different resolutions depending on device
JslGetStickStep = _jsl.JslGetStickStep
JslGetStickStep.argtypes = [ctypes.c_int]
JslGetStickStep.restype = ctypes.c_float

JslGetTriggerStep = _jsl.JslGetTriggerStep
JslGetTriggerStep.argtypes = [ctypes.c_int]
JslGetTriggerStep.restype = ctypes.c_float

JslGetPollRate = _jsl.JslGetPollRate
JslGetPollRate.argtypes = [ctypes.c_int]
JslGetPollRate.restype = ctypes.c_float

# calibration
JslResetContinuousCalibration = _jsl.JslResetContinuousCalibration
JslResetContinuousCalibration.argtypes = [ctypes.c_int]
JslResetContinuousCalibration.restype = None

JslStartContinuousCalibration = _jsl.JslStartContinuousCalibration
JslStartContinuousCalibration.argtypes = [ctypes.c_int]
JslStartContinuousCalibration.restype = None

JslPauseContinuousCalibration = _jsl.JslPauseContinuousCalibration
JslPauseContinuousCalibration.argtypes = [ctypes.c_int]
JslPauseContinuousCalibration.restype = None

# You can use c_float variable directly
# Example:
#     xOffset = ctypes.c_float()
#     yOffset = ctypes.c_float()
#     zOffset = ctypes.c_float()
#     JslGetCalibrationOffset(deviceHandle, xOffset, yOffset, zOffset)
JslGetCalibrationOffset = _jsl.JslGetCalibrationOffset
JslGetCalibrationOffset.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
JslGetCalibrationOffset.restype = None

JslSetCalibrationOffset = _jsl.JslSetCalibrationOffset
JslSetCalibrationOffset.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float]
JslSetCalibrationOffset.restype = None

# to create callback function pointer
# Example:
#     def cb(handle, simpleState, lastSimpleState, imuState, lastImuState, deltaTime):
#         # do whatever you want with the values
#         return
#     cbPointer = JslCallback(cb)
#     JslSetCallback(cbPointer)
JslCallback = ctypes.CFUNCTYPE(None, ctypes.c_int, JOY_SHOCK_STATE, JOY_SHOCK_STATE, IMU_STATE, IMU_STATE, ctypes.c_float)
# same as above
JslTouchCallback = ctypes.CFUNCTYPE(None, ctypes.c_int, TOUCH_STATE, TOUCH_STATE, ctypes.c_float)

# this function will get called for each input event from each controller
JslSetCallback = _jsl.JslSetCallback
JslSetCallback.argtypes = [ctypes.c_void_p]
JslSetCallback.restype = None

# this function will get called for each input event, even if touch data didn't update
JslSetTouchCallback = _jsl.JslSetTouchCallback
JslSetTouchCallback.argtypes = [ctypes.c_void_p]
JslSetTouchCallback.restype = None

# what kind of controller is this?
JslGetControllerType = _jsl.JslGetControllerType
JslGetControllerType.argtypes = [ctypes.c_int]
JslGetControllerType.restype = ctypes.c_int

# is this a left, right, or full controller?
JslGetControllerSplitType = _jsl.JslGetControllerSplitType
JslGetControllerSplitType.argtypes = [ctypes.c_int]
JslGetControllerSplitType.restype = ctypes.c_int

# what colour is the controller (not all controllers support this; those that don't will report white)
JslGetControllerColour = _jsl.JslGetControllerColour
JslGetControllerColour.argtypes = [ctypes.c_int]
JslGetControllerColour.restype = ctypes.c_int

# set controller light colour (not all controllers have a light whose colour can be set, but that just means nothing will be done when this is called -- no harm)
JslSetLightColour = _jsl.JslSetLightColour
JslSetLightColour.argtypes = [ctypes.c_int, ctypes.c_int]
JslSetLightColour.restype = None

# set controller rumble (Switch rumbles are not supported at this time)
JslSetRumble = _jsl.JslSetRumble
JslSetRumble.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
JslSetRumble.restype = None

# set controller player number indicator (not all controllers have a number indicator which can be set, but that just means nothing will be done when this is called -- no harm)
JslSetPlayerNumber = _jsl.JslSetPlayerNumber
JslSetPlayerNumber.argtypes = [ctypes.c_int, ctypes.c_int]
JslSetPlayerNumber.restype = None
