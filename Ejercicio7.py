correo = input ('Escribe un correo eléctrónico: ')
user = ''

while '@' not in correo:
    correo = input('Escribe un correo electrónico VÁLIDO: ')

c = len(correo)

for i in range(c):
    if correo[i] != '@':
        user = user + correo[i]
    if correo[i] == '@':
        break

print('Tu correo con dominio ceu.es será:', user + '@ceu.es')