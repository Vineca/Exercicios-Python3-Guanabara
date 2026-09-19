contagem = 'zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
numero = int(input('Digite um numero entre 0 e 20: '))
while not 0 <= numero <= 20:
    numero = int(input('Digite denovo um numero entre 0 e 20: '))
print(contagem[numero])