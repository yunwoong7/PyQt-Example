import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

__appname__ = "SignalSlot Widget"

class SignalSlotForm(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle(__appname__)
        self.dialog_widget = QDial()
        self.slider_widget = QSlider(Qt.Horizontal)
        self.spinbox_widget = QSpinBox()
        self.setupUI()

    def setupUI(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        self.dialog_widget.valueChanged.connect(self.slider_widget.setValue)
        self.slider_widget.valueChanged.connect(self.dialog_widget.setValue)
        self.slider_widget.valueChanged.connect(self.spinbox_widget.setValue)
        self.spinbox_widget.valueChanged.connect(self.slider_widget.setValue)

        h_layout.addWidget(self.slider_widget)
        h_layout.addWidget(self.spinbox_widget)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.dialog_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = SignalSlotForm()
    form.show()
    exit(app.exec_())