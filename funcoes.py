#definindo uma função
#def big_mac():
#    print("sanduiche bigMac")

#chamada da função
#print("inicio")
#big_mac()    
#print("fim")

def fazer_bigmac(nome):
    print(f"fazer sanduiche bigmac para {nome}")

def fazer_batata(tamanho):
    print(f"fazer batata {tamanho}")

def refrigerante(tipo, tamanho):
    print(f"refrigerante {tipo} {tamanho}")

def fazer_combo_bigmac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_bigmac(nome)
    fazer_batata(tamanho_batata)
    refrigerante(tipo_refri, tamanho_refri)

#fazer_bigmac("Valdecir")    
#fazer_batata("Grande")
#refrigerante("Coca","Media")
#fazer_bigmac("Neia")    
#fazer_bigmac("Erick")   
# fazer_combo_bigmac("Valdecir", "grande", "guarana", "pequeno") 

# exemplo de função de soma simples
def soma_num(num1, num2):
    return num1 + num2
resultado = soma_num(100, 50)
print(f"O resultado da soma é {resultado}")    

# exemplo de função para descobrir o maior numero da lista
def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([7, 5, 3, 5, 8, 100, 101, 2, 4, 99, 1592, -45])

print(f"O maior numero da lista é {resultado}")    
