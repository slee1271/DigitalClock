import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock") 
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                    "color: rgb(0, 255, 0);")
        self.setStyleSheet("background-color: black;")

        # Attempt to load the font
        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        if font_id == -1:
            print("Failed to load font. Using default font.")
            font_family = "Arial"  # Fallback system font
        else:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if not font_families:
                print("No font families found. Using default font.")
                font_family = "Arial"  # Fallback system font
            else:
                font_family = font_families[0]

        # Apply the loaded or fallback font
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()


    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())