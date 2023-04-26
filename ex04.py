algo=input('Digite algo:')
print('O tipo primitivo desse valor é:', type(algo))
print('Só existem epaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em letra maiúscula?', algo.isupper())
print('Está em letra minúscula?', algo.islower())
print('Está capitalizada?', algo.istitle())
# algo é um objeto=tem características, atributos e métodos
# e realiza funcionalidades