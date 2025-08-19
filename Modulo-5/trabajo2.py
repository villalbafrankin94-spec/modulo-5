a= int(input("Ingrese el primer numero: "))
b= int(input("Ingrese el segundo numero: "))
print("calculadora")
print("seleccione una opcion")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
opcion = int(input("ingrese la opcion q desee: "))
if opcion == 1:
    print("la suma es:", a + b)
elif opcion == 2:
    print("la resta es:", a - b)
elif opcion == 3:
    print("la multiplicacion es:", a * b)
elif opcion == 4:
    if b != 0:
        print("la division es:", a / b)
    else:
        print("no se puede dividir por cero")
else:
    print("opcion invalida")