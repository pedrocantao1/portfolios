print ('DESENVOLVIDO POR PEDROCANTAO')
num = int(input('Informe um número : '))
print ('Analisando o número {} ... ' .format(num))
if num <= 9:
    print ('Unidade 1')
    print ('Dezena 0')
    print ('Centena 0')
    print ('Milhar 0')
if num <= 99  >= 10:
    print ('Unidade 2')
    print ('Dezena 1 ')
    print ('Centena 0')
    print ('Milhar 0 ')
if num  >= 100 <= 999:
    print ('Unidade 3')
    print ('Dezena 2 ')
    print ('Centena 1')
    print ('Milhar 0 ')
if num >= 1000 <= 9999:
    print ('Unidade 4')
    print ('Dezena 3 ')
    print ('Centena 2')
    print ('Milhar 1 ')