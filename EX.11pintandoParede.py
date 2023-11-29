print('DESENVOLVIDO POR PEDROCANTAO')
largura = float(input('Qual a largura da parede em metros ? '))
altura = float(input('Qual a altura da parede em metros ? '))
area = float(largura) * float(altura)
litros = float(area) / 2
print ('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, area) )
print ('Para pintar essa parede, você precisará de {} litros de tinta, sendo que 2m de parede gasta 1 litro de tinta.'.format(litros))