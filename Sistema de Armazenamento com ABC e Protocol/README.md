# Sistema de Armazenamento com ABC e Protocol

Projeto em Python que compara duas abordagens de contrato: ABC (herança formal) e Protocol (contrato estrutural).

## Arquivos

| Arquivo | O que contém |
|---|---|
| `armazenador.py` | Classe abstrata base `Armazenador` (Parte A) |
| `armazenadores.py` | Classes `ArmazenadorArquivo` e `ArmazenadorBanco` |
| `protocolo.py` | O protocolo `Salvavel` (Parte B) |
| `nuvem.py` | Classe `ArmazenadorNuvem` (sem herança) |
| `funcoes.py` | Funções `executar_salvamento_formal()` e `executar_salvamento_flexivel()` |
| `main.py` | Código principal que executa o sistema |

## Como executar

Você precisa ter o Python instalado (versão 3.8 ou superior).

```
python main.py
```

## Saída esperada

```
--- Parte A: ABC ---
Salvando em arquivo local: dados do usuario
Salvando no banco de dados: dados do usuario
--- Parte B: Protocol ---
Salvando em arquivo local: dados do usuario
Salvando no banco de dados: dados do usuario
Salvando na nuvem: dados do usuario
```

## Perguntas do professor

**Em qual parte há contrato por herança?**
Na Parte A. `ArmazenadorArquivo` e `ArmazenadorBanco` herdam de `Armazenador` e são obrigados a implementar `salvar()`.

**Em qual parte há contrato estrutural?**
Na Parte B. `ArmazenadorNuvem` não herda de nada, mas funciona com `executar_salvamento_flexivel()` porque tem o método `salvar()`.

**Qual abordagem é mais rígida?**
ABC. A classe precisa declarar herança explicitamente e implementar todos os métodos abstratos.

**Qual abordagem é mais flexível?**
Protocol. Qualquer classe com o método certo já é compatível, sem precisar herdar de nada.

**Em qual situação ABC faz mais sentido? E em qual Protocol faz mais sentido?**
ABC faz mais sentido quando as classes fazem parte do mesmo sistema e você quer garantir que ninguém esqueça de implementar um método.
Protocol faz mais sentido quando você quer aceitar objetos de origens diferentes, como classes de bibliotecas externas que você não pode modificar.
