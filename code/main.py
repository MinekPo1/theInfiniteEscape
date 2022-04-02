import pygame, sys
from settings import *
from level import Level
from pygame import mixer
from button import Button

# Pygame setup
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, SCREEN)

pygame.display.set_caption("MENU")


mixer.music.load('..\sound&music\music\music11.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.7)




BG = pygame.image.load('MainMenu/MainMenuBackgrond.png')

def get_font(size):  # Returns Press-Start-2P in the desired size
	return pygame.font.Font("MainMenu/font.ttf", size)


def play():
	run = True
	while True:









		pygame.display.set_caption("GAME")

		SCREEN.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		SCREEN.fill('black')
		level.run()

		pygame.display.update()
		clock.tick(60)


def options():
	while True:




		pygame.display.set_caption("OPTIONS")

		color1 = (200, 168, 90)

		OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

		SCREEN.fill("black")

		OPTIONS_TEXT = get_font(16).render("@RiverBlak#7781", True, color1)
		OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(375, 65))
		SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

		OPTIONS_TEXT = get_font(16).render("@Lady Yami#3939", True, color1)
		OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(375, 115))
		SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

		OPTIONS_TEXT = get_font(16).render("@mikey0929#2441", True, color1)
		OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(375, 165))
		SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

		OPTIONS_TEXT = get_font(16).render("@MinekPo1#9801", True, color1)
		OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(375, 215))
		SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

		OPTIONS_TEXT = get_font(16).render("by BigExplosionTeam", True, color1)
		OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(375, 15))
		SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

		OPTIONS_BACK = Button(image=None, pos=(375, 300),
							  text_input="BACK", font=get_font(75), base_color=color1, hovering_color=color1)

		if OPTIONS_BACK == True:
			SCREEN.fill("black")


		OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
		OPTIONS_BACK.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
					main_menu()

		pygame.display.update()


def main_menu():
	while True:
		color1 = (200, 168, 90)

		SCREEN.blit(BG, (0, 0))

		MENU_MOUSE_POS = pygame.mouse.get_pos()

		MENU_TEXT = get_font(100).render("_", True, color1)
		MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

		PLAY_BUTTON = Button(image=pygame.image.load("MainMenu/Play Rect.png"), pos=(610, 50),
							 text_input="PLAY", font=get_font(32), base_color='black', hovering_color="black")
		OPTIONS_BUTTON = Button(image=pygame.image.load("MainMenu/Options Rect.png"), pos=(610, 132),
								text_input="CREDITS", font=get_font(32), base_color='black', hovering_color="black")
		QUIT_BUTTON = Button(image=pygame.image.load("MainMenu/Quit Rect.png"), pos=(610, 252),
							 text_input="QUIT", font=get_font(32), base_color='black', hovering_color="black")

		SCREEN.blit(MENU_TEXT, MENU_RECT)

		for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
			button.changeColor(MENU_MOUSE_POS)
			button.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
					play()
				if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
					options()
				if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
					pygame.quit()
					sys.exit()

		pygame.display.update()


main_menu()
