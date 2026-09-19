dicionario = {}
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Media de {dicionario["nome"]}: '))
dicionario['situação'] = 'Aprovado' if dicionario['media']>7 else 'Reprovado'
for c,v in dicionario.items():
    print(f'{c}: {v}')