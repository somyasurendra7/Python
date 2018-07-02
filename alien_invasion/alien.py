import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"""ALien class for the game"""

	def __init__(self, ai_settings, screen):
		"""Initialise alien class"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the alien image
		self.image = pygame.image.load('images/aliens.bmp')
		self.rect = self.image.get_rect()

		# starting the alien at the top left corner of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Check if the fleet ahs reached to the edge or not"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""Move alien to the right"""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def blitme(self):
		"""Draw the alien at the current location"""
		self.screen.blit(self.image, self.rect)
