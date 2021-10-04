#programa que cria o jogo pedra , papel e tesoura

from random import randint
from time import sleep
itens = ('pedra' , 'papel' , 'tesoura')
computador = randint(0 , 2)
print(''' suas opçoes:'
[ 0 ]  PEDRA
[ 1 ]  PAPEL
[ 2 ]  TESOURA ''')
jogador = int(input('qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(3)
print('-=' * 12 )
print(' computador jogou {} '.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(' JOGADOR VENCE')
    elif jogador == 2:
        print(' COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador  == 1:
    if jogador == 0:
        print(' COMPUTADOR VENCE ')
    elif jogador == 1:
        print(' EMPATE ')
    elif jogador == 2:
     print (' JOGADOR VENCE')
    else:
        print(' JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print(' JOGADOR VENCE ')
    elif jogador == 1:
        print(' COMPUTADOR VENCE ')
    elif jogador == 2:
        print(' EMPATE ')
    else:
        print(' JOGADA INVALIDA ')