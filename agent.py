import numpy as np
import time

REMAIN_TIME = 60000

def findValidDirections(x, y):
	validDirections = []

	if y != 0: validDirections.append("UP")
	if y != 0 and x != 0: validDirections.append("UP_LEFT")
	if y != 0 and x != 7: validDirections.append("UP_RIGHT")

	if y != 7: validDirections.append("DOWN")
	if y != 7 and x != 0: validDirections.append("DOWN_LEFT")
	if y != 7 and x != 7: validDirections.append("DOWN_RIGHT")

	if x != 0: validDirections.append("LEFT")
	if x != 7: validDirections.append("RIGHT")

	return validDirections

def checkUP(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	y -= 1
	while y >= 0 :
		if state[y][x] == currentPlayer: return True
		y -= 1
	
	return False

def checkDOWN(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	y += 1
	while y <= 7 :
		if state[y][x] == currentPlayer: return True
		y += 1
	
	return False

def checkLEFT(x, y, state, currentPlayer):

	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x -= 1
	while x >= 0 :
		if state[y][x] == currentPlayer: return True
		x -= 1
	
	return False

def checkRIGHT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x += 1
	while x <= 7 :
		if state[y][x] == currentPlayer: return True
		x += 1
	
	return False

def checkUP_LEFT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x -= 1
	y -= 1
	while x >= 0 and y >= 0 :
		if state[y][x] == currentPlayer: return True
		x -= 1
		y -= 1
	
	return False

def checkUP_RIGHT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x += 1
	y -= 1
	while x <= 7 and y >= 0 :
		if state[y][x] == currentPlayer: return True
		x += 1
		y -= 1
	
	return False

def checkDOWN_RIGHT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x += 1
	y += 1
	while x <= 7 and y <= 7 :
		if state[y][x] == currentPlayer: return True
		x += 1
		y += 1
	
	return False

def checkDOWN_LEFT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x -= 1
	y +=1
	while x >= 0 and y <= 7 :
		if state[y][x] == currentPlayer: return True
		x -= 1
		y += 1
	
	return False

class Board:

	def __init__(self):
		self.state = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0, 0],
                               [0, 0, 0, 1, 1, 0, 0, 0],
                               [0, 0, 0, 1, -1, 0, 0, 0],
                               [0, 0, 0, -1, -1, 0, 0, 0],
                               [0, 0, -1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]])
		self.turn = 1

	def findValidMove(self, currentPlayer):
		validMove = []
		for y in range(8):
			for x in range(8):

				if self.state[y][x] != 0:
					continue
			
				validDirections = findValidDirections(x,y)

				for direction in validDirections:

					
					if direction == "UP":
						if checkUP(x, y-1, self.state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "DOWN":
						if checkDOWN(x, y+1, self.state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "LEFT":
						if checkLEFT(x-1, y, self.state, currentPlayer):
							validMove.append((x, y))
							break
					
					if direction == "RIGHT":
						if checkRIGHT(x+1, y, self.state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "UP_LEFT":
						if checkUP_LEFT(x-1, y-1, self.state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "UP_RIGHT":
						if checkUP_RIGHT(x+1, y-1, self.state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "DOWN_LEFT":
						if checkDOWN_LEFT(x-1, y+1, self.state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "DOWN_RIGHT":
						if checkDOWN_RIGHT(x+1, y+1, self.state, currentPlayer):
							validMove.append((x, y))
							break

		return validMove
	
	def makeMove(self, Cell):
		pass

def select_move(cur_state=None, player_to_move=None, remain_time=None):
	validMove = cur_state.findValidMove(player_to_move)
	print(validMove)
	if validMove == []:
		return None

game = Board()
print(game.state)
select_move(game, -1)





