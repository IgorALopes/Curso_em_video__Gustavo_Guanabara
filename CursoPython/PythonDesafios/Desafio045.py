# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep
print('-=-'*7)
print('VAMOS JOGAR JOKENPÔ!')
print('-=-'*7)
sleep(1.5)
print('Tente me vencer!')
sleep(1)
player = str(input('Escolha e escreva "PEDRA", "PAPEL" ou "TESOURA"!\n')).strip().upper()
if player != 'PEDRA' and player != 'PAPEL' and player != 'TESOURA':
    print('Por favor, escolha uma opção válida. Começe novamente!')
else:
    print('Certo! Agora eu vou escolher!')
    sleep(1.5)
    print('Hummm...')
    joklist = ['PEDRA', 'PAPEL', 'TESOURA']
    machine = choice(joklist)
    sleep(2)
    print('Já sei!')
    sleep(1)
    print('Vamos começar!')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)
    if player == machine:
        print('EMPATOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PEDRA' and machine == 'TESOURA':
        print('Aff. VOCÊ GANHOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PEDRA' and machine == 'PAPEL':
        print('Haha! GANHEI! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'TESOURA' and machine == 'PAPEL':
        print('Aff. VOCÊ GANHOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'TESOURA' and machine == 'PEDRA':
        print('Haha! GANHEI! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PAPEL' and machine == 'PEDRA':
        print('Aff. VOCÊ GANHOU! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')
    elif player == 'PAPEL' and machine == 'TESOURA':
        print('Haha! GANHEI! Você jogou {} e eu joguei {}.'.format(player, machine))
        sleep(1)
        print('Vamos jogar novamente?')

# RESOLUÇÃO PROFESSOR:

from random import randint
# from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
