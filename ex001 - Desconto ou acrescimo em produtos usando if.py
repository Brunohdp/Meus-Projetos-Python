valor = float(input('Digite o valor do produto: R$'))
res = str(input('Você quer pagar a vista ou parcelado? '))
j = valor + (valor*20/100)
d = valor - (valor*35/100)
if res == 'parcelado':
    print(f'O valor parcelado tem um acrescimo de 20% no valor total, portanto, você pagará: R${j:.2f} pelo produto!')
else:
    print(f'O pagamento a vista tem um desconto de 35% do valor total, portanto, você pagará: RS{d:.2f} pelo produto!')
