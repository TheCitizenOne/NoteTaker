import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMenu, QMessageBox, QPushButton, QTextEdit, QToolBar, QVBoxLayout, QWidget)


# ----- Main system----- #
class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Note Taker")
        self.setGeometry(200, 200, 500, 600)
        
        self.cwidget = QWidget()
        self.setCentralWidget(self.cwidget)
        self.vlayout = QVBoxLayout(self.cwidget)

        self.tbox = QTextEdit()
        self.tbox.setPlaceholderText("Enter text here")
        self.vlayout.addWidget(self.tbox)

        self.menu_setup()

    # Menu setup (buttons, toolbar etc.)
    def menu_setup(self):
        menu1 = QMenu()
        menu1.addAction("Save File", self.save_file)
        menu1.addAction("Load File", self.load_file)

        menu2 = QMenu()
        menu2.addAction("Preferences", self.show_preferences)
        
        menu3 = QMenu()
        menu3.addAction("Note Taker Version", self.show_version)
        menu3.addAction("Documentation (WIP)")
        
        tbar_button1 = QPushButton("File")
        tbar_button1.setFlat(True)
        tbar_button1.setMaximumWidth(50)
        tbar_button1.setMenu(menu1)

        tbar_button2 = QPushButton("Edit")
        tbar_button2.setFlat(True)
        tbar_button2.setMaximumWidth(50)
        tbar_button2.setMenu(menu2)
        
        tbar_button3 = QPushButton("About")
        tbar_button3.setFlat(True)
        tbar_button3.setMaximumWidth(60)
        tbar_button3.setMenu(menu3)
        
        toolbar = QToolBar()
        toolbar.addWidget(tbar_button1)
        toolbar.addWidget(tbar_button2)
        toolbar.addWidget(tbar_button3)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

    # File saving
    def save_file(self):
        opts = QFileDialog.Options()
        fname, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=opts)
        if fname:
            try:
                with open(fname, 'w') as file:
                    file.write(self.tbox.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {e}")

    # File loading
    def load_file(self):
        opts = QFileDialog.Options()
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=opts)
        if fname:
            try:
                with open(fname, 'r') as file:
                    self.tbox.setText(file.read())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load file: {e}")

    # Trigger show preferences
    def show_preferences(self):
        self.preferences_window = Preferences()
        self.preferences_window.show()
        
    # Trigger show version
    def show_version(self):
        self.version_window = Version()
        self.version_window.show()


# ----- Preferences window ----- #
class Preferences(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Preferences")
        self.setFixedSize(400, 400)
        
# ----- Version and credits window ----- #
class Version(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Note Taker Version")
        self.setFixedSize(400, 200)
        
        vlayout = QVBoxLayout()

        information = QTextEdit()
        information.setFrameStyle(0)
        information.setText("Note Taker v0.1_a by citizen" + "\n"*2 + "Github: https://github.com/TheCitizenOne" + "\n" + "Lemmy: https://lemmy.world/u/the_citizen")
        information.setReadOnly(True)
        vlayout.addWidget(information)

        self.setLayout(vlayout)


# ----- Init program ----- #
app = QApplication(sys.argv)
window = Interface()
window.show()
sys.exit(app.exec_())
