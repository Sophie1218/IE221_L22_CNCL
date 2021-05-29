import pygame
from pygame.locals import MOUSEBUTTONUP, QUIT
import interface as itf
from option1.interface_op1 import option1
from option2.interface_op2 import option2


def menu():
    pygame.init()

    screen = itf.screen()
    itf.caption()
    running = True
    clock = pygame.time.Clock()

    title = itf.TextBox('K - means Visualization', (280, 118), itf.BLUE, itf.BACKGROUND)
    title.update_font_size(83)
    op1 = itf.TextBox('Option 1', (520, 300), itf.BLACK, itf.LIGHT_BLUE)
    op2 = itf.TextBox('Option 2', (520, 403), itf.BLACK, itf.LIGHT_BLUE)
    exit_button = itf.TextBox('Exit', (549, 506), itf.BLACK, itf.LIGHT_BLUE)

    while running:
        clock.tick(60)
        screen.fill(itf.BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONUP:
                # Press option 1 button
                if op1.is_click(event.pos):
                    print('option 1')
                    if not option1():
                        menu()
                # Press option 2 button
                if op2.is_click(event.pos):
                    if not option2():
                        menu()
                    print('option 2')
                # Press exit button
                if exit_button.is_click(event.pos):
                    pygame.event.post(pygame.event.Event(QUIT))
                    print('exit')

        title.show(screen)
        op1.show(screen)
        op2.show(screen)
        exit_button.show(screen)

        pygame.display.flip()

    pygame.quit()
