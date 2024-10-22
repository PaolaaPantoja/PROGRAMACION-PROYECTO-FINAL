
import datetime

# Tupla con el objeto timedelta
#tupla = (timedelta(seconds=65252, microseconds=610000),)
valores=[datetime.timedelta(seconds=65252, microseconds=610000), datetime.timedelta(seconds=65254, microseconds=360000)]
#aplanada=[elemento for tupla in valores for elemento in tupla]
total_seconds=[]
# Extraer las horas, minutos y segundos
for i in valores:
    total_seconds = int(valores.total_seconds())
for i in total_seconds:
    total_seconds = int(valores.total_seconds())  # Obtener los segundos totales
    hours = total_seconds // 3600  # 1 hora = 3600 segundos
    minutes = (total_seconds % 3600) // 60  # El resto dividido por 60 para obtener los minutos
    seconds = total_seconds % 60  # El resto son los segundos

# Formatear la salida en HH:MM:SS
formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

print(formatted_time)  # Output: 18:07:32