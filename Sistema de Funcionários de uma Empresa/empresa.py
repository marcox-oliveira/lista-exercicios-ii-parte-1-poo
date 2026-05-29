class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print("Funcionários da empresa", self.nome)
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()
            print("---")

    def mostrar_folha_pagamento(self):
        print("Folha de pagamento -", self.nome)
        for funcionario in self.funcionarios:
            pagamento = funcionario.calcular_pagamento()
            print(funcionario.nome, "| Pagamento: R$", pagamento)
