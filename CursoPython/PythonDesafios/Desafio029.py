#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
kmh = int(input('A quantos km/h o veículo passou pelo pardal? '))
if kmh > 80:
    print('Você foi multado por ultrapassar 80km/h.')
    print('Por ter atingido a velocidade de {}km/h, receberá uma multa de R${:.2f}.'.format(kmh, (kmh - 80) * 7))
else:
    print('Muito bem! Você não foi multado!')

#RESOLUÇÃO PROFESSOR:
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
