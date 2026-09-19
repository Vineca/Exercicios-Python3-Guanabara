nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media >= 7: print('Aprovado')
elif media < 5: print('Reprovado')
else:print('Recuperação')
