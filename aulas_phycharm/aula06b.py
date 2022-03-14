texto = input('Digite algo: ')

print('|{}| é alfabético? {}'.format(texto, texto.isalpha()))
print('|{}| é número inteiro? {}'.format(texto, texto.isnumeric()))
print('|{}| é digito? {}'.format(texto, texto.isdigit()))
print('|{}| é decimal? {}'.format(texto, texto.isdecimal()))
print('|{}| é alfanumérico? {}'.format(texto, texto.isalnum()))