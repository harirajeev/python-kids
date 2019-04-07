import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 800, 600
step = 7
direction = "left"

pygame.display.set_caption("Pygame Pony")
screen = pygame.display.set_mode(size)

background_image = pygame.image.load("background.png")

# Prepare pony images
ponyLeft = [pygame.image.load("pony-L-000.png").convert(), pygame.image.load("pony-L-001.png").convert()]
ponyRight = [pygame.image.load("pony-R-000.png").convert(), pygame.image.load("pony-R-001.png").convert()]

ponyImages = {}
ponyImages["left"] = ponyLeft
ponyImages["right"] = ponyRight

pony = None
ponyRect = None

clock = pygame.time.Clock()

def initPonyImage(image):
    """
    Set the transparant color of the image,
    and get the rectangle value.
    """
    global pony, ponyRect
    pony = image
    transparentColor = pony.get_at((0,0))
    pony.set_colorkey(transparentColor, RLEACCEL)

    ponyRect = pony.get_rect()
    ponyRect.centerx = width / 2
    ponyRect.centery = height / 2

def movePony(keys):
    """
    Move the pony to the direction of the key,
    it select also the image to show.
    """
    global pony, ponyRect, step, screen, direction, ponyImages
    speed = [0, 0]
    if keys[K_UP]:
        speed = [0, -step]
    elif keys[K_DOWN]:
        speed = [0, step]
    elif keys[K_LEFT]:
        direction = "left"
        speed = [-step, 0]
    elif keys[K_RIGHT]:
        direction = "right"
        speed = [step, 0]
    else:
        print("Unknown event")
    # Print info in the console
    print(f"Speed {speed} - X:{ponyRect.centerx} - Y:{ponyRect.centery} - Direction:{direction}")
    print(f"Left:{ponyRect.left} - Right:{ponyRect.right}")
    print(f"Top:{ponyRect.top} - Bottom:{ponyRect.bottom}")

    # TODO select the image to use
    oldx = ponyRect.centerx
    oldy = ponyRect.centery
    pony = ponyImages[direction][oldx % 2]
    transparentColor = pony.get_at((0,0))
    pony.set_colorkey(transparentColor, RLEACCEL)
    ponyRect = pony.get_rect()
    ponyRect.centerx = oldx + speed[0]
    ponyRect.centery = oldy + speed[1]

    if ponyRect.left > 800:
        ponyRect.centerx = 0
    if ponyRect.right < 0:
        ponyRect.centerx = 800
    if ponyRect.bottom >= 450:
        ponyRect.bottom = 450
    if ponyRect.bottom <= 360:
        ponyRect.bottom = 360

# Init the default image
initPonyImage(ponyLeft[0])

#Enable key event repeat when you hold a key
pygame.key.set_repeat(100,10)

# Main loop
while True:
    time = clock.tick(60) # 60fps
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            movePony(keys)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Repaint screen
    screen.blit(background_image, (0, 0))
    screen.blit(pony, ponyRect)
    pygame.display.flip()
