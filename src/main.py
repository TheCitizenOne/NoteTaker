from libs import sys, Qt
from interface import Interface


# Init the program
def main():
    app = Qt.Application(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
