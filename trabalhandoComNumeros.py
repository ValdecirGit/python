num1 = 5
num2 = 3.5
# verificar tipo de dados
print(type(num1))
print(type(num2))
#converter um tipo de dados para outro
a = float(num1)
b = int(num2)
valor = float("8")
valor2 = int("10")
# nao converte valor quebrado para inteiro
# valor3 = int("3.5")
valor4 = "3.5"
#converter string para float, primeiro converte pra float, depois pra inteiro
valor3 = int(float("3.5"))
print(valor3)
print(type(valor3))

#Operadores Aritméticos
print("soma 5 + 3.5 :")
print(num1 + num2)
print("subtração 5 - 3.5 :")
print(num1 - num2)
print("multiplicação 5 * 3.5 :")
print(num1 * num2)
print("divisão 10 / 3 :")
print(10 / 3)
print("flordivision:")
print(10 // 3)
print("resto da divisão 5 / 3.5  mod:")
print(num1 % num2)
print("exponenciação 3 elevado 3:")
print(3 ** 3)



