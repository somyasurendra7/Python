import pygame.font


class Button():
	"""Button class"""

	def __init__(self, ai_settings, screen, msg):
		"""Initialise the Button class"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# setting the dimensions and properties of the button
		self.width, self.height = 200, 50
		self.button_color = (200, 200, 200)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Building the button's rect object in the center
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button message
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""msg settings"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw a blank button on the screen"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
