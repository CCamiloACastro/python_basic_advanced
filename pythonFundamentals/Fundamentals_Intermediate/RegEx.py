"""
Un RegEx, o expresión regular, es una secuencia de caracteres que forma un patrón de búsqueda.
RegEx se puede usar para verificar si una cadena contiene el patrón de búsqueda especificado.

... mas información en
https://www.w3schools.com/python/python_regex.asp
"""
import re

# Search the string to see if it starts with "The" and ends with "Spain":
TXT = "The rain in Spain"
x = re.search("^The.*Spain$", TXT)

if x:
    print("YES! We have a match!")
else:
    print("No match")

# Regex functions

""" 
findall
Devuelve una lista que contiene todas las coincidencias
"""

x = re.findall("ai", TXT)
print('\nfindall()')
print(x)
print(len(x))

"""
search() 
Busca una coincidencia en la cadena y devuelve un "Match object" si hay una coincidencia.
Si hay más de una coincidencia, solo se devolverá la primera aparición de la coincidencia
"""

# match
print('\nsearch()')
x = re.search('\s', TXT)
print("El primer espacio blanco esta localizado en la posición:", x.start())
print(x)
# no match
x = re.search("Portugal", TXT)
print(x)

"""
split() 
Devuelve una lista donde la cadena se ha dividido en cada coincidencia
"""
print('\nsplit()')
x = re.split("\s", TXT)
print(x)
"""
sub() 
Reemplaza las coincidencias con el texto de su elección
"""
print('\nsub()')
x = re.sub("\s", "9", TXT)
print(x)
# Reemplaza solo los 2 primeros espacios
x = re.sub("\s", "9", TXT, 2)
print(x)

# Metacharacters
# son caracteres con un significado especial

print('\n\tMetacharacters')
# [] Un conjunto de caracteres

# Encuentra todos los caracteres en minúscula alfabéticamente entre "a" y "m"
print('\n[] Set de caracteres')
x = re.findall("[a-m]", TXT)  # modificar el rango
print(x)

# .	Any character (except newline character)
print('\n. Any character')
txt = "hello helpo hemmo ho heelloo heoo he planeto"
# Busca una secuencia que empiece con "he" seguido por "cualquier-any" carácter y un "o"
x = re.findall("he..o", txt)
print(x)

# ^	Starts with

print('\n^	Starts with')
x = re.search("^hello", txt)
print(x)

if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

# $	Ends with
print('\n$  Ends with')
x = re.findall("planet$", txt)
print(x)
print(type(x))
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

# *	Zero or more occurrences
print('\n*	Zero or more occurrences')
# Busca una secuencia que empiece con "he", seguido por 0 o más (Any) caracteres, hasta que encuentre el último "o"
x = re.findall("he.*o", txt)
print(x)

# +	One or more occurrences
print('\n+	One or more occurrences')
x = re.findall("he.+n", txt)
print(x)

# ?	Zero or one occurrences
print('\n?	Zero or one occurrences')
x = re.findall("he.?o", txt)
# Esta vez no se obtendrá un match, debido a que no hay ni cero o uno sino dos caracteres entre "he" y "o"
print(x)

# {}	Exactly the specified number of occurrences
print('\n{}	Exactly the specified number of occurrences')
# "he", seguido exactamente por 3 (any) caracteres, y "o"
x = re.findall("he.{3}o", txt)
print(x)

# |	Either or
print('\n|	Either or')
txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or "stays" or mainly:

x = re.findall("falls|stays|mainly", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \ Señala una secuencia especial (caracteres especiales)
print('\n\t Special Sequences')

# \A Returns a match if the specified characters are at the beginning of the string
print('\n\A Returns a match if the specified characters are at the beginning of the string')
x = re.findall("\AThe", TXT)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")

# Devuelve una coincidencia donde los caracteres especificados están al principio o al final de una palabra
# (la "r" al principio se asegura de que la cadena se trate como una "cadena sin procesar")

# Mira si "ain" es presente al comienzo de una palabra
x = re.findall(r"\bain", TXT)

print(f'ain" es presente al comienzo de una palabra {x}')

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# Mira si "ain" esta presente al final de una palabra

x = re.findall(r"ain\b", TXT)
print(f'ain" es presente al final de una palabra {x}')

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \d Devuelve una coincidencia donde la cadena contiene dígitos (números del 0 al 9)
print('\n\d Devuelve un match donde la cadena contiene dígitos (números del 0 al 9)')
txt = "That will be 59 dollars"
print(txt)
x = re.findall("\d", txt)
print(x)

# \D	Returns a match where the string DOES NOT contain digits
print('\n Retorna un match donde el string No contenga dígitos')
x = re.findall("\D", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \S	Returns a match where the string DOES NOT contain a white space character
print('\n\S	Retorna un match donde el string No contenga espacios')
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \w Returns a match where the string contains any word characters
# (characters from a to Z, digits from 0-9, and the underscore _ character)

print('\n\w Returns a match where the string contains any word characters')
x = re.findall("\w", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \W	Returns a match where the string DOES NOT contain any word characters
# bueno para contar espacios
print('\n\W	Returns a match where the string DOES NOT contain any word characters')
x = re.findall("\W", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \Z	Returns a match if the specified characters are at the end of the string
print('\n\Z	Returns a match if the specified characters are at the end of the string')

x = re.findall("dollars\Z", txt)
print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")
x = re.findall("will\Z", txt)
print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")

print('\n\t Sets')

txt = "The rain in Spain"

print('\nCheck if the string has any a, r, or n characters:')

x = re.findall("[arn]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print('\nCheck if the string has any characters between a and n:')

x = re.findall("[a-n]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print('Check si el string tine que caracteres que nos sean  a, r, or n')

x = re.findall("[^arn]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print('\nCheck if the string has any 0, 1, 2, or 3 digits:')

x = re.findall("[0123]", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print('\nCheck if the string has any digits:')
txt = "8 times before 11:45 AM"
print(txt)
x = re.findall("[0-9]", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print('\nCheck if the string has any two-digit numbers, from 00 to 44:')
x = re.findall("[0-4][0-4]", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

print('Check if the string has any two-digit numbers, from 00 to 45:')
x = re.findall("[0-4][0-5]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# In sets, +, *, ., |, (), $,{} has no special meaning


# Match object
print('\nMatch object')
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object
print(x.span())  # returns a tuple containing the start-, and end positions of the match.
print(x.string)  # returns the string passed into the function
print(x.group())  # returns the part of the string where there was a match
