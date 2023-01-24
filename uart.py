import serial
import time
import crc

class Uart:
    def __init__(self):
        self.port = '/dev/serial0'
        self.baudrate = 9600
        self.timeout = 1
        self.ser = serial.Serial(self.port, self.baudrate, self.timeout)
        self.check()

    def check(self):
        if self.ser.isOpen():
            print('Conexão estabelecida com sucesso!')
            return 1
        else:
            print('Falha ao estabelecer conexão!')
            return 0


    def enviar(self, msg):
        if self.check() == 1:
            self.ser.write(msg)
            print('Comando enviado com sucesso!')
        else:
            print('Falha ao enviar comando!') 


    def receber(self):
        if self.check() == 1:
            return self.ser.read(9)
        

    def fechar(self):
        self.ser.close()
        print('Conexão encerrada com sucesso!')