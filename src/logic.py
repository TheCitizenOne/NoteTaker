from libs import os, yaml, Qt


# Config system
class AppConfig:
    def __init__(self):
        home_dir = os.path.expanduser("~")
        self.config_dir = os.path.join(home_dir, '.config', 'notetaker')
        self.config_file = os.path.join(self.config_dir, 'config.yaml')

        self.config = {
            'window': {
                'width': 500,
                'height': 600
            },
            'font': {
                'family': "System",
                'size': 10,
                'bold': False,
                'italic': False,
                'underline': False
            }
        }

        os.makedirs(self.config_dir, exist_ok=True)

        if os.path.exists(self.config_file):
            self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as conf:
                loaded_config = yaml.safe_load(conf)
                if loaded_config:
                    self.config = loaded_config
        except Exception as err:
            print(f"Error loading config: {err}")

    def save_config(self):
        try:
            with open(self.config_file, 'w') as conf:
                yaml.dump(self.config, conf)
        except Exception as err:
            print(f"Error saving config: {err}")

    def get_font(self):
        font = Qt.Font()
        font.setFamily(self.config['font']['family'])
        font.setPointSize(self.config['font']['size'])
        font.setBold(self.config['font']['bold'])
        font.setItalic(self.config['font']['italic'])
        font.setUnderline(self.config['font']['underline'])
        return font

    def set_font(self, font):
        self.config['font']['family'] = font.family()
        self.config['font']['size'] = font.pointSize()
        self.config['font']['bold'] = font.bold()
        self.config['font']['italic'] = font.italic()
        self.config['font']['underline'] = font.underline()


# Application logic
class App:
    def __init__(self, interface):
        self.interface = interface
        self.file_filter = "Text Files (*.txt);;All Files (*)"

    # File saving
    def save_file(self):
        opts = Qt.FileDialog.Options()
        fname, _ = Qt.FileDialog.getSaveFileName(
            self.interface,
            "Save File",
            "",
            self.file_filter,
            options=opts
            )

        if fname:
            try:
                with open(fname, 'w') as file:
                    file.write(self.interface.tbox.toPlainText())
            except Exception as e:
                Qt.MessageBox.critical(
                    self.interface,
                    "Error",
                    f"Could not save file: {e}"
                    )

    # File loading
    def load_file(self):
        opts = Qt.FileDialog.Options()
        fname, _ = Qt.FileDialog.getOpenFileName(
            self.interface,
            "Open File",
            "",
            self.file_filter,
            options=opts
            )

        if fname:
            try:
                with open(fname, 'r') as file:
                    self.interface.tbox.setText(file.read())
            except Exception as e:
                Qt.MessageBox.critical(
                    self.interface,
                    "Error",
                    f"Could not load file: {e}"
                    )
