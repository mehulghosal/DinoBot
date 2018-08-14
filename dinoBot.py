import math, keyboard
from time import sleep
from PIL import ImageGrab, Image

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

#gameover (white back)
goSumW = 1475832
#gameover black back)
goSumB = 160512

lowobject = (list(ImageGrab.grab((470, 280, 580, 306)).getdata()))
lowobjectSum = 0
for i in lowobject: lowobjectSum += sum(i)
print(lowobjectSum)

highobject = (list(ImageGrab.grab((470, 265, 580, 280)).getdata()))
highobjectSum = 0
for i in highobject: highobjectSum += sum(i)
print((highobjectSum))

gameOverCheck = 0


# startGame()

# while True:

# 	gameOverImage = (list(ImageGrab.grab((588, 218, 780, 229)).getdata()))
# 	gameOverCheck = 0
# 	for i in gameOverImage: gameOverCheck += sum(i)
# 	print(gameOverCheck)

# 	if 1450000 < gameOverCheck < 1500000 or 150000 < gameOverCheck < 170000:
# 		print("break")
# 		break

# 	#515,280 --> +109, +26
# 	lowobject = (list(ImageGrab.grab((515, 280, 624, 306)).getdata()))
