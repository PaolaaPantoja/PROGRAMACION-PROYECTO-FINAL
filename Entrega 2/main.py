"""Programa para gestionar la BD e iniciar objetos
de la clase codigo"""

from database import Database
from codigo import Sensor

def main():

    def principal():
        """metodo inicio programa
        Args: eleccion(int): Menú 
        """
    db=Database("localhost", 3306,"root","root","sensor")  
    sensor1=Sensor(db)
    print("BIENVENIDO")
    sensor1.opcionesMenuPrincipal()
    

if __name__=="__main__":
    main()

