# Importera randombiblioteket
import random

# Skriv ut instruktioner till användaren
print('Klicka på ENTER för att slå tärningen! Skriv sluta för att avbryta.')

# Kör tärningskastningen för evigt
while True:
    # Ta in ett svar från användaren. Klickar användaren ENTER är texten ""
    # skriver användaren något sparas det i svar
    svar = input('> ')

    # Om svar innehåller ordet sluta -> hoppa ut ur loopen
    if svar == 'sluta':
        break
    
    # Slumpa fram tärningssidan
    sida = random.randint(1,6)

    # Skriv ut resultatet
    print('Tärningen blev: %s' % (sida))
 
# Skriv ett avskedsord
print('Tack och hej!')
