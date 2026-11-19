DARK_STYLE = """
QWidget {
    background-color: #0B1020;
    color: #E5E7EB;
    font-family: "Segoe UI";
    font-size: 10pt;
}

QMainWindow {
    background-color: #0B1020;
}

QFrame#sidebar {
    background-color: #080D19;
    border-right: 1px solid #202A40;
}

QLabel#logoLabel {
    color: #FFFFFF;
    font-size: 21pt;
    font-weight: bold;
}

QLabel#pageTitle {
    color: #FFFFFF;
    font-size: 23pt;
    font-weight: bold;
}

QLabel#sectionTitle {
    color: #F1F5F9;
    font-size: 13pt;
    font-weight: bold;
}

QLabel#mutedText,
QLabel#sidebarSection {
    color: #94A3B8;
}

QLabel#sidebarSection {
    font-size: 9pt;
    font-weight: bold;
}

QLabel#welcomeTitle {
    color: white;
    font-size: 19pt;
    font-weight: bold;
}

QLabel#welcomeDescription {
    color: #CBD5E1;
    font-size: 10pt;
}

QLabel#featureNumber {
    color: #A78BFA;
    font-size: 16pt;
    font-weight: bold;
}

QLabel#featureTitle {
    color: #F8FAFC;
    font-size: 12pt;
    font-weight: bold;
}

QLabel#errorMessage {
    color: #F87171;
    font-weight: bold;
}

QLabel#statusBadge {
    color: #C4B5FD;
    background-color: #29204A;
    border: 1px solid #49367D;
    border-radius: 8px;
    padding: 7px 12px;
}

QLabel#graphPlaceholder {
    color: #94A3B8;
    background-color: #0B1020;
    border: 1px dashed #39445B;
    border-radius: 10px;
    padding: 15px;
}

QFrame#contentCard,
QFrame#featureCard {
    background-color: #111B2E;
    border: 1px solid #202A40;
    border-radius: 13px;
}

QFrame#welcomeCard {
    background-color: #211A42;
    border: 1px solid #49367D;
    border-radius: 15px;
}

QPushButton {
    background-color: #202B42;
    color: #E5E7EB;
    border: 1px solid #34415B;
    border-radius: 8px;
    padding: 9px 14px;
}

QPushButton:hover {
    background-color: #303D58;
}

QPushButton:disabled {
    color: #64748B;
    background-color: #172033;
    border-color: #263247;
}

QPushButton#primaryButton {
    background-color: #7047EB;
    color: white;
    border: none;
    font-weight: bold;
    border-radius: 9px;
}

QPushButton#primaryButton:hover {
    background-color: #825FF3;
}

QPushButton#navButton {
    text-align: left;
    background-color: transparent;
    color: #AAB5C8;
    border: none;
    padding: 12px;
    border-radius: 8px;
}

QPushButton#navButton:hover {
    background-color: #172033;
    color: white;
}

QPushButton#navButton:checked {
    background-color: #29204A;
    color: #C4B5FD;
    border-left: 3px solid #8B5CF6;
}

QLineEdit,
QTextEdit,
QComboBox {
    background-color: #0B1324;
    color: #E5E7EB;
    border: 1px solid #34415B;
    border-radius: 8px;
    padding: 9px;
    selection-background-color: #7047EB;
}

QLineEdit:focus,
QTextEdit:focus,
QComboBox:focus {
    border: 1px solid #8B5CF6;
}

QComboBox QAbstractItemView {
    background-color: #111B2E;
    color: #E5E7EB;
    selection-background-color: #7047EB;
}

QTabWidget::pane {
    border: 1px solid #202A40;
    border-radius: 9px;
    background-color: #111B2E;
}

QTabBar::tab {
    background-color: #111B2E;
    color: #94A3B8;
    padding: 10px 17px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
}

QTabBar::tab:selected {
    background-color: #29204A;
    color: #C4B5FD;
}

QStatusBar {
    background-color: #080D19;
    color: #94A3B8;
    border-top: 1px solid #202A40;
}
QWidget#topHeader {
    background-color: #080D19;
    border-bottom: 1px solid #202A40;
}
"""


LIGHT_STYLE = """
QWidget {
    background-color: #F4F6FB;
    color: #1E293B;
    font-family: "Segoe UI";
    font-size: 10pt;
}

QMainWindow {
    background-color: #F4F6FB;
}

QFrame#sidebar {
    background-color: #FFFFFF;
    border-right: 1px solid #E2E8F0;
}

QLabel#logoLabel {
    color: #31205E;
    font-size: 21pt;
    font-weight: bold;
}

QLabel#pageTitle {
    color: #172033;
    font-size: 23pt;
    font-weight: bold;
}

QLabel#sectionTitle {
    color: #243047;
    font-size: 13pt;
    font-weight: bold;
}

QLabel#mutedText,
QLabel#sidebarSection {
    color: #64748B;
}

QLabel#sidebarSection {
    font-size: 9pt;
    font-weight: bold;
}

QLabel#welcomeTitle {
    color: #31205E;
    font-size: 19pt;
    font-weight: bold;
}

QLabel#welcomeDescription {
    color: #475569;
    font-size: 10pt;
}

QLabel#featureNumber {
    color: #7047EB;
    font-size: 16pt;
    font-weight: bold;
}

QLabel#featureTitle {
    color: #243047;
    font-size: 12pt;
    font-weight: bold;
}

QLabel#errorMessage {
    color: #DC2626;
    font-weight: bold;
}

QLabel#statusBadge {
    color: #5B21B6;
    background-color: #EDE9FE;
    border: 1px solid #C4B5FD;
    border-radius: 8px;
    padding: 7px 12px;
}

QLabel#graphPlaceholder {
    color: #64748B;
    background-color: #F8FAFC;
    border: 1px dashed #CBD5E1;
    border-radius: 10px;
    padding: 15px;
}

QFrame#contentCard,
QFrame#featureCard {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 13px;
}

QFrame#welcomeCard {
    background-color: #EDE9FE;
    border: 1px solid #C4B5FD;
    border-radius: 15px;
}

QPushButton {
    background-color: #F1F5F9;
    color: #334155;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 9px 14px;
}

QPushButton:hover {
    background-color: #E2E8F0;
}

QPushButton:disabled {
    color: #94A3B8;
    background-color: #F1F5F9;
}

QPushButton#primaryButton {
    background-color: #7047EB;
    color: white;
    border: none;
    font-weight: bold;
    border-radius: 9px;
}

QPushButton#primaryButton:hover {
    background-color: #825FF3;
}

QPushButton#navButton {
    text-align: left;
    background-color: transparent;
    color: #475569;
    border: none;
    padding: 12px;
    border-radius: 8px;
}

QPushButton#navButton:hover {
    background-color: #F1F5F9;
    color: #31205E;
}

QPushButton#navButton:checked {
    background-color: #EDE9FE;
    color: #5B21B6;
    border-left: 3px solid #7047EB;
}

QLineEdit,
QTextEdit,
QComboBox {
    background-color: #FFFFFF;
    color: #1E293B;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 9px;
    selection-background-color: #7047EB;
}

QLineEdit:focus,
QTextEdit:focus,
QComboBox:focus {
    border: 1px solid #7047EB;
}

QComboBox QAbstractItemView {
    background-color: #FFFFFF;
    color: #1E293B;
    selection-background-color: #EDE9FE;
}

QTabWidget::pane {
    border: 1px solid #E2E8F0;
    border-radius: 9px;
    background-color: #FFFFFF;
}

QTabBar::tab {
    background-color: #F1F5F9;
    color: #64748B;
    padding: 10px 17px;
    border-top-left-radius: 7px;
    border-top-right-radius: 7px;
}

QTabBar::tab:selected {
    background-color: #EDE9FE;
    color: #5B21B6;
}

QStatusBar {
    background-color: #FFFFFF;
    color: #64748B;
    border-top: 1px solid #E2E8F0;
}
QWidget#topHeader {
    background-color: #FFFFFF;
    border-bottom: 1px solid #E2E8F0;
}
"""


def get_stylesheet(theme):

    if theme == "light":
        return LIGHT_STYLE

    return DARK_STYLE