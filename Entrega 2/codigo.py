import datetime

import matplotlib.pyplot as plt

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
            elif eleccion==2:
                self.bateriaEstado()            
            elif eleccion==3:
                self.visualizacionGrafica()
            elif eleccion==4:
                self.db.cerrarConexion()
                break
            else:
                print("ingresó un dato incorrecto")


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
    
        ultimoid=("SELECT LAST_INSERT_ID();")
        valorA=self.db.obtenerResultados(ultimoid)
        resultado=valorA[-1]
        resultado2=resultado[0]
        
        

             
        opcion1=("SELECT cargador FROM bateria WHERE idbateria="+str(resultado2))
        opcion2=("SELECT carga FROM bateria WHERE idbateria="+str(resultado2))
        cargador=self.db.obtenerResultados(opcion1)
        carga=self.db.obtenerResultados(opcion2)
       
        prueba=carga[-1]
        prueba2=prueba[0]
        
        
       
        prueba3=cargador[-1]
        prueba4=prueba3[0]


        if prueba4 ==0:
            print("La batería no esta recibiendo carga")
            if prueba2<=15.0:
                print("La carga de la batería esta por debajo o igual a 15%")
            else:
                print("Carga de la bateria: ", prueba2 ,"%")
                     
        elif prueba4==1:
            print("La batería esta recibiendo carga")
            if prueba2 >=95.0:
                print("La bateria esta por encima o igual a 95%")
            else:
                print("Carga de la bateria: " , prueba2 ,"%")

        else:
            print("La batería no está funcionando correctamente")
            
        

    def visualizacionGrafica(self):
        print("Registros de los valores de humedad")
        sql=("SELECT valores FROM humedad")
        valores=self.db.obtenerResultados(sql)  
        aplanada=[elemento for tupla in valores for elemento in tupla]
        print(aplanada)

        sql = ("SELECT idhumedad FROM humedad")
        valoresA = self.db.obtenerResultados(sql)
        print(valoresA)
        aplanadaA = [elemento for tupla in valoresA for elemento in tupla]

        plt.figure()
        plt.bar(aplanada,aplanadaA, color='orange')
        plt.grid(True)
        plt.show()

        self.opcionesMenuPrincipal()
        
    

        








                
  
       

        

    
    
