import sys
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow, QMessageBox,
                             QPlainTextEdit, QTextEdit, QTextBrowser, QVBoxLayout, QWidget)

# ----- INTERFACE ----- #
class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window_width, self.window_height = 500, 600

        self.setWindowTitle("Note Taker")
        self.setGeometry(200, 200, self.window_width, self.window_height)
        self.cwidget = QWidget()
        self.setCentralWidget(self.cwidget)
        self.vlayout = QVBoxLayout(self.cwidget)

        self.logic = Logic(self)
        self.about = About()

        self.setup_menu()
        self.setup_ui()

    # Menu setup (toolbar, actions etc.)
    def setup_menu(self):
        self.file_menu = self.menuBar().addMenu("File")
        
        self.save_action = QAction("Save file", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.logic.save_file)
        self.file_menu.addAction(self.save_action)

        self.load_action = QAction("Load file", self)
        self.load_action.setShortcut("Ctrl+L")
        self.load_action.triggered.connect(self.logic.load_file)
        self.file_menu.addAction(self.load_action)

        self.edit_menu = self.menuBar().addMenu("Edit")

        self.prefaction = QAction("Preferences", self)
        self.prefaction.setShortcut("Ctrl + P")
        self.prefaction.triggered.connect(self.show_preferences)
        self.edit_menu.addAction(self.prefaction)

        self.help_menu = self.menuBar().addMenu("Help")

        self.docaction = QAction("Documentation (WIP)", self)
        self.help_menu.addAction(self.docaction)

        self.about_action = QAction("About Note Taker")
        self.about_action.triggered.connect(self.show_about)
        self.help_menu.addAction(self.about_action)

    # Text box setup
    def setup_ui(self):
        self.tbox = QTextEdit()
        self.tbox.setPlaceholderText("Enter text here")
        self.vlayout.addWidget(self.tbox)

    # Trigger show preferences
    def show_preferences(self):
        self.preferences_window = Preferences(self.window_width)
        self.preferences_window.show()
        
    # Trigger show version
    def show_about(self):
        self.about.show()


# --- Preferences window --- #
class Preferences(QWidget):
    def __init__(self, width):
        super().__init__()

        self.width = width

        self.setWindowTitle("Preferences")
        self.setFixedSize(400, 400)
        vlayout = QVBoxLayout()

        widthbox = QPlainTextEdit()
        widthbox.setPlainText("Work in Progress")
        vlayout.addWidget(widthbox)

        self.setLayout(vlayout)
        
# --- Version and credits window --- #
class About(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Note Taker by citizen")
        self.setFixedSize(400, 200)
        vlayout = QVBoxLayout()

        info = QTextBrowser()
        info.setFrameStyle(0)
        info.setHtml(f"""
        <h3>Note Taker v0.2_b by citizen</h3>
        <p>Github: <a href="https://github.com/TheCitizenOne">https://github.com/TheCitizenOne</p>
        <p>Lemmy: <a href="https://lemmy.world/">https://lemmy.world/</p>
        """)
        info.setReadOnly(True)
        info.setOpenExternalLinks(True)
        vlayout.addWidget(info)

        self.setLayout(vlayout)


# ----- LOGIC ----- #
class Logic:
    def __init__(self, interface):
        self.interface = interface
    
    # File saving
    def save_file(self):
        opts = QFileDialog.Options()
        fname, _ = QFileDialog.getSaveFileName(self.interface,"Save File", "", "Text Files (*.txt);;All Files (*)", options=opts)
        
        if fname:
            try:
                with open(fname, 'w') as file:
                    file.write(self.interface.tbox.toPlainText())
            except Exception as e:
                QMessageBox.critical(self.interface, "Error", f"Could not save file: {e}")

    # File loading
    def load_file(self):
        opts = QFileDialog.Options()
        fname, _ = QFileDialog.getOpenFileName(self.interface, "Open File", "", "Text Files (*.txt);;All Files (*)", options=opts)
        
        if fname:
            try:
                with open(fname, 'r') as file:
                    self.interface.tbox.setText(file.read())
            except Exception as e:
                QMessageBox.critical(self.interface, "Error", f"Could not load file: {e}")

        
# ----- Init program ----- #
app = QApplication(sys.argv)
window = Interface()
window.show()
sys.exit(app.exec_())