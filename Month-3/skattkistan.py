# Importera randomkoden
import random

# Skriv ut instruktionerna
print('Välkommen till skattkistan!')
print()
print('Välj en av kistorna från varje lass och försök samla så många mynt som möjligt!')
print('I en kista från varje lass finns dock en gömd pirat som tar alla mynt...')
print('Hur många kistor vågar du öppna?')
print()

# Starta med 0 mynt
mynt = 0

# Kör tills en pirat hoppar ut eller användaren avslutar
while True:
    # Skriv ut en fråga
    print('Ett nytt lass har kommit! Vilken kista väljer du? (1, 2, 3 eller 4. 5 om du är nöjd)')

    # Spara valet i en variabel
    kista = int(input('> '))

    # Slumpa fram i vilken kista piraten är i
    pirat = random.randint(1,4)
    
    # Om användaren skriver 5 vill vi hoppa ur loopen och sluta välja kistor
    if kista == 5:
        break
    
    # Om användaren val samma kista som piraten förlorar de alla mynt!
    if kista == pirat:
        # Skriv ut ett meddelande
        print('En pirat hoppar ut och tar alla dina mynt!')

        # Återställ mynten
        mynt = 0

        # Hoppa ur loopen
        break
    
    # Slumpa fram vad en kista ska innehålla
    skatt = random.randint(10,50)

    # Lägg till det innehållet
    mynt += skatt

    # Skriv ut hur många mynt användaren hittar
    print('Du öppnar kistan och hittar %s mynt!' % (skatt))

# Skriv ett avslutningsmeddelande
print('Nu är aktionen slut. Du fick %s mynt!' % (mynt))



    


