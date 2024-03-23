# faca um programa que leia altura e larguar de uma parede em metros, calcula
# calcula sua area e a quantidade de tinta necessario para pinta-la, sabendo que cada lata de tinta pinta uma area de 2m²
# (considerando que não exista outro tipo de lata de tinta com menor litragem)

print('PROGRAMA - PINTOR - 2000')

altura = float(input('Informe a altura da parede(em metros), por gentileza:'))
largura = float(input('Informe a largura da parede(em metros), por gentileza:'))

m2 = altura*largura
tinta = m2/2+m2%2

print('Sera necessario {:.0f} lata(s) de tinta(s) para pintar a parede de {:.3f}m².'.format(tinta, m2))