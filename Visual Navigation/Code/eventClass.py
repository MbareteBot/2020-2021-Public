import pygame, os, math
from PIL import Image

from pygame.locals import *
from windowClass import *
from statsCreator import *




class EventManager():

	def __init__(self):

		self.surface = ""
		
		self.screenDrawing = True

		self.mat_path = []

		self.line_posX = []
		self.line_posY = []

		self.changeDirectory = True
		self.directory_path = ""

		self.win_width = 0
		self.win_height = 0

	def getPressedButton(self, buttons_xpos, buttons_ypos):


		img_buttons_rect = []

		for size in range(0,3):
			img_buttons_rect.append([buttons_xpos[size], buttons_ypos[size], MainScreen.Imgs.img_buttons_size[size][0], MainScreen.Imgs.img_buttons_size[size][1]])

		for button in range(0,3):

			if pygame.Rect(img_buttons_rect[button]).collidepoint(self.eventSource):


				return button




	def setRobotPath(self):


		
		realRobot_angle = 0

		if len(self.line_posY) > 1:

			Vector1_relX = self.line_posX[-2] - self.line_posX[-1]
			Vector1_relY = self.line_posY[-2] - self.line_posY[-1]

			Vector2_relX = self.eventSource[0] - self.line_posX[-1]
			Vector2_relY = self.eventSource[1] - self.line_posY[-1]

			cross_product = Vector1_relX  * Vector2_relY - Vector1_relY * Vector2_relX

			Angle_Vectors_Cos_first = (((Vector1_relX  * Vector2_relX) + (Vector1_relY * Vector2_relY) ))

			Angle_Vectors_Cos_sec = Angle_Vectors_Cos_first / (math.sqrt(Vector1_relX**2 + Vector1_relY**2) * math.sqrt(Vector2_relX**2 + Vector2_relY**2))
			Angle_Vectors = math.acos(Angle_Vectors_Cos_sec)


			if cross_product < 0:
				Angle_Vectors = (180 - (Angle_Vectors * (180/math.pi))) * -1
			else:
				Angle_Vectors = 180 - (Angle_Vectors * (180/math.pi))


			if Angle_Vectors > 85 and Angle_Vectors < 95:
				realRobot_angle = 90

			elif Angle_Vectors < -85 and Angle_Vectors > -95:
				realRobot_angle = -90
			
			else:
				realRobot_angle = round(Angle_Vectors)

			self.mat_path.append(realRobot_angle)


		if len(self.line_posX) > 0:
			self.mat_path.append(round(math.sqrt( (((self.line_posX[-1] - self.eventSource[0])/(self.win_width/200))**2) + (((self.line_posY[-1] - self.eventSource[1])/((self.win_height - 70) / 130))**2) ),1))
			
		
		self.line_posX.append(self.eventSource[0])
		self.line_posY.append(self.eventSource[1])

		
		if self.changeDirectory:

			os.chdir("../..")
			
			directory_path = os.chdir(os.path.join(os.getcwd(), "MicroPython/Datos-Navegacion Visual"))
			self.changeDirectory = False

		print("Save in: ", self.directory_path)


		with open("RobotValues.txt","w") as Movement_Values: 

			for item in self.mat_path:
				Movement_Values.write("%s\n" % item)


		RobotValues_txt = []

		with open("RobotValues.txt","r") as f:

			for line in f:

				RobotValues_txt_Check = line[:-1]

				RobotValues_txt.append(RobotValues_txt_Check)

			print("Valores Utilizados:", RobotValues_txt)




	def runStats(self):
	
		myGraphs = graphMaker(2,3)

		mydata = [1,2,3,4,5]
		mylegends = ["Tema1", "Tema2","Tema3", "Tema4","Tema5"]

		myGraphs.plotGraph(mydata, mydata, "Progreso en Misiones", 0, 0)
		myGraphs.pieGraph(mydata, mylegends, 1,0)

		myGraphs.pieGraph(mydata, mylegends, 0,1)
		myGraphs.plotGraph(mydata, mydata, None, 1,1)

		#img_mat_user = pygame.image.save(self.surface, "img_mat_user.png")
		img_mat_user = Image.open("img_mat_user.png")
		img_mat_user.thumbnail((2000, 1300))
		myGraphs.showImage(img_mat_user,"Pista", 0,2)
		myGraphs.pieGraph(mydata, mylegends, 1,2)

		myGraphs.showGraphs()	



	def setEventSource(self, source):

		self.eventSource = source


	def setWindowReference(self, win_width, win_height):

		self.win_width = win_width
		self.win_height = win_height
