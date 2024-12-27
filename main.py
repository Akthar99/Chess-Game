import pygame
import sys
from settings import *


# ----------------------------game-attributes-------------------------

# ? chess board 
chess_board = []
board_rect = screen_height / 8 

# -----------------------------------end------------------------------

def create_board():
	for i in range(8):
		for n in range(8):
			# creating rectangles with two colors 
			# put rectangle togather with one after another to chass_board 
			if (n % 2 == 1):
				rectangle = pygame.Rect(n * board_rect, i * board_rect, board_rect, board_rect)
				chess_board.append(rectangle)
			else:
				rectangle = pygame.Rect(n * board_rect, i * board_rect, board_rect, board_rect)
				chess_board.append(rectangle)

'''
This function is very fucking simple
'''
def display_board(screen, dt):
	'''
	0 if laa_yellow
	1 if yellow
	'''
	state = 0
	orient = 1

	'''
	get the mouse position 
	'''
	point = pygame.mouse.get_pos()


	for i, rectangle in enumerate(chess_board):
		'''
		check for collition for each rectangle
		and if so change the color acording to the collition of the rectangle 
		'''
		# handle mouse event
		'''
		when the mouse enters specific rectangle turn that rectangle to different color 
		'''
		colide = rectangle.collidepoint(point)
		dark_color = Colors.yellow_ch() if colide else Colors.yellow()
		laa_color = Colors.laa_yellow_ch() if colide else Colors.laa_yellow()
		
		if (orient % 8 > 0):		
			if (state == 0):
				pygame.draw.rect(screen, laa_color, rectangle)
				state = 1
				orient += 1
			else:
				pygame.draw.rect(screen, dark_color, rectangle)
				state = 0
				orient += 1
		else:
			if (state == 0):
				pygame.draw.rect(screen, laa_color, rectangle)
				orient += 1
			if(state == 1):
				pygame.draw.rect(screen, dark_color, rectangle)
				orient += 1



def simple_game(screen, dt, **kwargs):
	player_pos = kwargs.get("player_pos")
	if player_pos is None:
		raise TypeError("player_pos: player position is not passed to sample_game function")

	pygame.draw.circle(screen, "red", player_pos, 40)

	# game event conditions 
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		player_pos.y -= 300 * dt
	if keys[pygame.K_s]:
		player_pos.y += 300 * dt
	if keys[pygame.K_a]:
		player_pos.x -= 300 * dt
	if keys[pygame.K_d]:
		player_pos.x += 300 * dt

def bouncing_game(screen, dt, **kwargs):
	speed = kwargs.get("speed")
	ball = kwargs.get("ball")
	ballrect = kwargs.get("ballrect")


	screen.blit(ball, ballrect)



def on_loop():
	pass

def on_render():
	pass

def on_event(event):
	if event.type == pygame.QUIT:
		running = False


def main():

	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Python Chess Game")
	clock = pygame.time.Clock()
	running = True
	# | delta time |
	dt = 0

	create_board()


	# | simple game attributes |
	player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

	# | bouncing ball game attributes |
	speed = [2, 2]
	ball = pygame.image.load('Assets/intro_ball.gif')
	ballrect = ball.get_rect()

	while running:
		for event in pygame.event.get():
			on_event(event)

		# fill the screen with a color to wipe away anything from last frame
		# screen.fill(Colors.white())

		# render area
		# --------------------------
		# simple_game(screen, dt, player_pos=player_pos)

		# game logic 
		# ballrect = ballrect.move(speed)
		# if (ballrect.left < 0 or ballrect.right > screen_width):
		# 	speed[0] = -speed[0]
		# if (ballrect.top < 0 or ballrect.bottom > screen_height):
		# 	speed[1] = -speed[1]
		# bouncing_game(screen, dt, ball=ball, ballrect=ballrect)


		on_loop(dt)
		on_render(dt)

		# drawing the chess board to the screen
		display_board(screen, dt)












		
		# --------------------------

		# flip() the display to put your work on screen 
		pygame.display.flip()

		dt = clock.tick(60) / 1000

	pygame.quit()
	sys.exit()



class Game:
	def __init__(self):
		self.screen = None
		self.clock = pygame.time.Clock()
		self.running = True
		# | delta time |
		self.dt = 0
		self.board = ChessBoard()
		self.on_init()

	# initializing the game runs only one time
	def on_init(self):
		pygame.init()
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		pygame.display.set_caption("Python Chess Game")

		# create the chess board 
		self.board.create_board()

	# game logic goes to here runs on a loop
	def on_loop(self):
		pass

	# drawing to the window goes here
	def on_render(self):
		# drawing the chess board to the screen
		self.board.display_board(self.screen, self.dt)


	# all the event handling goes to here 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False


	def run(self):
		while self.running:
			for event in pygame.event.get():
				self.on_event(event)

			self.on_loop()

			self.on_render()






			
			# --------------------------

			# flip() the display to put your work on screen 
			pygame.display.flip()

			self.dt = self.clock.tick(60) / 1000

		pygame.quit()
		sys.exit()



'''
I need to create two sprite groups, one for balck and one for white pieces 
onece i created the sprite groups i can keep track of each of the sprites with event 
first i have to load all the white pieces and add that to white_pieces group and do the same to black_pieces group 
after that i have to place them in the order of chess board placing it into chess_board rectangle list 
'''
class Piece(pygame.sprite.Sprite):
	'''
	each chess pieces has their own attributes 
	name -> name of the piece (Pawn, Knight)
	actor -> sprite image 
	legal_move -> available legal move for the piece 
	is_active -> keep track if the piece is taken down or not 
	rectangle -> position of chess board where the piece is belong
	value -> value of the piece 
	'''

	def __init__(self, name, actor, legal_moves, is_active, rectangle, value):
		self.name = name 
		self.actor = actor 
		self.legal_moves = legal_moves 
		self.is_active = is_active 
		self.rectangle = rectangle
		self.value = value

	def move(self, pos, dt):
		pass

	def update(self, Piece):
		pass

	def available_legal_moves(self):
		pass

	def draw(self, screen):
		pass




class ChessBoard:
	def __init__(self):
		# ? chess board 
		self.chess_board = []
		self.board_rect = screen_height / 8 


	'''
	This function is very fucking simple
	'''
	def display_board(self, screen, dt):
		'''
		0 if laa_yellow
		1 if yellow
		'''
		state = 0
		orient = 1

		'''
		get the mouse position 
		'''
		point = pygame.mouse.get_pos()


		for i, rectangle in enumerate(self.chess_board):
			'''
			check for collition for each rectangle
			and if so change the color acording to the collition of the rectangle 
			'''
			# handle mouse event
			'''
			when the mouse enters specific rectangle turn that rectangle to different color 
			'''
			colide = rectangle.collidepoint(point)
			'''
			colide variable check the cursor entering a rectangle 
			'''

			dark_color = Colors.yellow_ch() if colide else Colors.yellow()
			laa_color = Colors.laa_yellow_ch() if colide else Colors.laa_yellow()
			
			'''
			in below four statements all the rectangles in the chess_board is rendering 
			'''
			if (orient % 8 > 0):		
				if (state == 0):
					pygame.draw.rect(screen, laa_color, rectangle)
					state = 1
					orient += 1
				else:
					pygame.draw.rect(screen, dark_color, rectangle)
					state = 0
					orient += 1
			else:
				if (state == 0):
					pygame.draw.rect(screen, laa_color, rectangle)
					orient += 1
				if(state == 1):
					pygame.draw.rect(screen, dark_color, rectangle)
					orient += 1


	def create_board(self):
		for i in range(8):
			for n in range(8):
				# creating rectangles with two colors 
				# put rectangle togather with one after another to chass_board 
				if (n % 2 == 1):
					rectangle = pygame.Rect(n * self.board_rect, i * self.board_rect, self.board_rect, self.board_rect)
					self.chess_board.append(rectangle)
				else:
					rectangle = pygame.Rect(n * self.board_rect, i * self.board_rect, self.board_rect, self.board_rect)
					self.chess_board.append(rectangle)




 
if __name__ == "__main__":
	game = Game()
	game.run()