# Improtera kodbiblioteket random
import random

# Definera listan med alla svar
svaren = ['Ja!', 'Nej!', 'Utan tvekan', 'Vet ej', 'Absolut inte', 'Försök igen senare']

# Kör för alltid
while True:
    # Skriv ut frågan
    print('Tänk på en ja/nej-fråga och klicka på enter för att få ett svar.')

    # Låt en klicka på enter eller skriva in ett kommando
    svar = input()

    # Om vi skriver in sluta ska vi gå ur loopen
    if svar == 'sluta':
        break
    
    # Skriv ut ett random svar och en tom rad
    print(random.choice(svaren))
    print()

# Skriv ett meddelande innan programet avslutas
print('Hoppas du fick svar på dina frågor! Hejdå!')