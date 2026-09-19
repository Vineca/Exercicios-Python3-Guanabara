lista = ('pão', 2 , 'cafe', 1 , 'chá' , 50 , 'bulacha' , 2, 'queijo', 7, 'goiabada', 6 )
for comida in lista:
    if lista.index(comida) %2 == 0 : print(comida,'-'*20, end=' ')
    else : print(comida)
