# glosor.py - förhör dig på dina glosor!

# Skriv upp alla svenska ord och deras översättningar i en dictionary med så kallade 'key-value pairs'
# Ett key-value pair består av två värden: key och value. Key är 'nyckeln', vilket låter oss komma åt value. så dictionary[key] = value
glosor = {
    'undgå': 'elude',
    'dator': 'computer',
    'hemsida': 'website',
    'innovativ': 'innovative',
    'polkagris': 'candy-cane'
}

# Användaren börjar med 0 poäng
score = 0

# Gå igenom varje svenskt ord, eller 'nyckeln' till det engelska ordet
for key in glosor.keys():
    # Ställ en fråga
    print('\nVad är översättningen till ' + key + '?')

    # Ta in användarens svar på frågan om översättning
    svar = input('> ')

    # Gör alla bokstäver till små bokstäver. Ex. HeJ -> hej
    svar = svar.lower()

    # Kolla om svaret är rätt. 
    if ( svar == glosor[key] ):
        # OM det är rätt, ge användaren ett poäng och skriv att de hade rätt
        score += 1
        print('\nRätt svar!')
    else:
        # Annars, skriv att de hade fel och visa det rätta svaret
        print('\nFel svar! Rätt svar är: ' + glosor[key])

    # Skriv hur många poäng användaren har
    print('Du har', score, 'poäng!')

# När alla ord i dictionaryn har loopat igenom, skriv ut det totala resultatet
print('\n#########################')
print('Du fick', score, 'av', len(glosor), 'rätt!')