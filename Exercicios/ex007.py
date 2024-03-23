# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

n1 = float(input('Digite a nota da primeira prova do aluno(a), por gentileza: '))
n2 = float(input('Digite a nota da segunda prova do aluno(a), por gentileza: '))

media = (n1+n2)/2

print('A média do aluno(a) é de {:.1f}'.format(media))