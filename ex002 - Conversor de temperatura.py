print('='*33, 'CONVERSOR DE TEMPERATURAS', '='*33)                                                                  #Coloca o título no programa
conv = int(input('| Você quer converter a temperatura de qual unidade? Celsius[1]  Fahrenheit[2]  Kelvin[3]: '))    #Recebe a unidade que está
res = int(input('| Você quer fazer a conversão para qual unidade? Celsius[1]  Fahrenheit[2]  Kelvin[3]: '))         #Recebe a unidade que será convertida
temp = float(input('| Digite a temperatura que vai ser convertida: '))                                              #Recebe os Graus


print('-'*93)                                                                                       #Coloca 93 traços no programa (Layout)
if conv == 1 and res == 2:                                                                          #Se a primeira unidade for 1 e a segunda 2, converte °C para °F
    cf = (temp * 9 / 5) + 32                                                                        #Converte °C para °F
    print(f'| {temp}°C convertidos em fahrenheit são: {cf:.2f}°F', ' '*43, '|')                     #Mostra a conversão
else:
    if conv == 1 and res == 3:                                                                      #Se não, se a primeira unidade for 1 e a segunda 3, converte °C para K
        ck = temp + 273.15                                                                          #Converte °C para Kelvin
        print(f'| {temp}°C convertidos em Kelvin são: {ck:.2f}K', ' '*43, '|')                      #Mostra a conversão
    else:
        if conv == 2 and res == 1:                                                                  #Se não, se a primeira unidade for 2 e a segunda 1, converte °F para °C
            fc = (temp - 32) * 5 / 9                                                                #Converte °F para °C
            print(f'| {temp}°F convertidos em Celsius são: {fc:.2f}°C', ' '*43, '|')                #Mostra a conversão
        else:
            if conv == 2 and res == 3:                                                              #Se não, se a primeira unidade for 2 e a segunda 3, converte °F para K
                fk = (temp - 32) * 5 / 9 + 273.15                                                   #Converte °F para Kelvin
                print(f'| {temp}°F convertidos em Kelvin são: {fk:.2f}K', ' '*43, '|')              #Mostra a conversão
            else:
                if conv == 3 and res == 1:                                                          #Se não, se a primeira unidade for 3 e a segunda 1, converte K para °C
                    kc = temp - 273.15                                                              #Converte Kelvin para °C
                    print(f'| {temp}K convertidos em Celsius são: {kc:.2f}°C', ' '*43, '|')         #Mostra a conversão
                else:
                    if conv == 3 and res == 2:                                                      #Se não, se a primeira unidade for 3 e a segunda 2, converte K para °F
                        kf = (temp - 273.15) * 9 / 5 + 32                                           #Converte Kelvin para °F
                        print(f'| {temp}K convertidos em Fahrenheit são: {kf:.2f}°F', ' '*43, '|')  #Mostra a conversão

print('-'*93)                                                                                       #Coloca 93 traços no programa (Layout)
