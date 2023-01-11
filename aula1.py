print('Outro')
print('outro 1')
# digite 3 números e aponte o maior número

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print('O maior número: {}'.format(n1))

elif n2 > n1 and n2 > n3:
    print('O maior número é: {}'.format(n2))

elif n3 > n1 and n3 > n1:
    print('O maior número é: {}'.format(n3))