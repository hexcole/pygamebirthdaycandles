import pygame
import os

x = 20
y = 20
_image_library = {}
is_blushy = True
stringg = '/Users/nplotkin/PycharmProjects/Gamepractice/IMG_7295.PNG'

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()
pygame.mixer.music.load('/Users/nplotkin/PycharmProjects/Gamepractice/Fart sound effect.mp3')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blushy = not is_blushy
            pygame.mixer.music.play(0) 

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((255, 255, 255))

    if is_blushy:
        stringg = '/Users/nplotkin/PycharmProjects/Gamepractice/IMG_7295.PNG'
    else:
        stringg = '/Users/nplotkin/PycharmProjects/Gamepractice/IMG_72951.PNG'
    screen.blit(get_image(stringg), (x, y))

    pygame.display.flip()
    clock.tick(60)
