#realizar la ubicacion de las n reinas 
import random
n=8

#construccion de una matrix  para la resolucion del problema
matrixSolucion=[]
for i in range(n):
    listTemp1=['x']*n
    matrixSolucion.append(listTemp1)

#Metodo que me indica las columnas que estan disponibles
def disponibles(y,n,columna,diagonal_izquierda,diagonal_derecha):
    columnas_dsiponibles=[]
    for x in range (n):
        if(columna[x] or diagonal_izquierda[x+y]or diagonal_derecha[x-y+ n-1]):
            continue
        columnas_dsiponibles.append(x)
    return columnas_dsiponibles

#metodo que realiza el recorrido en las difernetes listas  y me retorna 
#una lissta con las tuplas de una posible solucion
def nReinasVegas(n):
    solucion=[]
    while(len(solucion)!=n and n>3):
        solucion=[]
        columna=[False]*n
        diagonal_derecha=[False]*(n*2)
        diagonal_izquierda=[False]*(n*2)
        for i in range(n):
            columnasDisponibles=disponibles(i,n,columna,diagonal_izquierda,diagonal_derecha)
            if(columnasDisponibles):
                x=random.choice(columnasDisponibles)
            else:
                break
            columna[x]=diagonal_izquierda[x+i]=diagonal_derecha[x-i+n-1]=True
            solucion.append((i,x))
    return solucion

solucionNQ=nReinasVegas(8)
for j in solucionNQ:
    matrixSolucion[j[0]][j[1]]='R'
print(solucionNQ)
for i in matrixSolucion:
    print('-')
    print(i)
