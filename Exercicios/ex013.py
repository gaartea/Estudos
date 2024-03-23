#faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Digite o salario atual do funcionário (em R$): '))

aumento = salario+(salario*0.15)

print(f'Salario atual: R${salario:.2f}')
print(f'Salario com aumento(15%): R${aumento:.2f}')