import pygame, os, math
from PIL import Image

from pygame.locals import *
from window_manager import *
from statsCreator import *


imageManager = (ImageManager(1024, 768))


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

		for size in range(0,len(buttons_xpos) - 1):
			img_buttons_rect.append([buttons_xpos[size], buttons_ypos[size], imageManager.img_buttons_size[size][0], imageManager.img_buttons_size[size][1]])

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
			
			directory_path = os.chdir(os.path.join(os.getcwd(), "MicroPython/src"))
			self.changeDirectory = False



		with open("RobotValues.txt","w") as Movement_Values: 

			for item in self.mat_path:
				Movement_Values.write("%s\n" % item)


		self.robot_movement_data = []



		with open("RobotValues.txt","r") as f:

			for line in f:

				RobotValues_txt_Check = line[:-1]

				self.robot_movement_data.append(RobotValues_txt_Check)





	def runStats(self, screen):
		
		robot_movement_data_id = []



		for element in range(1, len(self.robot_movement_data)):
			self.robot_movement_data.pop(element)
			element += 1
			if element >= len(self.robot_movement_data) - 1:
				break



		for element in range(0, len(self.robot_movement_data)):
			self.robot_movement_data[element] = float(self.robot_movement_data[element])



		for element in range(0, len(self.robot_movement_data)):
			robot_movement_data_id.append("R" + str(element + 1))



		mylegends = ["Tema1", "Tema2","Tema3", "Tema4"]


		pygame.image.save(screen, "img_mat_user.png")



		graphUI = graphMaker(2,3)



		graphUI.barGraph(robot_movement_data_id, self.robot_movement_data, "Progreso en Misiones", 0, 0)
		graphUI.pieGraph((1,2,3,4), mylegends, 1,0)

		graphUI.pieGraph((1,2,3,4), mylegends, 0,1)
		graphUI.plotGraph((1,2,3,4), mylegends, None, 1,1)

		img_mat_user = Image.open("img_mat_user.png")
		img_mat_user.thumbnail((2000, 1300))
		graphUI.showImage(img_mat_user,"Pista", 0,2)
		graphUI.pieGraph((1,2,3,4), mylegends, 1,2)

		graphUI.showGraphs()	



	def setEventSource(self, source):

		self.eventSource = source


	def setWindowReference(self, win_width, win_height):

		self.win_width = win_width
		self.win_height = win_height
