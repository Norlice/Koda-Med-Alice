import pgzrun
import random
import time

apple = Actor("pricka/apple")

HEIGHT = 500
WIDTH = 500

tidkvar = 3
score = 0

def draw():
    screen.clear()

    if tidkvar > 0:
        apple.draw()
        screen.draw.text('Tid kvar: ' + str(tidkvar), color="white", topleft=(10,10))
    else:
        screen.draw.text('Tiden är slut!', color="white", center=(250, 230))
        screen.draw.text('Du fick ' + str(score) + ' poäng!', color="white", center=(250, 250))

def on_mouse_down(pos):
    global score, tidkvar

    if apple.collidepoint(pos):
        sounds.splat.play()
        score += 1
        placera_apple()

    else:
        sounds.meow1.play()
        tidkvar = 0

def placera_apple():
    apple.x = random.randint(10,400)
    apple.y = random.randint(10,400)

def ticka():
    global tidkvar

    tidkvar -= 1

    if tidkvar > 0:
        clock.schedule(ticka, 1.0)

placera_apple()
ticka()
