from settings import *
from grid import Grid
from player import Player
from camera import CameraGroup


class Game:
	def __init__(self):
		# Init Game
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()

		# Camera
		self.camera_group = CameraGroup()
		self.camera_group.zoom_scale = 1.75

		# Sprites
		self.grid = Grid(WIDTH, HEIGHT)
		self.player = Player((5, 5), self.camera_group)

	def input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.player.move((1, 0))  # move right
		if keys[pygame.K_a]:
			self.player.move((-1, 0))  # move left
		if keys[pygame.K_w]:
			self.player.move((0, -1))  # move up
		if keys[pygame.K_s]:
			self.player.move((0, 1))  # move down

	def update(self):
		self.camera_group.update()

	def render(self):
		self.screen.fill(BG_COLOR)
		self.grid.draw(self.screen)
		self.camera_group.custom_draw(self.player)

	def run(self):
		while True:
			self.clock.tick(60)
			self.input()
			self.update()
			self.render()
			pygame.display.update()

if __name__ == '__main__':
	Game().run()
