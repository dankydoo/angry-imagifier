import sys

from util.angryimage import AngryImage


def main(args):
    angry = AngryImage('tom.jpeg', max_anger_x=10, max_anger_y=5, frame_count=3, frame_delay=20)
    angry.angrify()


if __name__ == '__main__':
    main(sys.argv)
