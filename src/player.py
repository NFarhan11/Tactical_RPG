from settings import pygame, GRID_SIZE

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
		self.image.fill("chartreuse4")
		self.rect = self.image.get_frect()
		x, y = pos
		self.rect.topleft = (x * GRID_SIZE, y * GRID_SIZE)

	def move(self, dp):
		dx, dy = dp
		self.rect.x += dx * GRID_SIZE
		self.rect.y += dy * GRID_SIZE