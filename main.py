from menu import Menu
from modbus import Modbus


#loop
    #menu 1
       #cada 500ms ler o commando
         #depois de 1 segundo chamar control

menu = Menu()
modbus = Modbus()


x = menu.print_dashboard()
print(x)

msg = 'envia_sinal_controle'
value = None
comando = modbus.envia_comando(msg, value)
print(comando)
modbus.recebe_comando(comando)