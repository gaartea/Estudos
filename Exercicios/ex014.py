#escreva um programa que leia a temperatura em graus Celsius e converta em Fahrenheit F=C * 1,8+32  

c = float(input('Digite a temperatura(°C): '))
f = c*1.8+32

print(f'{c}°C equivale a {f:.1f}°F')