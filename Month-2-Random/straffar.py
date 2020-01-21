import time
import random

print('Det står 2-2 i förlängningstid...')
time.sleep(1)
print('Allt avgörs i straffar.')
time.sleep(1)
print('Du är målvakt och det är en straff kvar.')
time.sleep(1)
print('Du måste bestämma dig var du ska hoppa. Räddar du vinner ni, annars förlorar ni.')
time.sleep(1)
print('Vad väljer du?')
print('1. hoppa till vänster')
print('2. stanna i mitten')
print('3. hoppa till höger')

hopp = int(input('> '))

skott = random.randint(1,3)

print('Motståndaren gör sig redo...')
time.sleep(1)
print('Domaren blåser i visselpipan...')
time.sleep(1)
print('Motståndaren skjuter och...')
time.sleep(1)

if hopp == skott:
    print('DU RÄDDAR SKOTTET! NI VANN!')
else:
    print('Du räddade inte skottet... ni förlorade.')
