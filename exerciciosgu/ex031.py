distancia = float(input('Qual a distancia em km? '))
print('O valor da passagem é {:.2f}'.format(distancia*0.50 if distancia <= 200 else distancia*0.45))