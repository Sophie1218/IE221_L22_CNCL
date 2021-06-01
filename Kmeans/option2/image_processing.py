# import libraries
import myprogram.interface as itf
from myprogram.model import kmeans
import pygame
from myprogram.option2.image_processing import Image
import matplotlib.pyplot as plt
import numpy as np


def option2():
    """
    interface option 2

            Parameters:


            Returns:
                    status of option 2: True/False
                    True: option 2 is running
                    False: option 2 is closed
    """
    pygame.init()
    screen = itf.screen()

    itf.caption()

    clock = pygame.time.Clock()
    K = 0
    shiftDown = False
    image = Image(None)
    running = True
    insert = itf.TextBox('Insert the image path', (850, 50), itf.BLUE, itf.BACKGROUND)
    input_box = itf.InputTextBox('', (850, 150), itf.BLACK, itf.BLACK)
    input_box.update_width_rect(300)
    show_image = itf.TextBox('Show', (950, 225), itf.WHITE, itf.BLACK)
    plus = itf.TextBox('+', (900, 300), itf.WHITE, itf.BLACK)
    minus = itf.TextBox('-', (950, 300), itf.WHITE, itf.BLACK)
    K_text = itf.TextBox('K = ' + str(K), (1000, 300), itf.BLACK, itf.BACKGROUND)
    run = itf.TextBox('Run and Show result', (850, 400), itf.WHITE, itf.BLACK)

    while running:
        clock.tick(60)
        screen.fill(itf.BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.is_click(event.pos):
                    input_box.update_active(True)
                else:
                    input_box.update_active(False)

                # Change K button +
                if plus.is_click(event.pos):
                    K += 1
                    K_text.update_text('K = ' + str(K))
                print('K+ button pressed')

                # Change K button -
                if minus.is_click(event.pos):
                    if K > 0:
                        K -= 1
                        K_text.update_text('K = ' + str(K))
                print('K- button pressed')

                # Press show button
                if show_image.is_click(event.pos):
                    if len(input_box.return_content()) > 0:
                        image.update_path(input_box.return_content())
                print('Show button pressed')

                # Press run button and show image after running K - means
                if run.is_click(event.pos):
                    if K > 0 and None != image.return_path():

                        img = image.process_image()
                        model = kmeans(n_clusters=K).fit(img)
                        labels = model.predict(img)
                        clusters = model.cluster_centers_

                        img2 = np.zeros_like(img)

                        for i in range(len(img2)):
                            img2[i] = clusters[labels[i]]

                        img2 = img2.reshape(image.return_size()[0], image.return_size()[1], 3)
                        plt.imshow(img2)
                        plt.show()

                    print('Run button pressed')

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = True
                if input_box.is_active():
                    if event.key == pygame.K_BACKSPACE:
                        input_box.minus_chr()
                    else:
                        input_box.add_chr(pygame.key.name(event.key), shiftDown)
                    input_box.update_width_rect(max(300, input_box.get_text_width() + 10))
        if None != image.return_path():
            try:
                image.show_image(screen)
            except:
                print("Error")
        # Draw interface
        # Input box for inserting path image
        input_box.show(screen)
        # Text 'Insert the path image'
        insert.show(screen)
        # Show button
        show_image.show(screen)
        # K button +
        plus.show(screen)
        # K button -
        minus.show(screen)
        # K value
        K_text.show(screen)
        # Run button
        run.show(screen)
        # End draw interface
        pygame.display.flip()

    pygame.quit()
    return running
