#!/usr/bin/python3
authorized =['0212394425','0213660857', '0857870596','0213548985','0217342905','0067305985']

import time
def set(property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()	
	except:
		print("Error writing to: " + property + " value: " + value)
 
 
def setServo(angle):
	set("servo", str(angle))
	
		
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

setServo(10)
 
while True:
	id = input('id: ')
	if id in authorized:
		print('allowed')
		print(id)
		setServo(180)
		time.sleep(5)
		setServo(90)	
	else:
		print('**********invalid***********')
		print(id)
