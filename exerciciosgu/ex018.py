angulo = float(input('Digite um angulo em graus: '))
import math
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem o seno = {:.2f}, cosseno = {:.2f} e a tangente = {:.2f}'.format(angulo, seno, cosseno, tangente))


