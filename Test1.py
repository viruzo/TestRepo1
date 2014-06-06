import sys
from PyQt5 import QtWidgets


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)

        form1 = QtWidgets.QMainWindow()
        form1.show()

        sys.exit(app.exec_())
    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
