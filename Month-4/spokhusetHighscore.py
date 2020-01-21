import random
import time

scores = []
highscores = []

print('Skriv in ditt användarnamn: ')
namn = input('> ')
print()

print('Välj en dörr (1,2,3), bakom en av dem står det en vampyr. Vilken väljer du?')

val = int(input('> '))
vampire = random.randint(1,3)

score = 0

while True:
    if val == vampire:
        print('Tyvärr blev du middag för vampyren... Försök igen.')
        print('Du fick %s poäng' % (score))
        print()

        scores.append( [score, namn] )
        scores.sort(reverse=True)

        if len(scores) < 3:
            highscores = scores
        else:
            highscores = scores[:3]

        print('----- HIGHSCORE -----')
        for player in highscores:
            print('%s poäng - %s' % ( player[0], player[1] ))
        print('---------------------\n')

        print('Klicka enter för att köra igen. Skriv något för att sluta.')
        if input('> ') == '':
            score = 0
            print('Skriv in ditt användarnamn: ')
            namn = input('> ')
        else: 
            break
    
    else:
        score += 1
        
    print('\nDu kommer in i ett nytt rum. Välj en ny dörr.')
    val = int(input('> '))
    vampire = random.randint(1,3)

print('tack och hej!')




