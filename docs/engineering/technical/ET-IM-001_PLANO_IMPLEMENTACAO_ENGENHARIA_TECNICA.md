# ET-IM-001 — PLANO OFICIAL DE IMPLEMENTAÇÃO DA ENGENHARIA TÉCNICA

## 1. Identificação

- **Atividade:** ET-IM-001
- **Projeto:** CASE-03 — PetPass AI
- **Disciplina:** Engenharia Técnica — Planejamento da Implementação
- **Data:** 03/08/2026
- **Estado:** Definido
- **Escopo:** sequência de construção dos componentes, workflows e entregas técnicas, sem início de desenvolvimento

## 2. Objetivo

Estabelecer a ordem oficial de implementação das estruturas documentadas pela Engenharia Técnica, preservando as camadas, os componentes, as entidades, os relacionamentos, os fluxos e os limites tecnológicos vigentes.

## 3. Fontes obrigatórias

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `ET-AR-002_ARQUITETURA_TECNOLOGICA_PETPASS_AI.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md`.
- `ET-DD-002_MODELO_LOGICO_DADOS_PETPASS_AI.md`.
- `ET-IF-001_FLUXOS_TECNICOS_PETPASS_AI.md`.

## 4. Condição geral para início da implementação

A ET-AR-002 aprovou exclusivamente o n8n para a camada CA-02 — Coordenação de Aplicação. Permanecem não determinadas as tecnologias das camadas CA-01, CA-03, CA-04 e CA-05, bem como os mecanismos de integração entre as camadas e entre workflows.

Consequentemente, este plano define a sequência oficial, mas **não autoriza o início da Fase 1** enquanto as tecnologias e os mecanismos necessários aos componentes envolvidos não estiverem documentalmente determinados. Essa condição preserva a proibição de completar a arquitetura por inferência.

## 5. Princípios de ordenação

1. FT-01 e FT-02 precedem a constituição da identidade digital, pois FT-03 depende da conclusão válida do cadastro e é excluído pelo bloqueio do cadastro.
2. FT-03 precede FT-05, pois fornece a identidade digital utilizada pela Ficha de Emergência.
3. FT-04 sucede a disponibilidade de uma Key Pass existente e antecede qualquer apresentação que dependa da representação regenerada.
4. FT-05 precede FT-06, pois disponibiliza o contato oficial cujo acionamento inicia o fluxo de contato de emergência.
5. Cada FT poderá ser materializado como workflow independente no n8n, conforme ET-AR-002.
6. Componentes compartilhados serão construídos na primeira fase em que forem necessários e reutilizados nas fases seguintes sem mudança de responsabilidade.

## 6. Fases de implementação

### Fase 1 — Cadastro Oficial

- **Objetivo:** materializar o cadastro válido e o bloqueio por falha de validação, preservando os resultados documentados para ambos os caminhos.
- **Componentes envolvidos:**
  - CT-01 — Apresentação do Cadastro do Pet;
  - CT-02 — Apresentação de Retorno do Cadastro;
  - CT-05 — Coordenação do Cadastro do Pet;
  - CT-09 — Avaliador das Regras do Cadastro;
  - CT-10 — Determinador do Resultado do Cadastro;
  - CT-13 — Registro Oficial do Pet;
  - CT-15 — Registro da Fotografia Vinculada, quando houver fotografia.
- **Workflows envolvidos:**
  - `WF-FT-01` — Cadastro válido do Pet;
  - `WF-FT-02` — Bloqueio do Cadastro por falha de validação.
- **Entidades e relações preservadas:** ED-01, ED-02 e, quando aplicável, ED-05; RL-01 e RL-04.
- **Dependências:** definições tecnológicas das camadas CA-01, CA-03 e CA-04; mecanismos de integração com CA-02; modelo lógico vigente; regras representadas pelos componentes CT-09 e CT-10.
- **Critério de entrada:** fontes obrigatórias vigentes; tecnologias e mecanismos necessários aos componentes da fase documentalmente determinados; responsabilidades das camadas preservadas.
- **Critério de saída:** CT-01, CT-02, CT-05, CT-09, CT-10, CT-13 e CT-15, quando aplicável, materializados dentro de seus limites; `WF-FT-01` e `WF-FT-02` capazes de reproduzir as sequências, os resultados e as exclusões documentadas em ET-IF-001; nenhuma identidade digital constituída a partir de cadastro inválido.
- **Artefatos produzidos:** implementação técnica dos componentes listados; workflows n8n correspondentes a FT-01 e FT-02; configuração técnica estritamente necessária às integrações previamente determinadas; registros objetivos de verificação dos critérios de saída.

### Fase 2 — Identidade Digital

- **Objetivo:** materializar a constituição da Key Pass e sua representação QR Code após cadastro válido, incluindo a regeneração da representação sem alteração da identidade.
- **Componentes envolvidos:**
  - CT-05 — Coordenação do Cadastro do Pet, reutilizado;
  - CT-06 — Coordenação da Identidade Digital;
  - CT-11 — Guardião das Regras da Identidade Digital;
  - CT-16 — Registro da Identidade Digital.
- **Workflows envolvidos:**
  - `WF-FT-03` — Constituição da Identidade Digital;
  - `WF-FT-04` — Regeneração da representação QR Code.
- **Entidades e relações preservadas:** ED-01, ED-02, ED-06 e ED-07; RL-05 e RL-06; agrupamento AL-02.
- **Dependências:** conclusão da Fase 1; cadastro oficial válido e confirmado; definições tecnológicas das camadas CA-03 e CA-04; mecanismos de integração com CA-02.
- **Critério de entrada:** critérios de saída da Fase 1 atendidos; tecnologia e mecanismos necessários aos componentes desta fase documentalmente determinados; invariantes de ED-06 e ED-07 preservadas.
- **Critério de saída:** CT-06, CT-11 e CT-16 materializados dentro de seus limites; `WF-FT-03` capaz de associar identidade exclusivamente após cadastro válido; `WF-FT-04` capaz de preservar a Key Pass durante a regeneração da representação; ausência de alteração das invariantes documentadas.
- **Artefatos produzidos:** implementação técnica dos componentes próprios da fase; workflows n8n correspondentes a FT-03 e FT-04; configuração técnica estritamente necessária às integrações previamente determinadas; registros objetivos de verificação dos critérios de saída.

### Fase 3 — Representação Institucional da Ficha de Emergência

- **Objetivo:** materializar a apresentação da Ficha de Emergência exclusivamente como representação institucional das informações oficiais cadastradas.
- **Componentes envolvidos:**
  - CT-03 — Apresentação Institucional da Ficha de Emergência;
  - CT-07 — Coordenação da Ficha de Emergência;
  - CT-12 — Guardião da Consistência Documental;
  - CT-13 — Registro Oficial do Pet, reutilizado;
  - CT-14 — Registro de Informações Associadas;
  - CT-15 — Registro da Fotografia Vinculada, reutilizado;
  - CT-16 — Registro da Identidade Digital, reutilizado.
- **Workflows envolvidos:**
  - `WF-FT-05` — Apresentação da Ficha de Emergência.
- **Entidades e relações preservadas:** ED-01 a ED-08; RL-07 a RL-13; agrupamento AL-03.
- **Dependências:** conclusão das Fases 1 e 2; informações oficiais disponíveis por CT-13 a CT-16; definições tecnológicas das camadas CA-01, CA-03 e CA-04; mecanismos de integração com CA-02.
- **Critério de entrada:** critérios de saída das Fases 1 e 2 atendidos; tecnologias e mecanismos necessários aos componentes da fase documentalmente determinados; informações oficiais requeridas pelo FT-05 disponíveis no Registro Oficial.
- **Critério de saída:** CT-03, CT-07, CT-12 e CT-14 materializados dentro de seus limites; `WF-FT-05` capaz de executar a sequência documentada; ED-08 apresentada sem se tornar origem primária; identidade institucional, dados oficiais e estados aprovados de ausência preservados.
- **Artefatos produzidos:** implementação técnica dos componentes próprios da fase; workflow n8n correspondente a FT-05; configuração técnica estritamente necessária às integrações previamente determinadas; registros objetivos de verificação dos critérios de saída.

### Fase 4 — Acionamento do Contato de Emergência

- **Objetivo:** materializar a entrega da intenção de contato ao ambiente de utilização, usando exclusivamente o número oficial apresentado e encerrando a responsabilidade do PetPass AI no limite documentado.
- **Componentes envolvidos:**
  - CT-04 — Acionador Visual do Contato de Emergência;
  - CT-08 — Coordenação do Contato de Emergência;
  - CT-14 — Registro de Informações Associadas, reutilizado;
  - CT-17 — Entrega da Ação de Contato ao Ambiente.
- **Workflows envolvidos:**
  - `WF-FT-06` — Acionamento do Contato de Emergência.
- **Entidades e relações preservadas:** ED-02, ED-04 e ED-08; RL-03 e RL-10.
- **Dependências:** conclusão da Fase 3; contato oficial apresentado pela Ficha de Emergência; definição tecnológica da camada CA-05; mecanismos de integração de CA-01 e CA-05 com CA-02.
- **Critério de entrada:** critérios de saída da Fase 3 atendidos; tecnologia e mecanismos necessários aos componentes da fase documentalmente determinados; número oficial disponível na ficha.
- **Critério de saída:** CT-04, CT-08 e CT-17 materializados dentro de seus limites; `WF-FT-06` capaz de entregar ao ambiente a intenção e o número oficial; nenhum mecanismo próprio de comunicação incorporado ao produto.
- **Artefatos produzidos:** implementação técnica dos componentes próprios da fase; workflow n8n correspondente a FT-06; configuração técnica estritamente necessária às integrações previamente determinadas; registros objetivos de verificação dos critérios de saída.

## 7. Ordem oficial das entregas

| Ordem | Fase | Entrega técnica principal | Workflows |
|---:|---|---|---|
| 1 | Cadastro Oficial | Caminhos de cadastro válido e bloqueado, com registro somente após validação | WF-FT-01 e WF-FT-02 |
| 2 | Identidade Digital | Key Pass e representação QR Code associadas ao cadastro válido; regeneração preservando a identidade | WF-FT-03 e WF-FT-04 |
| 3 | Representação Institucional | Ficha de Emergência baseada exclusivamente no Registro Oficial | WF-FT-05 |
| 4 | Contato de Emergência | Entrega da intenção de contato ao ambiente | WF-FT-06 |

Essa ordem é obrigatória. A conclusão documental de uma fase não autoriza a fase seguinte quando seu critério de entrada ainda não estiver integralmente atendido.

## 8. Dependências consolidadas entre as entregas

| Entrega de origem | Entrega dependente | Dependência documental |
|---|---|---|
| Fase 1 — FT-01 | Fase 2 — FT-03 | A identidade digital somente pode ser constituída após cadastro válido e confirmado. |
| Fase 1 — FT-02 | Fase 2 — FT-03 | O bloqueio exclui a continuidade para constituição da identidade digital. |
| Fase 2 — FT-03 | Fase 2 — FT-04 | A regeneração depende de Key Pass existente. |
| Fase 2 — FT-03 | Fase 3 — FT-05 | A identidade digital fornece Key Pass e QR Code utilizados pela ficha. |
| Fase 2 — FT-04 | Fase 3 — FT-05 | A representação regenerada poderá atualizar exclusivamente o QR Code utilizado na ficha. |
| Fase 1 — Registro Oficial | Fase 3 — FT-05 | A ficha depende das informações disponibilizadas pelo Registro Oficial. |
| Fase 3 — FT-05 | Fase 4 — FT-06 | O acionamento depende do contato oficial apresentado na ficha. |

## 9. Restrições do plano

- O plano não implementa componentes ou workflows.
- O plano não cria código nem inicia desenvolvimento.
- O plano não define infraestrutura física.
- O plano não modifica as cinco camadas de ET-AR-001.
- O plano não modifica os 17 componentes de ET-CP-001.
- O plano não modifica as oito entidades, os 13 relacionamentos ou os três agrupamentos lógicos.
- O plano não modifica os seis fluxos de ET-IF-001.
- O n8n permanece restrito à Coordenação e Orquestração.
- Nenhuma tecnologia ausente na ET-AR-002 é preenchida por inferência.
- Os artefatos de implementação e verificação somente poderão materializar o conteúdo já documentado nas fontes vigentes.

## 10. Declaração de conformidade metodológica

Este plano foi produzido exclusivamente a partir das seis fontes obrigatórias. A ordem das quatro fases decorre das dependências explícitas entre FT-01 a FT-06, componentes e entidades. Nenhuma arquitetura, componente, entidade, relação, fluxo ou tecnologia foi alterado ou acrescentado. As ausências tecnológicas registradas na ET-AR-002 permanecem como condições impeditivas de início, sem preenchimento por inferência. Nenhum workflow foi implementado, nenhum código foi criado e nenhuma atividade posterior foi iniciada.
