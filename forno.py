from bme import BME
from uart import Uart
from time import sleep
from modbus import Modbus

class Forno:
    def __init__(self):
        self.bme = BME()
        self.uart = Uart()
        self.modbus = Modbus()
        self.temperatura_interna = 0.0
        self.temperatura_ambiente = 0.0
        self.temperatura_referencia = 0.0
        
    def Liga_Forno(self):
        Uart.check()
        Uart.enviar(Modbus.envia_comando('envia_sinal_sistema_ligado', None))
        Uart.enviar(Modbus.envia_comando('envia_sinal_modo_dashboard', None))
        self.Update_temperatura_ambiente()
        #enviar temperatura ambiente
        print('Forno ligado!')

    def Desliga_Forno(self):
        Uart.enviar(Modbus.envia_comando('envia_sinal_sistema_desligado', None))
        Uart.enviar(Modbus.envia_comando('envia_sinal_funcionamento_desligado', None))
        Uart.fechar()
        BME.fechar()
        print('Forno desligado!')


    def Update_temperatura_ambiente(self):
        temperatura_ambiente = BME.get_internal_temperature()
        Uart.enviar(Modbus.envia_comando('envia_tempertura_ambiente', temperatura_ambiente))
        