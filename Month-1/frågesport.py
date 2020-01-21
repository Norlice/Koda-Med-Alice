score = 0

print('Vilket är det största landet till yta?')

svar = input('> ')

if svar == 'Ryssland':
    print('Rätt svar!')
    score +=1
else:
    print('Fel svar! Rätt svar är Ryssland')

print('Du fick ' + str(score) + ' poäng.')

