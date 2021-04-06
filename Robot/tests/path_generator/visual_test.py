"""
This creates a visual interface to test the math we use on the Path class
"""



import pygame
import math
import time


def get_distance(xy1, xy2):
    return round(math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2), 1)    

def get_angle(xy1, xy2, xy3):
    # v1_x, v1_y = xy1[0], xy1[1]
    # v2_x, v2_y = xy3[0], xy3[1]

    v1_x, v1_y = xy1[0] - xy2[0], xy1[1] - xy2[1]
    v2_x, v2_y = xy3[0] - xy2[0], xy3[1] - xy2[1]

    dot_product = v1_x * v2_x + v1_y * v2_y
    try:
        heading = math.acos((dot_product / (math.sqrt(v1_x**2 + v1_y**2) * math.sqrt(v2_x**2 + v2_y**2)))) * 180/math.pi 
    except ValueError: # 0 division error
        heading = 0

    x = v1_x * v2_y - v1_y * v2_x
    if x < 0:
        heading = -(180 - heading) 
    else:
        heading = 180 - heading

    return round(heading)
    

def set_path(coordenates):
    path = []
    for i in range(len(coordenates) - 1):
        path.append(get_distance(coordenates[i], coordenates[i+1]))
        if i < len(coordenates) - 2:
            path.append(get_angle(coordenates[i], coordenates[i+1], coordenates[i+2]))

    return path


print(set_path([[0,0], [4,5], [6,2], [7,8]]))
pygame.init()
screen = pygame.display.set_mode([500,500])

running = True
center = [screen.get_width()/2, 500 - screen.get_height()/2]
v1_xy = [1, screen.get_height()/2 - 30]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0,0,255), v1_xy, center)
    pygame.draw.line(screen, (0,0,255), center, [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])

    print("V1(" + str(v1_xy[0]) + "," + str(500 - v1_xy[1]) + ")",
            "V2(" + str(pygame.mouse.get_pos()[0]) + ", " + str(500 - pygame.mouse.get_pos()[1]) + ")" , 
            "Center: " + str(center),
            "--@:", get_angle([v1_xy[0], 500 - v1_xy[1]], center,[pygame.mouse.get_pos()[0], 500 - pygame.mouse.get_pos()[1]]))
            
    pygame.display.flip()
        