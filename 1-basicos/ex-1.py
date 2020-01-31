numeros = []

for i in range(4):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

media = (numeros[0] + numeros[1] + numeros[2] + numeros[3]) / 4

print('A média dos números é', media)