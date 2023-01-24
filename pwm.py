import RPi.GPIO as GPIO

class PWM:
    def __init__(self, pin_resistor = 23,pin_vent = 24, freq=999):
        self.resistor = pin_resistor
        self.vent = pin_vent
        self.freq = freq
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.resistor, GPIO.OUT)
        GPIO.setup(self.vent, GPIO.OUT)
        self.pwm_resistor = GPIO.PWM(self.resistor, self.freq)
        self.pwm_vent = GPIO.PWM(self.vent, self.freq)

    def iniciar(self, duty_resistor, duty_vent):
        self.pwm_resistor.start(duty_resistor)
        self.pwm_vent.start(duty_vent)

    def mudar_resistor(self, duty_resistor):
        self.pwm_resistor.ChangeDutyCycle(duty_resistor)
    
    def mudar_vent(self, duty_vent):
        self.pwm_vent.ChangeDutyCycle(duty_vent)
    
    def mudar_duty(self, duty_resistor, duty_vent):
        self.pwm_resistor.ChangeDutyCycle(duty_resistor)
        self.pwm_vent.ChangeDutyCycle(duty_vent)
    
    def change_freq(self, freq):
        self.freq = freq
        self.pwm_resistor.ChangeFrequency(freq)
        self.pwm_vent.ChangeFrequency(freq)

    def aplicar_sinal(self, sinal):
        if sinal > 0:
            self.mudar_resistor(sinal)
            self.mudar_vent(0)
        elif sinal < 0:
            self.mudar_resistor(0)
            self.mudar_vent(abs(sinal))

    def parar(self):
        self.pwm_resistor.stop()
        self.pwm_vent.stop()
        GPIO.cleanup()
        print('Conexão encerrada com sucesso!')
    
    