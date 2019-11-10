import random

while True:

    hemligt = random.randint(1,25)

    print('Gissa ett tal mellan 1 & 25')

    gissning = int(input('> '))
    gissningar = 1

    while gissning != hemligt:
        if gissning < hemligt:
            print('Gissa högre.')
        else:
            print('Gissa lägre.')

        gissning = int(input('> '))
        gissningar += 1

    print('Du gissade rätt! Talet var %s' % (hemligt))
    print('Det tog dig %s gissningar!' % (gissningar))
    print()

    print('Vill du spela igen? (ja/nej)')
    igen = input('> ')

    if igen == 'nej':
        break

print('Tack för att du spelade! Hejdå!')
