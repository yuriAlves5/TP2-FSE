from menu import Menu
from forno import Forno
import time

if __name__ == '__main__':
    menu = Menu()
    forno = Forno()
    option = 0
    loop = 0
    while True:
        option = menu.print_dashboard()
        if option == '1':
            while True:
                comando = forno.receber_comando()
                if comando == 'Liga_Forno':
                    forno.Liga_Forno()
                elif comando == 'Desliga_Forno':
                    forno.Desliga_Forno()
                elif comando == 'Inicia_aquecimento':
                    forno.Inicia_aquecimento()
                    forno.update_geral
                elif comando == 'Cancela_processo':
                    forno.Cancela_processo()

                time.sleep(0.5)
                
        else:
            break


# #loop
#     #menu 1
#        #cada 500ms ler o commando
#          #depois de 1 segundo chamar control

# menu = Menu()
# modbus = Modbus()


# x = menu.print_dashboard()
# print(x)

# msg = 'envia_sinal_controle'
# value = None
# comando = modbus.envia_comando(msg, value)
# print(comando)
# modbus.recebe_comando(comando)