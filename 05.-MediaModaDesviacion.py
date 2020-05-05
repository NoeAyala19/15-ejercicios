import statistics as stats
lista = []
suma = 0
n = int(input("¿Cuantos numeros agregaras?:"))
for i in range(n):
    valor = int(input("Ingrese el numero %i: "%(i+1)))
    lista.insert(i,valor)
    suma = suma+valor
print("La moda es: ",stats.mode(lista))
print("La media es :",stats.mean(lista))
print ("La desviacion estandar: ",stats.pstdev(lista))

