from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)

from app.gui.dashboard import Dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CivilFlow AI")
        self.resize(1200, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        title = QLabel("CivilFlow AI")
        title.setStyleSheet(
            "font-size:28px;"
            "font-weight:bold;"
            "padding:10px;"
        )

        layout.addWidget(title)

        self.dashboard = Dashboard()
        layout.addWidget(self.dashboard)

        central_widget.setLayout(layout)