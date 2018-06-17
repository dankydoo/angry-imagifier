import sys

from PIL import Image

from util.angryimage import AngryImage

def main(args):
    angry = AngryImage('batman.png', max_anger_x=40, max_anger_y=40)
    angry.angrify()
    pass


if __name__ == '__main__':
    main(sys.argv)
