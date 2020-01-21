print('Det har skett ett brott! Skriv info för att få ledtrådar, eller enter för att gå vidare. När du tror du löst fallet, skriv namnet på den skyldige!')

skyldige = 'Gjert'

svar = input('> ')
if svar == 'info':
    print('Det var en söndagseftermiddag. En person i rånarluva som krossade ett butiksfönster och stal en dyr klocka.')
    print('De misstänkta är:')
    print('Harald')
    print('Linnea')
    print('Gjert')

svar = input('> ')
if svar == 'info':
    print('Harald: "Det var inte jag, söndag mellan klockan 12 och 18 var jag och hjälpte att städa upp i parken."')

svar = input('> ')
if svar == 'info':
    print('Linnea: "Vadå klocka, tid är en illusion. Jag har inget arbete och behöver inte komma i tid. Förutom våra bokträffar, varje söndag klockan 12 till 16. De kommer jag alltid till."')

svar = input('> ')
if svar == 'info':
    print('Gjert: "Klockan 9 var jag på arbetet. Klockan 12 fick jag sparken och gick... hem. Typ det."')

print('Vem är den skyldige?')
gissning = input('> ')

if gissning == skyldige:
    print('Det är rätt! ' + skyldige + ' är den som utförde brottet!')
else:
    print('Det är tyvärr fel. Det var ' + skyldige + ' som utförde brottet!')