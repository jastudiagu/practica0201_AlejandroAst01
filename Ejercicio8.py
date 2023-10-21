p = input("Introduce un precio con dos decimales: ")

print(p[:p.find('.')], 'euros y' ,  p[p.find('.')+1:] , 'céntimos.')
