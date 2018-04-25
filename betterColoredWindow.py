#Maia Reynolds
#4/25/18
#betterColoredWindow.py - improving colorChangeWindow program

from ggame import *
from random import randint

color=[Color(0xFF0000,1),Color(0x00FF00,1),Color(0x0000FF,1)]
def mouseClick(event):
    num=randint(1,3)
    Sprite(RectangleAsset(1200,800,LineStyle(1,color[num-1]),color[num-1]))

App().listenMouseEvent("click",mouseClick)
App().run()