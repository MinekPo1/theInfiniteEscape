import pygame

COLOR = (200, 168, 90)


class Tile(pygame.sprite.Sprite):
	rect: pygame.Rect

	def __init__(self, pos, size):
		super().__init__()
		self.image = pygame.Surface(size)
		self.image.fill(COLOR)
		self.rect = self.image.get_rect(topleft=pos)  # type:ignore

	def update(self, x_shift):
		self.rect.x += x_shift
