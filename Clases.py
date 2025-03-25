salario = float(input("Ingrese su salario: "))
mes = int(input("Ingrese en numeros en qué mes está: "))
lista1 = [1,3,5,7,8,10,12]
lista2 = [4,6,9,11]
lista3 = [2]
import calendar
valor1 = (salario//31)
valor2 = (salario//30)
if mes in lista1:
    print("Su salario diario en este mes es aproximadamente de ", valor1," pesos.")
elif mes in lista2:
    print("Su salario diario en este mes es de aproximadamente ", valor2," pesos.")
elif mes in lista3:
    año = int(input("Ingrese el año actual: "))
    diasf = 29 if calendar.isleap(año) else 28
    valor3 = (salario // diasf)
    print("Su salario diario en este mes es de aproximadamente ", valor3," pesos.")
num = (salario*110)//100
print("Si a su salario se le agrega el 10%, sería de ", num,"pesos.")
mitad = (salario//2)
print("La mitad de su salario es de ", mitad, "pesos")
sum = salario*12
print("En todo el año, ganaría ",sum, "pesos." )