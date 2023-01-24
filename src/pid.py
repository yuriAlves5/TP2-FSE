class PID:
    def __init__(self,Kp=20.0,Ki=0.1,Kd=100.0,T=1,control_signal_MAX=100.0,control_signal_MIN=-100.0,):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.T = T
        self.control_signal_MAX = control_signal_MAX
        self.control_signal_MIN = control_signal_MIN
        self.referencia = 0.0
        self.erro_total = 0.0
        self.erro_anterior = 0.0

    def configura_constantes(self, kp, ki, kd):
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd

    def atualiza_referencia(self, referencia):
        self.referencia = referencia

    def control(self, medida_temp):

        erro = self.referencia - medida_temp

        self.erro_total += erro

        if self.erro_total >= self.control_signal_MAX:
            self.erro_total = self.control_signal_MAX
        elif self.erro_total <= self.control_signal_MIN:
            self.erro_total = self.control_signal_MIN

        delta_error = erro - self.erro_anterior
        control_signal = (
            (self.Kp * erro) + (self.Ki * self.T * self.erro_total) + (self.Kd / self.T * delta_error)
        )

        if control_signal >= self.control_signal_MAX:
            control_signal = self.control_signal_MAX

        elif control_signal <= self.control_signal_MIN:
            control_signal = self.control_signal_MIN

        if control_signal < 0 and control_signal > -40:
            control_signal = -40

        self.erro_anterior = erro

        return int(control_signal)