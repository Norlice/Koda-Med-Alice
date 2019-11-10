import random

print('Välkommen till skattkistan!')
print()
print('Välj en av kistorna från varje lass och försök samla så många mynt som möjligt!')
print('I en kista från varje lass finns dock en gömd pirat som tar alla mynt...')
print('Hur många kistor vågar du öppna?')
print()

mynt = 0

while True:
    print('Ett nytt lass har kommit! Vilken kista väljer du? (1, 2, 3 eller 4. 5 om du är nöjd)')

    kista = int(input('> '))
    krabba = random.randint(1,4)
    
    if kista == 5:
        break

    if kista == krabba:
        print('En pirat hoppar ut och tar alla dina mynt!')
        mynt = 0
        break

    skatt = random.randint(10,50)
    mynt += skatt

    print('Du öppnar kistan och hittar %s mynt!' % (skatt))

print('Nu är aktionen slut. Du fick %s mynt!' % (mynt))



    


