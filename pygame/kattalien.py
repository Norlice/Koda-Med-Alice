# Skriv din kod här :-)


# Updrag:
# Räkna poäng och visa dem i slutet
# Gör en timer
# Uppgradera hur ni vill!
# Byter knapp när man klickar på dem
# Skriva ut instruktionerna på toppen av skrämen

import random

WIDTH = 500
HEIGHT = 800

katt = Actor('cat2.png')
alien = Actor('alien.png')

alive = True
visa = 1

def draw():
    if alive == True:
        screen.fill('lightblue')

        if visa == 1:
            katt.draw()
        else:
            alien.draw()
    else:
        screen.fill('brown')
        screen.draw.text('Du klickade fel! Spelet slut.', color='white', center=(250, 400))

def on_mouse_down(pos, button):
    global alive, visa

    if katt.collidepoint(pos):
        if button == mouse.LEFT:
            print('Du klickade rätt!')
            placerakatt()
        else:
            print('Du klickade fel!')
            alive = False

    if alien.collidepoint(pos):
        if button == mouse.RIGHT:
            print('Du klickade rätt!')
            placeraalien()
        else:
            print('Du klickade fel!')
            alive = False

    visa = random.randint(1,2)

def placerakatt():
    katt.x = random.randint(20, 480)
    katt.y = random.randint(20, 780)

def placeraalien():
    alien.x = random.randint(20, 480)
    alien.y = random.randint(20, 780)

placerakatt()
placeraalien()
