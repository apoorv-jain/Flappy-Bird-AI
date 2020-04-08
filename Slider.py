import pygame
import numpy as np
class Slider:
    def __init__(self,surface,min_value,max_value,pos,width):
        self.surface = surface
        self.min_value = min_value
        self.max_value = max_value
        self.posx,self.posy = pos
        self.width = width
        self.slider = self.posx - width/2
        self.value = min_value
        self.scale = (max_value - min_value)/width

    def draw(self):
        pygame.draw.line(self.surface,(0,0,0),
                        (int(self.posx - self.width/2),self.posy),
                        (int(self.posx + self.width/2),self.posy),2)
        pygame.draw.circle(self.surface,(255,255,255),
                           (int(self.slider),self.posy),6)
        pygame.draw.circle(self.surface,(0,0,0),
                            (int(self.slider),self.posy),6 ,1)
        self.update()
    def update(self):
        events = pygame.event.get()
        Mouse_press = pygame.mouse.get_pressed()
        if Mouse_press[0]:
            self.slider,_ = pygame.mouse.get_pos()
            if self.slider > self.posx + self.width/2:
                self.slider = self.posx + self.width/2
            elif self.slider < self.posx - self.width/2:
                self.slider = self.posx - self.width/2
            self.value = (self.slider -self.posx + self.width/2) * self.scale + self.min_value
    def get_value(self):
        return self.value
