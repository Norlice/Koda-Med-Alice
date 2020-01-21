import random

print('*** RISKY BUISSNESS ***')
print('Du börjar på 100 men varje gång du klickar ENTER dras det av 1-30. Du får poäng för varje gång du klickar ENTER, men förlorar om du hamnar under 0! Skriv stopp när du tror att du inte kan klicka längre.')

kvar = 100
score = 0

while kvar > 0:
    print('Det är', kvar, 'kvar')

    svar = input('> ')
    if svar == 'stopp':
        break
    else:
        score += 1
        kvar -= random.randint(1,30)

if kvar < 0:
    print('Nej! Det blev', kvar, 'kvar!')
    score = 0

print('Du fick ', score, 'poäng!')
    
