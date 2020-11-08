import button
import pygame
import random

dictionary = ["acronym", "address", "affect", "alter", "annotate", "apple",
              "continuum", "clarify", "character", "credible", "carrot",
              "devise", "difference", "dragon", "dominate", "discuss",
              "emphasise", "employ", "equivalent", "explore", "event",
              "frequency", "focus", "forehead", "football", "fruit"]

#initialise pygame and the window
pygame.init()

window_width = 1024
window_height = 768

surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Hangman')

clock = pygame.time.Clock()
running = True

used_letters = []
found_letters = []
guessed_letters = []
found = 0
body_parts = 0

lost = False
won = False

#load images
stand = pygame.image.load("stand.png")
head = pygame.image.load("head.png")
limb = pygame.image.load("limb.png")
popupbox = pygame.image.load("popupbox.png")

font = pygame.font.SysFont("timesnewroman", 64)
font2 = pygame.font.SysFont("timesnewroman", 32)

word = list(random.choice(dictionary))

def guess(letter):
    global found
    global body_parts
    if not (letter in guessed_letters):
        guessed_letters.append(letter)
        if letter in word:
            indices = where_in_word(letter, word)
            for i in indices:
                found_letters.append(i)
                found += 1
                
        else:
            #indices = where_in_word(letter, guessed_letters)
            #for i in indices:
            #    guessed_letters[i] = (guessed_letters[i] + u"\u0336")
            body_parts += 1
            

def draw_answer():
    for i in range(0, len(word)):
        pygame.draw.line(surface, (0,0,0), (100+(i*80), 100), (100+((i+1)*80)-10, 100), 1)

    for i in found_letters:
        letter = font.render(word[i], False, (0,0,0))
        surface.blit(letter, (120+(i*80), 35))

    guessed_string = str(" ".join(guessed_letters))
    guessed = font2.render("Guesses: " + guessed_string, False, (0,0,0))
    surface.blit(guessed, (100, 120))
    
def draw_stand(x, y):
    surface.blit(stand, (x,y))
    if body_parts >= 1:
        surface.blit(head, (x+295, y+100))
    if body_parts >= 2:
        surface.blit(limb, (x+335, y+180))
    if body_parts >= 3:
        arm1 = pygame.transform.rotate(limb, 130)
        surface.blit(arm1, (x+260, y+190))
    if body_parts >= 4:
        arm2 = pygame.transform.rotate(limb, 230)
        surface.blit(arm2, (x+330, y+190))
    if body_parts >= 5:
        leg1 = pygame.transform.rotate(limb, 130)
        surface.blit(leg1, (x+260, y+260))
    if body_parts >= 6:
        leg2 = pygame.transform.rotate(limb, 230)
        surface.blit(leg2, (x+330, y+260))

def where_in_word(guess, word):
    indices = []
    previous_index = 0
    index = 0
    while True:
        try:
            index = word.index(guess, previous_index, len(word))
            if index >= 0:
                indices.append(index)
            previous_index = index + 1
        except:
            break
    if not indices:
        return -1
    else:
        return indices

while running:

    surface.fill((0, 255, 255))
    draw_stand(200,200)
    draw_answer()

    if found >= len(word):
        won = True
        surface.blit(popupbox, (200, 150))
        win = font.render("You won!", False, (0, 0, 0))
        play_again = font2.render("Play again?", False, (0,0,0))
        surface.blit(win, (250, 200))
        surface.blit(play_again, (250, 300))
        btn_yes = button.Button(surface, "Yes", 250, 400, font2)
        btn_yes.draw()
        if btn_yes.clicked():
            found = 0
            body_parts = 0
            word = random.choice(dictionary)
            found_letters = []
            guessed_letters = []
            won = False
        btn_no = button.Button(surface, "No", 500, 400, font2)
        btn_no.draw()
        if btn_no.clicked():
            running = False
    if body_parts >= 6:
        lost = True
        surface.blit(popupbox, (200, 150))
        win = font.render("You lost.", False, (0, 0, 0))
        play_again = font2.render("Play again?", False, (0,0,0))
        surface.blit(win, (250, 200))
        surface.blit(play_again, (250, 300))
        btn_yes = button.Button(surface, "Yes", 250, 400, font2)
        btn_yes.draw()
        if btn_yes.clicked():
            found = 0
            body_parts = 0
            word = random.choice(dictionary)
            found_letters = []
            guessed_letters = []
            lost = False
        btn_no = button.Button(surface, "No", 500, 400, font2)
        btn_no.draw()
        if btn_no.clicked():
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if not lost and not won:
                if len(key) < 2:
                    guess(key)

        #print(event)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
