import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to key press down event"""
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	# Quit the game by pressing 'q'
	elif event.key == pygame.K_q:
		sys.exit()


def check_up_event(event, ship):
	"""Respond to key press up event"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
	"""Respond to keyboard/ mouse press events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# move the ship to right when keyboard right key is pressed
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_up_event(event, ship)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	"""Start a new game when player clicks play"""
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
		if button_clicked and not stats.game_active:
			# reset to initial settings
			ai_settings.initialize_dynamic_settings()
			# hide the mouse
			pygame.mouse.set_visible(False)
			# resetting the game statistics
			stats.reset_stats()
			stats.game_active = True
			# Resetting the score board images
			sb.prep_score()
			sb.prep_high_score()
			sb.prep_level()
			sb.prep_ships()
			# empty aliens and bullets list
			aliens.empty()
			bullets.empty()
			# create a new fleet at the center of the ship
			create_fleet(ai_settings, screen, ship, aliens)
			ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	"""Update the screen settings"""
	# Change the screen color
	screen.fill(ai_settings.bg_color)
	# redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# calling the ship on screen
	ship.blitme()
	# calling the alien on screen
	aliens.draw(screen)
	# Display the score on screen
	sb.show_score()
	# Draw the button for an inactive game
	if not stats.game_active:
		play_button.draw_button()

	# Show the most recent screen available
	pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""Update the bullets position and settings"""
	bullets.update()
	# deleting older fired bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# check for bullets hitting the aliens and get rid of the alien
	check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""Respond to bullets hitting an alien"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)  # scoring is equivalent to number of aliens hit
			sb.prep_score()
		check_high_score(stats, sb)
	# check if aliens group are empty , if so, add new fleet to the group
	if len(aliens) == 0:
		# destroy existing bullets
		bullets.empty()
		ai_settings.increase_speed()
		# increasing the level
		stats.level += 1
		sb.prep_level()
		create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
	"""setting bullet limits"""
	# create a bullet and add it to the group
	if len(bullets) < ai_settings.bullets_allowed:  # check the condition that the no. of bullets fired is 3.
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
	"""Creating alien fleets"""
	# creating an alien
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_aliens_number_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	# first row of aliens
	# creating fleet of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_aliens_number_x(ai_settings, alien_width):
	"""fix the number of aliens in a row"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create alien and place it in position"""
	alien = Alien(ai_settings, screen)
	# spacing each alien = width of one alien
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
	"""Determine the number of rows pf aliens that can fit on the screen"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def check_fleet_edges(ai_settings, aliens):
	"""Check fleet position w.r.t edges"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break


def change_fleet_direction(ai_settings, aliens):
	"""Changes the fleet's direction"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""Update aliens position"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	# Alien-Ship collision
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
	# Look for aliens hitting the bottom
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""Respond to collision of ship"""
	if stats.ships_left > 0:
		# Decrement the no. of ships left
		stats.ships_left -= 1
		# update scoreboard
		sb.prep_ships()
		# empty aliens and bullets list
		aliens.empty()
		bullets.empty()
		# create new fleet in the center
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		# wait for 0.5 second
		sleep(1)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""Check if the aliens has reached the bottom or not"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break


def check_high_score(stats, sb):
	"""Checks the  high score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
