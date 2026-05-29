# Sistema de Impressão com Protocol

Projeto em Python usando Protocol para contrato estrutural sem herança obrigatória.

## Arquivos

| Arquivo | O que contém |
|---|---|
| `protocolo.py` | O protocolo `Imprimivel` |
| `itens.py` | Classes `Boleto`, `Etiqueta` e `RelatorioSimples` |
| `impressao.py` | Função `processar_impressao()` |
| `main.py` | Código principal que executa o sistema |

## Como executar

Você precisa ter o Python instalado (versão 3.8 ou superior).

```
python main.py
```

## Saída esperada

```
---
Imprimindo boleto
Código: 12345-6
Valor: R$ 150.0
---
Imprimindo etiqueta
Destinatário: João Silva
Endereço: Rua das Flores, 42
---
Imprimindo relatório
Título: Vendas do Mês
---
```

## Perguntas do professor

**Onde está o contrato nesse caso?**
No protocolo `Imprimivel`, definido em `protocolo.py`. Ele diz que qualquer objeto compatível deve ter o método `imprimir()`.

**Por que as classes podem funcionar sem herdar explicitamente do protocolo?**
Porque o Python usa verificação estrutural: se a classe tem o método `imprimir()`, ela já é compatível com o protocolo automaticamente. Não precisa declarar herança.

**Esse caso se aproxima mais de ABC ou de duck typing?**
De duck typing. A ideia é: "se o objeto tem o método certo, ele serve"; sem forçar uma herança.

**Qual a principal diferença entre esse caso e o das questões anteriores?**
Nas questões anteriores, as classes eram obrigadas a herdar da classe abstrata. Aqui, as classes são completamente independentes entre si; o que as une é apenas ter o método `imprimir()`.
