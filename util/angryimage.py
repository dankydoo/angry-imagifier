import os
import random
import shutil

from datetime import datetime
from PIL import Image


# pull out slack image constraints
class AngryImage(object):
    def __init__(self, image_path, frame_count=3, frame_delay=30, max_anger_x=15, max_anger_y=15):

        random.seed(datetime.now())
        self.frame_count = frame_count
        self.frame_delay = frame_delay
        self.image_path = image_path
        self.max_anger_x = max_anger_x
        self.max_anger_y = max_anger_y

        file, ext = os.path.splitext(image_path)
        self.out_filename = 'angry_' + file + '.gif'

        self.original_image = Image.open(image_path).resize((128, 128))

        # self.image.show()

        shutil.copy(self.image_path, self.image_path + '.bak')

    def angrify(self, out_filename=None, slackify=True, background_color=0xffffff):

        if not out_filename:
            out_filename = self.out_filename

        images = []
        # images.append(self.original_image)
        try:
            for i in range(self.frame_count):
                anger = self.get_anger(self.max_anger_x, self.max_anger_y)
                image = self.original_image.transform(self.original_image.size, Image.AFFINE, anger)
                if slackify:
                    image = image.resize(size=(128, 128))

                # image = image.convert('RGB')
                images.append(image)

            images[0].save(out_filename, save_all=True, append_images=images, duration=self.frame_delay, loop=0,
                           format='GIF',
                           optimize=True)

        except FileNotFoundError as ex:
            raise ex

    def get_anger(self, anger_x=None, anger_y=None):
        if not anger_x:
            anger_x = self.max_anger_x
        if not anger_y:
            anger_y = self.max_anger_y

        anger_x = random.randrange(-1 * anger_x, anger_x, 1)
        anger_y = random.randrange(-1 * anger_y, anger_y, 1)

        anger_adjust = (1, 0, anger_x, 0, 1, anger_y)
        return anger_adjust
