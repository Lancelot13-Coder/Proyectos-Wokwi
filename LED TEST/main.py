#Se llaman los Modulos a Trabajar
from  machine import Pin
from utime import sleep

#Se crea el Objeto

led_azul = Pin(5, Pin.OUT)

#Se crea el ciclo

while True:
  led_azul.value(1)
  sleep(2)
  print("off")
  led_azul.value(0)
  sleep(2)
  print("on") 















