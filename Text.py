import pygame.font
class Text(object):
    def __init__(self,screen):
        self.width = 100
        self.height = 100
        self.font = pygame.font.Font(None, 60)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
    # def draw_text():