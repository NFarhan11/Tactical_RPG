from settings import pygame, GRID_SIZE, WIDTH, HEIGHT


class Grid:
	def __init__(self, width, height):
		self.cols = width // GRID_SIZE
		self.rows = height // GRID_SIZE

	def draw(self, screen):
		for x in range(0, screen.get_width(), GRID_SIZE):  # columns
			for y in range(0, screen.get_height(), GRID_SIZE):  # rows
				rect = pygame.FRect((x, y), (GRID_SIZE, GRID_SIZE))
				pygame.draw.rect(screen, "antiquewhite4", rect, 1)


class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_frect(topleft=pos)
