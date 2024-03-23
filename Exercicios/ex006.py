# crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz

n = int(input('Digite um numero: '))

dobro=n*2
triplo=n*3
raiz=n**(1/2)

print('Numero avaliado: {}'.format(n))
print('Dobro: {}'.format(dobro))
print('Triplo: {}'.format(triplo))
print('Raiz Quadrada: {:.2f}'.format(raiz))