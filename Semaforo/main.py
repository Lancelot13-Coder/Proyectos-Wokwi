# Importar los Modulos

from machine import Pin
from utime import sleep

# Crear los Objetos

led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(4, Pin.OUT)

# Ciclo en Codigo

while True:
 
 led_rojo.value(1)
 print("Detengase")
 sleep(2)
 led_rojo.value(0)
 print("Alto")



 led_amarillo.value(1)
 print("Alistese")
 sleep(2)
 led_amarillo.value(0)
 print("Esperar")




 led_verde.value(1)
 print("Adelante")
 sleep(2)
 led_verde.value(0)
 print("Siga")

