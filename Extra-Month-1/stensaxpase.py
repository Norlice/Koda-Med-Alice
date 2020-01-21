import random

print('Välkommen till sten, sax, påse!')
print('Skriv 1. sten, 2. sax eller 3. påse')

val = int( input() )

if val == 1:
    print('Du valde sten!')

if val == 2:
    print('Du valde sax!')

if val == 3:
    print('Du valde påse!')

datornsVal = random.randint(1,3)

if datornsVal == 1:
    print('Datorn valde sten!')

if datornsVal == 2:
    print('Datorn valde sax!')

if datornsVal == 3:
    print('Datorn valde påse!')