
from reportlab.pdfgen import canvas  
from reportlab.lib.pagesizes import letter
import datetime

import qrcode


class Almacen:
    def _init_(self):
        self.nombre=""
        self.tel=""
        self.direccion=""

    def Datos_almacen(self):
        print("Digite los datos del Almacen")
        self.nombre=input("Nombre: ")
        self.tel=int(input("Telefono: "))
        self.direccion=input("Direccion: ")

    def Qr(self):
        input= self.nombreEmp

        qr= qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(input)
        qr.make(fit=True)
  
        img= qr.make_image(fill="black",back_color="white")
        img.save("nombre.png")


    def Empleado(self):
        self.nombreEmp=""

    def Datos_Empleado(self):
        print("Digite los datos del empleado")
        self.nombreEmp=input("Nombre: ")

    def Productos(self):
        self.nombrepro=""
        self.costo=""
        self.cantidad=""

    def Datos_Productos(self):
        print("Digite los datos del producto que desea llevar")
        self.nombrepro=input("Nombre: ")
        self.costo=int(input("Precio del producto que llevara: "))
        self.cantidad=int(input("Cantidad de productos a llevar: "))

    def calculo_precio_total(self):
        self.preciototal=(self.costo * self.cantidad)
        #print("El valor del sin eliva incluido es de: ",self.preciototal)

    def calculo_iva(self):
        self.calculoiva=(self.preciototal * 0.19)
        self.totaliva=(self.calculoiva + self.preciototal)
        #print("El valor del con el iva incluido es de: ",self.totaliva)

    def contraseña(self):
        x=int(input("Por favor Digite la contraseña: "))
        if x==2426:
            print("Contraseña correcta")
        else: 
            print("Contraseña incorrecta")
            exit


    def Factura(self):
        w, h = letter
        C = canvas.Canvas("Facturajorge.pdf",pagesize=letter)
        C.setLineWidth(.2)
        C.setFont('Helvetica',10)
        C.drawString(235,h -50, self.nombre)
        C.drawString(240,h -65, "NIT: 121020-22")
        C.drawString(195,h -80,"RESPONSABLE DE IVA.   FERXXO")
        C.drawString(222,h -95,"Agente Retenedor de ICA")
        C.drawString(240,h -110,"TEL:0226554")
        C.drawString(235,h -125,"Campoalegre,Huila")
        C.drawString(240,h -140,self.direccion)
        C.drawString(180,h -165,"Auto.DIAN 12313213213  FEC 01/04/SE22")
        C.drawString(180,h -180,"DESDE JK -33419   HASTA JK-10000000")
        C.drawString(180,h -195,"DCTO/EQUIVALENTE POS:  JK -52375")
        C.drawString(180,h -210,"VIGENCIA HASTA : 11/11/2004")
        C.drawString(180,h -225,f"Fecha:{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}")
        C.drawString(180,h -240,f"Hora:{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
        C.drawString(180,h -255,f"Cajero: {self.nombreEmp}")
        C.drawString(180,h -265,"===========================================")
        C.drawString(180,h -280,"DESCRIPCION         UNIDADES       PRECIO*Uni   ")
        C.drawString(180,h -290,"===========================================")
        C.drawString(195,h -305,f"{self.nombrepro}                         {self.cantidad}                {self.costo}")
        C.drawString(180,h -315,"===========================================")
        C.drawString(250,h -330,f"TOTAL SIN IVA       {self.preciototal}")
        C.drawString(250,h -345,f"IVA                          {self.calculoiva}")
        C.drawString(250,h -360,f"PRECIO TOTAL      {self.totaliva}")
        C.drawString(180,h -370,"===========================================")
        C.drawString(235,h -385,"FORMA DE PAGO:   EFECTIVO")
        C.drawString(180,h -400,"===========================================")
        C.drawString(235,h -415,"GRACIAS POR TU COMPRA")
        C.drawString(235,h -430,"      SI NOS SIGUES EN ")
        C.drawString(235,h -445,"       EN INSTAGRAM")
        C.drawString(225,h -460,"TENDRAS -20%$ EN TU COMPRA")
        C.drawImage("qrsergiolotrae.png",235,230,height=100, width=100)
        C.drawString(180,h -590,"===========================================")
        C.drawString(180,h -605,"TIQUETE POS Impreso por sofware Serca")
        C.drawString(180,h -620,"DESARROLLADO POR EL INGE SERGIO NARVAEZ")
        C.drawString(180,h -645,"===========================================")
        C.drawString(180,h -660,"CHISTE PARA ALEGRARTE EL DIA:")
        C.drawString(180,h -675,"-¿Por qué está feliz la escoba?")
        C.drawString(180,h -690,"-Porque ba-rriendo. <3")
        C.save()


x=Almacen()
x.Datos_almacen()
x.Datos_Empleado()
x.Qr()
x.Datos_Productos()
x.calculo_precio_total()
x.calculo_iva()
x.contraseña()
x.Factura()

