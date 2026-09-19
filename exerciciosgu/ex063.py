r = int(input('Quantos elementos de fibonacci você quer: '))
n0 = 0
n1 = 1
if (r == 1): print(0)
elif (r > 1):
    print(0)
    print(1)
while r > 2:
    termo = n0 + n1
    print(termo)
    n0 = n1
    n1 = termo
    r -= 1