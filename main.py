import pygame
import sys
from settings import Colors

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
	# window attributes
	screen_width, screen_height = 1280, 720

	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Python Chess Game")
	clock = pygame.time.Clock()
	running = True
	# | delta time |
	dt = 0

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
		screen.fill(Colors.white())

		# render area
		# --------------------------
		simple_game(screen, dt, player_pos=player_pos)

		# game logic 
		ballrect = ballrect.move(speed)
		if (ballrect.left < 0 or ballrect.right > screen_width):
			speed[0] = -speed[0]
		if (ballrect.top < 0 or ballrect.bottom > screen_height):
			speed[1] = -speed[1]
		bouncing_game(screen, dt, ball=ball, ballrect=ballrect)
		# --------------------------

		# flip() the display to put your work on screen 
		pygame.display.flip()

		dt = clock.tick(60) / 1000

	pygame.quit()
	sys.exit()


 
if __name__ == "__main__":
	main()