import pygame
from random import randint
import math
from sklearn.cluster import KMeans


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


pygame.init()

screen = pygame.display.set_mode((1200, 700))

# Caption and Icon
pygame.display.set_caption('K - means Visualization')
# icon = pygame.image.load('visual-thinking.png')
# pygame.display.set_icon(icon)

running = True

clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PINK = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRASS = (55, 155, 65)
GREY = (38, 50, 56)

LIGHT_RED = (255, 230, 230)
LIGHT_GREEN = (233, 255, 230)
LIGHT_BLUE = (230, 230, 255)
LIGHT_YELLOW = (255, 253, 235)
LIGHT_PINK = (255, 250, 250)
LIGHT_SKY = (230, 255, 255)
LIGHT_ORANGE = (255, 242, 235)
LIGHT_GRASS = (240, 244, 195)
LIGHT_GREY = (236, 239, 241)

COLORS = [RED, GREEN, BLUE, YELLOW, PINK, SKY, ORANGE, GRASS, GREY]
LIGHT_COLORS = [LIGHT_RED, LIGHT_GREEN, LIGHT_BLUE, LIGHT_YELLOW, LIGHT_PINK, LIGHT_SKY, LIGHT_ORANGE, LIGHT_GREY,
                LIGHT_GRASS]

font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

K = 0
error = 0
points = []
clusters = []
labels = []
# boundary
points_bp = []
for i in range(5, 490, 5):
    for j in range(5, 690, 5):
        points_bp.append([j, i])
labels_bp = []

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw interface
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))
    # K button +
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(text_plus, (860, 50))

    # K button -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(text_minus, (960, 50))

    # K value
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (1050, 50))

    # run button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(text_run, (900, 150))

    # random button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(text_random, (850, 250))

    # Reset button
    pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))
    screen.blit(text_reset, (850, 550))

    # Algorithm button
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(text_algorithm, (850, 450))

    # Draw mouse position when mouse is in panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True, BLACK)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    # End draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create point on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                labels_bp = []
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)
                print(points)

            # Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 8:
                    K = K + 1
                print("Press K +")

            # Change K button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
                print("Press K -")

            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                labels = []
                labels_bp = []
                if not clusters != []:
                    continue

                # Assign points to closet clusters
                for p in points:
                    distances_to_cluster = []
                    for c in clusters:
                        dis = distance(p, c)
                        distances_to_cluster.append(dis)

                    min_distance = min(distances_to_cluster)
                    label = distances_to_cluster.index(min_distance)
                    labels.append(label)

                for p in points_bp:
                    distances_to_cluster = []
                    for c in clusters:
                        dis = distance(p, c)
                        distances_to_cluster.append(dis)

                    min_distance = min(distances_to_cluster)
                    label_bp = distances_to_cluster.index(min_distance)
                    labels_bp.append(label_bp)
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1

                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x, new_cluster_y]

                print("run pressed")

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                labels = []
                labels_bp = []
                clusters = []
                for i in range(K):
                    random_point = [randint(0, 700), randint(0, 500)]
                    clusters.append(random_point)
                print("random pressed")

            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                K = 0
                error = 0
                points = []
                clusters = []
                labels = []
                labels_bp = []
                print("reset button pressed")

            # Algorithm
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                try:
                    kmeans = KMeans(n_clusters=K).fit(points)
                    labels = kmeans.fit_predict(points)
                    labels_bp = kmeans.predict(points_bp)
                    clusters = kmeans.cluster_centers_
                except:
                    print("error")
                print("Algorithm button pressed")
    # Draw boundary
    if not labels_bp != []:
        pass
    else:
        for j in range(len(labels_bp)):
            pygame.draw.rect(screen, LIGHT_COLORS[labels_bp[j]], (points_bp[j][0] + 50, points_bp[j][1] + 50, 5, 5))

    # Draw point
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)

        if not labels != []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
        else:
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5)
    # Draw cluster
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (int(clusters[i][0]) + 50, int(clusters[i][1]) + 50), 10)
    # Calculate and draw error
    error = 0
    if clusters != [] and labels != []:
        for i in range(len(points)):
            error += distance(points[i], clusters[labels[i]])

    text_error = font.render("Error = " + str(int(error)), True, BLACK)
    screen.blit(text_error, (850, 350))

    pygame.display.flip()

pygame.quit()

