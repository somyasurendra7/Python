from random import choice


class RandomWalk:
	"""generates random walk"""
	def __init__(self, num_points=500):
		"""Initialize the class"""
		self.num_points = num_points

		# walks starting at (0,0)
		self.x_values = [0]
		self.y_values = [0]

	def fine_walk(self):
		"""calculate walk points"""
		while len(self.x_values) < self.num_points:
			x_step = get_step(self.x_values)
			y_step = get_step(self.y_values)
			# Rejecting x and y still moves
			if x_step == 0 and y_step == 0:
				continue

			# calculating x and y
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)


def get_step(self):
	"""Determine the distance and direction of steps"""
	direction = choice([1, -1])
	distance = choice([0, 1, 2, 3, 4])
	step = direction * distance
	return step




