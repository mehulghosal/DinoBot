import math, keyboard, sys
from time import sleep
from PIL import ImageGrab, Image

def startGame():
	while True:
		if keyboard.is_pressed('space'):
			#sleep so it doesnt quit bc of the first frame
			sleep(1)
			break
	print("start")

def jump():
	global jumpTime, jumpInc, b4JumpTime
	keyboard.press('space')
	sleep(jumpTime)
	jumpTime += jumpInc
	keyboard.release('space')

def duck():
	keyboard.press('down')
	sleep(0.5)
	keyboard.release('down')

#pass in top left and bottom right coordinates of rectangle
#returns sum of pixel values contained in rectangle
def sumPixels(x1, y1, x2, y2):
	img = (list(ImageGrab.grab((x1, y1, x2, y2)).getdata()))
	s = 0
	for i in img: s += sum(i)
	return s
#print(sumPixels(588, 218, 780, 229)) --> 31992

gameOverCheck = 0

#increments slowly so jump sooner as game gets faster
rightCheck = 570
leftCheck = 515
inc = 0.05

jumpTime = 0.1
jumpInc = 0.0001

startGame()

while True:

	jumped = False

	background = sumPixels(602, 196, 603, 197)/3 #1 pix

	gameOverCheck = sumPixels(588, 218, 780, 229)/(2112*3) #192*11 = 2112 pix

	lowobjectSum = sumPixels(leftCheck, 247, rightCheck, 270)/((rightCheck-leftCheck)*(270-247)*3) #85*25 = 2125 pix
	highobjectSum = sumPixels(leftCheck, 205, rightCheck, 230)/((rightCheck-leftCheck)*(230-205)*3) #85*25 = 2125 pix
	print(lowobjectSum, highobjectSum, gameOverCheck)
	
	rightCheck += inc
	leftCheck += inc
	#inc += 0.001

	#white screen
	if background == 255:
		if 245 < gameOverCheck < 250:
			print("break")
			sys.exit()

		if lowobjectSum < 247:
			jump()
			jumped = True

		if not jumped and highobjectSum < 244:
			duck()

	#black back
	else: 
		if gameOverCheck > 10:
			print("break")
			sys.exit()

		if lowobjectSum > 3:
			jump()
			jumped = True
			b4JumpTime -= 0.001

		if not jumped and highobjectSum > 3:
			duck()