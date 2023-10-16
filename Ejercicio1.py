nu = input('Escribe tu nombre de usuario: ')
ne = int(input('Escribe un número entero: '))

while ne <= 0:
    ne = int(input('Escribe un número entero POSITIVO: '))


print((nu +'\n') * ne)


##Otra forma es: 
##for i in range(ne):
##    print(nu)