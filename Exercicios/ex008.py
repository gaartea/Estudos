# escreva um programa que leia um  valor em metros e a exiba convertido em centimetros e milimetros

n = int(input('Digite o tamanho(em metros) que será convertido em cm e mm, por gentileza: '))

cm = n*100
mm = n*1000

print('A medida em centimetros é de: {}cm.'.format(cm))
print('A medida em milimetros é de: {}mm.'.format(mm))