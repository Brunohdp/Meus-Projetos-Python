from time import sleep
from random import randint, choice
import emoji

print(emoji.emojize('                                                  \033[1;33m:open_mouth:\033[1;34m Ooooh!', use_aliases=True))
#sleep(3)
print(emoji.emojize('                              \033[1;4;31mOLAAAAAAA!!\033[0;1;30m Tudo bem com você? Eu me chamo \033[1;4;36mRobin!\033[m\033[33;1m :smiley:', use_aliases=True))
#sleep(5)
print(emoji.emojize('                              \033[1;30mFaz \033[35;1;4mmuuuiito\033[0;1;30m tempo que eu não converso com ninguém... \033[33;1m:cry:\033[1;30m', use_aliases=True))
#sleep(5)
nome = str(input('Qual é o seu \033[1;4;33mnome\033[0;1;30m? ')).strip().title()
print()
print(emoji.emojize(f'Muito prazer em te conhecer, \033[1;4;32m{nome}\033[0;1;30m! Vai ser \033[35;4mINCRÍVEL\033[m\033[0;1;30m jogar com você \033[33;1m:laughing:\033[30;1m', use_aliases=True))
print()
#sleep(5)


j = int(input(emoji.emojize('''O que você gostaria de jogar? Nós temos algumas opções: \033[1;33m:wink:
\033[1;30;42m[1]\033[4mPedra, Papel e tesoura \033[m
\033[1;30;44m[2]\033[4mAdivinhando um número  \033[m
\033[1;30;41m[3]\033[4mDeixa pra lá...\033[0;41m        \033[m
\033[30;1mR: ''', use_aliases=True)))
print()

if j == 1:
    escolha = ['Pedra', 'Papel', 'Tesoura']
    pc = choice(escolha)

    print(emoji.emojize('               \033[33;1;4mAAAAAH QUE ÓTIMA ESCOLHA!\033[m', use_aliases=True))
    sleep(2)
    print(emoji.emojize('\033[0;1;30mEu simplesmente \033[1;34;4mAMO\033[0;1;30m jogar \033[32;1;4mPedra, Papel e Tesoura\033[0;1;30m Hahaha!!! \033[31m:heart:\033[33m :sparkles:\033[1;30m', use_aliases=True))
    sleep(3)
    print(emoji.emojize('                      Ok, vamos lá!', use_aliases=True))

    r = int(input(emoji.emojize('''Escolha a sua jogada enquanto eu escolho a minha \033[1;33m:smiley:
\033[1;30;42m[1]\033[4mPedra\033[0;42m   \033[m
\033[1;30;44m[2]\033[4mPapel\033[0;44m   \033[m
\033[1;30;45m[3]\033[4mTesoura\033[0;45m \033[m
\033[1;30mR:''', use_aliases=True)))

    print('\033[31;1;4mProcessando...\033[m')
    sleep(2)

    if r == 1 and pc == 'Papel' or r == 2 and pc == 'Tesoura' or r == 3 and pc == 'Pedra':
        if r == 1:
            r = 'Pedra'
        elif r == 2:
            r = 'Papel'
        else:
            r = 'Tesoura'
            print(emoji.emojize(f'\033[44;30;1mEBAAAA! EU GANHEEIII!! \033[33;7;1m :astonished: \033[30;1;44m Você colocou \033[0;30;7m{r}\033[0;1;44;30m e eu \033[0;30;7m{pc}\033[0;1;30;44m. Você jogou muito bem. Parabéns! HaHa\033[m', use_aliases=True))
    elif r == 1 and pc == 'Pedra' or r == 2 and pc == 'Papel' or r == 3 and pc == 'Tesoura':
        if r == 1:
            r = 'Pedra'
        elif r == 2:
            r = 'Papel'
        else:
            r = 'Tesoura'
            print(emoji.emojize(f'\033[46;30;1mEMPATEEE!\033[33;7;1m:satisfied:\033[46;30;1m Nós dois colocamos \033[0;30;7m{pc}\033[0;1;30;46m HaHa\033[m', use_aliases=True))
    else:
        if r == 1:
            r = 'Pedra'
        elif r == 2:
            r = 'Papel'
        else:
            r = 'Tesoura'
            print(emoji.emojize(f'\033[41;30;1mAaah Você ganhou \033[1;7;33m:confused: :sweat:\033[1;30;41m. Você colocou \033[0;30;7m{r}\033[0;1;41;30m e eu \033[0;30;7m{pc}\033[0;1;30;41m. Você é muito bom nesse jogo, Parabéns! HeHe \033[7;33;1m:blush:', use_aliases=True))

elif j == 2:
    s = randint(1, 10)
    print('                                \033[30;43;1m BOA ESCOLHA!! \033[0;30;1m')
    sleep(5)
    print('                           Esse jogo é \033[34;4mSUPER\033[m\033[0;1;30m legal!')
    print('''                           \033[35;1mBom, ele funciona assim:\033[m
\033[31;4;1m** Eu vou pensar em um número entre 1 e 10 e você tem que tentar adivinhar em qual número eu pensei, ok?! **\033[m''')
    sleep(10)
    print()
    r = int(input('''\033[1;30m           Está pronto? \033[32mVamos lá!\033[m
\033[1;30mTente adivinhar em que número estou pensando: '''))

    if r == s:
        print(f'Caramba que sorte! Você acertou em cheio. Eu estava mesmo pensando no número {s}. Você é muito bom!')
    else:
        print(f'Aaah é uma pena. Você errou! Eu estava pensando no número {s} e não no {r} HAHA!')

else:
    print(emoji.emojize('\033[30;44m Ah! Tudo bem então. Já que você não quer brincar eu vou voltar a ficar sozinho\033[m\033[30;7;1m:disappointed:\033[m', use_aliases=True))

