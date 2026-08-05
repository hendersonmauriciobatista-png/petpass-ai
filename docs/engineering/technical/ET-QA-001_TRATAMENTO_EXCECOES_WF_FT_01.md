# ET-QA-001 — TRATAMENTO DAS EXCEÇÕES DO WF-FT-01

## 1. Identificação

- **Atividade:** ET-QA-001
- **Projeto:** CASE-03 — PetPass AI
- **Disciplina:** Engenharia Técnica — Qualidade
- **Objeto:** tratamento conceitual das exceções técnicas do WF-FT-01
- **Data:** 04/08/2026
- **Estado:** Definido

## 2. Objetivo

Definir o comportamento técnico oficial diante de falha de armazenamento, indisponibilidade posterior dos dados e falha da confirmação visual, sem alterar o caminho de sucesso do FT-01, as responsabilidades das camadas, os componentes, os modelos de dados ou as decisões da Engenharia de Produto.

## 3. Fontes obrigatórias

- `ET-GOV-001_CONGELAMENTO_ARQUITETURA_TECNICA.md`.
- `ET-AR-003_COMPLEMENTACAO_ARQUITETURA_TECNOLOGICA.md`.
- `WF-FT-01_ESPECIFICACAO_IMPLEMENTACAO_CADASTRO_VALIDO_PET.md`.
- `WF-FT-01-REV_PRONTIDAO_IMPLEMENTACAO.md`.
- `ET-IF-001_FLUXOS_TECNICOS_PETPASS_AI.md`.
- `ET-IM-001_PLANO_IMPLEMENTACAO_ENGENHARIA_TECNICA.md`.

## 4. Princípios obrigatórios de tratamento

1. Uma exceção técnica não pode ser convertida em resultado de sucesso.
2. O WF-FT-01 somente poderá produzir sua saída oficial quando todos os critérios documentais de conclusão estiverem comprovados na mesma execução.
3. Uma execução encerrada por exceção não poderá liberar a continuidade para WF-FT-03.
4. O n8n coordena detecção, interrupção e encaminhamento do resultado, mas não assume responsabilidades de Apresentação, Domínio ou Registro Oficial.
5. Nenhum tratamento poderá alterar os dados informados pelo usuário, criar regras de validação ou simular confirmação não recebida.
6. As exceções técnicas não modificam o FT-01; elas determinam exclusivamente o estado de uma execução que não alcançou o resultado esperado desse fluxo.

## 5. EX-FT01-01 — Falha de armazenamento

### 5.1 Exceção

- **Evento caracterizador:** após resultado válido produzido por CT-09 e CT-10 e solicitação coordenada por CT-05, CA-04 não confirma o armazenamento de ED-01 em ED-02 ou, quando aplicável, a vinculação de ED-05.
- **Impacto sobre o fluxo:** o critério de sucesso “registro armazenado com sucesso” não é atendido. A sequência não pode avançar para confirmação oficial nem para apresentação de sucesso.

### 5.2 Detecção

- **Camada responsável pela constatação:** CA-04 — Registro Oficial de Informações.
- **Componentes envolvidos:** CT-13 e, quando houver fotografia, CT-15.
- **Evidência mínima:** ausência de confirmação de armazenamento ou resultado explícito de falha devolvido por CA-04 a CA-02.
- **Responsabilidade de CA-02:** CT-05 reconhece que não recebeu a confirmação exigida e interrompe a continuidade do WF-FT-01.

### 5.3 Tratamento

1. CA-04 devolve a CA-02 resultado técnico de armazenamento não confirmado.
2. CT-05 impede a declaração de cadastro concluído.
3. CT-05 não libera WF-FT-03 nem qualquer funcionalidade dependente de cadastro concluído.
4. CA-02 encaminha a CA-01 o estado objetivo de falha técnica, sem apresentá-lo como erro de validação.
5. CT-02 informa que o cadastro não foi concluído devido à falha técnica de armazenamento.
6. CA-01 preserva os dados já apresentados pelo usuário durante a execução corrente.
7. Nenhuma confirmação visual de sucesso é apresentada.

Não há repetição automática, correção automática, armazenamento alternativo ou criação de registro presumido.

### 5.4 Encerramento

- **Estado final esperado do workflow:** `ENCERRADO COM FALHA TÉCNICA — ARMAZENAMENTO NÃO CONFIRMADO`.
- **Estado do cadastro:** não concluído para fins do WF-FT-01.
- **Critério documental de encerramento:** existência conjunta de evidência de falha ou ausência de confirmação de CA-04, interrupção registrada por CT-05, ausência de liberação do WF-FT-03 e retorno objetivo apresentado por CT-02.
- **Limite:** o encerramento da exceção encerra somente a execução corrente; não define política de nova tentativa.

### 5.5 Responsabilidades das camadas

| Camada | Responsabilidade |
|---|---|
| CA-01 | Preservar a entrada corrente e apresentar o retorno técnico recebido. |
| CA-02 | Coordenar a solicitação, reconhecer a ausência de confirmação e interromper a execução. |
| CA-03 | Manter inalterado o resultado de validação; não tratar falha de armazenamento. |
| CA-04 | Detectar e comunicar que o armazenamento ou a vinculação não foi confirmado. |

## 6. EX-FT01-02 — Indisponibilidade posterior dos dados

### 6.1 Exceção

- **Evento caracterizador:** após a operação de armazenamento, CA-04 não confirma que ED-01/ED-02 e, quando aplicável, ED-05 permanecem disponíveis para as funcionalidades subsequentes.
- **Impacto sobre o fluxo:** o critério de sucesso relativo à disponibilidade posterior dos dados não é atendido. A confirmação de conclusão não pode ser emitida e a continuidade para workflows dependentes permanece bloqueada.

### 6.2 Detecção

- **Camada responsável pela constatação:** CA-04 — Registro Oficial de Informações.
- **Componentes envolvidos:** CT-13 e, quando aplicável, CT-15.
- **Evidência mínima:** resultado de indisponibilidade ou ausência da confirmação de disponibilidade requerida pelo WF-FT-01.
- **Responsabilidade de CA-02:** CT-05 reconhece que a condição cumulativa de sucesso não foi comprovada.

### 6.3 Tratamento

1. CA-04 devolve a CA-02 o estado de disponibilidade não confirmada.
2. CT-05 impede a conclusão do WF-FT-01 e não libera WF-FT-03.
3. CA-02 não presume disponibilidade com base apenas no resultado anterior da operação de armazenamento.
4. CA-02 encaminha a CA-01 o estado objetivo de indisponibilidade técnica.
5. CT-02 informa que o cadastro não pôde ser concluído porque a disponibilidade dos dados não foi confirmada.
6. CA-01 preserva os dados já apresentados pelo usuário durante a execução corrente.
7. Nenhuma confirmação visual de sucesso é apresentada.

Não há reconstrução, duplicação, substituição ou armazenamento alternativo automático dos dados.

### 6.4 Encerramento

- **Estado final esperado do workflow:** `ENCERRADO COM FALHA TÉCNICA — DISPONIBILIDADE NÃO CONFIRMADA`.
- **Estado do cadastro no WF-FT-01:** conclusão não reconhecida, independentemente de ter existido uma operação anterior de armazenamento.
- **Critério documental de encerramento:** evidência de disponibilidade não confirmada, interrupção registrada por CT-05, bloqueio dos workflows posteriores e retorno objetivo apresentado por CT-02.
- **Limite:** esta atividade não define recuperação, reconciliação ou nova tentativa posterior.

### 6.5 Responsabilidades das camadas

| Camada | Responsabilidade |
|---|---|
| CA-01 | Preservar a entrada corrente e apresentar o retorno técnico recebido. |
| CA-02 | Exigir a confirmação de disponibilidade, interromper a execução quando ausente e bloquear continuidade. |
| CA-03 | Não presumir nem determinar disponibilidade do Registro Oficial. |
| CA-04 | Verificar e comunicar o estado de disponibilidade dos dados oficiais. |

## 7. EX-FT01-03 — Falha da confirmação visual

### 7.1 Exceção

- **Evento caracterizador:** CA-04 confirmou armazenamento e disponibilidade, CA-02 encaminhou o resultado oficial a CA-01, mas CT-02 não confirma a apresentação visual da conclusão ao usuário.
- **Impacto sobre o fluxo:** o critério de sucesso “confirmação visual apresentada” não é atendido. O workflow não pode ser declarado integralmente concluído.

### 7.2 Detecção

- **Camada responsável pela constatação:** CA-01 — Apresentação e Interação Institucional.
- **Componente envolvido:** CT-02.
- **Evidência mínima:** ausência da confirmação de apresentação visual ou resultado explícito de falha produzido por CT-02.
- **Responsabilidade de CA-02:** CT-05 reconhece que não recebeu a confirmação final necessária ao encerramento bem-sucedido.

### 7.3 Tratamento

1. CT-02 comunica a CA-02 que a confirmação visual não foi apresentada.
2. CT-05 registra que o WF-FT-01 não alcançou seu critério documental completo de conclusão.
3. CT-05 não libera WF-FT-03 durante essa execução.
4. O registro já confirmado por CA-04 permanece no Registro Oficial e não é removido, duplicado ou alterado pela falha de Apresentação.
5. CA-02 não solicita novo armazenamento e não presume que a confirmação foi visualizada.
6. Quando CA-01 puder apresentar retorno, CT-02 informa objetivamente a falha técnica de confirmação, sem declarar novo sucesso.

Não há repetição automática da apresentação, reversão automática do registro ou nova operação de armazenamento.

### 7.4 Encerramento

- **Estado final esperado do workflow:** `ENCERRADO COM FALHA TÉCNICA — CONFIRMAÇÃO VISUAL NÃO COMPROVADA`.
- **Estado do registro:** armazenamento e disponibilidade permanecem conforme confirmação de CA-04; o registro não é revertido pela exceção de Apresentação.
- **Estado da execução:** conclusão integral do WF-FT-01 não reconhecida e continuidade para WF-FT-03 bloqueada nessa execução.
- **Critério documental de encerramento:** evidência de falha ou ausência de confirmação de CT-02, preservação do registro oficial já confirmado, ausência de nova solicitação de armazenamento e bloqueio da continuidade por CT-05.
- **Limite:** esta atividade não define repetição posterior da apresentação nem retomada da execução.

### 7.5 Responsabilidades das camadas

| Camada | Responsabilidade |
|---|---|
| CA-01 | Detectar e comunicar que CT-02 não comprovou a apresentação visual. |
| CA-02 | Registrar a não conclusão integral, evitar novo armazenamento e bloquear continuidade nessa execução. |
| CA-03 | Não alterar o resultado válido de domínio por falha de Apresentação. |
| CA-04 | Preservar o registro já confirmado, sem duplicação ou reversão automática. |

## 8. Matriz consolidada de tratamento

| Exceção | Detecção | Tratamento central | Encerramento |
|---|---|---|---|
| EX-FT01-01 — Falha de armazenamento | CA-04 não confirma armazenamento; CT-05 reconhece ausência | Interromper antes do sucesso, preservar entrada corrente, informar falha e bloquear WF-FT-03 | Falha técnica; cadastro não concluído |
| EX-FT01-02 — Indisponibilidade posterior | CA-04 não confirma disponibilidade; CT-05 reconhece condição não atendida | Não presumir disponibilidade, informar falha e bloquear workflows posteriores | Falha técnica; conclusão não reconhecida |
| EX-FT01-03 — Falha da confirmação visual | CT-02 não comprova apresentação; CT-05 reconhece ausência | Preservar registro confirmado, não armazenar novamente e bloquear WF-FT-03 nessa execução | Falha técnica; confirmação visual não comprovada |

## 9. Critérios comuns de tratamento

- Toda exceção deve possuir evidência produzida pela camada responsável por sua detecção.
- CT-05 deve registrar o estado de não conclusão da execução.
- Nenhuma exceção pode produzir confirmação visual de sucesso.
- Nenhuma exceção pode liberar WF-FT-03 durante a execução afetada.
- Os dados apresentados pelo usuário devem permanecer preservados na execução corrente.
- Nenhuma camada pode assumir responsabilidade pertencente a outra camada.
- Nenhuma tentativa automática, compensação, alternativa de armazenamento ou correção é autorizada.

## 10. Critérios comuns de encerramento

Uma exceção somente estará documentalmente encerrada quando existirem, cumulativamente:

1. identificação inequívoca de uma das três exceções;
2. evidência da camada responsável pela detecção;
3. interrupção ou não conclusão registrada por CT-05;
4. ausência de resultado oficial de sucesso;
5. bloqueio da continuidade para WF-FT-03;
6. preservação dos limites de responsabilidade das camadas;
7. estado final correspondente registrado.

O encerramento de uma exceção não equivale à conclusão bem-sucedida do cadastro.

## 11. Limites

- Não são definidos código, nós ou gatilhos n8n.
- Não são definidos APIs, endpoints, contratos adicionais, banco físico ou infraestrutura.
- Não são definidos quantidade de tentativas, temporização, timeout, repetição, recuperação ou reconciliação.
- Não são criados novos componentes, entidades, relacionamentos ou fluxos.
- Não são alterados os critérios de sucesso do WF-FT-01.
- Não é autorizada a implementação.

## 12. Declaração de conformidade metodológica

A ET-QA-001 define exclusivamente o tratamento conceitual das três exceções registradas pelo corpus obrigatório. A arquitetura congelada, os componentes, os modelos, os fluxos e as decisões da Engenharia de Produto foram preservados. Nenhum código, nó n8n, API, banco de dados, infraestrutura ou implementação foi criado; nenhum documento anterior foi alterado e nenhuma atividade posterior foi iniciada.
