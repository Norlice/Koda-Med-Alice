# Skriv din kod här :-)
# https://github.com/AhmNouira/-Racing-Game

from random import randint

speed = 10
HEIGHT = 500
WIDTH = 300

car = Actor('racer/racecar')
cone = Actor('racer/bare')

car.pos = (150, 440)

kraschat = False

def draw():

    if kraschat:
        screen.clear()
        screen.fill('pink')
        screen.draw.text('Du krashade!', color='white', center=(WIDTH/2, HEIGHT/2), fontsize=60)
    else:
        screen.fill((128,128,128))
        car.draw()
        cone.draw()

def update():
    global kraschat

    if keyboard.left: car.x -= speed
    if keyboard.right: car.x += speed

    if kraschat == False:
        cone.y += 20

    if car.collidepoint(cone.pos):
        sounds.splat.play()
        print('träffad!')
        kraschat = True

    if cone.y >= HEIGHT:
        cone.y = -10
        cone.x = randint(0, WIDTH)
