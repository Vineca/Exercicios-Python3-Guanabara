from random import randint
cont = 0
while True:
    num = int(input('Digite um numero: '))
    parimpar = input('Voce quer par ou impar? [P/I] ').upper().strip()
    computador = randint(0, 10)
    if (parimpar == 'P' and (num+computador)%2 == 0) or (parimpar == 'I' and (num+computador)%2 != 0) :
        print(f'Você jogou {num} e o computador jogou {computador}.Você venceu!')
        cont += 1
    else :
        print ('voce perdeu otario')
        break
print(cont)