import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


class QpushButtonWidgetForm(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        # 배치될 위젯 변수 선언
        self.btn_push = QPushButton()
        self.edt_number = QLineEdit()
        # 레이아웃 선언 및 Form Widget에 설정
        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.setLayout(self.layout)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QPushButton Shortcut")
        self.click_cnt = 0
        self.edt_number.setText(str(self.click_cnt))
        self.layout.addWidget(self.edt_number)
        # 라벨1의 설정 및 레이아웃 추가
        self.btn_push.setText("더하기 단축키(Alt + F7)")
        self.btn_push.pressed.connect(self.pb1Pressed)
        self.btn_push.setShortcut("Alt+F1")
        self.layout.addWidget(self.btn_push)

    def pb1Pressed(self):
        self.click_cnt += 1
        self.edt_number.setText(str(self.click_cnt))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QpushButtonWidgetForm()
    form.show()
    exit(app.exec_())