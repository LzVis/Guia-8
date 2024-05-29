NombresYApellidosLista = []
while True:
    CantidadDeNombresAIngresar = int(input("introduzca la cantidad de datos a ingresar: "))
    print("----------------------")
    Confirmacion = input("Introduzca '-' para corregir la cantidad\nEnter y omitir para continuar\n")
    if Confirmacion != "-":
        break
    else:
        "Reiniciando ...\n"
for i in range(CantidadDeNombresAIngresar):
    Nombre = (input("Introduzca el nombre: ")).capitalize()
    Apellido = (input("Introduzca el apellido: ")).capitalize()
    NombresYApellido = Nombre + " " + Apellido 
    NombresYApellidosLista.append(NombresYApellido)

#NombresYApellidosLista = ["cristian valdes","antonio rojas"]

with open("NombresYApellidosLista.txt","a+") as f:
    for i in NombresYApellidosLista:
        f.writelines(i+"\n") 
    f.seek(0)
    lineas = f.readlines()
    print("Contenido actual del archivo:")
    for linea in lineas:
        print(linea, end='')