f = input("Escr la fecha de tu nacimiento en formato: dd/mm/aaaa: ")
dia = f[:f.find('/')]
mya = f[f.find('/')+1:]
mes = mya[:mya.find('/')]
año = mya[mya.find('/')+1:]

print('Naciste el día', dia , 'del mes', mes , ' y del año', año)