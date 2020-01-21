# bday.py - skriv in ett namn och se personens födelsedag!

# Skriv upp alla födelsedagar i en dictionary
bdays = {
    'alice': '25 augusti',
    'leif': '18 september',
    'jonna': '1 januari'
}

# Kör tills användaren skriver stopp
while True:
    print('\nSkriv in ett namn för att se personens födelsedag!')

    # Ta in ett namn från användaren
    namn = input('> ')

    # Gör alla bokstäver till små
    namn = namn.lower()

    # KOlla om användaren istället skrev "stopp", gå i så fall ut ur loopen
    if namn == 'stopp':
        break
    
    # Kolla om namnet finns i vår dictionary
    if namn in bdays:
        # I så fall, skriv ut namnet med stor bokstav och skriv ut födelsedagen
        print(namn.capitalize() + ' fyller år den ' + bdays[namn])
    else:
        # Annars skriv att namnet inte finns sparat
        print('Detta namn finns inte sparat!')

# Skriv ett hejdå-meddelande
print('Tack för att du använde detta program!')