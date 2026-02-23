'''
Curso: Lenguaje de programación Python
Facultad de Ingeniería, UNAM
Transformación digital
IT-PRO

Ejercicios: Estructuras de decisión y bucles en Python

Nombre: Aura del Carmen García Vázquez
No. cuenta: 425121087

Fecha de entrega: 23/02/2026
'''
#EJ1
print("\nEJERCICIO 1 MAYOR DE EDAD")

while True:
    try:
        edad=int(input("Ingresa edad: "))

        if edad < 0 or edad > 150:
                print("\n Edad invalida o ¿¡vampiro?!")
                continue
        break

    except ValueError: 
        print("Ingresa numero entero valido")

if edad >= 18:
    print("Mayor de edad")
else: 
    print("Menor de edad")

#EJ2
print("\nEJERCICIO 2 PAR O IMPAR")

while True:
    try:
        num=int(input("Ingresa num: "))
        break

    except ValueError: 
        print("Ingresa numero entero valido")

if num%2 == 0:
    print("Par")
else: 
    print("Impar")

#EJ3
print("\nEJERCICIO 3 Positivo, negativo o cero")

while True:
    try:
        num3=float(input("Ingresa num: "))
        break

    except ValueError: 
        print("Ingresa numero valido")

if num3 > 0:
    print("Num. Positivo")
elif num3 < 0: 
    print("Num. Negativo")
else:
    print("Cero")


#EJ4
print("\nEJERCICIO 4 Descuento en tienda")

while True:
    try:
        total_compra=float(input("Compra total: "))
        if edad < 0:
                print("\n Ingrese valor positivo")
                continue
        break

    except ValueError: 
        print("Ingresa cantidad valido")

if total_compra >= 1000:
    print(total_compra*0.9)
else:
    print(total_compra)

#EJ5
print("\nEJERCICIO 5 CLASIFICACIÓN CON LETRA")

while True:
    try:
        calif=int(input("Calificación: "))
        if calif < 0 or calif > 10:
                print("\n Calificación invalida")
                continue
        break

    except ValueError: 
        print("Invalido: Ingresa entero postivo dentro del rango")

if calif >= 9:
    print("A")
elif calif == 8:
    print("B")
elif calif == 7:
    print("C")
elif calif == 6:
    print("D")
else:
    print("F")

#EJ6
print("\nEJERCICIO 5 CLASIFICACIÓN CON LETRA")

while True:
    try:
        calif=int(input("Calificación: "))
        if calif < 0 or calif > 10:
                print("\n Calificación invalida")
                continue
        break

    except ValueError: 
        print("Invalido: Ingresa entero postivo dentro del rango")

if calif >= 9:
    print("A")
elif calif == 8:
    print("B")
elif calif == 7:
    print("C")
elif calif == 6:
    print("D")
else:
    print("F")

