"""Programa para gestionar la BD e iniciar objetos
de la clase hcodigo"""



from codigo import Sensor




def main():

    def principal():
        """metodo inicio programa
        Args: eleccion(int): Menú 
        """
    #db=_Database("localhost", 3306,"root","root","huerta")  
    sensor1=Sensor()
    
    sensor1.clasificacionEleccion(sensor1.opcionesMenuPrincipal())
    
    
 
    


if __name__=="__main__":
    main()

    