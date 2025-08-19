lista1= int(input("Ingrese el primer numero: "))
lista2= int(input("Ingrese el segundo numero: "))

print("calculadora")
print("seleccione una opcion")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion = int(input("ingrese la opcion q desee: "))
if opcion == 1:
    print("la suma es:", lista1 + lista2)
elif opcion == 2:
    print("la resta es:", lista1 - lista2)
elif opcion == 3:
    print("la multiplicacion es:", lista1 * lista2)
elif opcion == 4:
        print("la division es:", lista1 / lista2)
        