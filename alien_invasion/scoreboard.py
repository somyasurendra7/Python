import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
	"""class to report score"""

	def __init__(self, ai_settings, screen, stats):
		"""Initialise the class"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		# score font settings
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 20)
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Turn the score into a rendered image"""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render("Score: " + score_str, True, self.text_color, self.ai_settings.bg_color)

		# Display the score on the top of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = self.score_rect.left - (-5)
		self.score_rect.top = 10

	def show_score(self):
		"""Display the score on screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def prep_high_score(self):
		"""Turn the high score into a rendered image"""
		rounded_high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(rounded_high_score)
		self.high_score_image = self.font.render("High Score: " + high_score_str, True, self.text_color,
												 self.ai_settings.bg_color)

		# Display the high score at the center of the screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Display the game level"""
		self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_color,
											self.ai_settings.bg_color)

		# Positioning the level image
		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.score_rect.left - (-1)
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""Display the ships left"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = (500) + ship_number * ship.rect.width
			ship.rect.y = 0
			self.ships.add(ship)
