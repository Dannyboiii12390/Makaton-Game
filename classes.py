import pygame as py
py.init()
import os
import random

BLACK = (0,0,0)
LIGHT_BLUE = (52, 180, 235)

class Screen: # will be a class for the screen
    def __init__(self, width,height):
        self.width = width
        self.height = height
        
        self.WINDOW = py.display.set_mode((self.width,self.height))
        self.WINDOW.fill((255,255,255))
    
    def setbg(self):
        bg = py.transform.scale(py.image.load(os.path.join('Assets', 'space.png')), (self.width,self.height))
        self.WINDOW.blit(bg,(0,0))

class Box:
    
    def __init__(self,x,y,width,height):
        #self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, WINDOW):
        global BLACK
        bx = py.Rect(self.x, self.y, self.width, self.height)
        self.HB = py.draw.rect(WINDOW.WINDOW, BLACK, bx)

class hitBox(Box):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.numTimesPressed = 0

    def clicked(self):
        self.numTimesPressed += 1
        k = self.numTimesPressed%4
        return k

    def text(self,scr,string,w,h):
        global LIGHT_BLUE
        BOXFONT = py.font.SysFont('helvetica', int((125*scr.width)//(scr.height*1.8)))
        txt = BOXFONT.render(string, True, LIGHT_BLUE)
        width=w+txt.get_width()//2
        height=h+txt.get_height()//2
        scr.WINDOW.blit(txt,(width,height))


class imgBox(Box):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.randImgs()

    def draw(self,scr,k):
        bg = py.transform.scale(py.image.load(os.path.join('Assets', 'Signs',self.randSignList[k])), (self.width,self.height))
        scr.WINDOW.blit(bg,(self.x,self.y))
    
    def randImgs(self):
        signList = os.listdir("C:\Games\Makaton Game revisited\Assets\Signs")
        self.randSignList = []
        while len(self.randSignList) < 4:
            randomSign = random.choice(signList)
            if randomSign in self.randSignList:
                continue
            else:
                self.randSignList.append(randomSign)
        self.correct = self.randSignList[random.randint(0,3)][:-4]

    def checkCorrect(self,k):
        return self.correct == self.randSignList[k][:-4]
        






