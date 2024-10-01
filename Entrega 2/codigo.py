import datetime
#from database import Database





class Sensor():

    def __init__(self) -> None:
        
       

        self.humedad=0
        self.bateria=0
       

    
    def getHumedad(self):
        return self.humedad

    def getBateria(self):
        return self.bateria


  

       
    def opcionesMenuPrincipal(self):
        """funcion que despliega el menu para el usuario"""
    
        print("Bienvenido")
        print("------------")
        eleccion=int(input("Seleccione la opción deseada: \n"
        " 1. Registro de Humedad \n 2. Registro de nivel de batería \n" 
        " 3. Visualización de registros de humedad \n 4. Estado de la batería\n"))

        return eleccion
        print(eleccion)
        

    
    def clasificacionEleccion(self, numero):
        if numero==1:
            self.registrosHumedad()
        if numero==2:
            print("lee registro de la bateria del sensor")
        if numero==3:
            print("trae registros de humedad de la BD")
        if numero==4:
            print("trae estado de la bateria de la BD")


    def registrosHumedad(self):
        humedad=float(input("ingrese los valores de humedad: "))

        
       

        

    
    
