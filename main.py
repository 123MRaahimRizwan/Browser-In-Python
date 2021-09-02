# Importing the libraries.

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Creating the main class.
class MainWindow(QMainWindow):
    # Creating the constructor.
    def __init__(self):
        # Connecting the constructor with this super method.
        super(MainWindow, self).__init__()
        # Creating the browser
        self.browser = QWebEngineView()
        # Setting the home url
        self.browser.setUrl(QUrl("https://google.com"))
        # Adjusting the browser to the center
        self.setCentralWidget(self.browser)
        # Making the window to open at full screen
        self.showMaximized()
        # Creating the toolbar
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

        # Adding back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        tool_bar.addAction(back_btn)

        # Adding forward button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        tool_bar.addAction(forward_btn)

        # Adding reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        tool_bar.addAction(reload_btn)

        # Adding home button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        tool_bar.addAction(home_btn)

        # Adding url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        tool_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Calling the class and executing the above program
app = QApplication(sys.argv)
QApplication.setApplicationName("Google Browser")
window = MainWindow()
app.exec()
