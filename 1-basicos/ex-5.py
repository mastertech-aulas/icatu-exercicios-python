from random import randint

numeros = []
pares = []
impares = []

for i in range(10):
    numero = randint(0, 10)
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('A lista gerada aleatoriamente foi:', numeros)
print('Os números pares são:', pares)
print('Os números ímpares são:', impares)