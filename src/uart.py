import serial
from time import sleep


class Uart:
    def __init__(self):
        self.serial = serial.Serial("/dev/serial0", 9600, timeout=0.1)
        self.check()


    def check(self):
        if self.serial.is_open:
            print('Conexão estabelecida com sucesso!')
            return 1
        else:
            print('Falha ao estabelecer conexão!')
            return 0



    def envia_recebe(self, msg):
        resposta = None
        tentativas = 0
        self.enviar(msg)
        print(msg)
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
            self.serial.write(msg)
        else:
            print('Falha ao enviar comando!') 


    def receber(self):
        sleep(0.1)
        buffer = self.serial.read(9)
        return buffer
        

    def fechar(self):
        self.serial.close()
        print('Conexão encerrada com sucesso!')