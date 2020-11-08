import pygame

class Button:

    #could've inherited used pygame.sprite to do easier collision

    surface = 0
    text = ""
    x = 0
    y = 0
    font = 0

    image = pygame.image.load("button.png")
    
    def __init__(self, surface, text, x, y, font):
        self.text = text
        self.x = x
        self.y = y
        self.surface = surface
        self.font = font

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        drawtext = self.font.render(self.text, False, (0,0,0))
        self.surface.blit(drawtext, (self.x + 50, self.y + 20))

    def clicked(self):
        if pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            min_bound = (self.x, self.y)
            max_bound = (self.x + 150, self.y + 80)
            if (pos[0] > min_bound[0] and pos[0] < max_bound[0]) and (pos[1] > min_bound[1] and pos[1] < max_bound[1]):
                return True
        return False
        
