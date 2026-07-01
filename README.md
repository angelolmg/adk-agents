# Agente assistente de pesquisa acadêmica


PPGEEC2327 - TÓPICOS ESPECIAIS EM PROCESSAMENTO INTELIGENTE DA INFORMAÇÃO - T01 (2026.1 - 5T3456)

Docente: Prof. Dr Ivanovich Medeiros Dantas Silva

Discentes:   
- Angelo Leite Medeiros de Góes (20251012333)
- William Marcelino Costa do Nascimento (20251026230)

Este trabalho investiga a criação de agentes com a plataforma ADK do Google para auxiliar na criação e desenvolvimento de trabalhos acadêmicos.

O agente deverá ser capaz de auxiliar o usuário em tarefas como:

- Busca de literatura científica;
- Organização de referências bibliográficas;
- Resumos críticos de artigos;
- Comparação e análise de autores e tendências;
- Geração de novos tópicos de pesquisa.

## Como executar o agente localmente

#### Prerequisitos:
 - python

#### Instale o UV

```bash
pip install uv
```

#### Inicie o projeto com o uv

```bash
uv sync
```

#### Crie venv com o uv

```bash
uv venv
```

#### Ative o .venv

```bash
source .venv/bin/activate
```

#### Instale as dependências

```bash
uv add google-adk google-generativeai python-dotenv
```

#### Inicie o agente

```bash
adk web
```