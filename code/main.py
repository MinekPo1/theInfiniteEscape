import pygame
import sys
from settings import *
from level import Level
from pygame import mixer
from button import Button

# Pygame setup
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(r"../maps/test.tiemap.txt", SCREEN)

pygame.display.set_caption("MENU")


# mixer.init()
# mixer.music.load(r'..\sound&music\music\music1.wav')
# mixer.music.play(-1)
# mixer.music.set_volume(0.7)

COLOR1 = (200, 168, 90)


BG = pygame.image.load('MainMenu/MainMenuBackgrond.png')


def get_font(size):  # Returns Press-Start-2P in the desired size
	return pygame.font.Font("MainMenu/font.ttf", size)


def play():
	while True:
		pygame.display.set_caption("GAME")

		SCREEN.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		level.run()

		pygame.display.update()
		clock.tick(60)

def options():

	credit_text = {
		"@RiverBlak#7781": (375, 65),
		"@Lady Yami#3939": (375, 115),
		"@mikey0929#2441": (375, 165),
		"@MinekPo1#9801": (375, 215),
		"by BigExplosionTeam": (375, 15)
	}
	OPTIONS_BACK = Button(
		image=None, pos=(375, 300), text_input="BACK",
		font=get_font(75), base_color=COLOR1, hovering_color=COLOR1
	)
	while True:
		pygame.display.set_caption("OPTIONS")

		OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

		SCREEN.fill("black")

		for text,pos in credit_text.items():
			text_surf = get_font(16).render(text, False, COLOR1)
			text_rect = text_surf.get_rect(center=pos)
			SCREEN.blit(text_surf, text_rect)

		# if OPTIONS_BACK:
		# 	SCREEN.fill("black")

		OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
		OPTIONS_BACK.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and OPTIONS_BACK.checkForInput(
				OPTIONS_MOUSE_POS
			):
				return

		pygame.display.update()


def main_menu():
	COLOR1 = (200, 168, 90)
	PLAY_BUTTON = Button(
		image=pygame.image.load("MainMenu/Play Rect.png"), pos=(610, 50),
		text_input="PLAY", font=get_font(32), base_color='black', hovering_color="black"
	)

	OPTIONS_BUTTON = Button(
		image=pygame.image.load("MainMenu/Options Rect.png"), pos=(610, 132),
		text_input="CREDITS", font=get_font(32), base_color='black', hovering_color="black"
	)

	QUIT_BUTTON = Button(
		image=pygame.image.load("MainMenu/Quit Rect.png"), pos=(610, 252),
		text_input="QUIT", font=get_font(32), base_color='black', hovering_color="black"
	)

	while True:

		SCREEN.blit(BG, (0, 0))

		MENU_MOUSE_POS = pygame.mouse.get_pos()

		# MENU_TEXT = get_font(100).render("_", True, (255, 255, 255))
		# MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

		# SCREEN.blit(MENU_TEXT, MENU_RECT)

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
