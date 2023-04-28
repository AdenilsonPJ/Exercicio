print('Digite um numero:')
numero1=int(input())

print('Digite uma operação:')
operador=input()

print('Digite outro numero:')
numero2=int(input())

if operador=='+':
    resultado=numero1+numero2
    print(resultado)
elif operador=='-':
    resultado=numero1-numero2
    print(resultado)
elif operador=='*':
    resultado=numero1*numero2
    print(resultado)
elif operador=='/':
    resultado=numero1/numero2
    print(resultado)

else:
    print('Operação Incorreta!')