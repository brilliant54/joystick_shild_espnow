import network
from machine import Pin
import espnow
import utime
from kontrol import*

sta = network.WLAN(network.STA_IF)  
sta.active(True)


esp = espnow.ESPNow()
esp.active(True)


peer = b'\xa8B\xe3\xaa\xe48'
esp.add_peer(peer)

message1= None
while True :
    durum = ana_dongu(x_pot, y_pot, butonlar)
    message = str(durum)
    if message!=message1 : 
        print(f"Sending command : {message}")
        esp.send(peer, message)
        message1=message
    sleep(0.5)
