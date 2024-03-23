#crie um programa que leia o quanto de dinheiro uma pessoa tem na 
# carteira e mostre quantos dolares ela pode comprar 4,95 hoje(23/03/24)


real = float(input('Cateira: '))

dolar = real/4.95

print('Você possui em sua carteira: \nR${:.2f}\nE consegue adquirir:\n${:.2f}'.format(real, dolar))