calc = {
    1: "Sumar",
    2: "Restar",
    3: "Multiplicar",
    4: "Dividir"
}
print("calculadora")
print("seleccione una opcion")

opcion = int(input("ingrese la opcion: "))
a= int(input("ingrese un numero: "))
b= int(input("ingrese otro numero: "))
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