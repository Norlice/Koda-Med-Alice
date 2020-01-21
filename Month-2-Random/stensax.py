# Importera koden för slumpmässiga tal
import random

# Välkomstmeddelande och instruktioner
print('Välkommen till sten-sax-påse!')
print('Väljer du 1. Sten 2. Sax eller 3. Påse?')

# Ta in användarens val
val = int(input('> '))

# Slumpa fram datorns val
datorn = random.randint(1,3)

# Skriv ut det spelaren valde
if val == 1:
    print('Du valde Sten!')
if val == 2:
    print('Du valde Sax!')
if val == 3:
    print('Du valde Påse!')

# Skriv ut det datorn valde
if datorn == 1:
    print('Datorn valde Sten!')
if datorn == 2:
    print('Datorn valde Sax!')
if datorn == 3:
    print('Datorn valde Påse!')

print()
print('Lyckades du slå datorn?')
