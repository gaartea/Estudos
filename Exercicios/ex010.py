#crie um programa que leia o quanto de dinheiro uma pessoa tem na 
# carteira e mostre quantos dolares ela pode comprar 1*3.27


real = float(input('Cateira: '))

dolar = real*3.27

print('Você possui em sua carteira: \nR${:.2f}\nE consegue adquirir:\n${:.2f}'.format(real, dolar))