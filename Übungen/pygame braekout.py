import pygame
import time
import random

# pygame
pygame.init()
pygame.display.set_caption("Breakout in Python")

random.randint
# Variablen


MULTIPLIKATOR = 30
w = 20
h = 30
screen = pygame.display.set_mode((w * MULTIPLIKATOR, h * MULTIPLIKATOR))

print(w, h)
spielaktiv = True
clock = pygame.time.Clock()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

ball_x = 10
ball_y = 23
ball_x_alt = ball_x
ball_y_alt = ball_y
ball_tick_x = 1
ball_tick_y = 1

spieler_x = 10
spieler_y = 27

karte=[
[10,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[5,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,1,5,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

print(karte[0][0])
print(karte[1][0])
print(karte[0][1])
print(karte[2][5])


# functions
def kor(zahl):
    zahl = zahl * MULTIPLIKATOR
    return zahl

def element_zeichnen(spalte,reihe):
    global element
    element = pygame.draw.rect(screen, ORANGE, [kor(spalte)+1, kor(reihe)+1,kor(1)-1,kor(1)-1])
def ball_zeichnen(x, y):
    global ball
    ball = pygame.draw.ellipse(screen, ROT, [kor(x), kor(y),kor(1), kor(1)], 0)
def spieler_zeichnen(x, y):
    global spieler
    spieler = pygame.draw.rect(screen, WEISS, [kor(x), kor(y),kor(5), kor(1)], 0)
def ball_löschen(spalte,reihe):
    pygame.draw.rect(screen, SCHWARZ, [kor(spalte), kor(reihe),kor(1),kor(1)])


ball_größe = kor(0.04)

# map auswerten
for x in range(0,20):
    for y in range(0,27):
        if karte[y][x] != 0:
            element_zeichnen(x,y)

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat beendet")
    
    
    # logic
    ball_x_alt = ball_x
    ball_y_alt = ball_y
    ball_x += ball_tick_x
    ball_y += ball_tick_y



    # ball
    ball_löschen(ball_x_alt, ball_y_alt)
    ball_zeichnen(ball_x, ball_y)
    #spieler_zeichnen(spieler_x, spieler_y)

    #if spieler.colliderect(ball):
     #   ball_tick_y = ball_tick_y * -1
      #  ball_y = 26.2
    if ball.colliderect(element):
        ball_löschen(ball_x_alt, ball_y_alt)
    
    if ball_y > h - ball_größe or ball_y < 0:
        ball_tick_y = ball_tick_y * -1
    elif ball_x > w - ball_größe or ball_x < 0:
        ball_tick_x = ball_tick_x * -1
    
    
    #print(ball_x, ball_y)
    
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()