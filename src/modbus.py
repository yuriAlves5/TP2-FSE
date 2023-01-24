
import struct
from crc16 import calcula_crc
#8640

class Modbus:
    def __init__(self):
        registration_number = [8, 6, 4, 0]
        self.controles = {
            #solicitação de leitura
            'temperatura_interna': [0x01,0x23,0xC1,8,6,4,0],
            'temperatura_referencia': [0x01,0x23,0xC2,8,6,4,0],
            'solicita_comandos': [0x01, 0x23, 0xC3, *registration_number],

            #envia comandos
            'envia_sinal_controle': [0x01,0x16,0xD1,8,6,4,0],
            'envia_sinal_referencia' : [0x01,0x16,0xD2,8,6,4,0],
            'envia_sinal_sistema_ligado' : [0x01,0x16,0xD3,8,6,4,0,1],
            'envia_sinal_sistema_desligado' : [0x01,0x16,0xD3,8,6,4,0,0],
            'envia_sinal_modo_dashboard' : [0x01,0x16,0xD4,8,6,4,0,0],
            'envia_sinal_modo_curva' : [0x01,0x16,0xD4,8,6,4,0,1],
            'envia_sinal_funcionamento_ligado' : [0x01,0x16,0xD5,8,6,4,0,1],
            'envia_sinal_funcionamento_desligado' : [0x01,0x16,0xD5,8,6,4,0,0],
            'envia_tempertura_ambiente' : [0x01,0x16,0xD6,8,6,4,0],
            
        }

        self.comandos = {
            0xA1:"Liga_Forno" ,
            0xA2:"Desliga_Forno",
            0xA3:"Inicia_aquecimento",
            0xA4:"Cancela_processo",
            0xA5:"alterna_modo",
        } 


    def envia_comando(self, comando, valor):
        if comando in self.controles:
            msg_bytes = bytes(self.controles[comando])
            if valor:
                if type(valor) == int:
                    valor = struct.pack("<i", valor)
                    msg_bytes = msg_bytes + valor
                elif type(valor) == float:
                    valor = round(valor,2)
                    valor = struct.pack(">f", valor)
                    msg_bytes = msg_bytes + valor
            crc = calcula_crc(msg_bytes)
            return msg_bytes + crc
        else:
            return None

    def recebe_comando(self, msg):
        if len(msg) == 9:
            data = msg[3:7]
            crc_verf = calcula_crc(msg[0:7])
            if crc_verf == msg[7:9]:
                if msg[2] == 0xC1 or msg[2] == 0xC2:
                    z = round(struct.unpack('>f', data)[0],2)
                    print ('z aqui')
                    print (z)
                    return z
                if msg[2] == 0xC3:
                    print ('x aqui')
                    print(data)
                    x = struct.unpack("<i", data)[0]
                    print (x)
                    return self.comandos.get(struct.unpack("<i", data)[0])

                else:
                    return msg[2],struct.unpack("<i", data)[0]
            else:
                raise Exception('CRC inválido')

        else:
            return None, None