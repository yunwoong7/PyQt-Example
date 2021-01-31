import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__appname__ = "QCheckBox Widget"

class QCheckBoxWidgetForm(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle(__appname__)

        self.cb_1 = QCheckBox("CheckBox #1")
        self.cb_2 = QCheckBox("CheckBox #2")
        self.cb_3 = QCheckBox("CheckBox #3")
        self.cb_4 = QCheckBox("CheckBox #4")
        self.cb_5 = QCheckBox("CheckBox #5")

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout.addWidget(self.cb_1)
        self.layout.addWidget(self.cb_2)
        self.layout.addWidget(self.cb_3)
        self.layout.addWidget(self.cb_4)
        self.layout.addWidget(self.cb_5)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QCheckBoxWidgetForm()
    form.show()
    exit(app.exec_())