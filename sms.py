#!/usr/bin/env python
import serial
import time
import sys

class TextMessage:
    def __init__(self, recipient="0123456789", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5)
        time.sleep(1)

    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
	self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
	self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
	self.ser.write(self.content + "\r")
        time.sleep(1)
	self.ser.write(chr(26))

    def disconnectPhone(self):
        self.ser.close()


if len(sys.argv) < 2:
    print('usage: sms.py +79310000306 Message')
    exit(0)
sms = TextMessage(sys.argv[1], sys.argv[2])
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
