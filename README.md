# Python CORE for CW01 and CW02
MicroPython Core handling I2C communication for **CW01**(ESP8266) and **CW02**(ESP32).

## Instructions ##
- Use [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest) and flash MicroPython to the CW01/CW02.

## Python IDE ##

### mu-editor ###
Use *mu-editor* (find it here https://codewith.mu) 
- *mu-editor* needs to recognize Product ID: `0x6001` and Vendor ID: `0x0403` - pull request submitted.
- In the meantime use XinaBox version of the *mu-editor* from here: [XinaBox mu-editor](https://github.com/xinabox/mu-editor/releases/latest).

### Visual Studio Code (VSC) ###
Use *VSC* (find it here https://code.visualstudio.com)
- You need a plugin, such as [Pymakr](https://docs.pycom.io/pymakr/installation/vscode/)

### ESPlorer ###
Use *ESPlorer* [ESPlorer](https://github.com/xinabox/ESPlorer/releases/latest)
- This IDE allows you to switch DTR/RTS off - see note regarding CW01 below

### Note using CW01 ###
- The CW01 doesn't have an "auto resetting" circutry on it like the CW02 has, therefore the the CW01 will be stuck in "bootloader" mode when inserted into your computer with a standard IP01. However if you have an old IP01 with switches, then you can bypass that by setting the A-B switch in position `A` when programming the CW01 using mu-editor. And when loading the MicroPython using the [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest), the switches should be in `B` and `DCE`
- You can also just use an IDE that allows you to control DTR/RTS, such as ESPlorer (see above)

