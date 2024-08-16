from machine import Pin, ADC
from time import sleep

bt_a = Pin(16, Pin.IN, Pin.PULL_DOWN)
bt_b = Pin(17, Pin.IN, Pin.PULL_DOWN)
bt_c = Pin(18, Pin.IN, Pin.PULL_DOWN)
bt_d = Pin(19, Pin.IN, Pin.PULL_DOWN)
bt_e = Pin(22, Pin.IN, Pin.PULL_DOWN)
bt_f = Pin(23, Pin.IN, Pin.PULL_DOWN)
bt_joy = Pin(21, Pin.IN, Pin.PULL_DOWN)


x_pot = ADC(Pin(34))
y_pot = ADC(Pin(35))


x_pot.atten(ADC.ATTN_11DB)
y_pot.atten(ADC.ATTN_11DB)


def pot_okuma(x_pot, y_pot):
    return x_pot.read(), y_pot.read()


def durum_kontrol(x, y):
    if 2000 >= x >= 1700 and 2000 >= y >= 1700:
        return "sabit"
    elif 4095 >= x > 4000 and 2000 > y >= 1700:
        return "sag"
    elif 100 >= x >= 0 and 2000 >= y >= 1700:
        return "sol"
    elif 2000 >= x >= 1700 and 4095 >= y >= 4000:
        return "yukari"
    elif 2000 >= x >= 1700 and 100 >= y >= 0:
        return "asagi"
    return None


def buton_kontrol(butonlar):
    buton_ismi = ["a", "b", "c", "d", "e", "f", "joy"]
    basili_buton = [name for name, buton in zip(buton_ismi, butonlar) if buton.value() == 0]
    return basili_buton


def ana_dongu(x_pot, y_pot, butonlar):
        x_pot_value, y_pot_value = pot_okuma(x_pot, y_pot)

        durum = durum_kontrol(x_pot_value, y_pot_value)
        basili_buton = buton_kontrol(butonlar)
        sleep(0.1)
        for buton in basili_buton:
            return buton
            
        return durum


butonlar = [bt_a, bt_b, bt_c, bt_d, bt_e, bt_f, bt_joy]
