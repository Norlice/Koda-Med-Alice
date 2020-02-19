# Skriv din kod här :-)

# Uppdrag:
# Skapa en snygg slutskärm

import time

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
box = Rect((300, 300), (80, 80))

starttid = time.time()
print(starttid)

def draw():
    screen.clear()
    alien.draw()
    screen.draw.filled_rect(box, 'red')

def update():

    if keyboard.right:
        alien.x += 3
    if keyboard.left:
        alien.x -= 3
    if keyboard.up:
        alien.y -= 3
    if keyboard.down:
        alien.y += 3


    if box.x > alien.x:
        box.x -= 1
    if box.x < alien.x:
        box.x += 1
    if box.y > alien.y:
        box.y -= 1
    if box.y < alien.y:
        box.y += 1


    if alien.colliderect(box):
        sluttid = time.time()
        speltid = sluttid - starttid
        speltid = round(speltid, 2)

        print('Du blev uppäten av den röda lådan!')
        print('Du överlevde i ' + str(speltid) + ' sekunder')
        exit()
