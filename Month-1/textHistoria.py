print('Välkommen till Välj Ditt Eget Äventyr!')
print('Du kommer att tas med på en resa men får själv vara med och påverka historians gång!')
print('Se till att skriva en, liten bokstav när du gör ditt val.')
print()

print('SKEPP I SIKTE!')
print('Du slår upp ögonen när du hör navigatörens höga vrål från masten. Snabbt griper du tag i ditt teleskop och går ut ur din hytt. Ute på däck står kaptenen med blicken fäst på en liten prick i horisonten.')
print('"Det är ett skepp där ute, kapten! Vad ska vi göra?"')
print('Ska ni: a. styra mot skeppet eller b. fortsätta som vanligt?')

val = input()

if val == 'a':
    print('"Vi styr mot det!", säger du och dina sjömän nickar instämmande. Du tar tag i ratten och börjar styra mot skeppet, kanske mot ett nytt öde...')

if val == 'b':
    print('"Vi fortsätter som vanligt. Vi har inte råd att förlora tid.", säger du och dina sjömän tittar på varandra kort. Skeppet fortsätter med väldig fart mot ön som ni tänkte utforska...')