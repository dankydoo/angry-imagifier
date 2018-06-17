import random
import shutil

from datetime import datetime
from PIL import Image


class AngryImage(object):
    def __init__(self, image_path, frame_count=3, frame_delay=30, max_anger_x=15, max_anger_y=15):

        random.seed(datetime.now())
        self.frame_count = frame_count
        self.frame_delay = frame_delay
        self.image_path = image_path
        self.max_anger_x = max_anger_x
        self.max_anger_y = max_anger_y

        self.image = Image.open(image_path)

        # self.image.show()

        shutil.copy(self.image_path, self.image_path + '.bak')

    def angrify(self):

        frame_count = 3
        images = []
        try:
            for i in range(frame_count):
                anger = self.get_anger()
                image = self.image.transform(self.image.size, Image.AFFINE, anger)
                # image = image.convert('RGB')
                image.save(f'new{i}.png')
                # image.show()
                images.append(image)

            print('done')

            images[0].save('test.gif', save_all=True, append_images=images, duration=10, loop=0, format='GIF')
            # angry_image = Image.open('test.gif')

        except FileNotFoundError as fnfe:
            print(fnfe)
            raise fnfe
            pass

    def get_anger(self, anger_x=None, anger_y=None):

        if not anger_x:
            anger_x = random.randrange(-1 * self.max_anger_x, self.max_anger_x, 1)

        if not anger_y:
            anger_y = random.randrange(-1 * self.max_anger_y, self.max_anger_y, 1)

        anger_adjust = (1, 0, anger_x, 0, 1, anger_y)

        # a = 1
        # b = 0
        # anger_x = anger_x  # left/right (i.e. 5/-5)
        # d = 0
        # e = 1
        # anger_y = anger_y  # up/down (i.e. 5/-5)
        return anger_adjust
