import math, keyboard
from time import sleep
from PIL import *

def startGame():
	while True:
		if keyboard.is_pressed('space'):
			break
	print("start")

def jump():
	keyboard.press('space')
	print("pressed space")
	sleep(0.01)
	keyboard.release('space')
	print("released")

def duck():
	keyboard.press('down')
	print("pressed down")
	sleep(0.01)
	keyboard.release('down')
	print("released")


#significant coordinates of dinosaur
topRight = (425, 270)
bottomRight = (425, 308)

white = (255, 255, 255)
grey = (83, 83, 83)

duck()