from microbit import *
import radio
import tp3

uart.init(115200)
radio.config(group=2)
radio.on()
tp3 = tp3.RadioProtocol(1)

while True:
    message = tp3.receivePacket(radio.receive_bytes())
    msgUartStr = uart.read()
    if msgUartStr:
        tp3.sendPacket(str(msgUartStr), 2)
    if message:
        print(message)