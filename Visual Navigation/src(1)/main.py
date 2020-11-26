from screen_manager import *
import sys

pygame.init()


screen = ScreenManager()

monitor_width = pygame.display.Info().current_w
monitor_height = pygame.display.Info().current_h
screen.setWindow(round(monitor_width*75/100), round(monitor_height*80/100))
screen.setTitle("Program")




def Buttons():

	btn = Button(position=(50,50), dimensions = (180,130),bg_color = (100,100,100), caption="Click Aqui")
	

	if btn.hover():
		btn.bg_color = (80,80,80)
		pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

	else:
		btn.bg_color = (100,100,100)
		pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


	if btn.clicked():

		if btn.skin_path == None:
			btn.rect.width -= 1
			btn.rect.height -= 1
		else:
			btn.surface = pygame.transform.scale(btn.surface, (btn.width - 1, btn.height - 1))


	screen.draw(btn)










def main():


	clock = pygame.time.Clock()

	lbl = Label("Titulo", (200,200))
	mat_view = Widget((round((screen.width * 1.5)/100), round((screen.height*18)/100)),(round((screen.width * 97)/100), round((screen.height*80)/100)),skin_path = "./img/mats/pista_replay_img.jpg")

	running = True
	while running:

		for event in pygame.event.get():


			if event.type == pygame.QUIT:

				running = False
				sys.exit()



		
		screen.setBg(color=(200,200,200))

		screen.draw(mat_view)
		#Buttons((50,50),"Submit")

	


		screen.update()


		clock.tick(60)




main()

