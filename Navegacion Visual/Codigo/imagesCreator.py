import pygame
import os

dirname = os.path.dirname(__file__)


#pygame.init()


class ImageManager():


	def __init__(self, win_width, win_height):

		self.img_width = round((win_width * 98) / 100)
		self.img_height = round((win_height * 90) / 100)


		self.img_buttons = [pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_refresh.png")),
						pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_stats.png")),
						pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_createFile.png")),
						pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_time.png"))]


		self.img_buttons_size = [self.img_buttons[0].get_rect().size,
							self.img_buttons[1].get_rect().size,
							self.img_buttons[2].get_rect().size]




		self.img_buttons_chrono = [pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_play.png")), 
							pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_stop.png")), 
							pygame.image.load(os.path.join(dirname, "Imagenes/Botones/bt_return.png"))]




		self.img_mats = [pygame.image.load(os.path.join(dirname, "Imagenes/Pistas/pista_cityshaper_img.jpg")), 
					pygame.image.load(os.path.join(dirname, "Imagenes/Pistas/pista_intoorbit_img.jpg")), 
					pygame.image.load(os.path.join(dirname, "Imagenes/Pistas/pista_replay_img.jpg"))]

		self.img_mats_resized = [pygame.transform.scale(self.img_mats[0], (self.img_width, self.img_height)), 
							pygame.transform.scale(self.img_mats[1], (self.img_width, self.img_height)),
							pygame.transform.scale(self.img_mats[2], (self.img_width, self.img_height))]





		self.img_robot = pygame.transform.scale(pygame.image.load(os.path.join(dirname,"Imagenes/robot_img.png")), (85, 90))
		self.img_robot = pygame.transform.rotate(self.img_robot, -90)




	