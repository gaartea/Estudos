# faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa

import math

oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))

print(f'Cateto oposto: {oposto:.2f}')
print(f'Cateto adjacente: {adjacente:.2f}')
print(f'Hipotenusa: {math.hypot(oposto, adjacente):.2f}')
