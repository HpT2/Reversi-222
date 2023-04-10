import pygame
from agent import *

def loadImages(path, size):
	"""Load an image into the game, and scale the image"""
	img = pygame.image.load(f"{path}").convert_alpha()
	img = pygame.transform.scale(img, size)
	return img

def loadSpriteSheet(sheet, row, col, newSize, size):
	"""creates an empty surface, loads a portion of the spritesheet onto the surface, then return that surface as img"""
	image = pygame.Surface((32, 32)).convert_alpha()
	image.blit(sheet, (0, 0), (row * size[0], col * size[1], size[0], size[1]))
	image = pygame.transform.scale(image, newSize)
	image.set_colorkey('Black')
	return image

class Grid:
	def __init__(self) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((700, 500))
		pygame.display.set_caption('Reversi')
		self.state = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, -1, 0, 0, 0],
                               [0, 0, 0, -1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]])
		self.player1 = 1
		self.player2 = -1

		self.currentPlayer = 1

		self.RUN = True

		self.size = (50, 50)
		
		self.whitetoken = loadImages('assets/WhiteToken.png', self.size)
		self.blacktoken = loadImages('assets/BlackToken.png', self.size)

		self.bg = self.loadBackGroundImages()
		self.gridBg = self.createbgimg()

		self.availableMove = []

	def run(self):
		while self.RUN == True:
			self.availableMove = findValidMove(self.state, self.currentPlayer)

			if self.availableMove == []:
				self.currentPlayer = -self.currentPlayer
				continue

			if self.currentPlayer == 1:
				self.state = makeMove(self.state, select_move(self.state, 1), 1)
				self.currentPlayer = -1
			else:
				self.state = makeMove(self.state, random.choice(self.availableMove), -1)
				self.currentPlayer = 1
			#self.input()

			self.draw()

	def input(self):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				x = int((x-50) / 50)
				y = int((y-50) / 50)
				if (x, y) in self.availableMove:
					self.state = makeMove(self.state, (x, y), self.currentPlayer)
					self.currentPlayer = 1
			if event.type == pygame.QUIT:
				pygame.quit()

	def draw(self):
		self.screen.fill((0, 0, 0))
		self.drawGrid(self.screen)
		self.score()
		pygame.display.update()

	def score(self):
		w = 0
		b = 0
		for y in range(8):
			for x in range(8):
				if self.state[y][x] == 1:
					b += 1
				if self.state[y][x] == -1:
					w += 1
		print("w_score: {}    b_score: {}".format(w,b))


	def loadBackGroundImages(self):
		alpha = 'ABCDEFGHI'
		spriteSheet = pygame.image.load('assets/wood.png').convert_alpha()
		imageDict = {}
		for i in range(3):
			for j in range(7):
				imageDict[alpha[j]+str(i)] = loadSpriteSheet(spriteSheet, j, i, (self.size), (32, 32))
		return imageDict
	
	def createbgimg(self):
		gridBg = [
            ['C0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'E0'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C1', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'E1'],
            ['C1', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'B0', 'A0', 'E1'],
            ['C2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'E2'],
        ]
		image = pygame.Surface((960, 960))
		for j, row in enumerate(gridBg):
			for i, img in enumerate(row):
				image.blit(self.bg[img], (i * self.size[0], j * self.size[1]))
		return image

	def drawGrid(self, window):
		window.blit(self.gridBg, (0, 0))

		for x in range(8):
			for y in range(8):
				if self.state[y][x] == 1:
					window.blit(self.blacktoken, ( 50 + x*50, 50 + y*50))
				if self.state[y][x] == -1:
					window.blit(self.whitetoken, (50 + 50*x, 50 + y*50))


		for move in self.availableMove:
			if self.currentPlayer == 1:
				continue
				pygame.draw.rect(window, 'Black', (50 + (move[0] * 50) + 17, 50 + (move[1] * 50) + 15, 20, 20))
			else:
				pygame.draw.rect(window, 'White', (50 + (move[0] * 50) + 17, 50 + (move[1] * 50) + 15, 20, 20))				


	
grid = Grid()
grid.run()