import math, keyboard, sys
from time import sleep
from PIL import ImageGrab, Image

def startGame():
	while True:
		if keyboard.is_pressed('space'):
			#sleep so it doesnt quit bc of the first frame
			sleep(0.75)
			break
	print("start")

def jump():
	global jumpTime, jumpInc
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


#gameover (white back)
goSumW = 1475832
#gameover black back)
goSumB = 160512



gameOverCheck = 0

#increments slowly so jump sooner as game gets faster
rightCheck = 580
leftCheck = 470
inc = 0.04

jumpTime = 0.1
jumpInc = 0.001

startGame()

while True:

	jumped = False

	gameOverCheck = sumPixels(588, 218, 780, 229)
	#print(gameOverCheck)

	if gameOverCheck < 1570000 or 150000 < gameOverCheck < 170000:
		print("break")
		sys.exit()

	lowobjectSum = sumPixels(leftCheck, 280, rightCheck, 305)

	highobjectSum = sumPixels(leftCheck, 230, rightCheck, 260)
	
	rightCheck += inc
	leftCheck += inc
	#inc += 0.001

	if lowobjectSum < 2100000:
		jump()
		jumped = True

	if highobjectSum < 2500000 and not jumped:
		duck()