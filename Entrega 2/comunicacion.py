



import serial
import time



# Configura el puerto serial
puerto = 'COM3'  # Cambia por '/dev/ttyUSB0' o por algo 'COM3'
baudios = 9600
#ser = serial.Serial(puerto, baudios, timeout = 1)



def recibir_datos():
	#if ser.in_waiting > 0:
	#datos = ser.readline().decode('utf-8').strip()
	datos = input("Ingrese informacion\n")
	return datos.split(',')

while True:
	datos = recibir_datos()
	if datos:
		humedad, bateria = map(float, datos)
		print(f'humedad: {humedad}, temperatura: {bateria}')

time.sleep(1) # Espera 1 segundo antes de la próxima lectura


# Cierra el puerto serial al finalizar
ser.close()