import random
import time

def getHighscores():
    fil = open('highscores.txt', 'r')
    scores = fil.read()
    scores = scores.split(',')
    scores.pop()

    scores.sort(reverse=True)
    highscores = scores[:3]

    return highscores

while True:

    print('Välj en dörr (1,2,3), bakom en av dem står det en vampyr. Vilken väljer du?')
    
    val = int(input('> '))
    vampire = random.randint(1,3)

    score = 0

    while True:
        if val == vampire:
            print('Tyvärr blev du middag för vampyren... Försök igen.')
            print('Du fick %s poäng' % (score))

            fil = open('highscores.txt', 'a')
            scoreEntry = str(score) + ','
            fil.write(scoreEntry)
            fil.close()
            
            break

        score += 1
        
        print('Du kommer in i ett nytt rum. Välj en ny dörr.')
        val = int(input('> '))
        vampire = random.randint(1,3)

    highscores = getHighscores()
    print('--- HIGHSCORE ---')
    print(highscores)
    print('Klicka ENTER för att köra igen')
    input() 







