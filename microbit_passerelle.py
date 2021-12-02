from microbit import *
import radio
import tp3

'''
 * variables for script
'''
uart.init(115200)
radio.config(group=2)
radio.on()
tp3 = tp3.RadioProtocol(1)

'''
 * main programme
'''
while True:
    message = tp3.receivePacket(radio.receive_bytes())  # data from another microbit by radio frequency through the network protocol
    msgUartStr = uart.read()                            # data per serial port
    if msgUartStr:
        tp3.sendPacket(str(msgUartStr), 2)              # send configuration (TL or LT)
    if message:
        print(message)                                  # send data by serial to the gateway