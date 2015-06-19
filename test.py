# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
device.wake()
MonkeyRunner.alert('alert', 'title', 'okTitle') 
# Takes a screenshot
result = device.takeSnapshot()
# Writes the screenshot to a file
result.writeToFile('E:/mywork/shotbegin.png','png')
# Presses the Down button
device.press('KEYCODE_VOLUME_UP','DOWN_AND_UP')
device.press('KEYCODE_VOLUME_UP','DOWN_AND_UP')
device.press('KEYCODE_VOLUME_UP','DOWN_AND_UP')
device.press('KEYCODE_VOLUME_DOWN','DOWN_AND_UP')
device.press('KEYCODE_VOLUME_DOWN','DOWN_AND_UP')
# Takes a screenshot
result = device.takeSnapshot()
# Writes the screenshot to a file
result.writeToFile('E:/mywork/shotend.png','png')
