class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self):
        print("Imprimindo boleto")
        print("Código:", self.codigo)
        print("Valor: R$", self.valor)

class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self):
        print("Imprimindo etiqueta")
        print("Destinatário:", self.destinatario)
        print("Endereço:", self.endereco)

class RelatorioSimples:
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self):
        print("Imprimindo relatório")
        print("Título:", self.titulo)
