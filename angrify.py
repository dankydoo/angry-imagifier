import sys

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFormLayout, QLabel, QFileDialog

from util.angryimage import AngryImage


def main(args):
    app = QApplication(sys.argv)
    layout = QFormLayout()

    widget = QWidget()
    widget.resize(320, 240)
    widget.setWindowTitle('this working?')
    widget.setLayout(layout)

    dialog = QFileDialog()
    file_name = None
    if dialog.exec():
        file_name = dialog.selectedFiles()

        movie = QMovie(file_name[0])
        label = QLabel()
        label.setMovie(movie)
        layout.addWidget(label)
        movie.start()

    l2 = QLabel()
    layout.addWidget(l2)
    l2.setText('testing?')

    widget.show()

    sys.exit(app.exec_())

    angry = AngryImage('tom.jpeg', max_anger_x=10, max_anger_y=5, frame_count=3, frame_delay=20)
    angry.angrify()


if __name__ == '__main__':
    main(sys.argv)
