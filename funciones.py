def leerArchivo(ruta:str):
    file = open(ruta)
    linea = file.readline().strip().split(":")
    diccionarioGraficas = {}
    while(linea != [""]):
        id = linea[0]
        coordenadas = linea[1].split(";")
        #convertir coordenadas de string a int
        for indice in range(0,len(coordenadas)):
            coord = coordenadas[indice]
            x,y = coord.split(",")
            x = int(x[1:])
            y = int(y[:len(y)-1])
            coordenadas[indice] = (x,y)
        diccionarioGraficas[id] = coordenadas
        linea = file.readline().strip().split(":")

    
    file.close()
    return diccionarioGraficas


def compararGraficas(archivo):

    diccionario = leerArchivo(archivo)
    limiteSimilitud = 15

    arregloIguales = []
    arregloSimilares = []
    arregloDiferentes = []

    arregloIds = []
    arregloPendientes = []

    for id,coordenadas in diccionario.items():
        m = calcularPendiente(coordenadas)
        arregloIds.append(id)
        arregloPendientes.append(m)
   
        if len(arregloPendientes) > 1:
            for indice in range(0,len(arregloPendientes)-1):
                diferencia = abs(m-arregloPendientes[indice])
                if diferencia == 0:
                    arregloIguales.append((int(id),int(arregloIds[indice])))
                else:
                    if porcentajeDiferencia(diferencia,limiteSimilitud) < 50:
                        arregloDiferentes.append((int(id),int(arregloIds[indice])))
                    else:
                        arregloSimilares.append((int(id),int(arregloIds[indice])))
    escribirArchivo(arregloIguales,arregloSimilares,arregloDiferentes)


def porcentajeDiferencia(diferencia, valor:int):
    x = diferencia*100
    y = valor
    return round(x/y,0)

def calcularPendiente(coordenadas):
    y1 = int(coordenadas[len(coordenadas)-1][1])
    y0 = int(coordenadas[0][1])
    x1 = int(coordenadas[len(coordenadas)-1][0])
    x0 = int(coordenadas[0][0])
    return round((y1-y0)/(x1-x0))

def escribirArchivo(iguales,similares,diferentes):
    file = open("archivoRetorno","a")
    
    file.write("iguales:")
    escribirArreglo(iguales,file)

    file.write("similares:")
    escribirArreglo(similares,file)

    file.write("diferentes:")
    escribirArreglo(diferentes,file)

    file.close()


def escribirArreglo(arreglo,file):
    for i in range(0,len(arreglo)):
        file.write(str(arreglo[i]))
        if(i<len(arreglo)-1):
            file.write(";")
    file.write("\n")

