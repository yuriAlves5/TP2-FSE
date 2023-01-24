from bme import BME
from uart import Uart
from time import sleep
from modbus import Modbus
from pid import PID
from pwm import PWM

class Forno:
    def __init__(self):
        self.bme = BME()
        self.uart = Uart()
        self.modbus = Modbus()
        self.pid = PID()
        self.pwm = PWM()
        self.temperatura_interna = 0.0
        self.temperatura_ambiente = 0.0
        self.temperatura_referencia = 0.0
        self.estado = 0
        self.aquecer = 0
        

        
    def Liga_Forno(self):
        self.uart.check()
        if self.estado == 0:
            self.uart.enviar(self.modbus.envia_comando('envia_sinal_sistema_ligado', None))
            self.estado = 1
            self.uart.enviar(self.modbus.envia_comando('envia_sinal_modo_dashboard', None))
        self.update_geral()
        #enviar temperatura ambiente
        print('Forno ligado!')

    def Desliga_Forno(self):
        self.uart.enviar(self.modbus.envia_comando('envia_sinal_sistema_desligado', None))
        self.uart.enviar(self.modbus.envia_comando('envia_sinal_funcionamento_desligado', None))
        self.estado = 0
        print('Forno desligado!')
    
    def Inicia_aquecimento(self):
        if self.aquecer == 1:
            self.Controle()

        if self.estado == 1 and self.aquecer == 0:
            self.uart.enviar(self.modbus.envia_comando('envia_sinal_funcionamento_ligado', None))
            self.aquecer = 1
            print('Inicia aquecimento!')
        
    def Controle(self):
        if self.estado == 1 and self.aquecer == 1:
            self.Aquecendo()

    def Aquecendo(self):
        if self.estado == 1 and self.aquecer == 1:
            self.update_geral()
            self.pid.atualiza_referencia(self.temperatura_referencia)
            sinal = self.pid.control(self.temperatura_interna)
            self.pwm.aplicar_sinal(sinal)



    def Cancela_processo(self):
        self.uart.enviar(Modbus.envia_comando('envia_sinal_funcionamento_desligado', None))
        self.aquecer = 0
        print('Cancela processo!')



    def update_geral(self):
        if self.estado == 1:
            self.Update_temperatura_interna()
            self.Update_temperatura_referencia()
            self.Update_temperatura_ambiente()
            

    def Update_temperatura_ambiente(self):
        self.temperatura_ambiente = BME.get_internal_temperature()
        self.uart.enviar(self.modbus.envia_comando('envia_tempertura_ambiente', self.temperatura_ambiente))

    def Update_temperatura_interna(self):
        self.uart.enviar(self.modbus.envia_comando('temperatura_interna', None))
        self.temperatura_interna = self.modbus.recebe_comando(self.uart.receber())
        
    def Update_temperatura_referencia(self):
        self.uart.enviar(self.modbus.envia_comando('temperatura_referencia', None))
        self.temperatura_referencia = self.modbus.recebe_comando(self.uart.receber())
        