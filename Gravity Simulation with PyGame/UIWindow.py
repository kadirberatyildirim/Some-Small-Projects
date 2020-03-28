# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 630)
        MainWindow.setWindowTitle("Gravity Simulation")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.choicesScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.choicesScrollArea.sizePolicy().hasHeightForWidth())
        self.choicesScrollArea.setSizePolicy(sizePolicy)
        self.choicesScrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.choicesScrollArea.setWidgetResizable(True)
        self.choicesScrollArea.setObjectName("choicesScrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1165, 514))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.welcomeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.welcomeLabel.setText("Welcome to the gravity simulation created by Hign!")
        self.verticalLayout_2.addWidget(self.welcomeLabel)
        
        self.backgroundHLayout = QtWidgets.QHBoxLayout()
        self.backgroundHLayout.setObjectName("backgroundHLayout")
        
        self.backgroundLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.backgroundLabel.setText("Background :")
        self.backgroundHLayout.addWidget(self.backgroundLabel)
        
        self.backgroundRadioButton1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.backgroundRadioButton1.setMinimumSize(QtCore.QSize(0, 100))
        self.backgroundRadioButton1.setText("")
        self.backgroundRadioButton1.setObjectName("backgroundRadioButton1")
        self.backgroundRadioButton1.setChecked(True)
        self.backgroundRadioButton1.clicked.connect(self.changeBackgroundPicture)
        self.backgroundHLayout.addWidget(self.backgroundRadioButton1)
        
        self.backgroundRadioButton2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.backgroundRadioButton2.setText("")
        self.backgroundRadioButton2.setObjectName("backgroundRadioButton2")
        self.backgroundRadioButton2.clicked.connect(self.changeBackgroundPicture)
        self.backgroundHLayout.addWidget(self.backgroundRadioButton2)
        
        self.backgroundRadioButton3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.backgroundRadioButton3.setText("")
        self.backgroundRadioButton3.setObjectName("backgroundRadioButton3")
        self.backgroundRadioButton3.clicked.connect(self.changeBackgroundPicture)
        self.backgroundHLayout.addWidget(self.backgroundRadioButton3)
        
        self.backgroundRadioButton4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.backgroundRadioButton4.setText("")
        self.backgroundRadioButton4.setObjectName("backgroundRadioButton4")
        self.backgroundRadioButton4.clicked.connect(self.changeBackgroundPicture)
        self.backgroundHLayout.addWidget(self.backgroundRadioButton4)
        
        self.backgroundRadioButton5 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.backgroundRadioButton5.setText("")
        self.backgroundRadioButton5.setObjectName("backgroundRadioButton5")
        self.backgroundRadioButton5.clicked.connect(self.changeBackgroundPicture)
        self.backgroundHLayout.addWidget(self.backgroundRadioButton5)
        
        self.verticalLayout_2.addLayout(self.backgroundHLayout)
        
        self.massGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.massGroupBox.sizePolicy().hasHeightForWidth())
        self.massGroupBox.setSizePolicy(sizePolicy)
        self.massGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.massGroupBox.setObjectName("massGroupBox")
        self.massGroupBox.setTitle("Mass Initial Properties")
        #Frame has a grid layout! Frame is inside group box!
        self.gridLayout_3 = QtWidgets.QGridLayout(self.massGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.massGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        
        self.xLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy)
        self.xLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.xLabel.setObjectName("xLabel")
        self.xLabel.setText("x")
        self.gridLayout.addWidget(self.xLabel, 0, 1, 1, 2)
        
        self.yLabel = QtWidgets.QLabel(self.frame)
        self.yLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.yLabel.setObjectName("yLabel")
        self.yLabel.setText("y")
        self.gridLayout.addWidget(self.yLabel, 0, 3, 1, 1)
        
        self.scaleLabel = QtWidgets.QLabel(self.frame)
        self.scaleLabel.setObjectName("scaleLabel")
        self.scaleLabel.setText("Scale :")
        self.scaleLabel.setToolTip("How big the image will be drawn on the simulation")
        self.scaleLabel.setToolTipDuration(1000)
        self.gridLayout.addWidget(self.scaleLabel, 1, 0, 1, 1)
        
        self.ScaleXSpinBox = QtWidgets.QSpinBox(self.frame)
        self.ScaleXSpinBox.setObjectName("ScaleXSpinBox")
        self.ScaleXSpinBox.setRange(5, 30)
        self.gridLayout.addWidget(self.ScaleXSpinBox, 1, 1, 1, 2)
        
        self.ScaleYSpinBox = QtWidgets.QSpinBox(self.frame)
        self.ScaleYSpinBox.setObjectName("ScaleYSpinBox")
        self.ScaleYSpinBox.setRange(5, 30)
        self.gridLayout.addWidget(self.ScaleYSpinBox, 1, 3, 1, 1)
        
        self.positionLabel = QtWidgets.QLabel(self.frame)
        self.positionLabel.setObjectName("positionLabel")
        self.positionLabel.setText("Position :")
        self.positionLabel.setToolTip("(0,0) is top-left! x increases towards right-side, y increases towards bottom.")
        self.positionLabel.setToolTipDuration(1000)
        self.gridLayout.addWidget(self.positionLabel, 2, 0, 1, 1)
        
        self.PositionXSpinBox = QtWidgets.QSpinBox(self.frame)
        self.PositionXSpinBox.setObjectName("PositionXSpinBox")
        self.PositionXSpinBox.setRange(10, 1600)
        self.gridLayout.addWidget(self.PositionXSpinBox, 2, 1, 1, 2)
        
        self.PositionYSpinBox = QtWidgets.QSpinBox(self.frame)
        self.PositionYSpinBox.setObjectName("PositionYSpinBox")
        self.PositionYSpinBox.setRange(10, 900)
        self.gridLayout.addWidget(self.PositionYSpinBox, 2, 3, 1, 1)
        
        self.velocityLabel = QtWidgets.QLabel(self.frame)
        self.velocityLabel.setObjectName("velocityLabel")
        self.velocityLabel.setText("Velocity :")
        self.velocityLabel.setToolTip("Pixels per Frame! So -10 for x equals 10 pixels towards left-side per frame!")
        self.velocityLabel.setToolTipDuration(1000)
        self.gridLayout.addWidget(self.velocityLabel, 3, 0, 1, 1)
        
        self.velocityXSpinBox = QtWidgets.QSpinBox(self.frame)
        self.velocityXSpinBox.setObjectName("velocityXSpinBox")
        self.gridLayout.addWidget(self.velocityXSpinBox, 3, 1, 1, 2)
        
        self.velocityYSpinBox = QtWidgets.QSpinBox(self.frame)
        self.velocityYSpinBox.setObjectName("velocityYSpinBox")
        self.gridLayout.addWidget(self.velocityYSpinBox, 3, 3, 1, 1)
        
        self.meteorRadioButton = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meteorRadioButton.sizePolicy().hasHeightForWidth())
        self.meteorRadioButton.setSizePolicy(sizePolicy)
        self.meteorRadioButton.setObjectName("meteorRadioButton")
        self.meteorRadioButton.setText("Meteor")
        self.meteorRadioButton.toggled.connect(self.updateMassPictures)
        self.gridLayout.addWidget(self.meteorRadioButton, 4, 3, 1, 1)
        
        self.planetRadioButton = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planetRadioButton.sizePolicy().hasHeightForWidth())
        self.planetRadioButton.setSizePolicy(sizePolicy)
        self.planetRadioButton.setObjectName("planetRadioButton")
        self.planetRadioButton.setText("Planet")
        self.planetRadioButton.setChecked(True)
        self.planetRadioButton.toggled.connect(self.updateMassPictures)
        self.gridLayout.addWidget(self.planetRadioButton, 4, 1, 1, 2)
        
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        #frame_2 contains radio buttons for mass pictures!
        self.frame_2 = QtWidgets.QFrame(self.massGroupBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.massPictureRadioButton1 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton1.setText("")
        self.massPictureRadioButton1.setObjectName("massPictureRadioButton1")
        self.massPictureRadioButton1.setChecked(True)
        self.massPictureRadioButton1.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton1, 0, 0, 1, 1)
        
        self.massPictureRadioButton2 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton2.setText("")
        self.massPictureRadioButton2.setObjectName("massPictureRadioButton2")
        self.massPictureRadioButton2.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton2, 0, 1, 1, 1)
        
        self.massPictureRadioButton3 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton3.setText("")
        self.massPictureRadioButton3.setObjectName("massPictureRadioButton3")
        self.massPictureRadioButton3.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton3, 0, 2, 1, 1)
        
        self.massPictureRadioButton4 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton4.setText("")
        self.massPictureRadioButton4.setObjectName("massPictureRadioButton4")
        self.massPictureRadioButton4.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton4, 0, 3, 1, 1)
        
        self.massPictureRadioButton5 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton5.setText("")
        self.massPictureRadioButton5.setObjectName("massPictureRadioButton5")
        self.massPictureRadioButton5.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton5, 1, 0, 1, 1)
        
        self.massPictureRadioButton6 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton6.setText("")
        self.massPictureRadioButton6.setObjectName("massPictureRadioButton6")
        self.massPictureRadioButton6.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton6, 1, 1, 1, 1)
        
        self.massPictureRadioButton7 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton7.setText("")
        self.massPictureRadioButton7.setObjectName("massPictureRadioButton7")
        self.massPictureRadioButton7.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton7, 1, 2, 1, 1)
        
        self.massPictureRadioButton8 = QtWidgets.QRadioButton(self.frame_2)
        self.massPictureRadioButton8.setText("")
        self.massPictureRadioButton8.setObjectName("massPictureRadioButton8")
        self.massPictureRadioButton8.clicked.connect(self.changeMassPicture)
        self.gridLayout_2.addWidget(self.massPictureRadioButton8, 1, 3, 1, 1)
        
        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 2)
        
        spacerItem = QtWidgets.QSpacerItem(928, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 2)
        
        self.addMassPushButton = QtWidgets.QPushButton(self.massGroupBox)
        self.addMassPushButton.setObjectName("addMassPushButton")
        self.addMassPushButton.setText("Add Mass")
        self.addMassPushButton.clicked.connect(self.addMass)
        self.gridLayout_3.addWidget(self.addMassPushButton, 1, 2, 1, 1)
        
        self.verticalLayout_2.addWidget(self.massGroupBox)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        spacerItem1 = QtWidgets.QSpacerItem(908, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        
        self.simulateButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.simulateButton.setText("Simulate")
        self.simulateButton.setObjectName("simulateButton")
        self.simulateButton.clicked.connect(self.startSimulate)
        self.horizontalLayout.addWidget(self.simulateButton)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        
        self.choicesScrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.verticalLayout.addWidget(self.choicesScrollArea)
        
        self.currentMassesScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentMassesScrollArea.sizePolicy().hasHeightForWidth())
        self.currentMassesScrollArea.setSizePolicy(sizePolicy)
        self.currentMassesScrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.currentMassesScrollArea.setWidgetResizable(True)
        self.currentMassesScrollArea.setObjectName("currentMassesScrollArea")
        
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1165, 106))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.currentMassesPlainText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.currentMassesPlainText.setReadOnly(True)
        self.currentMassesPlainText.setObjectName("currentMassesPlainText")
        self.gridLayout_4.addWidget(self.currentMassesPlainText, 0, 0, 2, 1)
        
        self.removeMassSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.removeMassSpinBox.setObjectName("removeMassSpinBox")
        self.removeMassSpinBox.setRange(1, 50)
        self.gridLayout_4.addWidget(self.removeMassSpinBox, 0, 1, 1, 1)
        
        self.removeMassPushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.removeMassPushButton.setObjectName("removeMassPushButton")
        self.removeMassPushButton.setText("Remove Mass")
        self.removeMassPushButton.clicked.connect(self.removeMass)
        self.gridLayout_4.addWidget(self.removeMassPushButton, 1, 1, 1, 1)
        
        self.currentMassesScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        
        self.verticalLayout.addWidget(self.currentMassesScrollArea)
        
        MainWindow.setCentralWidget(self.centralwidget)
    
        self.startUpJobs()
    
    def startUpJobs(self):
        buttons1 = [self.backgroundRadioButton1, self.backgroundRadioButton2, self.backgroundRadioButton3, self.backgroundRadioButton4, self.backgroundRadioButton5]
        for i in list(range(0, 5)):
            buttons1[i].setIcon(QtGui.QIcon("Images/" + "Space" + str(i) + ".jpg"))
            buttons1[i].setIconSize(QtCore.QSize(160, 90))
            
        buttons = [self.massPictureRadioButton1, self.massPictureRadioButton2, self.massPictureRadioButton3, self.massPictureRadioButton4, self.massPictureRadioButton5, self.massPictureRadioButton6, self.massPictureRadioButton7, self.massPictureRadioButton8]
        for i in list(range(1, 9)):
            buttons[i-1].setIcon(QtGui.QIcon("Images/" + "Planet" + str(i) + ".png"))
            buttons[i-1].setIconSize(QtCore.QSize(70, 70))
            
        for i in range(len(self.masses)):
            self.currentMassesPlainText.insertPlainText(str(i+1) + "-->" + self.masses[i].massInfo() + "\n")
            
        self.backgroundPicture = 0
        self.massPicture = 0
        
    def updateMassPictures(self):
        buttons = [self.massPictureRadioButton1, self.massPictureRadioButton2, self.massPictureRadioButton3, self.massPictureRadioButton4, self.massPictureRadioButton5, self.massPictureRadioButton6, self.massPictureRadioButton7, self.massPictureRadioButton8]
        sender = self.sender()
        for i in list(range(1, 9)):
            buttons[i-1].setIcon(QtGui.QIcon("Images/" + sender.text() + str(i) + ".png"))
            buttons[i-1].setIconSize(QtCore.QSize(70, 70))
        
    def changeMassPicture(self):
        sender2 = self.sender()
        self.massPicture = int(sender2.objectName()[-1]) - 1
        
    def changeBackgroundPicture(self):
        sender3 = self.sender()
        self.backgroundPicture = int(sender3.objectName()[-1]) - 1
        
    def addMass(self):
        scale = [self.ScaleXSpinBox.value(), self.ScaleYSpinBox.value()]
        initialCoords = [self.PositionXSpinBox.value(), self.PositionYSpinBox.value()]
        velocity = [self.velocityXSpinBox.value(), self.velocityYSpinBox.value()]
        massType = "Planet" if self.planetRadioButton.isChecked() else "Meteor"
        picture = self.massPicture
        self.masses.append(mass.Mass(initialCoords, velocity, massType, scale, picture))
        self.updateCurrentMasses()
        
    def removeMass(self):
        self.masses.pop(self.removeMassSpinBox.value() - 1)
        self.updateCurrentMasses()
        
    def updateCurrentMasses(self):
        self.currentMassesPlainText.clear()
        for i in range(len(self.masses)):
            self.currentMassesPlainText.insertPlainText(str(i+1) + "-->" + self.masses[i].massInfo() + "\n")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    