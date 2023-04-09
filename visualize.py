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
	def __init__(self, board) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((700, 500))
		pygame.display.set_caption('Reversi')
		self.board = board
		self.player1 = 1
		self.player2 = -1

		self.currentPlayer = 1

		self.RUN = True

		self.size = (50, 50)
		
		self.whitetoken = loadImages('assets/WhiteToken.png', self.size)
		self.blacktoken = loadImages('assets/BlackToken.png', self.size)

		self.bg = self.loadBackGroundImages()
		self.gridBg = self.createbgimg()

	def run(self):
		while self.RUN == True:
			self.input()
			self.draw()

	def input(self):
		pass

	def draw(self):
		self.screen.fill((0, 0, 0))
		self.drawGrid(self.screen)
		pygame.display.update()

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
				if self.board.state[y][x] == 1:
					window.blit(self.blacktoken, ( 50 + x*50, 50 + y*50))
				if self.board.state[y][x] == -1:
					window.blit(self.whitetoken, (50 + 50*x, 50 + y*50))

		availMoves = self.board.findValidMove(self.currentPlayer)

		for move in availMoves:
			pygame.draw.rect(window, 'White', (50 + (move[0] * 50) + 17, 50 + (move[1] * 50) + 15, 20, 20))


	
grid = Grid(Board())
grid.run()