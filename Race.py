from random import randrange
import time

players = 4
raceLength = 20
waitTime = 0.1

positions = []

def printPos():
	global raceLength
	global positions
	global players
	for x in range(players):
		toPrint = ""
		for y in range(positions[x]):
			toPrint = toPrint + "*"
		for y in range(raceLength-len(toPrint)-1):
			toPrint = toPrint + "_"
		print "Player " + str(x+1) + ": " + toPrint

for x in range(players):
	positions.append(1)

while not raceLength-1 in positions:
	randomNumber = randrange(0, players)
	positions[randomNumber] += 1
	printPos()
	print ""
	time.sleep(waitTime)