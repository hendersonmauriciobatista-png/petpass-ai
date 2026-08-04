# GP-PP-09C — Especificação Funcional do MVP

## Classificação

EXPERIMENTAL

## Projeto

CASE-03 — PetPass AI.

## Objetivo

Especificar exclusivamente as funcionalidades identificadas em `GP-PP-09B_MATRIZ_RASTREABILIDADE_REQUISITOS_MVP.md`, mantendo a rastreabilidade com `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`.

## Fontes exclusivas

- `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`.
- `GP-PP-09B_MATRIZ_RASTREABILIDADE_REQUISITOS_MVP.md`.

Nenhuma outra fonte foi utilizada.

## Regra dos identificadores funcionais

Os identificadores `FNMVP-001` a `FNMVP-005` são identificadores documentais desta especificação. Eles não criam requisitos e não alteram os identificadores `RQMVP-001` e `RQMVP-002` registrados na matriz de rastreabilidade.

## FNMVP-001 — Cadastro do Pet

### Requisito de origem

`RQMVP-001` — “Uma ficha prática de cadastro e emergência veterinária.”

### Objetivo funcional

Disponibilizar o Cadastro do Pet como parte da ficha prática de cadastro e emergência veterinária.

### Entradas previstas

Campos autorizados de Pet.

A identificação individual dos campos: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Saídas previstas

Cadastro contendo os campos autorizados de Pet.

### Regras de negócio explicitamente aprovadas

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Validações previstas

A matriz exige a verificação de um cadastro válido, mas não define as validações que determinam essa validade.

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Condições de sucesso

O cadastro válido contém os campos autorizados de Pet.

### Condições de falha

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Dependências registradas

- Requisito `RQMVP-001`.
- Artefato registrado na matriz: `main.py`.
- Correspondência autorizada pela GP-PP-04, conforme registro da matriz.

### Ausências de informação

- Campos individuais do Pet: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Regras de negócio: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Validações específicas: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Tratamento de falha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## FNMVP-002 — Seção Tutor

### Requisito de origem

`RQMVP-001` — “Uma ficha prática de cadastro e emergência veterinária.”

### Objetivo funcional

Disponibilizar a seção Tutor no cadastro integrante da ficha prática de cadastro e emergência veterinária.

### Entradas previstas

Campos autorizados de Tutor.

A identificação individual dos campos: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Saídas previstas

Cadastro contendo os campos autorizados de Tutor.

### Regras de negócio explicitamente aprovadas

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Validações previstas

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Condições de sucesso

O cadastro válido contém os campos autorizados de Tutor.

### Condições de falha

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Dependências registradas

- Requisito `RQMVP-001`.
- Artefato registrado na matriz: `main.py`.
- Correspondência autorizada pela GP-PP-05, conforme registro da matriz.

### Ausências de informação

- Campos individuais do Tutor: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Regras de negócio: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Validações específicas: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Tratamento de falha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## FNMVP-003 — Seção Informações Médicas

### Requisito de origem

`RQMVP-001` — “Uma ficha prática de cadastro e emergência veterinária.”

### Objetivo funcional

Disponibilizar a seção Informações Médicas no cadastro integrante da ficha prática de cadastro e emergência veterinária.

### Entradas previstas

Campos autorizados de Informações Médicas.

A identificação individual dos campos: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Saídas previstas

Cadastro contendo os campos autorizados de Informações Médicas.

### Regras de negócio explicitamente aprovadas

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Validações previstas

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Condições de sucesso

O cadastro válido contém os campos autorizados de Informações Médicas.

### Condições de falha

**AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Dependências registradas

- Requisito `RQMVP-001`.
- Artefato registrado na matriz: `main.py`.
- Correspondência autorizada pela GP-PP-06, conforme registro da matriz.

### Ausências de informação

- Campos individuais das Informações Médicas: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Regras de negócio: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Validações específicas: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Tratamento de falha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## FNMVP-004 — Ficha de Emergência

### Requisito de origem

`RQMVP-001` — “Uma ficha prática de cadastro e emergência veterinária.”

### Objetivo funcional

Apresentar na Ficha de Emergência os dados informados no cadastro.

### Entradas previstas

Dados informados nos campos autorizados de Pet, Tutor e Informações Médicas.

### Saídas previstas

Ficha de Emergência apresentando os dados informados.

### Regras de negócio explicitamente aprovadas

A Ficha de Emergência apresenta os dados informados.

### Validações previstas

Verificar objetivamente que a Ficha de Emergência apresenta os dados informados.

### Condições de sucesso

Os dados informados são apresentados na Ficha de Emergência.

### Condições de falha

O comportamento previsto quando a condição de sucesso não for atendida: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Dependências registradas

- Requisito `RQMVP-001`.
- Dados informados no cadastro.
- Artefato registrado na matriz: `main.py`.
- Correspondência autorizada pela GP-PP-07, conforme registro da matriz.

### Ausências de informação

- Formato de apresentação além da identificação como Ficha de Emergência: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Tratamento de falha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## FNMVP-005 — Resumo Inteligente

### Requisito de origem

`RQMVP-002` — “Projeto desenvolvido para o Desafio DIO de IA Generativa.”

### Objetivo funcional

Gerar o Resumo Inteligente da Ficha de Emergência por IA Generativa real da OpenAI.

### Entradas previstas

Somente os dados informados na Ficha de Emergência.

### Saídas previstas

Resumo Inteligente apresentado em janela própria.

### Regras de negócio explicitamente aprovadas

- Utilizar somente os dados informados.
- Ignorar campos vazios.
- Não produzir diagnóstico.
- Não produzir tratamento.
- Não produzir prescrição.
- Não acrescentar informação inexistente.

### Validações previstas

- Verificar que somente os dados informados são enviados ao serviço.
- Verificar que campos vazios são ignorados.
- Verificar que o resumo é apresentado em janela própria.
- Verificar que o resumo não contém diagnóstico, tratamento, prescrição ou informação inexistente.

### Condições de sucesso

O acionamento envia somente os dados informados ao serviço, ignora campos vazios e apresenta o resumo em janela própria sem diagnóstico, tratamento, prescrição ou informação inexistente.

### Condições de falha

O comportamento previsto quando a condição de sucesso não for atendida: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

### Dependências registradas

- Requisito `RQMVP-002`.
- Dados informados na Ficha de Emergência.
- `openai_service.py`: comunicação com a Responses API.
- `main.py`: acionamento e apresentação do Resumo Inteligente.
- GP-PP-08, deliberação GP-PP-08A e GP-PP-09, conforme registro da matriz.

### Ausências de informação

- Formato textual específico do resumo: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Tratamento de falha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## Ausências gerais preservadas

- Endereço eletrônico da Issue #7 da DIO: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Repositório ou espaço específico da Issue #7 da DIO: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Critérios objetivos originalmente presentes na Issue #7: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Artefatos ou componentes originalmente presentes na Issue #7: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## Limites

Este artefato:

- não cria requisitos;
- não interpreta requisitos implícitos;
- não produz arquitetura;
- não produz código;
- não modifica artefatos existentes;
- não inicia implementação;
- não altera decisões metodológicas;
- não autoriza atividade posterior.

Classificação do artefato: EXPERIMENTAL.
