# importing necessary libraries
import math, sys
from time import sleep
from pynput.keyboard import Key, Controller
import pyscreenshot as ImageGrab

keyboard = Controller()
timesJumped = 0

# when jump detected, this function 'presses' the spacebar
def jump():
	global timesJumped
	keyboard.press(Key.space)
	keyboard.release(Key.space)
	timesJumped += 1
	# print("jump")

# this funtion will press the down key for ducking
def duck():
	keyboard.press(Key.down)
	keyboard.release(Key.down)
	print("duck")

# pass in top left and bottom right coordinates of rectangle
# returns sum of pixel values contained in rectangle
# uses python imaging library to take a screenshot
def sumPixels(x1, y1, x2, y2):
	img = (list(ImageGrab.grab((int(x1), int(y1), int(x2), int(y2))).getdata()))
	s = 0
	for i in img: s += sum(i)
	return s

#increments slowly so jump sooner as game gets faster
rightCheck = 850
leftCheck = 760
inc = 0.2

# waits so i can get chrome up
sleep(3)

keyboard.press(Key.space)
keyboard.release(Key.space)
sleep(1)

# main game loop
while True:

	# keeps track of whether already jumped this iteration - can't jump and duck at the same time
	jumped = False

	# check whether the background is white or black
	background = sumPixels(602, 196, 603, 197)/3

	# check if the game is over to exit the program
	gameOverCheck = sumPixels(850, 175, 1070, 200)/(220*25*3) 

	lowobjectSum = sumPixels(leftCheck, 240, rightCheck, 260)/((rightCheck-leftCheck)*(260-240)*3)
	highobjectSum = sumPixels(leftCheck, 205, rightCheck, 230)/((rightCheck-leftCheck)*(230-205)*3)
	
	# increment slowly to jump sooner - moves box to the right
	rightCheck += inc
	leftCheck += inc
	inc += 0.001

	#white screen
	if background >= 250:
		if 230 < gameOverCheck < 250:
			print("break")
			print(timesJumped)
			sys.exit()

		if lowobjectSum < 250:
			jump()
			jumped = True

		if not jumped and highobjectSum < 250:
			duck()

	#black back
	elif background < 30: 
		if gameOverCheck > 50:
			print("break")
			sys.exit()

		if lowobjectSum > 20:
			jump()
			jumped = True

		if not jumped and highobjectSum > 3:
			duck()