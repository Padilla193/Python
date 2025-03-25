s = float(input("Dime cuanto te ganas semanalmente: "))
h = int(input("Cuantas horas trabajas demas: "))
hT = int(input("Cuantas horas debiste trabajar: "))
valor1 = s + (s/2)
valor2 = s + s
ht = hT+h
if ht == 40:
    print("Te debes ganar ", s)
elif ht == 60:
    print("Te debes ganar ", valor1)
elif ht == 80:
    print("Te debes ganar ", valor2)
else:
    print("No puedo calcular tu salario.")

num = int(input("Ingrese su nota"))
if num>50:
    print("Aprobaste")
elif num ==50:
    print("Presenta un taller")
else:
    print("Perdiste")
    
lista = [1,2,3,4,5,6,7,8,9,10,["Hola"]]
lista2 = ["buenas", "Hola"]
#print(lista)
#print(lista[0:5])
#print(lista[10][0])
#print(lista[:8])
del(lista[0])
print(lista)
lista.remove(8)
print(lista)
lista.append("hola")
print(lista)
lista.insert(0,"Buenas")
print(lista)
lista.extend([11,22,33])
print(lista)
listaf= lista+lista2
print(listaf)
dupla = (1,2,3,4,5,5,5)
print(dupla.count(5))
diccionario = {"nombre": "Juanse", "apellido": "Padilla"}
print(diccionario)
for a, b in diccionario.items():
    print(a,b)
print(diccionario.items())
diccionario.pop("nombre")
print (diccionario)
for c in range(0,100+1,2):
    print(c)
num= 0
if num>0:
    print("positivo")
elif num ==0:
    print("es cero")
else:
    print("negativo")
edad= int(input("Ingresa tu edad: "))
if edad>= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

num = int(input("Ingrese su nota"))

if num>50:
    print("Aprobaste")
elif num ==50:
    print("Presenta un taller")
else:
    print("Perdiste")