#ler preco de protudo e mostre seu novo preco com 5% de desconto

produto = float(input("Qual o preço do produto? "))

promocional = produto*0.95

print(f'O valor atualizado com a promoção de 5% é de R${promocional:.2f}')