from funcionarios import FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
from empresa import Empresa
empresa = Empresa("Tech Ltda")

assalariado = FuncionarioAssalariado("Ana Silva", "111.111.111-11", 3000)
horista = FuncionarioHorista("Carlos Souza", "222.222.222-22", 80, 25)
comissionado = FuncionarioComissionado("Maria Lima", "333.333.333-33", 10000, 10)

empresa.adicionar_funcionario(assalariado)
empresa.adicionar_funcionario(horista)
empresa.adicionar_funcionario(comissionado)
empresa.listar_funcionarios()
empresa.mostrar_folha_pagamento()
