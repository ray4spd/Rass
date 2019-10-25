#This file contains Robot Rass's class
#The class is to give Rass all the commands that affect it
#Currently it has movment implemted given the correct wiring
#Possible improvements would be an overloaded construter incase of any changes in the wiring 

# importing libraries
import RPi.GPIO as GPIO
import time


class Rass(object):
	# Declaring variables
	# pin right forward
	pRF = 0
	# pin right backwards
	pRB = 0
	
	# pin left forward
	pLF = 0
	# pin right backwards
	pLB = 0

	# constructor
	def __init__(self):
		# These numbers are for Robot Rass GPIO Pins only, if Robot is changed, change numbers
		self.pRF = 17
		self.pRB = 27
		self.pLF = 6
		self.pLB = 5
		# Setting GPIO pins Access mode
		GPIO.setmode(GPIO.BCM)
		# Activating GPIO pins
		GPIO.setup(self.pRF, GPIO.OUT)
		GPIO.setup(self.pRB, GPIO.OUT)
		GPIO.setup(self.pLF, GPIO.OUT)
		GPIO.setup(self.pLB, GPIO.OUT)


	# right W1heel Forwards
	def rightWheelForwards(self):
        	GPIO.output(self.pRF, GPIO.HIGH)
        	GPIO.output(self.pRB, GPIO.LOW)

	# right wheel Stop
	def rightWheelStop(self):
        	GPIO.output(self.pRF, GPIO.LOW)
        	GPIO.output(self.pRB, GPIO.LOW)

	# right Wheel Backwards
	def rightWheelBackwards(self):
		GPIO.output(self.pRF, GPIO.LOW)
		GPIO.output(self.pRB, GPIO.HIGH)

	#left wheel
	
	# Left Wheel Backwords
	def leftWheelBackwards(self):
		GPIO.output(self.pLF, GPIO.LOW)
		GPIO.output(self.pLB, GPIO.HIGH)

	# Left wheel Stop
	def leftWheelStop(self):
		GPIO.output(self.pLF, GPIO.LOW)
		GPIO.output(self.pLB, GPIO.LOW)

	# Left Wheel Forwords
	def leftWheelForwards(self):
		GPIO.output(self.pLF, GPIO.HIGH)
		GPIO.output(self.pLB, GPIO.LOW)

	# movemnts

	def forwards(self):
		self.rightWheelForwards()
		self.leftWheelForwards()

	def backwards(self):
		self.rightWheelBackwards()
		self.leftWheelBackwards()


	def left(self):
		self.rightWheelForwards()
		self.leftWheelStop()

	def right(self):
		self.rightWheelStop()
		self.leftWheelForwards()

	def stop(self):
		self.rightWheelStop()
		self.leftWheelStop()

	#destructor
	def __del__(self):
		self.stop()
		GPIO.cleanup()
