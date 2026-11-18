from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel
)


class TopBar(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("TopBar")
        self.setFixedHeight(70)

        self.setup_ui()

    def setup_ui(self):

        layout = QHBoxLayout(self)
        layout.setContentsMargins(25, 10, 25, 10)

        self.page_title = QLabel("Accueil")
        self.page_title.setObjectName("PageTitle")

        self.status = QLabel("●  Système prêt")
        self.status.setStyleSheet(
            "color: #34D399; font-size: 12px;"
        )

        layout.addWidget(self.page_title)
        layout.addStretch()
        layout.addWidget(self.status)

    def set_title(self, title):

        self.page_title.setText(title)