##Autor : Julian Andres Riveros Camargo
## Reto 5 semana 4

##Entradas
TemperaturasMinimas=[]
TemperaturasMaximas=[]
DiasTotales=0

#Salidas
DiasTotales=0
diasConError=0
diasConErrorMinimo=0
diasConErrorMaximo=0
diasCon2Errores=0
promedioTMaximas=0
promedioTMinimas=0
porcentajeError=0


while True:
    ##Se piden las temperaturas del dia
    TemperaturasMinimas.append(float(input("Ingrese la temperatura minima registrada en el dia: ")))
    TemperaturasMaximas.append(float(input("Ingrese la temperatura maxima registrada en el dia: ")))
    ##De acuerdo a lo requerido, si ambas temperaturas marcan 0 indica que se debe romper el ciclo
    if TemperaturasMinimas[DiasTotales]==0 and TemperaturasMaximas[DiasTotales]==0:
        break
    ##En caso de que se ingrese una temperatura minima mayor a la temperatura maxima, se vuelve a
    ##pedir datos al usuario y no se almacenan dichos datos
    if TemperaturasMinimas[DiasTotales] > TemperaturasMaximas[DiasTotales]:
        print('\033[93m'+ "RECUERDE QUE LA TEMPERATURA MINIMA DEBE SER MENOR A LA TEMPERATURA MAXIMA"+'\033[0m')
        TemperaturasMinimas.pop()
        TemperaturasMaximas.pop()
        continue
#Se evalua si existen errores para el calculo de dias con error ya sea por temperatura minima, maxima o ambos
    if TemperaturasMinimas[DiasTotales]< 5 or TemperaturasMaximas[DiasTotales]> 35:
        diasConError = diasConError + 1

        if TemperaturasMinimas[DiasTotales]< 5:
            diasConErrorMinimo = diasConErrorMinimo + 1

        if TemperaturasMaximas[DiasTotales]> 35:
            diasConErrorMaximo = diasConErrorMaximo + 1


    if TemperaturasMinimas[DiasTotales]< 5 and TemperaturasMaximas[DiasTotales]> 35:
        diasCon2Errores = diasCon2Errores + 1

##Se evalua si las temperaturas no son errores para el calculo del promedio de temperaturas
##maximas y minimas
    if TemperaturasMinimas[DiasTotales]>=5:
        promedioTMinimas = promedioTMinimas + TemperaturasMinimas[DiasTotales]
    if TemperaturasMaximas[DiasTotales]<= 35:
        promedioTMaximas = promedioTMaximas + TemperaturasMaximas[DiasTotales]
    print("------------------------------------------------------------")

    DiasTotales= DiasTotales +1

##Se termina el ciclo de recoleccion de datos y se procede a imprimir las variables de salida

##Se calcula el promedio de las temperaturas
promedioTMaximas = promedioTMaximas /(DiasTotales - diasConErrorMaximo)
promedioTMinimas = promedioTMinimas /(DiasTotales - diasConErrorMinimo)

##Se calcula el porcentaje de error en contraste con los dias que duro la salida de campo
porcentajeError= (diasConError/DiasTotales)*100



print('\033[92m'+ "*******************************************************************"+'\033[0m')
print("El numero total de dias que duro la salida de campo fue: " + str(DiasTotales))
print("El numero de dias con errores fue: " + str(diasConError))
print("El numero de dias con error por temperatura minima: " + str(diasConErrorMinimo))
print("El numero de dias con error por temperatura maxima fue: " + str(diasConErrorMaximo))
print("El numero de dias donde se tuvieron ambos errores fue: " + str(diasCon2Errores))
print("El promedio de temperaturas minimas sin tener en cuente errores es: " +str(promedioTMinimas))
print("El promedio de temperaturas maximas sin tener en cuente errores es: " +str(promedioTMaximas))
print("El porcentaje de dias con error en contraste a los dias que duro la salida de campo es del :" + str(round(porcentajeError,3)) +"%")