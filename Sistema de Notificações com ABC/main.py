from notificadores import NotificadorEmail, NotificadorSMS, NotificadorApp
from central import CentralNotificacoes

central = CentralNotificacoes()

email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)
central.enviar_para_todos("Sua conta foi atualizada com sucesso!")
