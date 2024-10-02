import datetime
#from database import Database





class Sensor():

    def __init__(self, db) -> None:
        self.humedad=0
        self.bateria=0
        self.db=db
       
  
       
    def opcionesMenuPrincipal(self):
        """funcion que despliega el menu para el usuario"""

        while True:
    
            print("------------")
            eleccion=int(input("Seleccione la opción deseada: \n"
            " 1. Registro de Humedad \n 2. Registro de nivel de batería \n" 
            " 3. Visualización de registros de humedad \n 4. Cerrar conexión\n"))

            if eleccion==1:
                self.registrosHumedad()
            if eleccion==2:
                self.bateriaEstado()            
            if eleccion==3:
                print("trae registros de humedad de la BD")
            if eleccion==4:
                print("trae estado de la bateria de la BD")


    def registrosHumedad(self):
        """funcion que carga valores de humedad del sensor a la BD"""

        print("ingrese los valores de humedad o presione 7 para volver al menú anterior")

        while True:
            humedad=float(input(""))
        
            if humedad !=7:
                print("cargado ", humedad)
                hora=datetime.datetime.now()
                print(hora)
                sql=("INSERT INTO humedad(fecha, valores) VALUES (%s,%s)")
                datos=(hora, humedad)
                self.db.ejecutarConsultas(sql,datos)
            if humedad == 7:
                break
        self.opcionesMenuPrincipal()



# esta dos funciones se refieren al estado de la bateria

    def cargaBateria(self):

        cargador=int(input("ingrese si se esta cargando la bateria con 1 caso contrario 0 \n"))
        carga=int(input("ingrese porcentaje de carga de la bateria \n"))

        sql=("INSERT INTO bateria(cargador, carga)VALUES(%s,%s)")
        datos=(cargador, carga)
        self.db.ejecutarConsultas(sql,datos)

        return(cargador, carga)
        
        
    


    def bateriaEstado(self):
        """metodo para buscar el estado de la bateria"""
        self.cargaBateria()
        
        opcion1=("SELECT cargador FROM bateria WHERE idbateria=(select max(idbateria) FROM bateria)")
        opcion2=("SELECT carga FROM bateria WHERE idbateria=(select max(idbateria) FROM bateria)")
        cargador=self.db.obtenerResultados(opcion1)
        carga=self.db.obtenerResultados(opcion2)
        print(cargador)


        if cargador ==[(0,)]:
            print("La batería no esta recibiendo carga")
            if carga<=15:
                print("La carga de la batería esta por debajo o igual a 15%")
            else:
                print("Carga de la bateria: ", carga ,"%")
                     
        elif cargador==1:
            print("La batería esta recibiendo carga")
            if carga >=95:
                print("La bateria esta por encima o igual a 95%")
            else:
                print("Carga de la bateria: " , carga ,"%")

        else:
            print("La batería no está funcionando correctamente")
            
        self.opcionesMenuPrincipal()

                
  
       

        

    
    
