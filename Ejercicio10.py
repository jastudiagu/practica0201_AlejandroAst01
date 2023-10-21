lista = input('Escribe tu lista de la compra separando las cosas usando una coma: ')

for i in range (len(lista)):
    if lista[i] != ',':
        print(lista[i])