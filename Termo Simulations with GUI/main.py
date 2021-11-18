
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream

from modules.Window import Ui_MainWindow
import modules.breeze_theme #For dark theme

class termo_simulations(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(termo_simulations, self).__init__(parent)
        self.setupUi(self)
        self.link_buttons()
        
    def link_buttons(self):
        self.simulatePushButton.clicked.connect(self.start_simulation_tab1)

    def start_simulation_tab1(self):
        Simulate.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    file = QFile(":/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    MainWindow = QtWidgets.QMainWindow()
    ui = termo_simulations()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
