# Importera random
import random

# Kör tills användaren inte vill spela mer
while True:

    # Slumpa fram ett slumpmässigt tal mellan 1-25
    hemligt = random.randint(1,25)

    # Skriv ut instruktion
    print('Gissa ett tal mellan 1 & 25')

    # Ta in en gissning från användaren
    gissning = int(input('> '))

    # Nu har användaren gissat 1 gång
    gissningar = 1

    # Låt användaren fortsätta gissa så länge gissningen INTE är samma som det hemliga talet
    while gissning != hemligt:
        # Om gissningen är lägre, få användaren att gissa högre
        if gissning < hemligt:
            print('Gissa högre.')
        # Om gissningen är högre, få användaren att gissa lägre
        else:
            print('Gissa lägre.')

        # Fortsätt ta in gissningar
        gissning = int(input('> '))

        # Lägg till ett för varje gissning
        gissningar += 1

    # Skriv ut det rätta talet och hur många gissningar det tog
    print('Du gissade rätt! Talet var %s' % (hemligt))
    print('Det tog dig %s gissningar!' % (gissningar))
    print()

    # Fråga om användaren vill spela igen
    print('Vill du spela igen? (ja/nej)')
    # Ta in ett svar
    igen = input('> ')

    # Om svaret är nej, hoppa ut ur loopen. Låt annars loppen gå tillbaka och köra igen
    if igen == 'nej':
        break

# Skriv ett avslutningsmeddelande
print('Tack för att du spelade! Hejdå!')
