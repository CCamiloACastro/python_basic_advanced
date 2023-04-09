# File Handling Basic

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("archivo2.txt", "w+")
txt_file.write("Mi nombre es Camilo\nSoy Colombiano\n24 años\nY estoy practicando Python")
txt_file.write("\npara hacer diferentes programas")
txt_file.close()

with open("archivo2.txt", "a") as my_other_file:
    my_other_file.write("\nque puedan ayudar a la sociedad")

# "r" para leer, no puedo colocar un método read cuando se abre el archivo en "w"
# A mí solo me deja un read a la vez, open (read() o readlines() o un recorrido) close

file = open("archivo2.txt", "r")
# lee todas las lineas
print(file.read())
file.close()

file = open("archivo2.txt", "r")
print(file.read(10))
file.close()

file = open("archivo2.txt", "r")
# readlines me llama línea como una lista
print(file.readlines())
file.close()

file = open("archivo2.txt", "r")
print("\nLinea por linea\n")
print(file.readline())
print(file.readline())
file.close()

with open("archivo2.txt", "r") as text_file:
    print(text_file.readlines())

with open("archivo2.txt", "r") as text_file:
    count = 0
    for line in text_file.readlines():
        count += 1
        print(f"line ----> {count}")
        print(line)
