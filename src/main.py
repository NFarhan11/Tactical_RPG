from settings import *
from grid import Grid, Tile
from player import Player
from pytmx import load_pygame


class Game:
	def __init__(self):
		# Init Game
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()

		# Sprites
		self.grid = Grid(WIDTH, HEIGHT)
		self.player = Player((5, 5))
		self.all_sprites = pygame.sprite.Group()
		# cycle through all layers
		tmx_data = load_pygame("../assets/map/basic.tmx")
		for layer in tmx_data.visible_layers:  # visible layers
			if hasattr(layer, "data"):  # contains a data
				for x, y, surf in layer.tiles():
					pos = (x * 16, y * 16)
					Tile(pos, surf, self.all_sprites)
		self.all_sprites.add(self.player)

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
		pass

	def render(self):
		self.screen.fill(BG_COLOR)
		self.grid.draw(self.screen)
		self.all_sprites.draw(self.screen)

	def run(self):
		while True:
			self.clock.tick(60)
			self.input()
			self.update()
			self.render()
			pygame.display.update()

if __name__ == '__main__':
	Game().run()
