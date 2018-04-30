#Maia Reynolds
#4/30/18
#antsDemo.py - usings lists with graphics

from ggame import *
from random import randint

ants=50
width=900
height=400
#move each ant randomly up/down + left/right
def step():
    for ant in data["antList"]:
        ant.x+=randint(-4,3)
        ant.y+=randint(-4,3)
#putting fire ants randomly onn screen
if __name__=="__main__":
    data={}
    data["antList"]=[]

    red=Color(0xFF0000,1)
    ant=CircleAsset(20,LineStyle(1,red),red)

    for i in range(ants):
        data["antList"].append(Sprite(ant,(randint(1,width),randint(1,height))))

App().run(step)