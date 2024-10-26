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
            " 1. Registro de Humedad y carga de bateria\n" 
            " 2. Visualización gráfica de registros de humedad \n"
            " 3. Mostrar estado de la bateria\n"
            " 4. Cerrar conexión\n"))

            if eleccion==1:
                self.registrosHumedad()           
            elif eleccion==2:
                self.visualizacionGrafica()
            elif eleccion ==3:
                self.bateriaEstado()
            elif eleccion==4:
                self.db.cerrarConexion()
                break
            else:
                print("ingresó un dato incorrecto")


  
    
    def registrosHumedad(self):
        """funcion que carga valores de humedad del sensor y carga de la bateria a la BD"""

        print("ingreso de los valores de humedad, voltaje bateria y carga de la bateria o escriba 0,0,0 para volver al menú anterior")
            
        while True:

            def recibir_datos():
                datos = input("Ingrese informacion\n")
                return datos.split(',')

            datos=recibir_datos()

            valorCargador=0
            
            if datos:
                humedad, voltaje, bateria = map(float, datos)

                if (humedad or voltaje or bateria) ==0:
                    break
                
                
                print(f'humedad: {humedad}, voltaje: {voltaje}, bateria: {bateria}')
                time.sleep(3) # Espera 3 segundos antes de la próxima lectura

                
                hora=datetime.datetime.now()
                sql=("INSERT INTO humedad(fecha, valores) VALUES (%s,%s)")
                contenido=(hora, humedad)
                self.db.ejecutarConsultas(sql,contenido)

                valorCargador=0

                if (bateria <=27.0):
                    valorCargador=1
                    sql1=("INSERT INTO bateria(cargador, carga)VALUES(%s,%s)")
                    datosA=(valorCargador, bateria)
                    self.db.ejecutarConsultas(sql1,datosA)
                else:
                    sql1=("INSERT INTO bateria(cargador, carga)VALUES(%s,%s)")
                    datosA=(valorCargador, bateria)
                    self.db.ejecutarConsultas(sql1,datosA)



# efunciones se refieren al estado de la bateria


    def bateriaEstado(self):
        """metodo para buscar el estado de la bateria"""
      
        sql=("SELECT cargador FROM bateria ORDER BY idbateria DESC LIMIT 1")
        sql1=("SELECT carga FROM bateria ORDER BY idbateria DESC LIMIT 1")

        res=self.db.obtenerResultados(sql)
        res2=self.db.obtenerResultados(sql1)

        car1=res[-1]
        car=car1[0]
        
        res1=res2[-1]
        res=res1[0]

        if car ==0:
            print("La batería no esta recibiendo carga")                    
        elif car==1:
            print("La batería esta recibiendo carga")
        if res >=40.0:
            print("La bateria esta por encima o igual a 60%")
        elif res<=27.0:
            print("La carga de la batería esta por debajo o igual a 15%")
        else:
            print("La batería no está funcionando correctamente")
            
        

    def visualizacionGrafica(self):

        print("Registros de los valores de humedad")
        sql = ("SELECT valores FROM humedad1")
        valores = self.db.obtenerResultados(sql)
        aplanada = [elemento for tupla in valores for elemento in tupla]
        print(aplanada)

        sql = ("SELECT idhumedad FROM humedad1")
        valoresA = self.db.obtenerResultados(sql)
        print(valoresA)
        aplanadaA = [elemento for tupla in valoresA for elemento in tupla]


        fig, ax = plt.subplots()
        ax.plot(aplanadaA, aplanada, label='Humedad (%)', color='b')
        ax.set_ylabel('Humedad (%)')
        ax.set_xlabel('Tiempo')


        plt.show()

        self.opcionesMenuPrincipal()
        
    










                
  
       

        

    
    
