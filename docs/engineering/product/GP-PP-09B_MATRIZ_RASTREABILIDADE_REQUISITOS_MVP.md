# GP-PP-09B — Matriz de Rastreabilidade dos Requisitos do MVP

## Classificação

EXPERIMENTAL

## Projeto

CASE-03 — PetPass AI.

## Objetivo

Registrar a rastreabilidade dos requisitos do MVP utilizando exclusivamente como fonte primária o artefato `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md` e, para as correspondências autorizadas, as deliberações já aprovadas do CASE-03.

Origem: Product Owner, GP-PP-09B.

## Fonte primária exclusiva

- Artefato: `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`.
- Fonte autoritativa nele registrada: Issue #7 da DIO.
- Título registrado: "Ficha de Identificação Inteligente para Pets".
- Descrição registrada: "Projeto desenvolvido para o Desafio DIO de IA Generativa. Uma ficha prática de cadastro e emergência veterinária."

Origem: `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`, seção “Fonte primária”.

## Critério de composição da matriz

- A coluna “Descrição literal do requisito” reproduz somente texto presente na fonte primária.
- A coluna “Funcionalidade correspondente no MVP” utiliza somente funcionalidades autorizadas nas deliberações do Product Owner já aprovadas no CASE-03.
- A coluna “Artefato ou componente” identifica somente artefatos ou elementos já implementados e autorizados; não propõe arquitetura.
- O estado `PLANEJADO` é o estado inicial obrigatório desta matriz e não constitui avaliação do estado de implementação já observado no projeto.

Origem: Product Owner, GP-PP-09B.

## Matriz de rastreabilidade

| Identificação | Origem — fonte primária | Descrição literal do requisito | Funcionalidade correspondente no MVP | Artefato ou componente onde será implementado | Critério objetivo de verificação | Estado inicial |
|---|---|---|---|---|---|---|
| RQMVP-001 | Issue #7 da DIO, registrada em `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md` | “Uma ficha prática de cadastro e emergência veterinária.” | Cadastro do Pet; seção Tutor; seção Informações Médicas; Ficha de Emergência. Correspondências autorizadas respectivamente pelas GP-PP-04, GP-PP-05, GP-PP-06 e GP-PP-07. | `main.py`: Cadastro do Pet e Ficha de Emergência, já autorizados nas GP-PP-04 a GP-PP-07. | Verificar objetivamente que um cadastro válido contém os campos autorizados de Pet, Tutor e Informações Médicas e que a Ficha de Emergência apresenta os dados informados, conforme os critérios de aceite das GP-PP-04 a GP-PP-07. | PLANEJADO |
| RQMVP-002 | Issue #7 da DIO, registrada em `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md` | “Projeto desenvolvido para o Desafio DIO de IA Generativa.” | Geração do Resumo Inteligente da Ficha de Emergência por IA Generativa real da OpenAI. Correspondência autorizada pela GP-PP-08, pela deliberação GP-PP-08A do Product Owner e pela GP-PP-09. | `openai_service.py`: comunicação com a Responses API; `main.py`: acionamento e apresentação do Resumo Inteligente, conforme autorizado nas GP-PP-08 e GP-PP-09. | Verificar objetivamente que o acionamento autorizado envia somente os dados informados ao serviço, ignora campos vazios e apresenta o resumo em janela própria, sem diagnóstico, tratamento, prescrição ou informação inexistente, conforme os critérios de aceite da GP-PP-09. | PLANEJADO |

## Ausências de informação registradas

### AUS-001 — Localizador externo da fonte primária

O endereço eletrônico e o repositório ou espaço específico da Issue #7 da DIO não constam da fonte primária.

Tratamento: ausência registrada; nenhum endereço foi inferido.

Origem da constatação: `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`, seção “Limitação do localizador”.

### AUS-002 — Identificadores de requisitos na Issue #7

A fonte primária não fornece identificadores individuais de requisitos.

Tratamento: `RQMVP-001` e `RQMVP-002` são identificadores documentais desta matriz e não alteram o conteúdo literal da fonte.

Origem da constatação: conteúdo integral de `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`.

### AUS-003 — Critérios de verificação na fonte primária

A fonte primária não apresenta critérios objetivos de verificação.

Tratamento: os critérios registrados na matriz remetem exclusivamente aos critérios de aceite das deliberações GP-PP já aprovadas; nenhum critério foi atribuído à Issue #7.

Origem da constatação: conteúdo integral de `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md` e deliberações citadas na matriz.

### AUS-004 — Artefatos ou componentes na fonte primária

A fonte primária não identifica arquivos, artefatos técnicos ou componentes de implementação.

Tratamento: a matriz referencia somente os arquivos e elementos já autorizados e existentes no CASE-03; nenhuma arquitetura foi proposta.

Origem da constatação: conteúdo integral de `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md` e deliberações citadas na matriz.

## Limites deste artefato

Esta matriz:

- não cria requisitos;
- não interpreta requisitos implícitos;
- não propõe arquitetura;
- não produz código;
- não modifica decisões anteriores;
- não altera artefatos existentes;
- não autoriza atividade posterior.

Origem: Product Owner, GP-PP-09B.

## Declaração de rastreabilidade

As descrições literais registradas nesta matriz remontam à Issue #7 da DIO exclusivamente por meio do artefato autoritativo `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md`. As correspondências funcionais, técnicas e verificáveis são sustentadas apenas pelas deliberações do Product Owner já aprovadas e expressamente identificadas em cada linha.

Classificação do artefato: EXPERIMENTAL.
