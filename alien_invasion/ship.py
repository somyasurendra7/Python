import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	"""Ship class for the game"""

	def __init__(self, ai_settings, screen):
		"""Initialising the class"""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start each ship at the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position as per flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			# we will update the ship's center value not rect.
			# self.rect.centerx +=1
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			# self.rect.centerx -=1
			self.center -= self.ai_settings.ship_speed_factor

		# update rect from self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""Draw the ship at its current locations"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Positions the ship in the center"""
		self.center = self.screen_rect.centerx
