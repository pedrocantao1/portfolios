print ("DESENVOLVIDO POR PEDROCANTAO")
salario = float(input('Qual o salário do funcionário ? '))
pc = 15
totalpc = 100
reaj = float((salario * pc) / 100)
atual = salario + reaj
print('O salário de R${} , teve reajuste de 15% e passou a ser R${} ' .format(salario, atual))