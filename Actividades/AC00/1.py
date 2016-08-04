import string
A = string.ascii_lowercase
key = "uydgtnk"
encriptado = "nyhrcctxtmbohoqh"
abc = list(A)
abc_exp=[]
for num in range(10):
    abc_exp += abc

lista_indices_encriptado = []
for letra in list(encriptado):
    indice = list(abc).index(letra)
    lista_indices_encriptado.append(indice)

lista_indices_key = []
for letra in list(key):
    indice = list(abc).index(letra)
    lista_indices_key.append(indice)

lista_indices_key_exp = []
for num in range(10):
    lista_indices_key_exp += lista_indices_key

a=0
indice_letra = 0
lista_respuesta = []
for indice in range(len(lista_indices_encriptado)):
        indice_letra = lista_indices_encriptado[indice] - lista_indices_key_exp[indice]
        if indice_letra<0:
            indice_letra = (26 + lista_indices_encriptado[indice]) - lista_indices_key_exp[indice]
        lista_respuesta.append(indice_letra)

respuesta = ""
for indice in lista_respuesta:
    respuesta += abc_exp[indice]

print(respuesta)