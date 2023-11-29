import math
print ('DESENVOLVIDO POR PEDROCANTAO')
print ("Calcular a hipotenusa . ")
oposto = float(input('Qual o comprimento do cateto oposto : '))
adjacente = float(input('Qual o comprimento do cateto adjacente : '))
hip = float(oposto ** 2 ) + float(adjacente ** 2)
hipt = math.sqrt(hip)
print ('A hipotenusa é {} ' .format(hipt))