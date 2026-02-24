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
print("\nEJERCICIO 6 TIPO DE TRIANGULO")

while True:
    try:
        lado1=float(input("Primer lado: "))
        lado2=float(input("Segundo lado: "))
        lado3=float(input("Tercer lado: "))

        if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
            print("\n No es triángulo")
            continue
        break

    except ValueError: 
        print("Invalido: ¿metiste letras o simbolos raros?")

if lado1 == lado2 and lado2 == lado3:
    print("Triángulo Equilátero")
elif lado1 == lado2 or lado1 == lado3:
    print("Triángulo Isósceles")
else:
    print("Triángulo Escaleno")

#EJ7
print("\nEJERCICIO 7 CAJERO SIMPLE")
saldo_inicial=float(input("Saldo inicial: "))
saldo=saldo_inicial
while True:
    try:
        print("\n---------CAJERO MENU-------------")
        print("1) Consultar Saldo")
        print("2) Depositar")
        print("3) Retirar")
        print("4) Salir")


        opcion=input("\nIngrese la opción deseada: ")
        match opcion:
            case "1":
                print(f"Su saldo es de: {saldo}")
                print("--------------")
                continue
            case "2":
                deposito=float(input("Depositar: "))
                saldo=saldo + deposito
                print(f"Finaliza con: {saldo}")
                print("--------------")
                continue
            case "3":
                retiro=float(input("Retirar: "))
                saldo=saldo - retiro
                print(f"Ahora tiene: {saldo}")
                print("--------------")
                continue
            case "4":
                break

    except ValueError: 
        print("Invalido: ¿metiste letras o simbolos raros?")

#EJ8
print("\nEJERCICIO 8 Acceso con doble condición")

while True:
    try:
        edad=int(input("Ingresa edad: "))
        credencial= input("¿Tiene credencial? (S/N): ")
        if edad < 0 or edad > 150:
            print("\n Edad invalida")
            continue
        break

    except ValueError: 
        print("Ingresa numero entero valido")

if edad >=18  and credencial == "S":
    print("\nAcceso permitido")
else:
    print("\nAcceso denegado")


#EJ9
print("\nEJERCICIO 9 RANGO CON COMPARACIÓN ENCADENADA")

while True:
    try:
        num9=float(input("Ingresa numero: "))
        break

    except ValueError: 
        print("Ingresa numero valido")

if 0 <= num9 <= 100:
    print("\n Dentro del rango")
else:
    print("\nFuera del rango")

#EJ10
print("\nEJERCICIO 10 USUARIO Y CONTRASEÑA")

user=input("Ingresa usuario: ")
password= input("Ingresa contraseña: ")

if user == "admin"  and password == "1234":
    print("\nAcceso")
else:
    print("\nAcceso denegado")

#Me cansé de poner el try-except ValueError
#EJ11
print("\nEJERCICIO 11 VOCAL O CONSONANTE")

letra11= str(input("Ingresa letra: ")).lower()
print(letra11)

if len(letra11)>1:
    print("Entrada inválida")
else:
    if letra11 not in ["a","e","i","o","u"]:
        print("Consonante")
    else:
        print("Vocal")

#EJ12
print("\nEJERCICIO 12 LISTA DE INVITADOS")

invitados=["ana","luis","paco"]
nombre=str(input("Ingresa nombre: ")).lower()
print(nombre)

if nombre in invitados:
    print("Invitado")
else:
    print("No invitado")

#EJ13
print("\nEJERCICIO 13 CONTADOR CON WHILE")
a=0
while a != 10:
    a+=1
    print(a)

#EJ14
print("\nEJERCICIO 14 SUMA ACUMULADA(TERMINA CON CERO)")
c=0
b=None
while b != 0:
    b=float(input("Ingresa número a sumar o cero para terminar: "))
    c+=b
    if b != 0:
        continue
    print(f"Suma = {c}")

#EJ15
print("\nEJERCICIO 15 ADIVINA EL NÚMERO")
guess=7
num15=0
while num15 != guess:
    num15=int(input("Ingresa número: "))
    if num15 > guess:
        print("Muy alto")
        continue
    elif num15 < guess:
        print("Muy bajo")
        continue
    else: 
        print("Correcto")

#EJ16
print("\nEJERCICIO 16 DO-WHILE SIMULADO: MENÚ QUE SE REPITE")
while True:
    print("\n---------MENU-------------")
    print("1) Saludar")
    print("2) Mostrar tabla de 5")
    print("3) Salir")

    opcion=input("\nIngrese la opción deseada: ")
    match opcion:
        case "1":
            print("--------------")
            print("Holis, bolis, este es un saludo")
            print("--------------")
            continue
        case "2":
            print("--------------")            
            a=0
            while a != 10:
                a+=1
                print(a*5)
            print("--------------")
            continue
        case "3":
            print("--------------")
            break
        case _:
            print("--------------")
            print("Escoja entre las opciones")
            continue

#EJ17
print("\nEJERCICIO 17 TABLA DE MULTIPLICAR")
a=int(input("Ingrese entero: "))
for i in range(10):
    print(a*(i+1))

#EJ18
print("\nEJERCICIO 18 SUMA DE PARES")
n=int(input("Ingrese entero: "))
suma=0
for i in range(2,n+1,2):
    suma+=i
print(f"Suma de los pares hasta {n} es de {suma}")

#EJ19
print("\nEJERCICIO 19 ENUMERA CARACTERES")
txt=list(input("Ingrese texto: "))
print(txt)

for i in enumerate(txt):
    print(i)

#No puede ingresar cero, falta marcar error
#EJ20
print("\nEJERCICIO 20 PROMEDIO DE CALIFICACIÓN")
k=int(input("Ingrese cantidad a promediar: "))
sum_prom=0
for i in range(k):
    nw_cali=float(input(f"Ingresa calificación {i+1}: "))
    sum_prom+=nw_cali
print(sum_prom/k)

#EJ21
print("\nEJERCICIO 21 CONTRASEÑA  CON 3 INTENTOS")
count=0
while True:
    count+=1
    password=input(f"Intento {count}: Ingresa contraseña: ")
    if password == "1234":
        print("Acceso")
        break 
    elif count ==3:
        print("Bloquedo")
        break        

#EJ22
print("\nEJERCICIO 22 SALTAR MÚLTIPLOS DE 3")
impr=0
while impr != 30:
    impr+=1
    if impr % 3 == 0:
        continue
    print(impr)

#EJ23
print("\nEJERCICIO 23 BUSCAR ELEMENTO (for-else)")
nums=[4,8,15,16,23,42]
n=int(input("Ingrese entero: "))

for i,valor in enumerate(nums):
    if n == valor:
        print("Encontrado")
        break
else:
    print("No encontrado")
    

#EJ24
print("\nEJERCICIO 24 RETO INTEGRADOR: MINI SISTEMA DE INSCRIPCIÓN")
while True:
    nombre=str(input("Nombre: ")).strip()
    edad=int(input("Edad: "))
    carrera=str(input("Carrera: "))
    if nombre=="":
        print("Error en el nombre, vuelve a ingresar los datos\n")
        continue
    break
if edad < 18:
    print("No elegible")
else: 
    print("Registro existoso")

print(nombre,edad,carrera)
