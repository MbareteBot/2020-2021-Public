# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 575)
        MainWindow.setMinimumSize(QtCore.QSize(1147, 575))
        MainWindow.setMaximumSize(QtCore.QSize(1147, 575))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1147, 580))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopBar = QtWidgets.QFrame(self.centralwidget)
        self.TopBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.TopBar.setStyleSheet("background-color: #1C1D20;")
        self.TopBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopBar.setLineWidth(0)
        self.TopBar.setObjectName("TopBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TopBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ToggleFrame = QtWidgets.QFrame(self.TopBar)
        self.ToggleFrame.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ToggleFrame.setStyleSheet("")
        self.ToggleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToggleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToggleFrame.setObjectName("ToggleFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ToggleFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_ToggleMenu = QtWidgets.QPushButton(self.ToggleFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_ToggleMenu.sizePolicy().hasHeightForWidth())
        self.Btn_ToggleMenu.setSizePolicy(sizePolicy)
        self.Btn_ToggleMenu.setStyleSheet("QPushButton {\n"
                                          "    image: url(:/img/img/menu.png);\n"
                                          "    border: 0px solid;\n"
                                          "    color: white\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(70,70,70);\n"
                                          "}")
        self.Btn_ToggleMenu.setText("")
        self.Btn_ToggleMenu.setIconSize(QtCore.QSize(16, 16))
        self.Btn_ToggleMenu.setDefault(False)
        self.Btn_ToggleMenu.setObjectName("Btn_ToggleMenu")
        self.verticalLayout_2.addWidget(self.Btn_ToggleMenu)
        self.horizontalLayout.addWidget(self.ToggleFrame)
        self.TitleBar = QtWidgets.QFrame(self.TopBar)
        self.TitleBar.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.TitleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBar.setObjectName("TitleBar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.TitleBar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout.addWidget(self.TitleBar, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.TopBar)
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LeftBar = QtWidgets.QFrame(self.MainFrame)
        self.LeftBar.setMinimumSize(QtCore.QSize(60, 0))
        self.LeftBar.setMaximumSize(QtCore.QSize(60, 16777215))
        self.LeftBar.setStyleSheet("\n"
                                   "background-color: rgb(28, 29, 32);")
        self.LeftBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftBar.setLineWidth(0)
        self.LeftBar.setObjectName("LeftBar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.LeftBar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Btn_LeftFrame = QtWidgets.QFrame(self.LeftBar)
        self.Btn_LeftFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.Btn_LeftFrame.setStyleSheet("background-color: #1C1D20;")
        self.Btn_LeftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Btn_LeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Btn_LeftFrame.setLineWidth(0)
        self.Btn_LeftFrame.setObjectName("Btn_LeftFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Btn_LeftFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_pathCreator = QtWidgets.QPushButton(self.Btn_LeftFrame)
        self.Btn_pathCreator.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_pathCreator.setStyleSheet("QPushButton {\n"
                                           "    color: white;\n"
                                           "    image: url(:/img/img/rayo.png);\n"
                                           "    border: 0px solid;\n"
                                           "    \n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(70, 70, 70);\n"
                                           "}\n"
                                           "")
        self.Btn_pathCreator.setText("")
        self.Btn_pathCreator.setObjectName("Btn_pathCreator")
        self.verticalLayout_4.addWidget(self.Btn_pathCreator)
        self.Btn_graphs = QtWidgets.QPushButton(self.Btn_LeftFrame)
        self.Btn_graphs.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_graphs.setStyleSheet("QPushButton {\n"
                                      "    image: url(:/img/img/grafico-circular.png);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(70, 70, 70);\n"
                                      "}\n"
                                      "")
        self.Btn_graphs.setText("")
        self.Btn_graphs.setObjectName("Btn_graphs")
        self.verticalLayout_4.addWidget(self.Btn_graphs)
        self.Btn_timer = QtWidgets.QPushButton(self.Btn_LeftFrame)
        self.Btn_timer.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_timer.setStyleSheet("QPushButton {\n"
                                     "    image: url(:/img/img/reloj-de-pared.png);\n"
                                     "    border: 0px solid;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(70, 70, 70);\n"
                                     "}")
        self.Btn_timer.setText("")
        self.Btn_timer.setObjectName("Btn_timer")
        self.verticalLayout_4.addWidget(self.Btn_timer)
        self.verticalLayout_3.addWidget(
            self.Btn_LeftFrame, 0, QtCore.Qt.AlignTop)
        self.Btn_settings = QtWidgets.QPushButton(self.LeftBar)
        self.Btn_settings.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_settings.setStyleSheet("QPushButton {\n"
                                        "    color: white;\n"
                                        "    image: url(:/img/img/configuraciones.png);\n"
                                        "    border: 0px solid;\n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(70, 70, 70);\n"
                                        "}\n"
                                        "")
        self.Btn_settings.setText("")
        self.Btn_settings.setObjectName("Btn_settings")
        self.verticalLayout_3.addWidget(self.Btn_settings)
        self.horizontalLayout_2.addWidget(self.LeftBar)
        self.ContentFrame = QtWidgets.QFrame(self.MainFrame)
        self.ContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContentFrame.setObjectName("ContentFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ContentFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.ContentFrame)
        self.stackedWidget.setStyleSheet("background-color: rgb(57,57,57)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Frame_matDesigner = QtWidgets.QWidget()
        self.Frame_matDesigner.setObjectName("Frame_matDesigner")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Frame_matDesigner)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.configBar = QtWidgets.QFrame(self.Frame_matDesigner)
        self.configBar.setMinimumSize(QtCore.QSize(0, 50))
        self.configBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.configBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configBar.setObjectName("configBar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.configBar)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Btn_square = QtWidgets.QPushButton(self.configBar)
        self.Btn_square.setMinimumSize(QtCore.QSize(40, 40))
        self.Btn_square.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Btn_square.setStyleSheet(
            "image: url(:/img/img/dotted-square.png);")
        self.Btn_square.setText("")
        self.Btn_square.setObjectName("Btn_square")
        self.horizontalLayout_7.addWidget(self.Btn_square)
        self.Btn_straightLine = QtWidgets.QPushButton(self.configBar)
        self.Btn_straightLine.setMinimumSize(QtCore.QSize(40, 40))
        self.Btn_straightLine.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Btn_straightLine.setStyleSheet(
            "image: url(:/img/img/pencil.png);")
        self.Btn_straightLine.setText("")
        self.Btn_straightLine.setObjectName("Btn_straightLine")
        self.horizontalLayout_7.addWidget(self.Btn_straightLine)
        self.Btn_colorPick = QtWidgets.QPushButton(self.configBar)
        self.Btn_colorPick.setMinimumSize(QtCore.QSize(40, 40))
        self.Btn_colorPick.setMaximumSize(QtCore.QSize(40, 16777215))
        self.Btn_colorPick.setStyleSheet(
            "image: url(:/img/img/drop-silhouette.png);")
        self.Btn_colorPick.setText("")
        self.Btn_colorPick.setObjectName("Btn_colorPick")
        self.horizontalLayout_7.addWidget(self.Btn_colorPick)
        self.verticalLayout_5.addWidget(
            self.configBar, 0, QtCore.Qt.AlignHCenter)
        self.mats = QtWidgets.QStackedWidget(self.Frame_matDesigner)
        self.mats.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mats.setStyleSheet("border-top: 2px solid rgb(70,70,70);")
        self.mats.setObjectName("mats")
        self.Frame_mat_replay = QtWidgets.QWidget()
        self.Frame_mat_replay.setAutoFillBackground(False)
        self.Frame_mat_replay.setStyleSheet("border-image: url(:/img/img/pista_replay_img.jpg);\n"
                                            "\n"
                                            "")
        self.Frame_mat_replay.setObjectName("Frame_mat_replay")
        self.mats.addWidget(self.Frame_mat_replay)
        self.verticalLayout_5.addWidget(self.mats)
        self.stackedWidget.addWidget(self.Frame_matDesigner)
        self.Frame_graphMaker = QtWidgets.QWidget()
        self.Frame_graphMaker.setObjectName("Frame_graphMaker")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Frame_graphMaker)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Frame_settings = QtWidgets.QFrame(self.Frame_graphMaker)
        self.Frame_settings.setStyleSheet("\n"
                                          "")
        self.Frame_settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_settings.setObjectName("Frame_settings")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Frame_settings)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_4.addWidget(self.Frame_settings)
        self.stackedWidget.addWidget(self.Frame_graphMaker)
        self.Frame_timer = QtWidgets.QWidget()
        self.Frame_timer.setObjectName("Frame_timer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Frame_timer)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Timer_Frame = QtWidgets.QFrame(self.Frame_timer)
        self.Timer_Frame.setMaximumSize(QtCore.QSize(500, 400))
        self.Timer_Frame.setStyleSheet("background-color: rgb(70,70,70)")
        self.Timer_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Timer_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Timer_Frame.setObjectName("Timer_Frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Timer_Frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_2 = QtWidgets.QFrame(self.Timer_Frame)
        self.frame_2.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.TimerNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.TimerNumber.setMinimumSize(QtCore.QSize(0, 300))
        self.TimerNumber.setObjectName("TimerNumber")
        self.verticalLayout_6.addWidget(self.TimerNumber)
        self.TimerBtns_Frame = QtWidgets.QFrame(self.frame_2)
        self.TimerBtns_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.TimerBtns_Frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TimerBtns_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimerBtns_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimerBtns_Frame.setObjectName("TimerBtns_Frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.TimerBtns_Frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.Btn_startTimer = QtWidgets.QPushButton(self.TimerBtns_Frame)
        self.Btn_startTimer.setMinimumSize(QtCore.QSize(150, 40))
        self.Btn_startTimer.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Btn_startTimer.setStyleSheet(
            "image: url(:/img/img/flecha-correcta.png);")
        self.Btn_startTimer.setText("")
        self.Btn_startTimer.setObjectName("Btn_startTimer")
        self.horizontalLayout_10.addWidget(self.Btn_startTimer)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.Btn_stopTimer = QtWidgets.QPushButton(self.TimerBtns_Frame)
        self.Btn_stopTimer.setMinimumSize(QtCore.QSize(150, 40))
        self.Btn_stopTimer.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Btn_stopTimer.setStyleSheet("image: url(:/img/img/detener.png);")
        self.Btn_stopTimer.setText("")
        self.Btn_stopTimer.setObjectName("Btn_stopTimer")
        self.horizontalLayout_10.addWidget(self.Btn_stopTimer)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.TimerBtns_Frame)
        self.horizontalLayout_9.addWidget(self.frame_2)
        self.horizontalLayout_6.addWidget(self.Timer_Frame)
        self.stackedWidget.addWidget(self.Frame_timer)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.ContentFrame)
        self.verticalLayout.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1147, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menuBar)
        self.menuEditar.setObjectName("menuEditar")
        MainWindow.setMenuBar(self.menuBar)
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionDeshacer = QtWidgets.QAction(MainWindow)
        self.actionDeshacer.setObjectName("actionDeshacer")
        self.actionGenerar_Codigo = QtWidgets.QAction(MainWindow)
        self.actionGenerar_Codigo.setObjectName("actionGenerar_Codigo")
        self.actionTomar_Captura = QtWidgets.QAction(MainWindow)
        self.actionTomar_Captura.setObjectName("actionTomar_Captura")
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addAction(self.actionTomar_Captura)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionGenerar_Codigo)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuEditar.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.mats.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # SETS UP THE DRAWING EFFECT WHEN CLICKING ON THE MATS
        self.Frame_mat_replay.mousePressEvent = self.mousePressEvent
        self.Frame_mat_replay.paintEvent = self.paintEvent
        self.Frame_mat_replay.mouseMoveEvent = self.mouseMoveEvent
        self.Frame_mat_replay.mouseReleaseEvent = self.mouseReleaseEvent

        # MENU BAR
        self.actionGuardar.triggered.connect(self.savePath)
        self.actionDeshacer.triggered.connect(self.goBack)
        self.actionAbrir.triggered.connect(self.openExistingPath)
        self.actionTomar_Captura.triggered.connect(self.saveCapture)
        self.actionGenerar_Codigo.triggered.connect(self.generateCode)

        # CREATING BUTTONS FUNCTIONALIY

        # LEFT BAR BUTTONS
        self.Btn_timer.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.Frame_timer))
        self.Btn_graphs.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.Frame_graphMaker))
        self.Btn_pathCreator.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.Frame_matDesigner))

        # FRAME MAT DESIGNER
        self.Btn_square.clicked.connect(self.activateRectDrawing)
        self.Btn_square.setShortcut("Alt+1")
        self.Btn_straightLine.clicked.connect(self.activateLineDrawing)
        self.Btn_straightLine.setShortcut("Alt+2")
        self.Btn_colorPick.clicked.connect(self.colorPicker)

        # FRAME TIMER
        self.timer = QtCore.QTimer()
        self.curr_time = QtCore.QTime(00, 00, 00)
        self.timer.timeout.connect(self.showTimer)
        self.timer.start(10)
        self.TimerNumber.display("00:00")

        self.Btn_startTimer.clicked.connect(self.playTimer)
        self.Btn_stopTimer.clicked.connect(self.stopTimer)

        self.pressedBtn = "PAUSE"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mbarete"))
        self.TimerNumber.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>zxZ</p></body></html>"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionDeshacer.setText(_translate("MainWindow", "Deshacer"))
        self.actionDeshacer.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionGenerar_Codigo.setText(
            _translate("MainWindow", "Generar Codigo"))
        self.actionGenerar_Codigo.setShortcut(
            _translate("MainWindow", "Ctrl+Shift+D"))
        self.actionTomar_Captura.setText(
            _translate("MainWindow", "Tomar Captura"))
        self.actionTomar_Captura.setShortcut(
            _translate("MainWindow", "Ctrl+Shift+C"))