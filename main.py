import random
n = random.randint(1, 100)
cont = 1

tentativa = int(input('Tente acertar um número inteiro de 1 a 100: '))
while tentativa != n:
    cont += 1

    if tentativa > n:
        print('O número é menor')

    elif tentativa < n:
        print('O número é maior')

    elif tentativa == n:
        print('Acertou!')
        break

    tentativa = int(input('Tente acertar um número inteiro de 1 a 100: '))
print(f'Quantidade de tentativas: {cont}')








