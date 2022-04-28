#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Informe um numero inteiro: '))
n2 = int(input('Informe outro numero inteiro: '))
soma = n1+n2
if n1 > n2:
    for a in range(n2+n1):
        print(soma)
        

    print('Os numeros são iguais.')
print(f'A soma dos numeros foi de {soma}')