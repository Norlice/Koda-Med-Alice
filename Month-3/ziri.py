# Skriv ut ett välkomstmeddelande
print('Hej där! Jag är Ziri.')

# Låter en prata för alltid
while True:
    # Ta in ett svar från användaren
    svar = input('> ')

    # Om vi säger hejdå ska vi hoppa ut ur loopen
    if 'hejdå' in svar:
        break
    # Se om vissa ord finns i svaret vilket ändrar vad Chattis säger
    if 'hej' in svar:
        print('Hej där!')
    # Här kollar vi om heter och du/jag finns i svaret för att avgöra om vi frågar eller säger vårt eget namn
    if 'heter' in svar and 'du' in svar:
        print('Jag heter Ziri.') 
    if 'heter' in svar and 'jag' in svar:
        print('Vad roligt att träffas!')
    if 'skämt' in svar:
        print('Det var en gång... som var sandad!')

# Skriv ett hejdå
print('Hejdå!')
