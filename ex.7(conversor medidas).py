print('DESENVOLVIDO POR PEDROCANTAO')
metro = float(input('Uma distância em metros : '))
km = metro / float(1000)
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print ('A medida de {} m corresponde a {} km - quilômetro' .format(metro, km))
print ('A medida de {} m corresponde a {} hm - hectômetro' .format(metro, hm))
print ('A medida de {} m corresponde a {} dam - decâmetro '.format(metro, dam))
print ('A medida de {} m corresponde a {} dm - decímetro'.format(metro, dm))
print ('A medida de {} m corresponde a {} cm - centímetro '.format(metro, cm))
print ('A medida de {} m corresponde a {} mm - milímetro '.format(metro, mm))