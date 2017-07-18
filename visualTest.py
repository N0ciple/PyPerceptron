import pygame, sys
import perceptron
from myPoints import MyPoint
from random import random
import time

pygame.init()
my_perceptron = perceptron.Perceptron(2)
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
circle_rad = 7
screen.fill([255, 255, 255])

mypoint = list()

for i in range(50):
    #x = int(width * random() - width/2)
    #y = int(height * random() - height/2)
    x = random()*2-1
    y = random()*2-1
    pt = MyPoint(x,y)
    pt.draw(screen,size,circle_rad)
    mypoint.append(pt)



for p in mypoint:
    p.drawPred(screen,size,circle_rad,my_perceptron.predict(p.arr))

# Variables for the loop
i=0
prevtime = time.time()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if i < len(mypoint):
        #train on a new point
        my_perceptron.train(mypoint[i])
        i+=1

    else:
        # if all the nodes are processed
        print('DONE')


    for point in mypoint:
        result = my_perceptron.predict(point.arr)
        point.drawPred(screen, size, circle_rad,result)

    # Compute the coeeficient of the line obtained by the perceptron
    # y = a * x + b
    a = -float(my_perceptron.weight[0]) / float(my_perceptron.weight[1])
    b = -float(my_perceptron.weight[2]) / float(my_perceptron.weight[1])


    # Draw the curent classification line
    pt1 = MyPoint(-1, a*-1+b)
    pt2 = MyPoint(1, a*1+b)
    pygame.draw.line(screen,[255,255,0],pt1.convCord(size),pt2.convCord(size),5)


    pygame.display.update()
    screen.fill([255,255,255])
