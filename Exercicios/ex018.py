# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('Informe o ângulo: '))

print(f'O Cosseno de {angulo}° é {math.cos(math.radians(angulo)):.2f}')
print(f'O Seno de {angulo}° é {math.sin(math.radians(angulo)):.2f}')
print(f'A Tangente de {angulo}° é {math.tan(math.radians(angulo)):.2f}')



