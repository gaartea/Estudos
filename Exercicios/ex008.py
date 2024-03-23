# escreva um programa que leia um  valor em metros e a exiba convertido em centimetros e milimetros

n = float(input('Digite o tamanho(em metros) que será convertido em cm e mm, por gentileza: '))

cm = n*100
mm = n*1000

print('A medida em centimetros é de: {:.0f}cm.'.format(cm))
print('A medida em milimetros é de: {:.0f}mm.'.format(mm))