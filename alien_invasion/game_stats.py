# game statistics class
class GameStates:
	"""Track game statistics for alien ships collisions"""

	def __init__(self, ai_settings):
		"""Initialise the class"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False  # start alien invasion in an inactive state
		self.high_score = 0  # High Score

	def reset_stats(self):
		"""storing statistics for the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
