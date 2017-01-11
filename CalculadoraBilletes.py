#!/usr/bin/env python
# -*- coding: utf-8 -*-
##autor Yesid Rangel
##Date: 09-01-2017
## version: 0.1

from tkinter import *
windows1 = Tk()
windows1.title("Calculadora de billetes 2017")
windows1.geometry("600x500+400+100")

## Fondo
imagenFondo = PhotoImage(file="fondo.png")
my_imagenFondo = Label(windows1, image=imagenFondo).place(x = 0, y = 0)

## etiquetas de titulo

LblCantidad = Label(windows1, text="Cantidad", font=(22), width=(20)) ##Etiqutea de texto cantidad
LblCantidad.place(x=35, y=5)

LblGasto = Label(windows1, text="  Gastos  ", font=(24), width=(20)) ##Etiqutea de texto cantidad
LblGasto.place(x=270, y=5)

LblPago = Label(windows1, text="  Valor a pagar ", font=(24), width=(20)) ##Etiqutea de texto Saldo pagado
LblPago.place(x=270, y=205)

LblPago = Label(windows1, text="Valor en billes ", font=(24), width=(12)) ##Etiqutea de texto Saldo pagado
LblPago.place(x=200,y=335)

LblPago = Label(windows1, text="Dinero a devolver", font=(24), width=(15)) ##Etiqutea de texto Saldo pagado
LblPago.place(x=335,y=335)

#Entradas de valores de billetes
valorCien= IntVar()
entrada_valorCien =  Entry(windows1,textvariable = valorCien,font=(15), width=8) ## Entrada del valor de billete de CienMil
entrada_valorCien.place(x= 35,y=40)

valorCincuenta= IntVar()
entrada_valorCincuenta =  Entry(windows1,textvariable = valorCincuenta,font=(15), width=8) ## Entrada del valor de billete de CincuentaMil
entrada_valorCincuenta.place(x= 35,y=75)

valorVeinte= IntVar()
entrada_valorVeinte =  Entry(windows1,textvariable = valorVeinte, font=(15), width=8) ## Entrada del valor de billete de valor VeinteinteMil
entrada_valorVeinte.place(x= 35,y=110)

valorDiez= IntVar()
entrada_valorDiez =  Entry(windows1,textvariable = valorDiez,font=(15), width=8) ## Entrada del valor de billete de DiezMil
entrada_valorDiez.place(x= 35,y=145)

valorCinco= IntVar()
entrada_valorCinco=  Entry(windows1,textvariable = valorCinco, font=(15), width=8) ## Entrada del valor de billete de CincoMil
entrada_valorCinco.place(x= 35,y=180)

valorDos= IntVar()
entrada_valorDos =  Entry(windows1,textvariable = valorDos, font=(15), width=8) ## Entrada del valor de billete de DosMil
entrada_valorDos.place(x= 35,y=215)

valorMil= IntVar()
entrada_valorMil =  Entry(windows1,textvariable = valorMil, font=(15), width=8)## Entrada del valor de billete de Mil
entrada_valorMil.place(x= 35,y=250)

valorMoneda= IntVar()
entrada_valorMoneda =  Entry(windows1,textvariable = valorMoneda, font=(15), width=8) ## Entrada del valor de Moneda
entrada_valorMoneda.place(x= 35,y=285)

## Etiquta del simbolo de multiplicacion
LblSimbolo100= Label(windows1, text="X",font=(15), width=(3))  ##Coloca una x alfrente al ladado del valor de 100mil
LblSimbolo100.place(x= 115,y=40)

LblSimbolo50= Label(windows1, text="X",font=(15), width=(3)) ##Coloca una x alfrente al ladado del valor de 50mil
LblSimbolo50.place(x= 115,y=75)

LblSimbolo20= Label(windows1, text="X",font=(15), width=(3)) ##Coloca una x alfrente al ladado del valor de 20mil
LblSimbolo20.place(x= 115,y=110)

LblSimbolo10= Label(windows1, text="X",font=(15), width=(3)) ##Coloca una x alfrente al ladado del valor de 10mil
LblSimbolo10.place(x= 115,y=145)

LblSimbolo5= Label(windows1, text="X",font=(15), width=(3)) ##Coloca una x alfrente al ladado del valor de 5mil
LblSimbolo5.place(x= 115,y=180)

LblSimbolo2= Label(windows1, text="X",font=(15), width=(3)) ##Coloca una x alfrente al ladado del valor de 2mil
LblSimbolo2.place(x= 115,y=215)

LblSimboloMil= Label(windows1, text="X",font=(15), width=(3)) ##Coloca una x alfrente al ladado del valor de mil
LblSimboloMil.place(x= 115,y=250)

LblSimboloMoneda= Label(windows1, text="$",font=(15), width=(3)) ##Coloca una $ al frente al ladado del valor de las monedas
LblSimboloMoneda.place(x= 115,y=285)

##Etiquetas con la imagen de los billestes
imagen100 = PhotoImage(file="cienMil.png")
Lblimagen100 = Label(windows1, image=imagen100).place(x= 153,y=36) #Coloca la imagen del billete de 100.000

imagen50 = PhotoImage(file="cincuentaMil.png")
Lblimagen50= Label(windows1, image=imagen50).place(x= 153,y=72)#Coloca la imagen del billete de 50.000


imagen20 = PhotoImage(file="veinteMil.png")
Lblimagen20= Label(windows1, image=imagen20).place(x= 153,y=106)#Coloca la imagen del billete de 20.000

imagen10 = PhotoImage(file="diezMil.png")
Lblimagen10= Label(windows1, image=imagen10).place(x= 153,y=142)#Coloca la imagen del billete de 10.000

imagen5 = PhotoImage(file="cincoMil.png")
Lblimagen5= Label(windows1, image=imagen5).place(x= 153,y=177)#Coloca la imagen del billete de 5.000

imagen2 = PhotoImage(file="dosMil.png")
Lblimagen2= Label(windows1, image=imagen2).place(x= 153,y=213)#Coloca la imagen del billete de 2.000

imagenMil = PhotoImage(file="mil.png")
LblimagenMil= Label(windows1, image=imagenMil).place(x= 153,y=248)#Coloca la imagen del billete de 1.000

imagenMonedas = PhotoImage(file="monedas.png")
LblimagenMonedas= Label(windows1, image=imagenMonedas).place(x= 153,y=282)#Coloca la imagen de las monedas

#Entradas de valores de Gastos
Descuento= IntVar()
entrada_Descuento =  Entry(windows1,textvariable = Descuento,font=(15), width=8) ## Entrada de gasto #1
entrada_Descuento.place(x= 270,y=40)

Descuento2= IntVar()
entrada_Descuento2 =  Entry(windows1,textvariable = Descuento2,font=(15), width=8) ## Entrada de gasto #2
entrada_Descuento2.place(x= 270,y=75)

Descuento3= IntVar()
entrada_Descuento3 =  Entry(windows1,textvariable = Descuento3,font=(15), width=8) ## Entrada de gasto #3
entrada_Descuento3.place(x= 370,y=40)

Descuento4= IntVar()
entrada_Descuento4 =  Entry(windows1,textvariable = Descuento4,font=(15), width=8) ## Entrada de gasto #4
entrada_Descuento4.place(x= 370,y=75)


#Entradas de valores de valor pagado
Pago= IntVar()
entrada_Pago =  Entry(windows1,textvariable = Pago,font=(15), width=20) ## Entrada de gasto #1
entrada_Pago.place(x=270,y=245)

## funcion para hacer la usma total mas descuentos

def Valor_general():
    ##Cantidad de billes
    _cien = valorCien.get()
    _cincuenta = valorCincuenta.get()
    _veinte = valorVeinte.get()
    _diez = valorDiez.get()                     ## obtiene los valores de las entradas
    _cinco = valorCinco.get()                   ## de cada billete puesto por usuario
    _dos = valorDos.get()
    _mil = valorMil.get()
    _moneda = valorMoneda.get()

    ##cantidad de gastos
    _gasto1 = Descuento.get()
    _gasto2 = Descuento2.get()
    _gasto3 = Descuento3.get()
    _gasto4 = Descuento4.get()

    ## valor del que se paga
    _pago = Pago.get()

    ##Valor de billetes
    totalCien = int (_cien * 100000)
    totalCincuenta = int (_cincuenta * 50000)
    totalVeinte = int (_veinte * 20000)
    totalDiez = int (_diez * 10000)                   ## multiplica el valor puesto 
    totalCinco = int (_cinco * 5000)                  ## el usuario por su respectiva denominacion
    totalDos = int (_dos * 2000)
    totalMil = int (_mil * 1000)
    totalMoneda = int (_moneda)

    ## Total en billetes
    totalBilletes = (totalCien + totalCincuenta + totalVeinte + totalDiez + totalCinco + totalDos + totalMil + totalMoneda) ## obtine la suma total de la cantidad de billetes
    ## Total en gastos
    totalGastos= int (_gasto1 + _gasto2 + _gasto3 + _gasto4)    ## se obtine el Valor total de gastos

    ## Valor en entero de lo que esta pagando
    totalPago = int (_pago)

    ## Diferencia entre total a pagar mas gastos
    diferencia  = int (totalPago - totalGastos)

    ##genera el el sultado general
    resultado = (totalBilletes - diferencia)
    

    ## Etiqueta que imprime el valor total monetario
    LblTotalBilletes= Label(windows1, text=totalBilletes, font=(15), width=(12)) 
    LblTotalBilletes.place(x= 200,y=390)

    ## Etiqueta que imprime el resultado
    LblTotal= Label(windows1, text= resultado, font=(15), width=(15)) 
    LblTotal.place(x= 335,y=390)

## boton que genra el total
boton = Button(windows1, text = "TOTAL", command=Valor_general, width=(20) )
boton.place(x=35,y=335)

windows1.mainloop()
 