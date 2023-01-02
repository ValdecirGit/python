# Collections (lista)
#-------------------------------------------------------------------------------------------------
familia = ["Valdecir", "Neia", "Erick", "Caue", "Valdecir"]
#                  0       1        2       3
#                 -4      -3       -2      -1

 
print("captura o primeiro valor da lista")
#print(familia[0]) 
print("captura nome da lista de tras pra frente")
#print(familia[-1]) 
print("captura do índice tal pra frente")
#print(familia[2:]) 
print("captura do índice inicial até indice final, este tipo de pesquisa exclui indice final")
#print(familia[2:3]) 

#alterando valor da lista
#--------------------------------------------------------------------------
print(f"O valor deste índice 2 neste momento é: {familia[2]}")
#familia[2] = "Erick Wallace"
print(f"O valor deste índice 2 foi alterado para: {familia[2]}")

#funções para trabalhar com listas
#--------------------------------------------------------------------------

print("Adicionando outra lista na minha lista 'familia' ja existente usando função EXTEND")
#familia.extend(["Doralicia","Iraci"])
#print(familia)

print("Adicionando somente 1 valor ao final da minha lista existente usando função APPEND")
#familia.append("Lilica")
#print(familia)

print("Inserindo novo valor no meio da lista usando insert e dizendo em qual indice adiciona-lo usando função INSERT")
#familia.insert(1,"Pingo")
#print(familia)

print("Remover último valor da lista usando função POP")
#familia.pop()
#print(familia)

print("Remover valor específico da lista usando função REMOVE")
#familia.remove("Pingo")
#print(familia)

print("Limpar toda a lista usando função CLEAR")
#print(familia)
#### familia.clear()
#print(familia)

print("Retorna índice da lista cfe valor")
#print(familia.index("Caue"))

print("Retorna quantos itens iguais eu tenho na lista")
print(f"A lista possui {familia.count('Valdecir')} nomes = Valdecir")
print(f"A lista possui {familia.count('Doralicia')} nomes = Doralicia")
print(f"A lista possui {familia.count('Neia')} nomes = Neia")
print(f"A lista possui {familia.count('Joao')} nomes = Joao")


# lista de numeros
idade_familia = [45,39,20,12,45,88,61]
#print("Idades da família")
#print(idade_familia)

print("Ordenando idade da família usando a função SORT")
#idade_familia.sort()
#print(idade_familia)

print("Ordenando listas de nomes (ordem alfabética) da família usando a função SORT")
#familia.sort()
#print(familia)

print("Inverte valores da lista de idade da familia usando função REVERSE")
#idade_familia.reverse()
#print(idade_familia)

print("Inverte valores da lista de nomes da familia usando função REVERSE")
#familia.reverse()
#print(familia)


# copiar listas
#---------------------------------------------------------------
print("copiando lista familia para familia2, usa espaço da memória para copiar como referência")

familia2 = familia

print(familia2)

print("remove valdecir da variavel familia")
familia.remove("Valdecir")
print(f"varivel familia= {familia}")
print(f"varivel familia2= {familia2}")

print("copiando lista familia para familia3, copia para nova variavel como nova lista usando função COPY")

familia3 = familia.copy()

print("remove valdecir da variavel familia")
familia.remove("Caue")
print(f"varivel familia= {familia}")
print(f"varivel familia3= {familia3}")


# lista imutável, tuple, que não pode ser alterada
print("Listas TUPLE, imutável, não podem serem alteradas")
coordenadas = ("25 49 40 52 43 30")
print(coordenadas)

print("Retorna indice 0")
print(coordenadas[0])

print("Qtde de 25")
print(coordenadas.count("25"))
