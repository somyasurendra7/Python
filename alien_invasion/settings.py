# settings class for the game


class Settings:
	"""A setting class for game variables"""

	def __init__(self):
		"""Initialising the setting class"""
		self.screen_width = 700
		self.screen_height = 700
		self.bg_color = (10, 10, 10)
		# ship settings
		self.ship_limit = 3

		# adding settings for bullet
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (230, 0, 0)
		self.bullets_allowed = 3

		# adding settings for aliens
		self.fleet_drop_speed = 50

		# speeding up the levels
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialise the settings for game"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.25

		# Scores
		self.alien_points = 10

		# fleet direction to the right = 1, and to the left = -1
		self.fleet_direction = 1

	def increase_speed(self):
		"""increase speed settings and alien scores"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
