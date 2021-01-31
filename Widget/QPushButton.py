import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__appname__ = "QPushButton Widget"

class QPushButtonWidgetForm(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle(__appname__)
        self.btn_push = QPushButton()
        self.edt_number = QLineEdit()
        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(self.layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QPushButton Shortcut")
        self.click_cnt = 0
        self.edt_number.setText(str(self.click_cnt))

        self.btn_push.setText("더하기 단축키(Alt + F7)")
        self.btn_push.pressed.connect(self.buttonClicked)
        self.btn_push.setShortcut("Alt+F7")

        self.layout.addWidget(self.edt_number)
        self.layout.addWidget(self.btn_push)

    def buttonClicked(self):
        self.click_cnt += 1
        self.edt_number.setText(str(self.click_cnt))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QPushButtonWidgetForm()
    form.show()
    exit(app.exec_())