print('Välkommen till meningsgeneraren!')

print('Skriv in ett djur: ')
djur = input()

print('Skriv in en färg: ')
färg = input()

print('Skriv in en sak: (med en / ett framför) ')
sak = input()

print('En stor %s gick in på ett café och beställde %s mjölk. Mjölken smakade väldigt konstigt och två minuter senare förvandlades han till %s!' % (djur, färg, sak))