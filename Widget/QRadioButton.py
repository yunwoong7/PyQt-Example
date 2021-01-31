import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__appname__ = "QRadioButton Widget"

class QRadioButtonWidgetForm(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle(__appname__)

        self.rb_1 = QRadioButton("Radio Button #1")
        self.rb_2 = QRadioButton("Radio Button #2")
        self.rb_3 = QRadioButton("Radio Button #3")
        self.rb_4 = QRadioButton("Radio Button #4")
        self.rb_5 = QRadioButton("Radio Button #5")

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout.addWidget(self.rb_1)
        self.layout.addWidget(self.rb_2)
        self.layout.addWidget(self.rb_3)
        self.layout.addWidget(self.rb_4)
        self.layout.addWidget(self.rb_5)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QRadioButtonWidgetForm()
    form.show()
    exit(app.exec_())