#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex. Digite um número: 6.127. O número 6.127 te a parte inteira 6.
from math import floor, trunc

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, floor(n)))

#RESOLUÇÃO PROFESSOR:
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))
#OU
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
