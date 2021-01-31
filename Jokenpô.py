
# *Importa as funções choice e sleep das bibliotecas random e time,
# *respectivamente.
from random import randint
from time import sleep

print('\033[34;1;4m-='*6, 'DESAFIO 045 - JOKENPÔ', '=-'*6)  # Títulos

# *Pra passar os números para as opções tem que mandar printar o número
# *sorteado -1 dentro de 'esc[]'. Isso pq dentro dessa string o primeiro item
# *equivale a 0 e o último a 2, e os núros sorteados são de 1 a 3, os mesmos
# *das escolhas do usuário
esc = ('Pedra', 'Papel', 'Tesoura')
pc = randint(1, 3)  # *Cria uma lista com as jogadas e randomiza a escolha

r = str('S')

print('\033[0;33;1m-' * 27)
print('| \033[0;1;30;45m VAMOS JOGAR JOKENPO!! \033[0;33;1m |')  # Design

while r == str('S'):

    print('|', '-' * 23, '|')
    print(
        '| \033[0;30;41m \033[4mEscolha a sua jogada\033[0;41;30m: \033[0;1;33m |')
    print('|', '-'*23, '|')

    # *Mostra as opções
    print('''| \033[0;42;30m [1]\033[4mPedra\033[0;42m              \033[0;33;1m |
| \033[0;40m [2]\033[4mPapel\033[0;7;30m              \033[0;33;1m |
| \033[46;30m [3]\033[4mTesoura\033[0;46m            \033[0;1;33m |''')

    j = int(input('| R: '))  # *Recebe a jogada
    print('-' * 25)
    print()

    print('-' * 14)         # *Cria efeito de delay por processamento
    print('| \033[0;47m    \033[0;1;30;47;4mJO\033[0;47;30m    \033[0;1;33m |')
    sleep(1)
    print('| \033[0;47m    \033[0;1;30;47;4mKEN\033[0;47;30m   \033[0;1;33m |')
    sleep(1)
    print('| \033[0;47m    \033[0;1;30;47;4mPO\033[0;47;30m    \033[0;1;33m |')
    sleep(1)
    print('-' * 14)
    print()

    # *Cria a condição necessária para saber quando ele ganha e vc perde
    if j == 1 and pc == 2 or j == 2 and pc == 3 or j == 3 and pc == 1:
        print('-'*52)
        print(
            f'| \033[0;1;30;41m EU GANHEEII! Você escolheu \033[45m{esc[j-1]:^7}\033[0;1;30;41m e eu \033[45m{esc[pc-1]:^7}\033[0;1;41;30m! \033[0;1;33m |')
        print('-' * 52)  # Diz que ele ganhou e exibe as escolhas
    elif j == pc:  # *Cria a condição necessária para saber se os dois fizeram a mesma escolhe e foi um empate
        print('-' * 42)
        print(
            f'| \033[0;1;40m EMPATEEE! Nós dois escolhemos \033[0;40;46;1m{esc[pc-1]:^7}\033[0;1;40m! \033[0;1;33m |')
        print('-' * 42)  # *Diz que foi empate e exibe as escolhas
    else:  # *Se nenhuma das condições acima acontecer, ele assume que vc ganhou
        print('-' * 53)
        print(
            f'| \033[1;30;42m VOCÊ GANHOOUU! Eu escolhi \033[44m{esc[pc-1]:^7}\033[1;30;42m e você \033[44m{esc[j-1]:^7}\033[0;1;30;42m! \033[0;1;33m |')
        print('-' * 53)  # *Diz que você ganhou e exibe as escolhas
    print()
    print('-' * 38)
    r = str(input(
        '| \033[1;30;47m Você quer jogar novamente? [S/N] \033[0;33;1m | \n| R: ')).upper()
    print('-' * 38)
    print()
    print()
    if r == 'S':
        print('-' * 27)
        print(
            '| \033[30;46;1m       \033[4mEBAAAA!!!\033[0;46m       \033[0;33;1m |')
        print(
            '| \033[30;46;1m      \033[4mVAMOS LÁ!!!\033[0;46m      \033[0;33;1m |')
    else:
        print('-' * 23)
        print('| \033[42;30;1m Ah, é uma pena D: \033[0;33;1m |')
        print('-' * 23)
