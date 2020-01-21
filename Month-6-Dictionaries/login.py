# secrets.py eller något sådan

import json

# users = {
#     'dragonmaster': {
#         'lösenord': 'drakarÄrBäst',
#         'hemlis': 'Jag älskar att mosa blåbär'
#     },
#     'xx_fifachamp_xx': {
#         'lösenord': 'fifafifa',
#         'hemlis': 'Det bästa fifa är Fifa 14'
#     }
# }

# Hämta användare
users = json.load( open('users.json') )

inloggad = False

while inloggad == False:
    print('Välkommen! Dessa kommandon kan du göra: ')
    print('\t1. logga in')
    print('\t2. registrera dig')

    val = int( input('> ') )

    if val == 1:
        
        print('Skriv in ditt användarnamn: ')
        username = input('> ')

        print('Skriv in ditt lösenord')
        password = input('> ')

        if username in users and password == users[username]['lösenord']:
            inloggad = True
        else:
            print('Användarnamnet eller lösenordet var fel. Försök igen')

    elif val == 2:
        print('Skriv in ditt användarnamn: ')
        username = input('> ')

        print('Skriv in ditt lösenord')
        password = input('> ')

        print('Skriv in din hemlis')
        hemlis = input('> ')

        users[username] = {
            'lösenord': password,
            'hemlis': hemlis
        }

        inloggad = True

# Inloggad
print('Välkommen ' + username + '!')

while True:    
    print('\nDessa kommandon finns:')
    print(' 1. se hemlis')
    print(' 2. ändra hemlis')
    print(' 3. logga ut')

    val = int( input('> ') )

    if val == 1:
        print('Din hemlis är: ' + users[username]['hemlis'])

    if val == 2:
        print('Skriv in din nya hemlis: ')
        nyHemlis = input('> ')

        users[username]['hemlis'] = nyHemlis
        print('Din hemlis är ändrad!')

    if val == 3:
        print('Tack och hej!')
        break

# Spara informationen
json.dump( users, open('users.json', 'w' ) )

