import csv

print("1)-------------------------------")
thislist = [1, 2, 3,4,5,6,7,8,9]
contador=0
sumar=0
for x in thislist:
  contador=contador+1
  print(x)
  sumar=int(sumar+x)
print("el promedio es: ",sumar/contador)

print("2)-------------------------------")
aprobados=0.0
notasaprovados=0.0
desaprovados=0.0
notas=0.0
z=0.0

csvarchivo = open('notas.csv')  
entrada = csv.DictReader(csvarchivo)

for x in entrada:
  print(x['Notas'])
  notas = float(x['Notas'])
  if(notas>=4):
    aprobados = aprobados + 1
    notasaprovados = notasaprovados + notas
  else:
    desaprovados = desaprovados + 1

csvarchivo.close()

print('Aprovados: ',aprobados,'\nDesaprobados: ',desaprovados, '\nPromedio aprovados: ',notasaprovados/notas)

resultado = "Aprovados: "+str(aprobados)+"\nDesaprobados: "+str(desaprovados)+"\nPromedio aprovados: "+str(notasaprovados/notas)

print("3)-------------------------------")
f = open("resultado.txt", "w") #abro en lectura
f.write(str(resultado)) #escribe
f.close()

print("5)-------------------------------")
f = open("numeros1.csv", "w") #abro en ESCRI
f.write('Numeros\n') #escribe
f.write('1\n') #escribe
f.write('-2\n')
f.close()

f = open("numeros2.csv", "w") #abro en ESCRI
f.write('Numeros\n') #escribe
f.write('-1\n') #escribe
f.write('2\n')
f.close()


print("-----------NUMEROS1.CSV----------")
numeroleido=0
csvarchivo = open('numeros1.csv','r')  
entrada = csv.DictReader(csvarchivo)

for x in entrada:
  print(x['Numeros'])
  numeroleido=int(x['Numeros'])
  if(numeroleido >= 0 ):
    print(numeroleido,"es mayor a 0")
    f = open("numerospositivos.csv", "a") 
    f.write(str(numeroleido)+"\n")
    f.close()
  else:
    print(numeroleido,"es menor a 0")
    f = open("numerosnegativos.csv", "a") 
    f.write(str(numeroleido)+"\n")
    f.close()


print("-----------NUMEROS1.CSV----------")
numeroleido=0
csvarchivo = open('numeros2.csv','r')  
entrada = csv.DictReader(csvarchivo)

for x in entrada:
  print(x['Numeros'])
  numeroleido=int(x['Numeros'])
  if(numeroleido >= 0 ):
    print(numeroleido,"es mayor a 0")
    f = open("numerospositivos.csv", "a") 
    f.write(str(numeroleido)+"\n")
    f.close()
  else:
    print(numeroleido,"es menor a 0")
    f = open("numerosnegativos.csv", "a") 
    f.write(str(numeroleido)+"\n")
    f.close()

