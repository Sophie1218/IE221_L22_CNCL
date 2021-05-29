import matplotlib.pyplot as plt
from pygame.image import load
from pygame.transform import scale


class Image:
    def __init__(self, path):
        self.path = path

    def process_image(self):
        img = plt.imread(self.path)
        return img.reshape(img.shape[0] * img.shape[1], 3)

    def return_size(self):
        img = plt.imread(self.path)
        return [img.shape[0], img.shape[1]]

    def show_image(self, screen):
        max_width = 750
        max_height = 600
        image = load(self.path)
        if image.get_height() > 650:
            ratio = min(max_width / image.get_width(), max_height / image.get_height())
            image = scale(image, (int(image.get_width() * ratio), int(image.get_height() * ratio)))
        if image.get_width() > 750:
            ratio = min(max_width / image.get_width(), max_height / image.get_height())
            image = scale(image, (int(image.get_width() * ratio), int(image.get_height() * ratio)))
        screen.blit(image, (50, 50))

    def return_path(self):
        return self.path

    def update_path(self, path):
        self.path = path
