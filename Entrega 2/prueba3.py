import serial
import time
import matplotlib.pyplot as plt

# Configuración del puerto serial
puerto = 'COM3' # Cambia esto por tu puerto si es diferentebaudios = 9600
# Intentar abrir el puerto serial
try:
    ser = serial.Serial(puerto, baudios, timeout=1)
    print(f'Puerto {puerto} abierto correctamente')
except serial.SerialException as e:
    print(f'Error al abrir el puerto: {e}')
    exit()

# Listas para almacenar los datos
tiempo = []
temperaturas = []
luces = []
humedades = []

# Configuración del gráfico
plt.ion() # Habilitar modo interactivo
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

def recibir_datos():
    if ser.in_waiting > 0:
        datos = ser.readline().decode('utf-8').strip()
        return datos.split(',')

#Contador para el tiempo
contador = 0

try:
    while True:
        datos = recibir_datos()
        if datos:
            try:

            # Parsear los datos recibidos
                temperatura, luz, humedad = map(float, datos) # Añadir los datos a las listas
                tiempo.append(contador)
                temperaturas.append(temperatura)
                luces.append(luz)
                humedades.append(humedad)
 # Limitar el tamaño de las listas para que no crezcan indefinidamen 

                if len(tiempo) > 50: # Solo mantener los últimos 50 puntos 
                    tiempo.pop(0)
                    temperaturas.pop(0)
                    luces.pop(0)
                    humedades.pop(0)
 # Actualizar las gráficas
                ax1.clear()
                ax2.clear()
                ax3.clear()
                ax1.plot(tiempo, temperaturas, label='Temperatura (°C)', color='r') 
                ax2.plot(tiempo, luces, label='Luz', color='g') 
                ax3.plot(tiempo, humedades, label='Humedad (%)', color='b') 
                ax1.set_ylabel('Temperatura (°C)')
                ax2.set_ylabel('Luz')
                ax3.set_ylabel('Humedad (%)')
                ax3.set_xlabel('Tiempo (s)')
 # Mostrar leyendas
                ax1.legend()
                ax2.legend()
                ax3.legend()
                # Refrescar la gráfica
                plt.pause(0.1)
                contador += 1
            except ValueError:
                print("Error al convertir los datos.")
        time.sleep(0.1) # Esperar 0.1 segundos antes de la próxima lectura
except KeyboardInterrupt:
    print("Interrupción manual detectada. Cerrando el programa...")
finally:
    ser.close() # Asegurarse de cerrar el puerto serial 
    print("Puerto serial cerrado.")