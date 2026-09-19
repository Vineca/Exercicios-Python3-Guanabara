velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado no valor de: R${:.2f}'.format((velocidade -80)*7))