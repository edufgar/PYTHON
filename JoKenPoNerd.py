from random import randint
from time import sleep

print('-=' * 20)
print(' ' * 12, 'JO KEN PO NERD')
print('-=' * 20)

itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
computador = randint(0, 2)
print('''Suas Opções:
[ 0 } PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LAGARTO
[ 4 ] SPOCK''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    elif jogador == 3:
        print('COMPUTADOR VENCE')
    elif jogador == 4:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 3:
        print('JOGADOR VENCE')
    elif jogador == 4:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('COMPUTADOR VENCE')
    elif jogador == 4:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 3:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 3:
        print('EMPATE')
    elif jogador == 4:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 4:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    elif jogador == 3:
        print('JOGADOR VENCE')
    elif jogador == 4:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

