'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Nome completo: ')

print(f'Nome completo maiusculo: {nome.upper()}')
print(f'Nome completo minusculo: {nome.lower()}')
print(f'Quantidade de letras(sem contar espaço): {len(nome) - nome.count(' ')}')
print(f'Quantidade de palavras: {len(nome.split())}')
separa = nome.split()
print(f'Quantas letras tem o primeiro nome: {len(separa[0])}') 