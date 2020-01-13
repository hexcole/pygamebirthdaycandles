import pygame
import os
import random
import time

_image_library = {}
is_blushy = True
stringg = '/Users/nplotkin/PycharmProjects/Gamepractice/white-smiling-face_263a.png'
string2 = '/Users/nplotkin/PycharmProjects/Gamepractice/birthday-cake_1f382.png'

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()
pygame.mixer.music.load('/Users/nplotkin/PycharmProjects/Gamepractice/HappyBirthday.wav')
pygame.mixer.music.play(1)

screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if is_blushy:
                is_blushy = False

                pygame.mixer.music.stop()
                pygame.mixer.music.load('/Users/nplotkin/PycharmProjects/Gamepractice/wakawaka1.wav')
                pygame.mixer.music.play(1)
                time.sleep(1.8)

    if is_blushy:
        screen.fill((255, 255, 255))
        stringg = '/Users/nplotkin/PycharmProjects/Gamepractice/white-smiling-face_263a.png'
        string2 = '/Users/nplotkin/PycharmProjects/Gamepractice/birthday-cake_1f382.png'
        screen.blit(get_image(stringg), (100, 110))
        screen.blit(get_image(string2), (180, 179))
    else:
        screen.fill((0, 0, 0))
        stringg = '/Users/nplotkin/PycharmProjects/Gamepractice/Untitled.png'
        string2 = '/Users/nplotkin/PycharmProjects/Gamepractice/birthday-cake_1f3821.png'
        screen.blit(get_image(stringg), (100+random.randint(-10, 10), 110))
        screen.blit(get_image('/Users/nplotkin/PycharmProjects/Gamepractice/cooltext346335303095809.png'), (0, 0+random.randint(-2, 2)))
        screen.blit(get_image(string2), (180, 179+random.randint(-2, 2)))

    pygame.display.flip()
    clock.tick(60)
