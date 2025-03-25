p1 = (input("¿Como te gusta que te llamen?  "))
print("Bueno", p1, "¿y cuantos años tienes?  ")
p2 = int(input())
print(p1, "¿sabes a cuantos meses equivale tu edad?")
pregunta = (input())
num = p2*12
lista1 = ["Si","si","SI"]
lista2 = ["No","no","NO"]
if pregunta in lista1:
    p3= int(input("Dime a cuanto equivale: "))
elif pregunta in lista2:
    print("Esto equivale a ", num, "meses.")
if p3 >num:
    print("Estuviste cerca, el número correcto era", num)
elif p3 == num:
    print("Correcto")
elif p3 <num:
    print("Estuviste cerca, el número correcto era", num)