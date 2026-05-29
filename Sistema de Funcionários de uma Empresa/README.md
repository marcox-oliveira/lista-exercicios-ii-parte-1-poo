# Sistema de Funcionários de uma Empresa

Projeto em Python com classes, herança e polimorfismo.

## Arquivos

| Arquivo | O que contém |
|---|---|
| `funcionario.py` | Classe abstrata base `Funcionario` |
| `funcionarios.py` | Classes `FuncionarioAssalariado`, `FuncionarioHorista` e `FuncionarioComissionado` |
| `empresa.py` | Classe `Empresa` |
| `main.py` | Código principal que executa o sistema |

## Como executar

Você precisa ter o Python instalado (versão 3.6 ou superior).

```
python main.py
```

## Saída esperada

```
Funcionários da empresa Tech Ltda
Nome: Ana Silva
CPF: 111.111.111-11
---
Nome: Carlos Souza
CPF: 222.222.222-22
---
Nome: Maria Lima
CPF: 333.333.333-33
---
Folha de pagamento - Tech Ltda
Ana Silva | Pagamento: R$ 3000
Carlos Souza | Pagamento: R$ 2000
Maria Lima | Pagamento: R$ 1000.0
```

## Perguntas do professor

**Qual é a superclasse da hierarquia?**
A classe `Funcionario`, definida em `funcionario.py`.

**Quais são as subclasses?**
`FuncionarioAssalariado`, `FuncionarioHorista` e `FuncionarioComissionado`.

**Onde ocorre sobrescrita?**
Cada subclasse sobrescreve o método `calcular_pagamento()` com sua própria regra de cálculo.

**Onde ocorre polimorfismo?**
No método `mostrar_folha_pagamento()` da `Empresa`, que chama `calcular_pagamento()` para cada funcionário e cada um calcula de forma diferente.

**Qual a vantagem de usar ABC nesse caso?**
O ABC garante que toda subclasse de `Funcionario` implemente `calcular_pagamento()`. Se esquecer, o Python gera um erro na hora de criar o objeto.
