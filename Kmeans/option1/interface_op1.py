from option1.point import Point, PointCluster
import interface as itf
from random import randint
import pygame
from pygame.draw import rect
from pygame.font import SysFont
from myprogram.model import kmeans


def option1():
    pygame.init()

    screen = itf.screen()
    itf.caption()
    running = True
    K = 0
    error = 0
    points_user = []
    clusters = []
    points_bp = []

    for i in range(5, 490, 5):
        for j in range(5, 690, 5):
            points_bp.append(Point(j, i))

    clock = pygame.time.Clock()
    font_small = SysFont('sans', 20)
    K_text = itf.TextBox('K = ' + str(K), (1050, 50), itf.BLACK, itf.BACKGROUND)
    plus = itf.TextBox('+', (850, 50), itf.WHITE, itf.BLACK)
    minus = itf.TextBox('-', (950, 50), itf.WHITE, itf.BLACK)
    run = itf.TextBox('Run', (850, 150), itf.WHITE, itf.BLACK)
    random = itf.TextBox('Random', (850, 250), itf.WHITE, itf.BLACK)
    reset = itf.TextBox('Reset', (850, 550), itf.WHITE, itf.BLACK)
    algorithm = itf.TextBox('Algorithm', (850, 450), itf.WHITE, itf.BLACK)

    while running:
        clock.tick(60)
        screen.fill(itf.BACKGROUND)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw interface
        # Draw panel
        rect(screen, itf.BLACK, (50, 50, 700, 500))
        rect(screen, itf.BACKGROUND_PANEL, (55, 55, 690, 490))
        # K button +
        plus.show(screen)
        # K button -
        minus.show(screen)
        # K_value
        K_text.show(screen)
        # Run button
        run.show(screen)
        # Random button
        random.show(screen)
        # Reset button
        reset.show(screen)
        # Algorithm button
        algorithm.show(screen)
        # Draw mouse position when mouse is in panel
        if 50 < mouse_x < 750 and 50 < mouse_y < 550:
            text_mouse = font_small.render('(' + str(mouse_x - 50) + ',' + str(mouse_y - 50) + ')', True, itf.BLACK)
            screen.blit(text_mouse, (mouse_x + 10, mouse_y))

        # End draw interface

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Create point on panel
                for i in points_user:
                    i.update_label(None)
                for i in points_bp:
                    i.update_label(None)
                if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                    points_user.append(Point(mouse_x - 50, mouse_y - 50))

                # Change K button +
                if plus.is_click(event.pos):
                    if K < 8:
                        K += 1
                        K_text.update_text('K = ' + str(K))
                    print('K+ button pressed')

                # Change K button -
                if minus.is_click(event.pos):
                    if K > 0:
                        K -= 1
                        K_text.update_text('K = ' + str(K))
                    print('K- button pressed')

                # Run button
                if run.is_click(event.pos):
                    for i in points_user:
                        i.update_label(None)
                    for i in points_bp:
                        i.update_label(None)
                    if not clusters != []:
                        continue

                    # Assign points to closet clusters
                    for p in points_user:
                        distances_to_cluster = []
                        for c in clusters:
                            dis = p.distance(c)
                            distances_to_cluster.append(dis)

                        min_distance = min(distances_to_cluster)
                        p.update_label(distances_to_cluster.index(min_distance))

                    for p in points_bp:
                        distances_to_cluster = []
                        for c in clusters:
                            dis = p.distance(c)
                            distances_to_cluster.append(dis)

                        min_distance = min(distances_to_cluster)
                        p.update_label(distances_to_cluster.index(min_distance))

                    for i in range(K):
                        sum_x = 0
                        sum_y = 0
                        count = 0
                        for j in points_user:
                            if j.return_label() == i:
                                sum_x += j.return_coordinates()[0]
                                sum_y += j.return_coordinates()[1]
                                count += 1

                        if count != 0:
                            new_cluster_x = sum_x / count
                            new_cluster_y = sum_y / count
                            clusters[i].update_coordinates(new_cluster_x, new_cluster_y)
                    print('run pressed')

                # Random button
                if random.is_click(event.pos):
                    for i in points_user:
                        i.update_label(None)
                    for i in points_bp:
                        i.update_label(None)
                    clusters = []
                    for i in range(K):
                        random_point = PointCluster(randint(0, 700), randint(0, 500))
                        random_point.update_label(i)
                        clusters.append(random_point)
                    print(clusters)
                # Reset button
                if reset.is_click(event.pos):
                    K = 0
                    error = 0
                    points_user = []
                    points_bp = []
                    clusters = []

                    print('reset button pressed')
                # Algorithm button
                if algorithm.is_click(event.pos):
                    X = []
                    X_bp = []
                    labels = []
                    labels_bp = []

                    for i in points_bp:
                        X_bp.append(i.return_coordinates())
                    for i in points_user:
                        X.append(i.return_coordinates())
                    try:
                        model = kmeans(n_clusters=K).fit(X)
                        labels = model.predict(X)
                        labels_bp = model.predict(X_bp)
                        for i in range(len(labels)):
                            points_user[i].update_label(labels[i])
                        for i in range(len(labels_bp)):
                            points_bp[i].update_label(labels_bp[i])
                        if not clusters != []:
                            for i in range(K):
                                new_cluster = PointCluster(int(model.cluster_centers_[i][0]),
                                                           int(model.cluster_centers_[i][1]))
                                new_cluster.update_label(i)
                                clusters.append(new_cluster)
                            print('hi')
                        else:
                            for i in range(K):
                                clusters[i].update_coordinates(int(model.cluster_centers_[i][0]),
                                                               int(model.cluster_centers_[i][1]))

                    except:
                        print('Error')
                print('Algorithm button pressed')

        # Draw boundaries
        for i in points_bp:
            i.draw_boundary(screen)

        # Draw points
        for i in points_user:
            i.show(screen)

        # Draw clusters
        for i in clusters:
            i.show(screen)

        # Calculate and draw error
        error = 0
        if clusters != [] and points_user != []:
            for i in range(len(points_user)):
                if None != points_user[i].return_label():
                    error += points_user[i].distance(clusters[points_user[i].return_label()])

        text_error = itf.TextBox("Error = " + str(int(error)), (850, 350), itf.BLACK, itf.BACKGROUND)
        text_error.show(screen)
        pygame.display.flip()

    pygame.quit()
    return running
