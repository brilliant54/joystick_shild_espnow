import network
import espnow
import machine

sta = network.WLAN(network.STA_IF)  
sta.active(True)

esp = espnow.ESPNow()
esp.active(True)


while True:
    print("çalışma başladı")
    _, msg = esp.recv()
    if msg :
        print(msg)
