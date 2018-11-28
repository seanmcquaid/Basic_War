import pygame.font
class Text(object):
    def __init__(self,screen):
        self.width = 125
        self.screen = screen
        self.height = 125
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0,0,0)
        self.back_color = (0,102,0)
        self.font = pygame.font.Font(None, 60)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
    def title(self):
        self.image_message = self.font.render("WAR!", True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
    def player_point_counter(self):
        self.xy1 = (0,0)
        self.font = pygame.font.Font(None, 30)
        self.image_message1 = self.font.render("PLAYER POINT COUNTER:", True, self.text_color)
    def comp_point_counter(self):
        self.xy2 = (300,0)
        self.font = pygame.font.Font(None, 30)
        self.image_message2 = self.font.render("COMPUTER POINT COUNTER:", True, self.text_color)
    def deck_counter(self):
        self.xy3 = (200,150)
        self.font = pygame.font.Font(None, 30)
        self.image_message3 = self.font.render("CARDS LEFT: 52", True, self.text_color)
    def draw_counters(self):
        self.screen.fill(self.back_color, self.rect)
        self.screen.blit(self.image_message1,self.xy1)
        self.screen.blit(self.image_message2,self.xy2)
        self.screen.blit(self.image_message3,self.xy3)
    def draw_title_text(self):
        self.screen.fill(self.back_color, self.rect)
        self.screen.blit(self.image_message,self.image_message_rect)