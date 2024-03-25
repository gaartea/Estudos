# crie um programa que leia um numero real qlqer e mostre na tela a sua porção inteira
# ex ; digite um numero: 6.127 o numero 6.127 tem a parte inteira de 6

import math

n = float(input("Digite um numero: "))

print(f'O numero {n} tem a parte inteira de {math.trunc(n)}.')