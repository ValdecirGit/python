minha_string = "    aqui valor da variavel uva eu "

minha_string2 = "Valdecir"

minha_string3 = "qualquer texto"
                #0123456789

#tipo de variavel
print(type(minha_string))

#concatenando string
print(f"Valdecir testando concatenação com {minha_string}")

#Funções de String
print("função deixar tudo em maísculo")
print(minha_string.upper())

print("função deixar tudo em mínusculo")
print(minha_string.lower())

print("função deixar a primeira letra em Maiúsculo")
print(minha_string.capitalize())


print("função para verificar se todo texto é maiúsculo, retorna verdadeirou ou falso")
print(minha_string.isupper())

print("função para verificar se todo texto é minúsculo, retorna verdadeirou ou falso")
print(minha_string.islower())

print("função Strip para remover espaços antes e depois do texto")
print(f"antes {minha_string}")
print(f"depois {minha_string.strip()}")

print("função Replace para substituir caracter por outro")
print(minha_string.replace("variavel", "nova_variavel"))

print("função Replace para substituir todos os 'us' que encontrar no texto")
print(minha_string.replace("u", "UU"))

print("função Replace para substituir todos o primeiro 'u' que encontrar no texto")
print(minha_string.replace("u", "UU",1))

print("função Replace para substituir todos o primeiro e o segundo 'u' que encontrar no texto")
print(minha_string.replace("u", "UU",2))

print("função len para saber o tamanho da string, qntos caracter possui")
print(len(minha_string2))

print("função para ler posicao específica da stringm aqui pega o primeiro caracter")
print(minha_string2[0])

print("função para ler posicao específica da stringm aqui pega o ultimo caracter")
print(minha_string2[7])

print("função para ler partes específicas da string aqui pega o ultimo caracter")
print(minha_string2[0:3])

print("função para ler partes específicas da string de tras pra frente")
print(minha_string2[-4:-1])

print("função para retornar indice do caracter na variavel string")
print(minha_string3.index("u"))

print("função para retornar indice de onde inicia o texto completo da variavel string")
print(minha_string3.index("texto"))

print("função para retornar indice de onde inicia parte do texto da variavel string")
print(minha_string3.index("quer"))

print("Verifique se texto esta na variavel string, se existir traz valor como true, senão como false")
x = "texto" in minha_string3               
print(x)


print("texto de multiplas linhas usando aspas ... ")
minha_string4 = """linha 1,
linha 2,
linha 3,
linha 4.
                """
print(minha_string4)          

print("texto de multiplas linhas usando caracter de escape '\n' ... ")
minha_string4 = "linha 1,\nlinha 2,\nlinha 3,\nlinha 4."
print(minha_string4)  


print("adicionando aspas no texto usando caracter de escape '\"' ... ")
minha_string4 = "adicionando entre \"aspas\" no texto"
print(minha_string4)  


