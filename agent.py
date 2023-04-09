import numpy as np
import time
import copy
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
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		y -= 1
	
	return False

def checkDOWN(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	y += 1
	while y <= 7 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		y += 1
	
	return False

def checkLEFT(x, y, state, currentPlayer):

	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x -= 1
	while x >= 0 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		x -= 1
	
	return False

def checkRIGHT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x += 1
	while x <= 7 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		x += 1
	
	return False

def checkUP_LEFT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x -= 1
	y -= 1
	while x >= 0 and y >= 0 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		x -= 1
		y -= 1
	
	return False

def checkUP_RIGHT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x += 1
	y -= 1
	while x <= 7 and y >= 0 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		x += 1
		y -= 1
	
	return False

def checkDOWN_RIGHT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x += 1
	y += 1
	while x <= 7 and y <= 7 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		x += 1
		y += 1
	
	return False

def checkDOWN_LEFT(x, y, state, currentPlayer):
	if state[y][x] == currentPlayer or state[y][x] == 0: return False
	x -= 1
	y +=1
	while x >= 0 and y <= 7 :
		if state[y][x] == 0: return False
		if state[y][x] == currentPlayer: return True
		x -= 1
		y += 1
	
	return False

def searchUP(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while y >= 0:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		y -= 1

def searchDOWN(state,x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while y <= 7:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		y += 1

def searchLEFT(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while x >= 0:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		x -= 1

def searchRIGHT(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while x <= 7:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		x += 1

def searchUP_LEFT(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while x >= 0 and y >= 0:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		x -= 1
		y -= 1

def searchDOWN_LEFT(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while x >= 0 and y <= 7:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		x -= 1
		y += 1

def searchUP_RIGHT(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while x <= 7 and y >= 0:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		x += 1
		y -= 1

def searchDOWN_RIGHT(state, x, y, currentPlayer):
	if state[y][x] == 0 or state[y][x] == currentPlayer:
		return state
	oldstate = copy.deepcopy(state)

	while x <= 7 and y <= 7:
		if state[y][x] == 0: return oldstate
		if state[y][x] == currentPlayer:
			return state
		state[y][x] = currentPlayer
		x += 1
		y += 1

def findValidMove(state, currentPlayer):
		validMove = []
		for y in range(8):
			for x in range(8):

				if state[y][x] != 0:
					continue
			
				validDirections = findValidDirections(x,y)

				for direction in validDirections:

					
					if direction == "UP":
						if checkUP(x, y-1, state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "DOWN":
						if checkDOWN(x, y+1, state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "LEFT":
						if checkLEFT(x-1, y, state, currentPlayer):
							validMove.append((x, y))
							break
					
					if direction == "RIGHT":
						if checkRIGHT(x+1, y, state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "UP_LEFT":
						if checkUP_LEFT(x-1, y-1, state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "UP_RIGHT":
						if checkUP_RIGHT(x+1, y-1, state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "DOWN_LEFT":
						if checkDOWN_LEFT(x-1, y+1, state, currentPlayer):
							validMove.append((x, y))
							break

					if direction == "DOWN_RIGHT":
						if checkDOWN_RIGHT(x+1, y+1, state, currentPlayer):
							validMove.append((x, y))
							break

		return validMove
	
def makeMove(state, Cell, currentPlayer):
		x, y = Cell
		state[y][x] = currentPlayer
		if y > 1: state = searchUP(state, x, y-1, currentPlayer)
		if y < 6: state = searchDOWN(state, x, y+1, currentPlayer)
		if x > 1: state = searchLEFT(state, x-1, y, currentPlayer)
		if x < 6: state = searchRIGHT(state, x+1, y,currentPlayer)
		if x > 1 and y > 1: state = searchUP_LEFT(state, x-1, y-1, currentPlayer)
		if x > 1 and y < 6: state = searchDOWN_LEFT(state, x-1, y+1, currentPlayer)
		if x < 6 and y > 1: state = searchUP_RIGHT(state, x+1, y-1, currentPlayer)
		if x < 6 and y < 6: state = searchDOWN_RIGHT(state, x+1, y+1, currentPlayer)
		return state


def select_move(cur_state=None, player_to_move=None, remain_time=None):
	validMove = cur_state.findValidMove(player_to_move)
	#print(validMove)
	if validMove == []:
		return None

"""test some move
game = Board()
print(game.state)
select_move(game, 1)
game.makeMove((2,4), 1)
game.makeMove((2,5),-1)
game.makeMove((3,5),1)
game.makeMove((4,5),-1)
game.makeMove((4,6),1)
game.makeMove((4,7),-1)
game.makeMove((5,5),1)
game.makeMove((6,5),-1)
print(game.state)
select_move(game, -1)
"""





