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
#------------------------------------------------------------------
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
print("resto da divisão 10 / 3  mod:")
print(10 % 3)
print("exponenciação 3 elevado 3:")
print(3 ** 3)

#outros calculos 
#------------------------------------------------------------------
print('neste calculo, primeira multiplica depois soma')
print(3 + 5 * 7 + 3)
print('neste calculo, primeira soma o que tem dentro do parenteses depois multilplica')
print((3 + 5) * (7 + 3))


#funcoes
#------------------------------------------------------------------

#abosulto
print("função abs (absoluto):")
print(abs(-15))
print("função pow (exponenciação):")
print(pow(3,3))
print("função max (numero maximo):")
print(max(1,5,8,-7,-59))
print("função min (numero minimo):")
print(min(1,5,8,-7,-59))
print("função round (arredondamento automatico pra cima ou baixo):")
print(round(8.3))
print("função round (arredondamento automatico pra cima ou baixo):")
print(round(8.6))

#outra biblioteca para arredondamento
import math
#------------------------------------------------------------------
print('arredondamento para baixo')
print(math.floor(8.9))
print(math.floor(8.2))
print('arredondamento para cima')
print(math.ceil(8.9))
print(math.ceil(8.000002))
print('raiz quadrada')
print(math.sqrt(9))

