# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Informe os dia(s) em que o carro foi alugado: '))
distancia = float(input('Informe a quantidade de quilometro(s) rodado(s) com o veiculo: '))

formula = (dias*60) + (distancia*0.15)

print(f'O veiculo rodou {distancia:.1f}Km durante {dias} dias, logo o valor a ser pago é de R${formula:.2f}.')