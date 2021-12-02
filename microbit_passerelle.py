from microbit import *
import radio
import protocol

'''
 * variable for script
'''
radioProtocol = protocol.RadioProtocol(1)

'''
 * init comm
'''
uart.init(115200)
radio.config(group = 2)
radio.on()

'''
 * main programme
'''
while True:
    message = radioProtocol.receivePacket(radio.receive_bytes())  # data from another microbit by radio frequency through the network protocol
    msgUartStr = uart.read()                            # data per serial port
    if msgUartStr:
        radioProtocol.sendPacket(str(msgUartStr), 2)              # send configuration (TL or LT)
    if message:
        print(message)                                  # send data by serial to the gateway