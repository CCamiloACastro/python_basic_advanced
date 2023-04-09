# json file
import json
# Conversion Dictionary to Json

# Ejemplo 1
x = {
    "name": "Camilo",
    "age": 24,
    "country": "Colombia",
    "languages": ["Python", "Flutter", "Matlab"]
}
# convert into JSON with ident = 2 = 2
y = json.dumps(x, indent=2 )
# the result is a JSON string:
print(type(y))
print(y)

json_file1 = open("jsonfile1.json", "w+")
json_file1.write(y)
json_file1.close()

# Ejemplo 2

json_file2 = open("jsonfile2.json", "w+")

json_test = {
    "name": "Camilo",
    "surname": "CCamiloACastro",
    "age": 24,
    "languages": ["Python", "Flutter", "Matlab"]
}
# conversión y escritura en el archivo abierto
json.dump(json_test, json_file2, indent=2)

json_file2.close()

# Lectura "r" por defecto
with open("jsonfile2.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
# Convert from JSON to Python (dictionary):
json_dict = json.load(open("jsonfile2.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])
