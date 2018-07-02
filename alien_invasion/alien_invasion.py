import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStates
import game_functions as gf
from pygame.sprite import Group


def run_game():
	"""Initialise game and create an object of the game"""

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")

	# Make a ship
	ship = Ship(ai_settings, screen)
	# Storing bullet as groups
	bullets = Group()
	# Make an alien
	alien = Alien(ai_settings, screen)
	# Storing alien as groups
	aliens = Group()
	# creating fleets
	gf.create_fleet(ai_settings, screen, ship, aliens)
	# Make gaming instances and score instances
	stats = GameStates(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	# Make a play button
	play_button = Button(ai_settings, screen, "Play")

	# Start the main loop for the program
	while True:
		# using the check_events module from game_functions.py
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
