# Importera våra kodbibliotek
import random
import time

# Skriv ett öppningsmeddelande
print('Du befinner dig i ett land fyllt av drakar...')
print('Efter dagar av letande har du tagit dig in i en grotta fylld med skatter. Problemet är att en drake vaktar skatten!')
print('För att ta dig förbi draken behöver du muta den!')

# Skriv ut en tom rad för att det ska bli enklare att läsa
print('')

print('Ska du ge draken 1. en kanelbulle eller 2. en diamant?')

# Få in valet från spelaren. Vi använder int för att få in ett nummer
val = int(input('> '))

# Slumpa fram det draken föredrar
draken = random.randint(1,2)

# Få spänningen att stiga
print('Du går långsamt fram till draken...')
time.sleep(2)
print('Du lägger ner objektet framför den...')
time.sleep(2)
print('Och...')
time.sleep(2)

# OM vi gett rätt så vinner vi, ANNARS förlorar vi
if val == draken:
    print('Draken låter dig passera! Du är rik!')
else:
    print('Draken käkar upp dig i ett nafs...')
