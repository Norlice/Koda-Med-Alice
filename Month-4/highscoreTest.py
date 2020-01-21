highscores = []
scores = []

while True:
    user = input('> ').split(' ')
    score = int(user[0])
    name = user[1]

    scores.append( [score, name] )
    scores.sort(reverse=True)

    if len(scores) < 3:
        highscores = scores
    else:
        highscores = scores[:3]

    print(highscores)