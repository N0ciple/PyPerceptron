import numpy as np
import pygame

def f(point):
    return 0.2*point.x >= point.y -0.2


class MyPoint :
    def __init__(self,pt_x,pt_y):
        self.x = pt_x
        self.y = pt_y
        self.arr = np.ones((2,1))
        self.arr[0] = self.x
        self.arr[1] = self.y
        if  f(self) :
            self.label = 1
        else:
            self.label = -1

    def convCord(self,size):
        return [int((self.x + 1 )*size[0]/2), int((-self.y + 1 )*size[1]/2)]

    def draw(self,my_screen,size,circle_rad):
        if self.label==1:
            pygame.draw.circle(my_screen, [0, 255, 0], self.convCord(size), circle_rad)

        else:
            pygame.draw.circle(my_screen, [255, 0, 0], self.convCord(size), circle_rad)

    def drawPred(self, my_screen, size, circle_rad,pred):

        if self.label == pred:
            pygame.draw.circle(my_screen, [0, 0, 255], self.convCord(size), circle_rad+5)

        else:
            pygame.draw.circle(my_screen, [0, 0, 0], self.convCord(size), circle_rad+5)

        self.draw(my_screen, size, circle_rad)



