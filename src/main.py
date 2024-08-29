from settings import *
from grid import Grid
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

grid = Grid(WIDTH, HEIGHT)
player = Player((5, 5))
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while True:
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
		player.move((1, 0))  # move right
	if keys[pygame.K_a]:
		player.move((-1, 0))  # move left
	if keys[pygame.K_w]:
		player.move((0, -1))  # move up
	if keys[pygame.K_s]:
		player.move((0, 1))  # move down

	screen.fill(BG_COLOR)
	grid.draw(screen)
	all_sprites.draw(screen)

	pygame.display.update()
	clock.tick(60)


