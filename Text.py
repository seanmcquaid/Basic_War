import pygame.font
class Text(object):
    def __init__(self,screen):
        self.width = 125
        self.screen = screen
        self.height = 125
        self.player_points = 0
        self.comp_points = 0
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0,0,0)
        self.back_color = (0,102,0)
        self.font = pygame.font.Font(None, 60)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
    def title(self):
        self.font = pygame.font.Font(None, 60)
        self.image_message = self.font.render("WAR!", True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
    def instructions(self):
        self.xy1 = (100,100)
        self.font = pygame.font.Font(None, 28)
        self.image_message1 = self.font.render("Press Spacebar to Continue to Each Round", True, self.text_color)
        self.image_message2 = self.font.render("Highest Card Wins!", True, self.text_color)
    def player_point_inc(self):
        self.player_points += 2
    def comp_point_inc(self):
        self.comp_points += 2
    def player_point_counter(self):
        self.xy2 = (0,0)
        self.font = pygame.font.Font(None, 25)
        self.image_message2 = self.font.render("PLAYER POINT COUNTER: %d" %self.player_points, True, self.text_color)
    def comp_point_counter(self):
        self.xy3 = (300,0)
        self.font = pygame.font.Font(None, 25)
        self.image_message3 = self.font.render("COMPUTER POINT COUNTER: %d" %self.comp_points, True, self.text_color)
    def deck_counter(self,deck_length):
        self.xy4 = (225,150)
        self.font = pygame.font.Font(None, 28)
        self.image_message4 = self.font.render("CARDS LEFT: %d" %deck_length, True, self.text_color)
    def winner(self,round_winner):
        self.round_winner = round_winner
        self.xy5 = (225,300)
        self.font = pygame.font.Font(None, 23)
        self.image_message0 = self.font.render("ROUND WINNER: %s" %self.round_winner, True, self.text_color)
    def draw_title_text(self):
        self.screen.fill(self.back_color, self.rect)
        self.screen.blit(self.image_message,self.image_message_rect)
    def draw_instructions(self):
        self.screen.fill(self.back_color, self.rect)
        self.screen.blit(self.image_message1,self.xy1)
    def draw_counters(self):
        self.screen.fill(self.back_color, self.rect)
        self.screen.blit(self.image_message2,self.xy2)
        self.screen.blit(self.image_message3,self.xy3)
        self.screen.blit(self.image_message4,self.xy4)
    def draw_winner_player(self):
        self.screen.fill(self.back_color, self.rect)
        self.screen.blit(self.image_message0,self.xy5)