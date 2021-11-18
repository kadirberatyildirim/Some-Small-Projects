# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from modules.Simulation import Simulate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Int validator for LineEdit widgets
        self.onlyInt = QtGui.QIntValidator()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 880)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Main window layout is grid layout where only tab_widget sits
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        #=======================================================================Tab 1
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #This tab is a grid layout containing 2 plot areas and some lineedit and buttons
        self.tab1GridLayout = QtWidgets.QGridLayout(self.tab)
        self.tab1GridLayout.setObjectName("gridLayout_2")
        #Grid layout contains only vertical layout, where all widgets are in
        self.tab1VerticalLayout = QtWidgets.QVBoxLayout()
        self.tab1VerticalLayout.setObjectName("verticalLayout")
        #Horizontal layout for plot areas
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.simulationFrame = Simulate(50, 0.01)
        self.horizontalLayout_3.addWidget(self.simulationFrame)
        
        self.graphFrame = FigureCanvas(Figure(figsize=(5, 3)))
        self.horizontalLayout_3.addWidget(self.graphFrame)
        
        self.tab1VerticalLayout.addLayout(self.horizontalLayout_3)
        #Horizontal layout for lineedits
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.NLabel = QtWidgets.QLabel("N:")
        self.horizontalLayout.addWidget(self.NLabel)
        
        self.NLineEdit = QtWidgets.QLineEdit(self.tab)
        self.NLineEdit.setObjectName("NLineEdit")
        self.NLineEdit.setValidator(self.onlyInt)
        self.horizontalLayout.addWidget(self.NLineEdit)

        self.radiusLabel = QtWidgets.QLabel("Radius:")
        self.horizontalLayout.addWidget(self.radiusLabel)
        
        self.radiusLineEdit = QtWidgets.QLineEdit(self.tab)
        self.radiusLineEdit.setObjectName("radiusLineEdit")
        self.radiusLineEdit.setValidator(self.onlyInt)
        self.horizontalLayout.addWidget(self.radiusLineEdit)

        self.dtLabel = QtWidgets.QLabel("dt:")
        self.horizontalLayout.addWidget(self.dtLabel)
        
        self.dtLineEdit = QtWidgets.QLineEdit(self.tab)
        self.dtLineEdit.setObjectName("dtLineEdit")
        self.dtLineEdit.setValidator(self.onlyInt)
        self.horizontalLayout.addWidget(self.dtLineEdit)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.tab1VerticalLayout.addLayout(self.horizontalLayout)
        #Horizontal layout for bottom buttons
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        
        self.simulatePushButton = QtWidgets.QPushButton(self.tab)
        self.simulatePushButton.setObjectName("simulatePushButton")
        self.simulatePushButton.clicked.connect(self.start_simulation_tab1)
        self.horizontalLayout_2.addWidget(self.simulatePushButton)
        
        self.tab1VerticalLayout.addLayout(self.horizontalLayout_2)
        
        self.tab1GridLayout.addLayout(self.tab1VerticalLayout, 0, 0, 1, 1)
        #=======================================================================Tab 2
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NLineEdit.setText(_translate("MainWindow", "50"))
        self.NLineEdit.setPlaceholderText(_translate("MainWindow", "# of particles"))
        self.radiusLineEdit.setText(_translate("MainWindow", "0.01"))
        self.radiusLineEdit.setPlaceholderText(_translate("MainWindow", "Radius of particles"))
        self.dtLineEdit.setText(_translate("MainWindow", "0.05"))
        self.dtLineEdit.setPlaceholderText(_translate("MainWindow", "Time delta dt"))
        self.simulatePushButton.setText(_translate("MainWindow", "Simulate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
