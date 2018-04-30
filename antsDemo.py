#Maia Reynolds
#4/30/18
#antsDemo.py - usings lists with graphics

from ggame import *
from random import randint

ants=10
width=900
height=400

if __name__=="__main__":
    data={}
    data["antList"]=[]

    red=Color(0xFF0000,1)
    ant=CircleAsset(20,LineStyle(1,red),red)

    for i in range(ants):
        data["antList"].append(Sprite(ant,(randint(1,width),randint(1,height))))

App().run(step)