import random
import time

print('Du går in i ett spökhus.')
print('Det finns tre dörrar, bakom ett står ett spöke. Vilken väljer du?')

dörr = int(input('> '))
spöke = random.randint(1,3)

print('Du öppnar dörren och...')
print()
time.sleep(2)

while dörr != spöke:
    print('Du kommer in i ett nytt rum.')
    print('Framför dig ser du tre dörrar. Vilken väljer du?')

    dörr = int(input('> '))
    spöke = random.randint(1,3)

    print('Du öppnar dörren och...')
    print()
    time.sleep(2)

print('Det står ett stort spöke och tar dig ned i mörkrets djup!')