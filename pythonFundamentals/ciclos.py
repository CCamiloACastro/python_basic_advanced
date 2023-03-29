# Uso de for

for num in range(1, 6):  # OUTPUT 1 2 3 4 5
    print(num)
# uso de While

valid_response = False
while not valid_response:
    response = input("Dí que 'si': ")
    if response.lower() == 'si':
        valid_response = True
        print('Gracias <3')
    else:
        print("Ayy porfa!!!")
