nombres = ["ANGEL MAURICIO","MARCO ANTONIO","EDGAR DANIEL","BETHZY ALEYDIZ","FABIOLA MICHEL","FRIDA VISTORIA","ERNESTO YAIR","ANGEL YAEL","AMBAR NAHOMI","URIEL","LUIS ENRIQUE","BRAYAN ALEXANDER","ERICK","FERNANDA ABIGAIL","ESTEFANI SARAHI","YUMIKO JATZERY","HANSEL DANIEL","JULIO ALBERTO","ENRIQUE UCIEL","YOJAN JOEL","PEDO EDUARDO","MIRELLA YAMILE","ALISON DAYANA","PRISCILA","SERGIO ALEXIS","RICARDO","SAMUEL JESHUA","VANESSA ISABEL","SARAHI VALERIA","DAVID GERSSAYN","JOSE ANGEL","GABRIEL","CRISTIAN YUREM","ARTURO AZAEL","ARMANDO"]

for nombre in nombres:
    if nombre[0] in "AEIOU":
        print(nombre)

contador_vocal = 0
for nombre in nombres:
    if nombre[0] in "AEIOU":
        contador_vocal += 1
print("Cantidad de nombres que inician con vocal:", contador_vocal)

for nombre in nombres:
    if len(nombre) > 10:
        print(nombre)


nombres_ordenados = sorted(nombres)
print("Primeros 3 nombres en orden alfabetico:", nombres_ordenados[:3])


for nombre in nombres:
    if "Y" in nombre:
        print(nombre)

calificaciones = [85, 60, 78, 95, 97, 73, 70, 100, 34, 68, 80, 54]


for cal in calificaciones:
    if cal >= 60:
        print("Aprobado:", cal)
    else:
        print("Reprobado:", cal)


aprobados = 0
reprobados = 0
for cal in calificaciones:
    if cal >= 60:
        aprobados += 1
    else:
        reprobados += 1
print("Total de aprobados:", aprobados)
print("Total de reprobados:", reprobados)

maxima = calificaciones[0]
minima = calificaciones[0]
for cal in calificaciones:
    if cal > maxima:
        maxima = cal
    if cal < minima:
        minima = cal
print("La calificacion mas alta es:", maxima)
print("La calificacion mas baja es:", minima)


for cal in calificaciones:
    if cal % 2 == 0:
        print(cal, "es par")
    else:
        print(cal, "es impar")

n = int(input(" ¿Cuantos datos deseas ingresar? "))
datos = []
contador = 0

while contador < n:
    valor = float(input("Ingresa el valor: "))
    datos.append(valor)
    contador += 1

indice = 0
suma = 0
maximo = datos[0]
minimo = datos[0]
positivos = 0
negativos = 0
ceros = 0

while indice < n:
    valor = datos[indice]
    suma += valor

    if valor > maximo:
        maximo = valor
    if valor < minimo:
        minimo = valor

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        ceros += 1

    indice += 1

promedio = suma / n

print("\nResultados del analisis:")
print("Datos ingresados:", datos)
print("Suma total:", suma)
print("Promedio:", promedio)
print("Maximo:", maximo)
print("Minimo:", minimo)
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
print("promedio:", promedio)
print("valor maximo:", maximo)
print("valor minimo:", minimo)
print("cantidad de positivos:", positivos)
print("cantidad de negativos:", negativos)
print("cantidad de ceros:", ceros)