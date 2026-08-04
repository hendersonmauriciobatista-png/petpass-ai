# GP-PP-09D — Consolidado das Deliberações do Product Owner para o MVP

## Identificação do consolidado

Projeto: CASE-03 — PetPass AI.

Classificação: NORMATIVO.

Data da consolidação: 01/08/2026.

## Ordem cronológica

As deliberações estão reproduzidas integralmente na ordem cronológica dos artefatos normativos: DP-PP-001, DP-PP-002, DP-PP-003, DP-PP-004 e DP-PP-005.

---

# DP-PP-001 — Campos do Cadastro do Pet

## Identificação

DP-PP-001.

Classificação: NORMATIVO.

Projeto: CASE-03 — PetPass AI.

Funcionalidade: Cadastro do Pet (`FNMVP-001`).

## Assunto

Campos da funcionalidade Cadastro do Pet (`FNMVP-001`).

## Contexto

Registrar formalmente a Deliberação do Product Owner referente aos campos da funcionalidade Cadastro do Pet (`FNMVP-001`), transformando a decisão aprovada em artefato normativo do projeto.

## Deliberação

Cadastro do Pet composto exclusivamente pelos campos:

- Nome do Pet
- Espécie
- Raça
- Sexo
- Idade
- Peso
- Cor
- Foto (opcional)

## Justificativa

Deliberação aprovada pelo Product Owner para definir formalmente os campos do MVP do PetPass AI, preservando o escopo aprovado.

## Restrições

Nenhum outro campo está autorizado.

Qualquer ampliação dependerá de nova deliberação do Product Owner.

## Impacto

Autoriza a especificação e futura implementação da funcionalidade Cadastro do Pet.

## Rastreabilidade

Origem:

- GP-PP-09A
- GP-PP-09B
- GP-PP-09C

---

# DP-PP-002 — Campos Obrigatórios e Opcionais do Cadastro do Pet

## Identificação

DP-PP-002.

Classificação: NORMATIVO.

Projeto: CASE-03 — PetPass AI.

Funcionalidade: Cadastro do Pet (`FNMVP-001`).

## Assunto

Classificação dos campos obrigatórios e opcionais da funcionalidade Cadastro do Pet (`FNMVP-001`).

## Contexto

Registrar formalmente a Deliberação do Product Owner referente à classificação dos campos obrigatórios e opcionais da funcionalidade Cadastro do Pet (`FNMVP-001`), transformando a decisão aprovada em artefato normativo do projeto.

## Deliberação

Campos obrigatórios:

- Nome do Pet
- Espécie
- Raça

Campos opcionais:

- Sexo
- Idade
- Peso
- Cor
- Foto

## Justificativa

Deliberação aprovada pelo Product Owner para simplificar o MVP, garantir a identificação mínima necessária do pet e manter o cadastro objetivo e aderente aos objetivos definidos pela Issue da DIO.

## Restrições

Nenhum outro campo poderá ser classificado como obrigatório ou opcional sem nova deliberação formal do Product Owner.

## Impacto

Autoriza a implementação das validações obrigatórias da funcionalidade Cadastro do Pet e estabelece o conjunto mínimo de informações necessárias para o MVP.

## Rastreabilidade

Origem:

- GP-PP-09A
- GP-PP-09B
- GP-PP-09C
- DP-PP-001

---

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

---

# DP-PP-004 — Tratamento de Falhas do Cadastro do Pet

## Identificação

DP-PP-004.

Classificação: NORMATIVO.

Projeto: CASE-03 — PetPass AI.

Funcionalidade: Cadastro do Pet (`FNMVP-001`).

## Assunto

Tratamento de falhas da funcionalidade Cadastro do Pet (`FNMVP-001`).

## Contexto

Registrar formalmente a Deliberação do Product Owner referente ao tratamento de falhas da funcionalidade Cadastro do Pet (`FNMVP-001`), transformando a decisão aprovada em artefato normativo do projeto.

## Deliberação

Tratamento de Falhas autorizado para a funcionalidade Cadastro do Pet:

Quando houver erro em qualquer campo obrigatório:

- impedir o salvamento do cadastro;
- destacar visualmente o(s) campo(s) com erro;
- apresentar mensagem objetiva informando o motivo do bloqueio;
- preservar todos os dados já preenchidos pelo usuário.

## Justificativa

Deliberação aprovada pelo Product Owner por estar alinhada aos objetivos do software definidos pela Issue da DIO, preservando a experiência do usuário e evitando perda de informações durante o preenchimento do cadastro.

## Restrições

- Não limpar automaticamente o formulário.
- Não utilizar IA para validar ou corrigir dados.
- Não implementar mensagens inteligentes.
- Não criar tratamentos adicionais sem nova deliberação formal do Product Owner.

## Impacto

Autoriza a implementação do tratamento de falhas da funcionalidade Cadastro do Pet.

## Rastreabilidade

Origem:

- GP-PP-09A
- GP-PP-09B
- GP-PP-09C
- DP-PP-001
- DP-PP-002
- DP-PP-003

---

# DP-PP-005 — Critérios de Sucesso do Cadastro do Pet

## Identificação

DP-PP-005.

Classificação: NORMATIVO.

Projeto: CASE-03 — PetPass AI.

Funcionalidade: Cadastro do Pet (`FNMVP-001`).

## Assunto

Critérios de sucesso da funcionalidade Cadastro do Pet (`FNMVP-001`).

## Contexto

Registrar formalmente a Deliberação do Product Owner referente aos critérios de sucesso da funcionalidade Cadastro do Pet (`FNMVP-001`), transformando a decisão aprovada em artefato normativo do projeto.

## Deliberação

Critérios de sucesso da funcionalidade Cadastro do Pet:

O cadastro será considerado concluído com sucesso quando:

- todos os campos obrigatórios estiverem preenchidos conforme as validações autorizadas;
- nenhuma regra de validação for violada;
- o registro for armazenado com sucesso;
- o sistema apresentar confirmação visual da conclusão do cadastro;
- os dados permanecerem disponíveis para utilização nas funcionalidades subsequentes do MVP.

## Justificativa

Deliberação aprovada pelo Product Owner por representar de forma coerente os critérios de conclusão da funcionalidade, alinhados aos objetivos do software definidos na Issue da DIO e ao escopo do MVP.

## Restrições

- Não considerar concluído qualquer cadastro que viole regras de validação.
- Não criar critérios adicionais sem nova deliberação formal do Product Owner.
- Não utilizar critérios implícitos ou inferidos.

## Impacto

Autoriza a implementação dos critérios de conclusão da funcionalidade Cadastro do Pet e estabelece a condição normativa para aceitação da implementação.

## Rastreabilidade

Origem:

- GP-PP-09A
- GP-PP-09B
- GP-PP-09C
- DP-PP-001
- DP-PP-002
- DP-PP-003
- DP-PP-004
