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
			if event.type == pygame.QUIT:
				running = False

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


		# drawing the chess board to the screen
		display_board(screen, dt)












		
		# --------------------------

		# flip() the display to put your work on screen 
		pygame.display.flip()

		dt = clock.tick(60) / 1000

	pygame.quit()
	sys.exit()


 
if __name__ == "__main__":
	main()