from notificador import Notificador
class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print("E-mail enviado:", mensagem)

class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print("SMS enviado:", mensagem)

class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        print("Notificação no app enviada:", mensagem)
