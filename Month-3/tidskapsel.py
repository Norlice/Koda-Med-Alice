kapsel = []

print('Tänk att du ska gräva ned en tidskapsel som ska hittas om 500 år! Vad skulle du fylla den med?')

while len(kapsel) < 5:
    print('Vad vill du lägga till i kapseln?')
    nySak = input('> ')

    kapsel.append(nySak)

print() 
print('----- 500 år senare ------')
print('I ett bygge av ett 700-våningshus hittar man en kapsel...')
print('I kapseln finns:')
for sak in kapsel:
    print('- %s' % (sak))

