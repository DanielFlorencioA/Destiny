'''
Valor1= float(input("Digite o Primeiro valor inteiro: "))
Valor2= float(input("Digite o Segundo valor inteiro: "))
Valor3= float(input("Digite o Terceiro valor inteiro: "))
Valor4= float(input("Digite o Quarto valor inteiro: "))
Valor5= float(input("Digite o Quinto valor inteiro: "))
Media = (Valor1 + Valor2 + Valor3 + Valor4 + Valor5)/5
print("Primeiro valor é: " , Valor1)
print("Segundo valor é: " , Valor2)
print("Terceiro valor é: " , Valor3)
print("Quarto valor é: " , Valor4)
print("Quinto valor é: " , Valor5)
if Media >=0:
    print ("A media é:", Media )
else: 
    print ("Operação invalida")
'''

'''
number = int(input('Numero: '))

if number >= 1:
    for i in range(1, number):
        if number % i != 0:
            print(number, 'é primo')
        else:
            print(number, 'não é primo')
            break
elif number == 0:
    print(number, 'é zero')
else:
    print(number, 'é negativo')
'''

'''
ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
'''

'''
def verificar_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False

resultado = verificar_palindromo("arara")
print(resultado)
'''