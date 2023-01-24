import serial
import time


class Uart:
    def __init__(self):
        self.ser = serial.Serial("/dev/serial0", 9600, timeout=0.1)
        self.check()

    def check(self):
        if self.ser.isOpen():
            return 1
        else:
            print('Falha ao estabelecer conexão!')
            return 0



    def envia_recebe(self, msg):
        resposta = None
        tentativas = 0
        self.enviar(msg)
        while not resposta and tentativas < 4:
            try:
                resposta = self.receber()
                print(resposta)
                if resposta != None:
                    return resposta
                else:
                    tentativas = tentativas + 1
            except Exception as e:
                print(e)

    def enviar(self, msg):
        if self.check() == 1:
            self.ser.write(msg)
        else:
            print('Falha ao enviar comando!') 


    def receber(self):
        if self.check() == 1:
            return self.ser.read(9)
        

    def fechar(self):
        self.ser.close()
        print('Conexão encerrada com sucesso!')