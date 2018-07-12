from random import randint


class Die:
	"""Class for die roll"""
	def __init__(self, num_sides=6):
		"""Initialize the die class"""
		self.num_sides = num_sides

	def roll(self):
		"""returns a roll of die"""
		return randint(1, self.num_sides)

	


