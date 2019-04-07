import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
step = 20

pygame.display.set_caption("Pygame Pony")
screen = pygame.display.set_mode(size)

background_image = pygame.image.load("background.png")

pony = pygame.image.load("pony.gif")
transparentColor = pony.get_at((0,0))
pony.set_colorkey(transparentColor, RLEACCEL)

ponyRect = pony.get_rect()
ponyRect.centerx = width / 2
ponyRect.centery = height / 2

clock = pygame.time.Clock()

def movePony(keys):
    global ponyRect, step, screen
    speed = [0, 0]
    if keys[K_UP]:
        speed = [0, -step]
    elif keys[K_DOWN]:
        speed = [0, step]
    elif keys[K_LEFT]:
        speed = [-step, 0]
    elif keys[K_RIGHT]:
        speed = [step, 0]
    else:
        print("Unknown event")
    print(f"Speed {speed} - X:{ponyRect.centerx} - Y:{ponyRect.centery}")
    print(f"Left:{ponyRect.left} - Right:{ponyRect.right}")
    print(f"Top:{ponyRect.top} - Bottom:{ponyRect.bottom}")

    ponyRect.centerx += speed[0]
    ponyRect.centery += speed[1]

    if ponyRect.left > 800:
        ponyRect.centerx = 0
    if ponyRect.right < 0:
        ponyRect.centerx = 800
    if ponyRect.bottom >= 450:
        ponyRect.bottom = 450
    if ponyRect.bottom <= 360:
        ponyRect.bottom = 360

while True:
    time = clock.tick(60) # 60fps
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            movePony(keys)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_image, (0, 0))
    screen.blit(pony, ponyRect)
    pygame.display.flip()
