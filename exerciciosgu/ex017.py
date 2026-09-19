import math
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
Hipotenusa = math.sqrt(math.pow(cateto_oposto,2) + math.pow(cateto_adjacente, 2))
print('Um triangulo com cateto oposto = {}, cateto adjacente = {} tem sua hipotenusa = {:.2f}'.format(cateto_oposto, cateto_adjacente, Hipotenusa))





