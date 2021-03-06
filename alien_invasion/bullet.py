import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""Class to manage bullet"""

	def __init__(self, ai_settings, screen, ship):
		"""Initialise the bullet class"""
		super(Bullet, self).__init__()
		self.screen = screen

		# Creating rectangle for bullet and then setting the positions

		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# storing the bullet's position as a decimals value
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""Move the bullet up the screen"""
		# update the decimal position of the bullet
		self.y -= self.speed_factor
		# update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draws the bullet"""
		pygame.draw.rect(self.screen, self.color, self.rect)
