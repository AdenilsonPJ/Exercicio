import operator

dict_operadores={
'+':operator.add,
'-':operator.sub,
'*':operator.mul,
'/':operator.truediv
}

print('Digite um numero:')
numero1=int(input())

print('Escolha uma operação:')
operador=input()

print('Digite outro numero:')
numero2=int(input())

print(dict_operadores[operador](numero1,numero2))