import math                                             #Importa a biblioteca math

print('='*10, 'DESAFIO 0016 - PARTE INTEIRA', '='*10)   #Mostra qual o projeto
print()                                                 #Pula uma linha
print('-'*10, 'OPERAÇÕES MATEMÁTICAS', '-'*10)          #Inicia o layout com o título


n = float(input('| Digite um número real: '))           #Recebe o número float digitado
print('-' * 34)                                         #Todos desse tipo são divisórias que fazem parte do layout
resp = int(input('| O que você quer fazer com ele? |\n| Arredondar[1]                  |\n| Pegar a parte inteira[2]       |\n| Calcular raiz[3]               |\n| Fazer Fatorial[4]              |\n| Fazer a potência[5]            |\n| R: '))  #Dá 5 opções para o usuário e armazena a resposta em forma int para usar com as condições
print('-' * 34)


if resp == 1:                       #Se o usuário digitar 1 aparecerá 2 opções, se ele quer arredondar o número para baixo ou para cima, e, dependendo da resposta o valor é convertido e exibido na tela
    print('-' * 55)
    a = int(input('| Você quer arredondar para cima[1] ou para baixo[2]? |\n| R: '))
    if a == 1:
        print('-' * 55)
        print(f'| O número {n:^5} arredondado para cima é igual a: {math.ceil(n):^4}|')
        print('-' * 55)
    else:
        print('-' * 56)
        print(f'| O número {n:^5} arredondado para baixo é igual a: {math.floor(n):^4}|')
        print('-' * 56)
else:
    if resp == 2:                   #Se o usuário digitar 2, aparecerá a conversão para o número apenas com a parte inteira direto
        print('-' * 50)
        print(f'| A parte inteira do número {n:^5} é igual a: {math.trunc(n):^4}|')
        print('-' * 50)
    else:
        if resp == 3:               #Se o usuário digitar 3, ele irá fazer a raiz e perguntar se o usuário deseja arredondar o valor, se a resposta for "n", o programa termina, se for "s" ele irá perguntar se deseja arredondar para cima, baixo ou cancelar, aí o usuário escolhe e o valor é exibido na tela ou o programa encerra
            raiz = math.sqrt(n)
            print('-'*49)
            print(f'| A raíz quadrada de {n:^5} é igual a: {raiz:^10.6f}|')
            print('-' * 49)
            print('-'*36)
            r = str(input('| Deseja arredondar o valor? [S/N] |\n| R: '))
            print('-' * 36)
            if r == 's':
                print('-' * 28)
                c = int(input('| Você quer:               |\n| Arredondar para cima[1]  |\n| Arredondar para baixo[2] |\n| Cancelar[3]              |\n| R: '))
                print('-' * 28)
                if c == 1:
                    print('-' * 51)
                    print(f'| {raiz:^10.6f} arredondado para cima é igual a: {math.ceil(raiz):^4}|')
                    print('-' * 51)
                else:
                    if c == 2:
                        print('-' * 52)
                        print(f'| {raiz:^10.6f} arredondado para baixo é igual a: {math.floor(raiz):^4}|')
                        print('-'*52)
        else:
            if resp == 4:           #Se o usuário digitar 4, irá aparecer uma mensagem de aviso dizendo que o valor precisa ser inteiro e perguntando se é ou não. Se a resposta for "s", a conta é feita, se for "n" ele irá perguntar se deseja arredondar o número para cima, para baixo, pegar o valor inteiro ou cancelar. Após escolher, a conta é feita com o valor escolhido
                r = str(input('*** Para poder calcular o fatorial você precisa ter um número inteiro ***.\nO seu número é inteiro? [S/N]\nR: '))
                if r == 's':
                    print('-' * 44)
                    print(f'| O fatorial do número {n:^5} é igual a: {math.factorial(n)} |')
                    print('-' * 44)
                else:
                    print('-' * 28)
                    r2 = int(input('| Você quer:               |\n| Arredondar para cima[1]  |\n| Arredondar para baixo[2] |\n| Pegar a parte inteira[3] |\n| Cancelar[4]              |\nR: '))
                    print('-' * 28)
                    if r2 == 1:
                        print('-' * 65)
                        print(f'| O fatorial de {n:^5} arredondado para cima ({math.ceil(n):^3}) é igual a: {math.factorial(math.ceil(n))} |')
                        print('-' * 65)
                    else:
                        if r2 == 2:
                            print('-' * 66)
                            print(f'| O fatorial de {n:^5} arredondado para baixo ({math.floor(n):^3}) é igual a: {math.factorial(math.floor(n))} |')
                            print('-' * 66)
                        else:
                            if r2 == 3:
                                print('-' * 74)
                                print(f'| O fatorial de {n:^5} pegando apenas a parte inteira ({math.trunc(n):^3}) é igual a: {math.factorial(math.trunc(n))} |')
                                print('-' * 74)
            else:
                if resp == 5:       #Se o usuário digitar 5, irá aparecer uma mensagem pedindo o valor da potência para fazer a exponenciação. Após o valor ser escolhido, a conta é feita e o resultado exibido na tela
                    print('-' * 44)
                    p = int(input('| Digite um número para fazer a potência: '))
                    print('-' * 44)
                    print('-' * 61)
                    print(f'| O número {n:^5} elevado a potência  {p:^2} é igual a {math.pow(n, p):^10} |')
                    print('-' * 61)
