import pygame
import random as r
import time
import math

def main():
    run = True
    width, height = (500,500)
    win = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Bubble sort vis")
    clock = pygame.time.Clock()
    win.fill((40,40,40))
    x = 0
    i = 0

    l = []

    for j in range(width):
        l.append(j)
        r.shuffle(l)


    while run:

        win.fill((40,40,40))

        for count in range(500):
            if i >= (len(l) - x - 1):
                i = 0
                x += 1

            if x == len(l):
                run = False

            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]

            for index, item in enumerate(l):
                if len(l) - x <= index:
                    pygame.draw.line(win, (0, 255, 0), [index, width], [index, item], 1)
                else:
                    pygame.draw.line(win, (255, 255, 255), [index, width], [index, item], 1)

            i += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

        pygame.display.update()



main()

print('done')
