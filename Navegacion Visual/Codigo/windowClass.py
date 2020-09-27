from imagesCreator import *
import math


win_leftPadding = 5
win_rightPadding = 5

win_topPadding = 50
win_bottomPadding = 5

win_paddingOffset = 5




class WindowManager():

	def __init__(self):

		self.surface = ""
		self.virtualRobotRotations = []
		self.virtualRobot_angle = 0
		self.robotOffset_X = []
		self.robotOffset_Y = []
		self.robotPosX = []
		self.robotPosY = []

		self.lines_color = (125,125,125)

		self.win_width = 0
		self.win_height = 0

		self.mouse_pos = 0





	def setWindow(self, win_width, win_height):

		self.surface = pygame.display.set_mode((win_width, win_height))

		self.win_width = win_width
		self.win_height = win_height

		self.Imgs = ImageManager(self.win_width, self.win_height)



	def setTitle(self, title):

		pygame.display.set_caption(title);


	def drawButtons(self, Xpos, Ypos):


		for i in range(len(self.Imgs.img_buttons)):
			self.surface.blit(self.Imgs.img_buttons[i], (Xpos[i], Ypos[i]))


	def drawBackground(self):

		self.surface.fill((230,230,230))

		self.surface.blit(self.Imgs.img_mats_resized[2],(win_leftPadding + win_rightPadding, win_topPadding))


	def setText(self, text, size, font, color, posX, posY):

		font_object = pygame.font.SysFont(font, size)
		text_surface = font_object.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.center = posX, posY
		self.surface.blit(text_surface, text_rect)


	def drawGrid(self, horizontal_amount, vertical_amount):

		x_pos = 0
		y_pos = 50

		for i in range(0,horizontal_amount):
			pygame.draw.line(self.surface, (0,0,0), (0,y_pos),(self.mat_size[0],y_pos))
			y_pos += self.mat_size[1]/horizontl_amount

		for i in range(0,vertical_amount):
			pygame.draw.line(self.surface, (0,0,0), (x_pos,100),(x_pos,self.mat_size[1]))
			x_pos += self.mat_size[0]/ vertical_amount
 

		
	def setVirtualRobotRotation(self):



		self.robotPosX.append(self.mouse_pos[0])
		self.robotPosY.append(self.mouse_pos[1])




		img_robot_copy = pygame.transform.rotate(self.Imgs.img_robot, self.virtualRobot_angle)


		self.robotOffset_X.append(img_robot_copy.get_width()/2)
		self.robotOffset_Y.append(img_robot_copy.get_height()/2)

		if len(self.virtualRobotRotations) < 1:

			self.virtualRobotRotations.append(0)

		else:
			
			self.virtualRobotRotations.append(self.virtualRobot_angle)

			self.virtualRobotRotations[-2] = self.virtualRobotRotations[-1]


		print("X,Y:", self.robotPosX, self.robotPosY)
		print("Angle:", self.virtualRobotRotations)


	def drawRobotPath(self):


		if self.MouseInsideDrawSection():

			self.virtualRobot_angle = ((math.atan2(self.mouse_pos[1] - self.robotPosY[-1], self.mouse_pos[0] - self.robotPosX[-1]) * 180/math.pi) % 360) *-1

		
		img_robot_copy = pygame.transform.rotate(self.Imgs.img_robot, self.virtualRobot_angle)

		self.surface.blit(pygame.transform.rotate(self.Imgs.img_robot, self.virtualRobot_angle), 
			(self.robotPosX[-1] - img_robot_copy.get_width()/2, self.robotPosY[-1] - img_robot_copy.get_height()/2))

		
		for i in range(0, len(self.virtualRobotRotations) -1):
			self.surface.blit(pygame.transform.rotate(self.Imgs.img_robot, self.virtualRobotRotations[i]), 
				(self.robotPosX[i] - self.robotOffset_X[i + 1], self.robotPosY[i] - self.robotOffset_Y[i + 1]))





		pygame.draw.circle(self.surface, self.lines_color,(self.robotPosX[0], self.robotPosY[0]), 15)	

		for pos in range(len(self.robotPosX)-1):

			pygame.draw.line(self.surface, self.lines_color, (self.robotPosX[pos],self.robotPosY[pos]),
												(self.robotPosX[pos+1],self.robotPosY[pos+1]),10)


		for pos in range(len(self.robotPosX) - 1):
			pygame.draw.circle(self.surface, self.lines_color, (self.robotPosX[pos + 1], self.robotPosY[pos + 1]), 15)


			self.setText("R" + str(pos + 1), 15, "arial", (0,0,0), self.robotPosX[pos + 1], self.robotPosY[pos + 1])


		
	def draw(self, img, xpos, ypos):

		self.surface.blit(img, (xpos, ypos))




	def setMousePos(self, pos):

		self.mouse_pos = pos



	def MouseInsideDrawSection(self):

		if self.mouse_pos[0] > win_leftPadding + win_paddingOffset and self.mouse_pos[0] < self.win_width - (win_rightPadding + win_paddingOffset + 3) and self.mouse_pos[1] > win_topPadding + win_paddingOffset and self.mouse_pos[1] < self.win_height - 15:
			return True

		
