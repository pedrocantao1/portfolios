print('DESENVOLVIDO POR PEDROCANTAO')
dias = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos km rodados nesses dias?'))
tdias = dias * 60
tkm = km * 0.15
tt = tdias + tkm
print ('Você rodou {} dias e, {} km rodados , o total do aluguel deu {}R$ . ' .format(dias, km, tt))
print('Sendo {}R$ dos dias, e {}R$ dos km rodados . ' .format(tdias, tkm))