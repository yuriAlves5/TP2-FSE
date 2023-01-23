import serial
import time

def __init__(self):
    self.port = '/dev/serial0'
    self.baudrate = 9600
    self.timeout = 1
    self.ser = serial.Serial(self.port, self.baudrate, self.timeout)
    self.check()

def check(self):
    if self.ser.isOpen():
        print('Conexão estabelecida com sucesso!')
    else:
        print('Falha ao estabelecer conexão!')

