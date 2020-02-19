# Skriv din kod här :-)

# Uppdrag:
# - Fler uppgraderingar
# - Få kakan att rotera snabbare desto fler kakor man har
# - Skriva ut hur många autokakor man har, alltså hur många kakor man får automatiskt per sekund

WIDTH = 700
HEIGHT = 700

kaka = Actor('cookieclicker/cookie')
kaka.center = (350, 350)

uppgradering1 = Rect((20, 100), (100, 40))

kakor = 0
autokakor = 0

def draw():
    screen.clear()
    kaka.draw()
    screen.draw.text('Kakor: ' + str(kakor), color='white', center=(350, 30))

    if kakor >= 25:
        screen.draw.filled_rect(uppgradering1, 'green')
    else:
        screen.draw.filled_rect(uppgradering1, 'red')

    screen.draw.textbox('+1', uppgradering1)

def on_mouse_down(pos):
    global kakor, autokakor

    if kaka.collidepoint(pos):
        kakor += 1
        kaka.angle += 2

    if uppgradering1.collidepoint(pos) and kakor >= 25:
        autokakor += 1
        kakor -= 25


def geAutokakor():
    global kakor, autokakor

    kakor += autokakor
    kaka.angle += 2

    clock.schedule(geAutokakor, 1)

geAutokakor()
