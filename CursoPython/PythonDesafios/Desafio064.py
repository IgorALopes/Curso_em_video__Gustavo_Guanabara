# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
c = 0
soma = 0
while n < 999:
    n = int(input('Digite um número: [999 para parar] '))
    soma += n
    c += 1
print('Foram digitados {} números e a soma deles é {}.'.format(c - 1, soma - 999))

# RESOLUÇÃO PROFESSOR:
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

