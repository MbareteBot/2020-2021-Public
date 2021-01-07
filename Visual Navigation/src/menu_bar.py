from ui_main import *
from mat_designer import matDesignerWidget
from code_editor import *

import os
import pickle


class menuBar(Ui_MainWindow):

    # ASK FOR THE DIRECTORY AND SAVE THE CURRENT PATH (ONLY LINES ARE TAKING INTO ACCOUNG WHEN DEFINIG A "PATH")
    # ALL LINES ARE CONSIDERED AS THE PATH
    def savePath(self):

        realRobotCoordenates = []

        winWidth, winHeight = self.centralwidget.width(), self.centralwidget.height()

        for line in self.clicksPositions:
            realRobotCoordenates.append(
                [round(200/(winWidth/line[0])), round(130/(winHeight/(winHeight-line[1])))])

        path = QtWidgets.QFileDialog.getSaveFileName(
            self.centralwidget, "Guardar Como", os.getcwd(), "Mbarete files (*.mbarete)")
        print(path)
        try:
            with open(path[0], "wb") as file:

                pickle.dump(self.clicksPositions, file)
                pickle.dump(realRobotCoordenates, file)

                print("\n---------------------------------")
                print("Successfully saved binary file")
        except:
            print("Fail to save binary file")

    # OPEN AN EXISTING PATH (*.mbarete) AND DRAW THAT PATH ON THE MAIN FRAME

    def openExistingPath(self):

        path = QtWidgets.QFileDialog.getOpenFileName(
            self.centralwidget, "Select File", os.getcwd(), "Mbarete files (*.mbarete)")
        path_data = []

        try:
            with open(path[0], "rb") as f:
                for _ in range(2):
                    path_data.append(pickle.load(f))

            self.clicksPositions = path_data[0]
            print(self.clicksPositions)
        except:
            print("Fail to open file")

        self.lastPressedBtn = "LINE"
        self.lineDrawing(self.Frame_mat_replay)

    # TAKE A SCREENSHOT

    def saveCapture(self):

        path = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, "Select Directory", os.getcwd(), "Image files (*.png)")
        try:
            screen = QtWidgets.QApplication.primaryScreen()
            screenshot = screen.grabWindow(
                self.stackedWidget.currentWidget().winId())
            screenshot.save(path[0], 'png')
        except:
            print("Fail to save capture")

    def generateCode(self):
        dialog = CodeEditorWindow()
        dialog.show
