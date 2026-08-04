# DP-PP-003 — Regras de Validação do Cadastro do Pet

## Identificação

DP-PP-003.

Classificação: NORMATIVO.

Projeto: CASE-03 — PetPass AI.

Funcionalidade: Cadastro do Pet (`FNMVP-001`).

## Assunto

Regras de validação da funcionalidade Cadastro do Pet (`FNMVP-001`).

## Contexto

Registrar formalmente a Deliberação do Product Owner referente às regras de validação da funcionalidade Cadastro do Pet (`FNMVP-001`), transformando a decisão aprovada em artefato normativo do projeto.

## Deliberação

Validações autorizadas para o Cadastro do Pet:

Nome do Pet

- Obrigatório.
- Não pode permanecer vazio.

Espécie

- Obrigatória.
- Seleção restrita às opções:
  - Cão
  - Gato

Raça

- Obrigatória.
- Não pode permanecer vazia.

Sexo

- Opcional.
- Valores permitidos:
  - Macho
  - Fêmea
  - Não informado

Idade

- Opcional.
- Número inteiro positivo.

Peso

- Opcional.
- Número decimal positivo.

Cor

- Opcional.
- Texto livre.

Foto

- Opcional.
- Arquivo de imagem.

## Justificativa

Deliberação aprovada pelo Product Owner para estabelecer regras mínimas de validação coerentes com o escopo do MVP e com os objetivos definidos na Issue da DIO.

## Restrições

Não implementar qualquer validação não prevista nesta deliberação.

Não utilizar IA para validar informações.

Não criar regras adicionais sem nova deliberação formal do Product Owner.

## Impacto

Autoriza a implementação das validações da funcionalidade Cadastro do Pet.

## Rastreabilidade

Origem:

- GP-PP-09A
- GP-PP-09B
- GP-PP-09C
- DP-PP-001
- DP-PP-002
