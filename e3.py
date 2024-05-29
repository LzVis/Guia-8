matriz_notas = [
    ["Juan", [5, 2, 6], "Matemáticas"],
    ["María", [4, 6, 3], "Ciencias"],
    ["Carlos", [7, 3, 5], "Historia"],
    ["Ana", [2, 6, 1], "Matemáticas"],
    ["Pedro", [5, 1, 7], "Ciencias"],
    ["Laura", [6, 7, 3], "Historia"],
    ["Luis", [4, 5, 2], "Matemáticas"],
    ["Sofía", [6, 3, 4], "Ciencias"],
    ["David", [7, 2, 5], "Historia"],
    ["Elena", [5, 6, 7], "Matemáticas"],
    ["Miguel", [3, 4, 1], "Ciencias"],
    ["Clara", [7, 5, 2], "Historia"],
    ["Javier", [4, 6, 3], "Matemáticas"],
    ["Paula", [5, 2, 7], "Ciencias"],
    ["Diego", [6, 3, 4], "Historia"],
    ["Raquel", [7, 5, 1], "Matemáticas"],
    ["Mario", [6, 4, 2], "Ciencias"],
    ["Eva", [3, 7, 5], "Historia"],
    ["Julia", [4, 6, 1], "Matemáticas"],
    ["Daniel", [2, 5, 3], "Ciencias"]
]

with open("datos.txt","w+") as f:
    for i in matriz_notas:
        sum = 0
        for x in i[1]:
            sum+=x
        nota = sum/3
        nota = round(nota,2)
        estado = "Aprobado" if nota>=4 else "Desaprobado"
        f.write(str(i[0])+" "+(str(nota)) + " " + str(i[2])+ " " + estado + "\n")