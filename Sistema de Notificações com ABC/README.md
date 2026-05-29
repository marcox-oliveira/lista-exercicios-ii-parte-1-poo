# Sistema de Notificações com ABC

Projeto em Python com classes, herança e polimorfismo.

## Arquivos

| Arquivo | O que contém |
|---|---|
| `notificador.py` | Classe abstrata base `Notificador` |
| `notificadores.py` | Classes `NotificadorEmail`, `NotificadorSMS` e `NotificadorApp` |
| `central.py` | Classe `CentralNotificacoes` |
| `main.py` | Código principal que executa o sistema |

## Como executar

Você precisa ter o Python instalado (versão 3.6 ou superior).

```
python main.py
```

## Saída esperada

```
E-mail enviado: Sua conta foi atualizada com sucesso!
SMS enviado: Sua conta foi atualizada com sucesso!
Notificação no app enviada: Sua conta foi atualizada com sucesso!
```

## Perguntas do professor

**Qual classe representa o contrato formal?**
A classe `Notificador`, definida em `notificador.py`.

**Onde há polimorfismo?**
No método `enviar_para_todos()` da `CentralNotificacoes`, que chama `notificar()` para cada objeto da lista e cada um responde de forma diferente.

**Por que faz sentido usar ABC nesse caso?**
Porque garante que todo notificador tenha o método `notificar()`. A central pode chamar esse método sem se preocupar com qual tipo de notificador está usando.
**O que aconteceria se uma subclasse de Notificador não implementasse notificar()?**
O Python geraria um erro na hora de criar o objeto, impedindo o uso da classe incompleta.
