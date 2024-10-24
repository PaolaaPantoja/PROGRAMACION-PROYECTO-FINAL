import datetime
import time




#import matplotlib.pyplot as plt


           

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

        print("ingrese los valores de humedad o escriba cerrar para volver al menú anterior")
            
  
        
     
        
        while True:

            def recibir_datos():

                datos = input("Ingrese informacion\n")
                
                return datos.split(',')

            
            datos=recibir_datos()

            
            if datos:
                
                humedad, bateria, cargador = map(float, datos)
                
                if (humedad or bateria or cargador) ==0:
                    break
                
                if cargador==1:
                    mensaje="SI"
                else:
                    mensaje="NO"
                print(f'humedad: {humedad}, bateria: {bateria}, cargando: {mensaje}')
                time.sleep(3) # Espera 1 segundo antes de la próxima lectura

            
                #print("cargado ", humedad)
                hora=datetime.datetime.now()
                #print(hora)
                sql=("INSERT INTO humedad(fecha, valores) VALUES (%s,%s)")
                contenido=(hora, humedad)
                self.db.ejecutarConsultas(sql,contenido)
                sql1=("INSERT INTO bateria(cargador, carga)VALUES(%s,%s)")
                datosA=(cargador, bateria)
                self.db.ejecutarConsultas(sql1,datosA)




                
        



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

        sql = ("SELECT fecha FROM humedad")
        valoresA = self.db.obtenerResultados(sql)
        print(valoresA)
        aplanadaA = [elemento for tupla in valoresA for elemento in tupla]
        print("que es esto", aplanadaA)
        
        
        for i in aplanadaA:
            time_delta = datetime.timedelta(valoresA)

# Extraer el total de segundos
            total_seconds = int(time_delta.total_seconds())

# Calcular horas, minutos y segundos
            hours = total_seconds // 3600  # Obtener las horas
            minutes = (total_seconds % 3600) // 60  # Obtener los minutos
            seconds = total_seconds % 60  # Obtener los segundos

# Formatear el resultado como HH:MM:SS
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            print(formatted_time)  # Output: 18:07:32
        











        #plt.figure()
        #plt.bar(aplanada,aplanadaA, color='orange')
        #plt.grid(True)
        #plt.show()

        self.opcionesMenuPrincipal()
        
    










                
  
       

        

    
    
