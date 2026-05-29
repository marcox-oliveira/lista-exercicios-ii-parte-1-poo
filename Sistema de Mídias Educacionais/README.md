# Sistema de Mídias Educacionais

Projeto em Python com classes, herança e polimorfismo.

## Arquivos

| Arquivo | O que contém |
|---|---|
| `midia.py` | Classe abstrata base `Midia` |
| `midias.py` | Classes `Video`, `Podcast` e `TextoNarrado` |
| `plataforma.py` | Classe `Plataforma` |
| `main.py` | Código principal que executa o sistema |

## Como executar

Você precisa ter o Python instalado (versão 3.6 ou superior).

```
python main.py
```

## Saída esperada

```
Mídias da plataforma EduStream
Título: Introdução ao Python
Duração: 45 minutos
---
Título: IA no Cotidiano
Duração: 30 minutos
---
Título: Conceitos de POO
Duração: 20 minutos
---
Reproduzindo todas as mídias:
Reproduzindo vídeo: Introdução ao Python em 1080p
Reproduzindo podcast: IA no Cotidiano com Prof. Alternei
Reproduzindo texto narrado: Conceitos de POO em Português
```

## Perguntas do professor

**Qual é a classe abstrata do sistema?**
A classe `Midia`, definida em `midia.py`.

**Onde aparece a hierarquia?**
`Video`, `Podcast` e `TextoNarrado` herdam de `Midia`.

**Onde aparece o polimorfismo?**
No método `reproduzir_todas()` da `Plataforma`, que chama `reproduzir()` em cada mídia e cada uma responde de forma diferente.

**Por que Midia não deveria ser instanciada diretamente?**
Porque ela é abstrata; não tem uma implementação de `reproduzir()`. O Python gera um erro se você tentar criar um objeto `Midia()` diretamente.
