#Aca va el primer ejercicio de la tarea de logica:

"""info: cantidad de cajas que tiene que pedir felipe
    datos: P/D 744, 12 por caja, espacio en caja(12U), X dias a la semana
    estrategia: 744/12 = 62 cajas"""

ProdD = 744
EspacioC = 12
print ("la cantidad de cajas que tiene que pedir son:", ProdD/EspacioC ,"para los pañales\n")



#Segundo ejercicio:

'''Info: Resultado suma,resta, multiplicacion, resto(div) resultado de la div como entero y flotante
    Datos: dos variable, valores 5 y 4.3
    estrategia: asignara los valores y luego dar opciones de operaciones, ya finalizar con un print en pantalla '''
#Inicio proceso resultados;
Varia1 = 5
Varia2 =float(4.3)
OAlgebraico = input("Elija operador algebraico:")

if  OAlgebraico == "+":
    print ("Resultado de la suma es:", Varia1+Varia2)

elif OAlgebraico== "-":
    print("resultado de la resta es:", (Varia1-Varia2))

elif OAlgebraico == "*":
    print ("Resultado de la multiplicacion es:", Varia1*Varia2)

elif OAlgebraico == "/":
    print ("Resultado de la division es:", Varia1/Varia2)

elif OAlgebraico == "%":
    print ("Resultado de la division es:", Varia1%Varia2)

elif OAlgebraico == "//":
    print ("Resultado de la division es:", Varia1//Varia2)

#Fin Proceso.


#tercer ejercio;

#Inicio proceso productos A y B:

"""
    info: precio de cantidad de productos A y B
    datos: comprar cierta cantidad de productos A y B
    estrategia: sumar la cantidad de productos de A y luego de B , y lo proximo a hacer es divir por el 21% del IVA"""

CantidadPA = int(input("\nCantidad de Productos A: "))
PrecioPA = float(input("\nPrecio del producto: "))
print ("la cantidad de productos A salen un total sin IVA de:", round(CantidadPA*PrecioPA,2))
print ("Los productos A con IVA salen:", float(CantidadPA*(PrecioPA*1.21)))

CantidadPB = int(input("\nCantidad de Productos B: "))
PrecioPB = float(input("\nPrecio del producto B: "))
print ("El precio de los productos B sin IVA es de:", round(CantidadPB*PrecioPB,2))
print ("El precio con IVA incluido saldria:", float(CantidadPB*(PrecioPB*1.21)))

input ()

#Fin Proceso:

#Proceso pulseras, aros y promos:
lnPulsera = int(input("cuantas pulsera vendiste: "))
lnAros = int(input("cantidad de pulseras vendidas: "))
lnPromo = int(input("cantidad de promos vendidas: "))

input ("Procesando datos...  Apretar enter para seguir")
print ("\n"*2)

lnTotalPrecioP = (lnPulsera - lnPromo)
