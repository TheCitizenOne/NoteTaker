# System
import sys
import os
import yaml

# QtWidgets
from PyQt5 import QtWidgets, QtCore, QtGui


# Qt components
class Qt:
    # Main container
    Application = QtWidgets.QApplication
    MainWindow = QtWidgets.QMainWindow
    Widget = QtWidgets.QWidget
    MessageBox = QtWidgets.QMessageBox

    # Layout
    VBoxLayout = QtWidgets.QVBoxLayout
    HBoxLayout = QtWidgets.QHBoxLayout
    FormLayout = QtWidgets.QFormLayout
    SpacerItem = QtWidgets.QSpacerItem

    # Button + control
    PushButton = QtWidgets.QPushButton

    # Menu
    Menu = QtWidgets.QMenu
    MenuBar = QtWidgets.QMenuBar
    Action = QtWidgets.QAction

    # Text
    Label = QtWidgets.QLabel
    TextEdit = QtWidgets.QTextEdit
    LineEdit = QtWidgets.QLineEdit
    TextBrowser = QtWidgets.QTextBrowser

    # IO
    FileDialog = QtWidgets.QFileDialog
    FontDialog = QtWidgets.QFontDialog

    # Alignment
    AlignTop = QtCore.Qt.AlignTop
    AlignBottom = QtCore.Qt.AlignBottom

    # Font
    Font = QtGui.QFont
    FontDatabase = QtGui.QFontDatabase


# Get platform information
def get_platform():
    if sys.platform.startswith('win'):
        return 'windows'

    elif sys.platform.startswith('darwin'):
        return 'mac'

    else:
        return 'unix/linux'


__all__ = ['sys', 'os', 'yaml', 'Qt', 'get_platform']
