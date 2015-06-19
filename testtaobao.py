from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
#from com.android.hierarchyviewerlib.device import ViewNode

print 'begin run'

print 'wait for connection ..... '
device = MonkeyRunner.waitForConnection()

print 'start activity com.taobao.tao.welcome.Welcome'
#device.startActivity(component='com.taobao.taobao/com.taobao.tao.welcome.Welcome')

print 'sleep 3 seconds wait for start activity .... '
className = device.getProperty('am.current.comp.class')
print 'current activity class name is : ' + className

print 'wait for welcome activity finish .....'
#MonkeyRunner.sleep(5.0)
print 'touch on search window try to entry search activity, waiting ...'
easy_device = EasyMonkeyDevice(device)
#easy_device.touch(By.id('id/home_searchedit'),MonkeyDevice.DOWN_AND_UP)

print 'read to type zifuchuan'
#MonkeyRunner.sleep(3.0)
#device.type('haohaoxuexi')
#device.type('1')

print 'click button search'
#MonkeyRunner.sleep(3.0)
#easy_device.touch(By.id('id/searchbtn'),MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(1.0)
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_DPAD_UP',MonkeyDevice.DOWN_AND_UP) 
MonkeyRunner.sleep(0.5)
device.press('KEYCODE_DPAD_UP',MonkeyDevice.DOWN_AND_UP) 

print 'over!'
