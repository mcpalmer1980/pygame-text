"""Quick test of unfinished long word breaking option"""

import pygame
import ptext

screen = pygame.display.set_mode((854, 480))
screen.fill((0, 30, 60))
clock = pygame.time.Clock()

long_str = '''
Hello this is a verylongwordwaytoobigtofit. The other words are much shorter. Hyphens are automatically added.
'''	

pygame.draw.line(screen, (255,255,255), (270, 0), (270, 480))
ptext.draw(long_str, (90, 210), width=180, lineheight=1.1, breakwords=True)
ptext.draw("Outlined Text", (400, 70), fontname="fonts/Boogaloo.ttf", fontsize=48, owidth=4, ocolor=(255,255,0), color=(0,0,0))
ptext.draw("OutlinedText", (90, 70), width=180, fontname="fonts/Boogaloo.ttf", fontsize=48, owidth=4, ocolor=(255,255,0), color=(0,0,0))


while not any(event.type in (pygame.KEYDOWN, pygame.QUIT) for event in pygame.event.get()):
	pygame.display.flip()
	clock.tick(30)

