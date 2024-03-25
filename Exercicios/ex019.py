 # Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
#lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nome1 = input('Escreva o nome do primeiro aluno: ')
nome2 = input('Escreva o nome do segundo aluno: ')
nome3 = input('Escreva o nome do terceiro aluno: ')
nome4 = input('Escreva o nome do quarto aluno: ')

lista = [nome1,nome2,nome3,nome4]

print (f'O escolhido foi: {random.choice(lista)}')