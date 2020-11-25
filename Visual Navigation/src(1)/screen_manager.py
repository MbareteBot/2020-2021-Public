import pygame, math
from pygame.locals import MOUSEBUTTONDOWN



class ScreenManager():


	def __init__(self):

		print("Main windows initialized")

		self.surface = None

		self.width = 0
		self.height = 0


		self.graphical_elements = []


		self.mouse_collition = True
		self.active_element = 0



	def setWindow(self, width, height):

		self.surface = pygame.display.set_mode((width, height))

		self.width = width
		self.width = height



	def setTitle(self,title="Window"):
		pygame.display.set_caption(title)



	def setBg(self, img=None, pos = (0,0), color=(200,200,200)):

		if img == None:
			self.surface.fill(color)
		else:
			self.surface.blit(img, pos)






	def update(self):


		# Check for collitions within the mouse and any element from the screen parent(buttons, etc)
		self.mouse_collition = False
		# for element in range(0, len(self.graphical_elements)): 

		# 	if self.graphical_elements[element].surface.collidepoint(pygame.mouse.get_pos()):
		# 		self.mouse_collition = True 
		# 		self.active_element = element


		# 		self.graphical_elements[element].hoverEffect()

		# 		break







		pygame.display.update()

			


	def label(self, text="Text", pos=(0,0), size=20, font='arial', color=(0,0,0)):

		x,y = pos
		font_object = pygame.font.SysFont(font, size)
		text_surface = font_object.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.center = x, y
		self.surface.blit(text_surface, text_rect)


		
	def draw(self, element):


		if element.skin_path == None:
			pygame.draw.rect(self.surface, element.bg_color, element.surface)
			self.label(element.caption, 
						((element.position[0] + element.width)/2, (element.position[1] + element.height)/2)
						)
		
		else:				
			self.surface.blit(element.surface)

#		if element not in self.graphical_elements:
#			self.graphical_elements.append(element)


		#for element in range(0,len(self.graphical_elements)):

		#	if self.graphical_elements[element].skin_path == None:
		#		pygame.draw.rect(self.surface, self.graphical_elements[element].bg_color, self.graphical_elements[element].surface)
		#	else:
		#		self.surface.blit(element.surface, element.position)


#

#	def addGraphicalElement(self, element):

#		self.graphical_elements.append(element)





class Button():

	def __init__(self, 
					position, 
					dimensions = None, 
					skin_path = None,
					bg_color = (200,200,200),
					caption = "cta"):



		self.width, self.height = dimensions
		self.position = position
		self.skin_path = skin_path


		if self.skin_path == None:
			self.surface = pygame.Rect(self.position, (self.width, self.height))
			self.caption = caption
			self.bg_color = bg_color

		else:

			if dimensions == None:
				self.surface = pygame.image.load(skin_path) 
			else:
				self.surface = pygame.transform.scale(pygame.image.load(skin_path), dimensions)
		

		self.hover_effect_enabled = True





	def hover(self):

		if self.hover_effect_enabled:
			if self.surface.collidepoint(pygame.mouse.get_pos()):
				return True
			else:
				return False


			#if self.mouse_collition:
			#	print("collition")
			#	self.graphical_elements[element].surface = pygame.Rect(self.graphical_elements[element].position, (self.graphical_elements[element].width + 5, self.graphical_elements[element].height) )
				

	def clicked(self):

		if self.surface.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
			return True
		else:
			return False


