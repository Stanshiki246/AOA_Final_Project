import pygame
from os import path
from math import ceil
pygame.init()
"""
Name: Stanley Tantysco, Isabella, Alessandro, and Michael Stanley Chinaza
Sorting words from E-book
"""
#Background screen Class object
class BackGround:
    def __init__(self):
        self.width=800
        self.height=600
        self.color=(140,206,239)

#Button Class object
class Button:
    def __init__(self,screen,rectx,recty,width,height,text):
        """Initialize button attributes."""
        self.screen = screen
        self.rectx = rectx
        self.recty = recty

        # Set the dimensions and properties of the button.
        self.width, self.height = width,height
        self.button_color = (0,0,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 50)

        # Build the button's rect object.
        self.rect = pygame.Rect(self.rectx, self.recty, self.width, self.height)

        # The button message only needs to be prepped once.
        self.show_text(text)
    #Text rendering function
    def show_text(self,text):
        """Turn msg into a rendered image, and center text on the button."""
        self.text_rendering = self.font.render(text, True, self.text_color,
            self.button_color)
        self.text_rendering_rectx = self.rectx+15
        self.text_rendering_recty = self.recty+10
        self.text_rendering_rect = (self.text_rendering_rectx,self.text_rendering_recty)
    #Button rendering function
    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_rendering, self.text_rendering_rect)
#Text Class object
class Text:
    def __init__(self,size,name,color,bg_color,rectx,recty,screen):
        self.size=size
        self.name=name
        self.color=color
        self.bg_color=bg_color
        self.rectx=rectx
        self.recty=recty
        self.screen=screen
        self.font="C:\Windows\Fonts\Arial.ttf"
        self.Font=pygame.font.Font(self.font,self.size)
        self.text_rendering=self.Font.render(self.name,True,self.color,self.bg_color)
        self.text_getRect=self.text_rendering.get_rect()
        self.text_getRect.center=(self.rectx,self.recty)
    #Text rendering function
    def DrawText(self):
        self.screen.blit(self.text_rendering,self.text_getRect)
    #Update text function
    def Update(self):
        self.text_rendering=self.Font.render(self.name,True,self.color,self.bg_color)
#E-book Class object
class Book:
    def __init__(self,rectx,recty,screen,name,dict):
        self.width=50
        self.height=50
        self.image=pygame.image.load('book_icon.png')
        self.image=pygame.transform.scale(self.image,(self.width,self.height))
        self.rectx=rectx
        self.recty=recty
        self.screen=screen
        self.rect=pygame.Rect(self.rectx,self.recty,self.width,self.height)
        self.center=(self.rectx,self.recty)
        self.name=name
        self.font=pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 30)
        self.color=(255,255,255)
        self.passedcolor=(255,0,0)
        self.bg_color=(0,0,0)
        self.screen_color=(140,206,239)
        self.text_rendering=self.font.render(self.name,True,self.color,self.bg_color)
        self.text_rectx=self.rectx+20
        self.text_recty=self.recty+10
        self.text_rects=(self.text_rectx,self.text_recty)
        self.dict=dict
        self.book=dict[int(self.name)]
        self.kb_text=str(ceil(path.getsize('Data_Sets\\'+self.book+'.txt')/1024))
        self.kb_rectx=self.rectx+10
        self.kb_recty=self.recty+50
        self.kb_rects=(self.kb_rectx,self.kb_recty)
        self.kb_text_rendering=self.font.render(self.kb_text,True,self.color,self.screen_color)
        self.Passed=False

    #Rendering function
    def Draw(self):
        self.screen.fill(self.screen_color,self.rect)
        self.screen.blit(self.image,self.center)
        self.screen.blit(self.text_rendering,self.text_rects)
        self.screen.blit(self.kb_text_rendering,self.kb_rects)
    #Update function
    def Update(self):
        if self.Passed:
            self.text_rendering=self.font.render(self.name,True,self.passedcolor,self.bg_color)
            self.kb_text_rendering=self.font.render(self.kb_text,True,self.passedcolor,self.screen_color)
        else:
            self.text_rendering=self.font.render(self.name,True,self.color,self.bg_color)
            self.kb_text_rendering=self.font.render(self.kb_text,True,self.color,self.screen_color)

