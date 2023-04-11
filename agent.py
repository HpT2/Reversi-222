import timeit	
import time
import copy
import random
import numpy as np

	
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
	return oldstate

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
	return oldstate

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
	return oldstate

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
	return oldstate

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
	return oldstate

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
	return oldstate

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
	return oldstate

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
	return oldstate

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

def select_move(cur_state, player_to_move, remain_time=10):
	start = time.perf_counter()
	validMove = findValidMove(cur_state, player_to_move)
	state = copy.deepcopy(cur_state)
	#print(validMove)
	
	if validMove == []:
		return None

	if (0,0) in validMove: return (0,0)
	if (0,7) in validMove: return (0,7)
	if (7,0) in validMove: return (7,0)
	if (7,7) in validMove: return (7,7)

	if player_to_move == 1: depth = 0
	else: depth = -10

	move = minimax_alpha_beta(state, player_to_move, validMove, depth, float('-inf'), start, remain_time, -64, 64)

	return move[1] if move and move[1] else random.choice(validMove)


def minimax_alpha_beta(cur_state, player_to_move, validMove, depth, best_val,start, remain_time, alpha, beta):

	execution_time = time.perf_counter() - start
	if execution_time > 2.9995 or remain_time -  execution_time  <= 0.0005:
		#print(execution_time)
		return None
	
	best_move = None
	if depth == 20 or validMove == []:
		#print(player_to_move)
		return evaluate(cur_state, player_to_move), None

	
	for a_move in validMove:
		
		if a_move == (0,0) or a_move == (0,7) or a_move == (7,0) or a_move == (7,7):
			return evaluate(cur_state, player_to_move) +18, None



		state = makeMove(cur_state, a_move, player_to_move)
		new_valid_move = findValidMove(state, -player_to_move)
		res = minimax_alpha_beta(state, -player_to_move, new_valid_move, depth+1, best_val, start, remain_time, -beta, -alpha)
		if res == None:	
			return None
		new_val = -res[0]

		if new_val > alpha:
			alpha = new_val
			best_move = a_move

		
		if alpha >= beta:
			return alpha, best_move


	return (best_val, best_move)

def evaluate(state, player_to_move):
	score = 0
	for y in range(8):
		for x in range(8):
			if state[y][x] == player_to_move:
				score += 1
			#if state[y][x] == -player_to_move:
			#	score -= 1
	return score - len(findValidMove(state, -player_to_move))
