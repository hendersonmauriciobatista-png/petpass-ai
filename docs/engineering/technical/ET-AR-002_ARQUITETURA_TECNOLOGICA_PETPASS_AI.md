# ET-AR-002 — ARQUITETURA TECNOLÓGICA DO PETPASS AI

## 1. Identificação

- **Atividade:** ET-AR-002
- **Projeto:** CASE-03 — PetPass AI
- **Artefato:** Arquitetura Tecnológica do PetPass AI
- **Classificação:** Engenharia Técnica
- **Estado:** Definido
- **Data:** 03/08/2026

## 2. Objetivo

Definir as tecnologias responsáveis por materializar as camadas arquiteturais, os componentes técnicos e os fluxos do PetPass AI, preservando integralmente as decisões da Engenharia de Produto e sem definir infraestrutura física ou iniciar implementação.

## 3. Fontes obrigatórias

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md`.
- `ET-DD-002_MODELO_LOGICO_DADOS_PETPASS_AI.md`.
- `ET-IF-001_FLUXOS_TECNICOS_PETPASS_AI.md`.
- `DP-PP-001_CAMPOS_CADASTRO_PET.md` a `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md`.
- Deliberações tecnológicas aprovadas na atividade ET-AR-002.

## 4. Deliberações tecnológicas aprovadas

1. O n8n constitui o orquestrador oficial dos fluxos técnicos do PetPass AI.
2. Cada Fluxo Técnico (FT) poderá ser implementado como workflow independente no n8n.
3. O n8n será responsável exclusivamente pela coordenação e orquestração dos processos técnicos.
4. As regras de domínio permanecerão subordinadas às deliberações documentadas pela Engenharia de Produto.
5. A Arquitetura Tecnológica preservará integralmente a separação entre Apresentação, Coordenação, Domínio, Registro Oficial e Limite com o Ambiente.

## 5. Tecnologia responsável por camada arquitetural

| Camada | Componentes abrangidos | Tecnologia responsável | Fundamentação e limite |
|---|---|---|---|
| CA-01 — Apresentação e Interação Institucional | CT-01 a CT-04 | **NÃO DETERMINADA PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDA.** | A camada e seus componentes foram definidos em ET-AR-001 e ET-CP-001, mas nenhuma tecnologia de apresentação foi aprovada nas fontes desta atividade. |
| CA-02 — Coordenação de Aplicação | CT-05 a CT-08 | **n8n** | Tecnologia explicitamente aprovada para coordenação e orquestração dos fluxos técnicos. Não incorpora responsabilidades de domínio, registro, apresentação ou ambiente. |
| CA-03 — Domínio e Regras do PetPass AI | CT-09 a CT-12 | **NÃO DETERMINADA PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDA.** | As regras permanecem subordinadas às DP-PP. O n8n poderá coordenar sua aplicação, mas não passa a ser, por essa autorização, a tecnologia responsável pela camada de Domínio. |
| CA-04 — Registro Oficial de Informações | CT-13 a CT-16 | **NÃO DETERMINADA PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDA.** | Nenhuma tecnologia de armazenamento ou persistência foi aprovada. O n8n poderá coordenar solicitações ao Registro Oficial, sem assumir sua responsabilidade. |
| CA-05 — Limite com o Ambiente de Utilização | CT-17 | **NÃO DETERMINADA PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDA.** | Nenhuma tecnologia de comunicação com o ambiente foi aprovada. O limite definido pela DP-PP-015 permanece preservado. |

## 6. Tecnologia de orquestração

O **n8n** é a tecnologia oficial da camada CA-02 — Coordenação de Aplicação. Sua aplicação tecnológica abrange os componentes CT-05, CT-06, CT-07 e CT-08, exclusivamente para coordenar as sequências documentadas em ET-IF-001.

A adoção do n8n não altera:

- as responsabilidades das cinco camadas de ET-AR-001;
- os componentes de ET-CP-001;
- as entidades de ET-DD-001;
- os relacionamentos e invariantes de ET-DD-002;
- as sequências e limites dos fluxos de ET-IF-001;
- as decisões de negócio formalizadas nas DP-PP.

## 7. Mapeamento entre Fluxos Técnicos e workflows

Cada associação abaixo registra a possibilidade aprovada de implementação independente. Não determina decomposição física, gatilhos, nós, mensagens, protocolos ou interfaces.

| Fluxo Técnico | Finalidade documentada | Mapeamento tecnológico autorizado | Situação |
|---|---|---|---|
| FT-01 — Cadastro válido do Pet | Cadastro Oficial | Workflow n8n `WF-FT-01` | Poderá ser implementado como workflow independente. |
| FT-02 — Bloqueio do Cadastro por falha de validação | Cadastro Oficial | Workflow n8n `WF-FT-02` | Poderá ser implementado como workflow independente. |
| FT-03 — Constituição da Identidade Digital | Identidade Digital | Workflow n8n `WF-FT-03` | Poderá ser implementado como workflow independente. |
| FT-04 — Regeneração da representação QR Code | Identidade Digital | Workflow n8n `WF-FT-04` | Poderá ser implementado como workflow independente. |
| FT-05 — Apresentação da Ficha de Emergência | Representação Institucional | Workflow n8n `WF-FT-05` | Poderá ser implementado como workflow independente. |
| FT-06 — Acionamento do Contato de Emergência | Contato de Emergência | Workflow n8n `WF-FT-06` | Poderá ser implementado como workflow independente. |

Os identificadores `WF-FT-01` a `WF-FT-06` estabelecem somente correspondência documental entre cada FT e sua possível representação como workflow. Não criam novos componentes nem autorizam implementação.

## 8. Relações de coordenação entre workflows

As relações tecnológicas preservam exclusivamente as relações já documentadas em ET-IF-001:

- `WF-FT-01` poderá permitir a continuidade coordenada de `WF-FT-03` após cadastro válido.
- `WF-FT-02` impedirá a continuidade para `WF-FT-03` quando houver falha de validação.
- `WF-FT-03` poderá fornecer a identidade digital necessária à coordenação de `WF-FT-05`.
- `WF-FT-04` poderá atualizar a representação utilizada por `WF-FT-05`, preservando a mesma Key Pass.
- `WF-FT-05` poderá disponibilizar o acionamento que inicia `WF-FT-06`.

O mecanismo tecnológico dessas relações não foi determinado pelas fontes obrigatórias e não é inferido neste documento.

## 9. Integrações arquiteturais previstas

| Origem | Destino | Finalidade arquitetural | Tecnologia ou mecanismo de integração |
|---|---|---|---|
| CA-01 — Apresentação | CA-02 — Coordenação/n8n | Encaminhar solicitações funcionais e receber resultados para apresentação. | **NÃO DETERMINADO PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDO.** |
| CA-02 — Coordenação/n8n | CA-03 — Domínio | Solicitar aplicação das regras documentadas e receber seus resultados. | **NÃO DETERMINADO PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDO.** |
| CA-02 — Coordenação/n8n | CA-04 — Registro Oficial | Coordenar solicitações de registro, consulta e obtenção das informações oficiais previstas. | **NÃO DETERMINADO PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDO.** |
| CA-02 — Coordenação/n8n | CA-05 — Limite com o Ambiente | Entregar ao ambiente a intenção de contato e o número oficial apresentado. | **NÃO DETERMINADO PELAS FONTES OBRIGATÓRIAS — NÃO INFERIDO.** |
| Workflows n8n relacionados | Workflows n8n relacionados | Preservar as relações entre FT documentadas em ET-IF-001. | n8n, sem mecanismo interno definido nesta atividade. |

Não são previstas integrações diretas que contrariem as relações permitidas e os limites estabelecidos em ET-AR-001.

## 10. Limites de responsabilidade do n8n

O n8n poderá exclusivamente:

- coordenar a execução dos Fluxos Técnicos documentados;
- preservar a ordem e os limites de interação definidos em ET-IF-001;
- encaminhar solicitações entre as camadas pelas relações autorizadas;
- receber resultados das camadas e coordenar sua continuidade;
- representar cada FT como workflow independente, quando essa opção for adotada posteriormente.

O n8n não poderá:

- criar, alterar, substituir ou interpretar regras de domínio;
- criar validações, tratamentos de falha ou critérios de sucesso não documentados;
- assumir responsabilidades da camada de Apresentação;
- assumir a condição de Registro Oficial ou definir sua persistência;
- gerar ou alterar a Key Pass fora das regras normativas;
- tratar o QR Code como identificador independente;
- definir o mecanismo tecnológico de comunicação do telefone de emergência;
- modificar entidades, relacionamentos, cardinalidades ou invariantes dos modelos de dados;
- preencher ausências documentais por comportamento de workflow;
- promover decisões técnicas de implementação não aprovadas nesta atividade.

## 11. Restrições tecnológicas

- Somente o n8n foi tecnologicamente aprovado neste artefato.
- Não são definidos linguagem, framework de apresentação, banco de dados, mecanismo de persistência, API, protocolo, infraestrutura, hospedagem ou recurso de comunicação.
- A configuração física do n8n, seus nós, gatilhos, credenciais, conexões e forma de execução não são definidos.
- A separação entre Apresentação, Coordenação, Domínio, Registro Oficial e Limite com o Ambiente é obrigatória.
- Nenhuma tecnologia poderá transferir para a Coordenação responsabilidades pertencentes às demais camadas.
- Toda futura materialização tecnológica permanecerá subordinada às DP-PP e aos artefatos da Engenharia Técnica vigentes.
- Este documento não autoriza implementação.

## 12. Definições tecnológicas não determinadas

Permanecem sem determinação nas fontes obrigatórias:

- tecnologia da camada de Apresentação;
- tecnologia da camada de Domínio;
- tecnologia da camada de Registro Oficial;
- tecnologia da camada de Limite com o Ambiente;
- mecanismos de integração entre as camadas;
- mecanismo de relação entre workflows;
- infraestrutura física de execução.

Essas ausências são registradas sem preenchimento por inferência e não alteram a decisão aprovada de adoção do n8n como orquestrador oficial.

## 13. Declaração de conformidade metodológica

A ET-AR-002 foi produzida exclusivamente a partir das fontes obrigatórias e das deliberações tecnológicas expressamente aprovadas. O documento adota somente o n8n, limita-o à Coordenação e Orquestração, preserva as cinco camadas, os componentes, os modelos de dados, os fluxos e as decisões da Engenharia de Produto. Tecnologias e mecanismos ausentes foram registrados como não determinados, sem inferência. Nenhuma infraestrutura física foi definida e nenhuma implementação foi iniciada.
