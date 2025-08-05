visitas = []
alumnosMin = 3

def espaciadoInterfaz(tipo):
     if tipo == "linea":
        print(" -------------------------")
     if tipo == "vacio":
        print("                             ")

for i in range(alumnosMin):
    print(f"Estudiante {i+1}:")
    nombre = input("Nombre: ")
    curso = input("Curso: ")
    motivo = input("Motivo: ")

    visitaIndividual = {
        "nombre": nombre,
         "curso": curso,
         "motivo": motivo
    }
    visitas.append(visitaIndividual)

conteo = len(visitas)

print("<- Cantidad de visitas: ", conteo," ->")
print("- - Datos de las visitas - -")
for i in range(conteo):
    print(" Nombre: ",visitas[i]["nombre"])
    print(" Curso: ",visitas[i]["curso"])
    print(" Motivo: ",visitas[i]["motivo"])
    espaciadoInterfaz("linea")

if visitas:
     print(visitas[0]["nombre"])
else:
     print("No hay visitas registradas.")