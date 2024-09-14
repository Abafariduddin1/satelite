import pgzrun
import random

WIDTH=700
HEIGHT=500
TITLE="Sequence"

storesattelite=[]
sattelitepos=0
lines=[]
def on_mouse_down(pos): 
    global sattelitepos
    if storesattelite[sattelitepos].collidepoint(pos):
        lines.append((storesattelite[sattelitepos].pos, storesattelite[sattelitepos+1].pos))
        sattelitepos=sattelitepos+1



def drawsattelite():
    for i in range(8):
        x=random.randint(50,600)
        y=random.randint(50,400)
        actor1 = Actor("satalite.png")
        actor1.pos=(x,y)
        storesattelite.append(actor1)



def draw():
    screen.blit("bg.png", (0,0))
    labels = 1
    for i in storesattelite:
        i.draw()
        screen.draw.text(str(labels),(i.x,i.y+20),color="white",fontsize=25)
        labels=labels+1
    for i in lines:
        print(i)    

 




drawsattelite()
pgzrun.go()