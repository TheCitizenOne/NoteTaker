from libs import Qt
from logic import AppConfig, App


# Main interface
class Interface(Qt.MainWindow):
    def __init__(self):
        super().__init__()

        self.appconf = AppConfig()

        self.winwidth = self.appconf.config['window']['width']
        self.winheight = self.appconf.config['window']['height']
        self.cfont = self.appconf.get_font()

        self.setWindowTitle("Note Taker")
        self.setGeometry(200, 200, self.winwidth, self.winheight)
        self.cwidget = Qt.Widget()
        self.setCentralWidget(self.cwidget)
        self.vlayout = Qt.VBoxLayout(self.cwidget)

        self.logic = App(self)
        self.preferences = Preferences(self)
        self.about = About()

        self.setup_menu()
        self.setup_ui()

    # Menu setup (toolbar, actions etc.)
    def setup_menu(self):
        self.file_menu = self.menuBar().addMenu("File")
        self.file_menu.setAcceptDrops(True)

        self.save_action = Qt.Action("Save file", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.logic.save_file)
        self.file_menu.addAction(self.save_action)

        self.load_action = Qt.Action("Load file", self)
        self.load_action.setShortcut("Ctrl+L")
        self.load_action.triggered.connect(self.logic.load_file)
        self.file_menu.addAction(self.load_action)

        self.edit_menu = self.menuBar().addMenu("Edit")

        self.prefaction = Qt.Action("Preferences", self)
        self.prefaction.setShortcut("Ctrl + P")
        self.prefaction.triggered.connect(self.show_preferences)
        self.edit_menu.addAction(self.prefaction)

        self.help_menu = self.menuBar().addMenu("Help")

        self.docaction = Qt.Action("Documentation (WIP)", self)
        self.help_menu.addAction(self.docaction)

        self.about_action = Qt.Action("About Note Taker")
        self.about_action.triggered.connect(self.show_about)
        self.help_menu.addAction(self.about_action)

    # Text box setup
    def setup_ui(self):
        self.tbox = Qt.TextEdit()
        self.tbox.setFont(self.cfont)
        self.tbox.setPlaceholderText("Enter text here")
        self.vlayout.addWidget(self.tbox)

    # Trigger show preferences
    def show_preferences(self):
        self.preferences.show()

    # Trigger show version
    def show_about(self):
        self.about.show()


# --- Preferences window --- #
class Preferences(Qt.Widget):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface

        self.setWindowTitle("Preferences")
        self.setFixedSize(400, 300)

        # Main (vertical) layout
        vertical_layout = Qt.VBoxLayout()
        vertical_layout.setContentsMargins(20, 20, 0, 0)

        # Form layout
        form_layout = Qt.FormLayout()
        form_layout.setSpacing(10)

        title = Qt.Label("Preferences")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.widthbox = Qt.LineEdit()
        self.widthbox.setFixedSize(50, 25)
        self.widthbox.setText(str(self.interface.winwidth))

        self.heightbox = Qt.LineEdit()
        self.heightbox.setFixedSize(50, 25)
        self.heightbox.setText(str(self.interface.winheight))

        self.fontbutton = Qt.PushButton()
        self.update_font_button()
        self.fontbutton.setFixedSize(200, 25)
        self.fontbutton.clicked.connect(self.open_font_dialog)

        form_layout.addRow(title)
        form_layout.addItem(Qt.SpacerItem(0, 5))
        form_layout.addRow("Starting Width: ", self.widthbox)
        form_layout.addRow("Starting Height: ", self.heightbox)
        form_layout.addRow("Font: ", self.fontbutton)

        vertical_layout.addLayout(form_layout)
        vertical_layout.addStretch()

        # Horizontal layout
        horizontal_layout = Qt.HBoxLayout()

        self.applybutton = Qt.PushButton("Apply")
        self.applybutton.clicked.connect(self.apply_changes)

        self.okbutton = Qt.PushButton("Close")
        self.okbutton.clicked.connect(self.close)

        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.applybutton)
        horizontal_layout.addWidget(self.okbutton)
        horizontal_layout.addItem(Qt.SpacerItem(20, 60))

        vertical_layout.addLayout(horizontal_layout)
        self.setLayout(vertical_layout)

    def update_font_button(self):
        font_name = f"{self.interface.cfont.family()}"

        if self.interface.cfont.bold():
            font_name += " Bold"
        if self.interface.cfont.italic():
            font_name += " Italic"
        if self.interface.cfont.underline():
            font_name += " Underline"

        font_name += f": {self.interface.cfont.pointSize()}pt"

        self.fontbutton.setText(font_name)

    def open_font_dialog(self):
        font, ok = Qt.FontDialog.getFont(self.interface.cfont, self)
        if ok:
            self.interface.cfont = font
            self.interface.tbox.setFont(self.interface.cfont)
            self.update_font_button()
            self.fontbutton.adjustSize()

    def apply_changes(self):
        try:
            width = int(self.widthbox.text())
            height = int(self.heightbox.text())

            self.interface.appconf.config['window']['width'] = width
            self.interface.appconf.config['window']['height'] = height
            self.interface.appconf.set_font(self.interface.cfont)

            self.interface.appconf.save_config()

            Qt.MessageBox.information(
                self,
                "Applied",
                "Preferences saved successfully!"
                )
        except ValueError:
            Qt.MessageBox.critical(
                self,
                "Error",
                "Please enter valid numbers."
                )


# --- Version and credits window --- #
class About(Qt.Widget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Note Taker by citizen")
        self.setFixedSize(450, 400)
        vlayout = Qt.VBoxLayout()

        info = Qt.TextBrowser()
        info.setFrameStyle(0)
        info_html = """
        <h3>Note Taker v0.3_a by citizen</h3>
        <p>Github: <a href="https://github.com/communotron">
        https://github.com/communotron</a></p>
        <p>Lemmy: <a href="https://lemmy.world/u/the_citizen">
        https://lemmy.world/u/the_citizen</a></p>
        """
        info.setHtml(info_html)

        info.setReadOnly(True)
        info.setOpenExternalLinks(True)
        vlayout.addWidget(info)

        changelog = Qt.TextEdit()
        changelog.setFrameStyle(1)
        changelog.setText("""Note Taker v0.3_a CHANGELOG:

        1-) Made build system for installation.
        2-) Added preferences system for make UI more user-friendly.
        3-) Logic and interface has been separated.
        4-) Created config file for store user preferences.
        5-) Created libs.py for store and manage all libraries from one place.
        6-) Made a place for changelog in about window.
        7-) Opitimizations and bug fix.
        """)

        changelog.setReadOnly(True)
        vlayout.addWidget(changelog)

        self.setLayout(vlayout)
