#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.
km = int(input('Quantos Km terá a viagem? '))
if km <= 200:
    print('Sua passagem custará R$ {:.2f}.'.format(km * 0.5))
else:
    print('Sua passagem custará R$ {:.2f}.'.format(km * 0.45))

#RESOLUÇÃO PROFESSOR:
'''distância = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''
#OU
distância = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))