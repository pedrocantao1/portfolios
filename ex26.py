frase = input('Digite um frase : ').strip()
print('A letra A aparece {} Vezes na frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')))
