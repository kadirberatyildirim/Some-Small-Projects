#!/usr/bin/env python

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
import sys
from UIWindow import Ui_MainWindow
import mass, simulation

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.masses = [mass.Mass([800, 50], [10, 0], "Planet"), mass.Mass([700, 450], [0, -10], "Meteor")]
        
        self.setupUi(self)
        
        self.show()
        
    def startSimulate(self):
        simulation.simulate(self.backgroundPicture, self.masses)
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())