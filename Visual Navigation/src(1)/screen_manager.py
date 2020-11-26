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
		self.height = height



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

			



	
	def draw(self, element):

		# Draw a button element

		if element.__class__.__name__ == "Button":
			if element.skin_path == None:
				# Button box
				pygame.draw.rect(self.surface, element.bg_color, element.rect)
				# Button caption, draw and center the caption within the button
				self.surface.blit(element.label.surface, (element.label.x, element.label.y))

			
			else:				
				self.surface.blit(element.surface, (element.x, element.y))


		elif element.__class__.__name__ == "Label":
			# Drawing text
			self.surface.blit(element.surface, (element.x, element.y))



		elif element.__class__.__name__ == "Widget":


			if element.skin_path == None:
				pygame.draw.rect(self.surface, element.bg_color, element.surface)
			
			else:				
				self.surface.blit(element.surface, (element.x, element.y))



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


class Label():

	def __init__(self,
					text="Text", 
					position=(0,0), 
					size=20, 
					font='arial', 
					color=(0,0,0),
					skin_path = None,
					bg_color = None,
					dimensions = None):


		self.x, self.y = position
		self.size = size
		self.font_object = pygame.font.SysFont(font, self.size)
		self.surface = self.font_object.render(text, True, color)
		self.rect = self.surface.get_rect()
		self.width, self.height = self.rect.width, self.rect.height
		


		# Centered position of the label within a container




class Button():

	def __init__(self, 
					position, 
					dimensions = None, 
					skin_path = None,
					bg_color = (200,200,200),
					caption = "cta"):


		self.width, self.height = dimensions
		self.x, self.y = position
		self.skin_path = skin_path
		self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

		if self.skin_path == None:
			self.caption = caption
			self.bg_color = bg_color

		else:			
			self.surface = pygame.transform.scale(pygame.image.load(skin_path), (self.width, self.height))
		

		self.hover_effect_enabled = True



		self.label = Label(text=caption, position=(0,0), size=20, font='arial', color=(0,0,0))


		# Coordenates for the center of the button
		self.label.x = self.x + self.width - self.width/2 - self.label.width/2
		self.label.y = (self.y + self.height + self.label.height)/2




	def hover(self):

		if self.hover_effect_enabled:
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				return True
			else:
				return False


			#if self.mouse_collition:
			#	print("collition")
			#	self.graphical_elements[element].surface = pygame.Rect(self.graphical_elements[element].position, (self.graphical_elements[element].width + 5, self.graphical_elements[element].height) )
				

	def clicked(self):

		if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
			return True
		else:
			return False






class Widget():

	def __init__(self,
					position,
					dimensions,
					color=(200,200,200),
					skin_path=None):

		self.x, self.y = position
		self.width, self.height = dimensions
		self.bg_color = color
		self.skin_path = skin_path

		if skin_path == None:
			self.surface = pygame.Rect((self.x, self.y), (self.width, self.height))
			self.bg_color = color

		else:

			if dimensions == None:
				self.surface = pygame.image.load(skin_path) 
			else:
				self.surface = pygame.transform.scale(pygame.image.load(skin_path), dimensions)
		







