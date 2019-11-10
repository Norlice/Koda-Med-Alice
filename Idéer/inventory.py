kista = ['gammal bok', 'fiskespö', 'yxa', 'diamanter']

print(kista[1])

while True:
    print('I kistan hittar du:')
    for sak in kista:
        print('- %s' % (sak))

    print()
    nySak = input('> ')

    print()
    print('Du dumpar %s i kistan.' % (nySak))
    kista.append(nySak)


