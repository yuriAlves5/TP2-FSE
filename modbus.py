
from crc16 import calcula_crc
import struct
#8640


controles = {
    #solicitação de leitura
    "temperatura_interna": [0x01, 0x23 , 0xC1 , 8 , 6 , 4 , 0],
    "temperatura_referencia": [0x01, 0x23 , 0xC2 , 8 , 6 , 4 , 0],
    "solicita_comandos": [0x01, 0x23 , 0xC3 , 8 , 6 , 4 , 0],

    #envia comandos
    "envia_sinal_controle": [0x01, 0x16 , 0xD1 , 8 , 6 , 4 , 0],
    "envia_sinal_referencia" : [0x01, 0x16 , 0xD2 , 8 , 6 , 4 , 0],
    "envia_sinal_sistema_ligado" : [0x01, 0x16 , 0xD3 , 8 , 6 , 4 , 0 , 1],
    "envia_sinal_sistema_desligado" : [0x01, 0x16 , 0xD3 , 8 , 6 , 4 , 0 , 0],
    "envia_sinal_modo_dashboard" : [0x01, 0x16 , 0xD4 , 8 , 6 , 4 , 0 , 0],
    "envia_sinal_modo_curva" : [0x01, 0x16 , 0xD4 , 8 , 6 , 4 , 0 , 1],
    "envia_sinal_funcionamento_ligado" : [0x01, 0x16 , 0xD5 , 8 , 6 , 4 , 0 , 1],
    "envia_sinal_funcionamento_desligado" : [0x01, 0x16 , 0xD5 , 8 , 6 , 4 , 0 , 0],
    "envia_tempertura_ambiente" : [0x01, 0x16 , 0xD6 , 8 , 6 , 4 , 0],
}
