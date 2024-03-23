msg = input("Digite algo: ")

print ("O tipo primitivo desse valor é ", type(msg))
print ('Só tem espaço? ', msg.isspace())
print ('{} é um numero? '.format(msg), msg.isnumeric())
print ('{} é alfabetica? '.format(msg), msg.isalpha())
print ('{} é alfanumerico? '.format(msg), msg.isalnum())
print ('{} esta em maiusculo? '.format(msg), msg.isupper())
print ('{} esta em minusculo? '.format(msg), msg.islower())
print ('{} esta em capitalizada? '.format(msg), msg.istitle())

