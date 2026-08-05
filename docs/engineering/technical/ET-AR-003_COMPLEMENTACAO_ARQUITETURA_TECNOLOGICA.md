# ET-AR-003 — COMPLEMENTAÇÃO DA ARQUITETURA TECNOLÓGICA

## 1. Identificação

- **Atividade:** ET-AR-003
- **Projeto:** CASE-03 — PetPass AI
- **Disciplina:** Engenharia Técnica — Arquitetura Tecnológica
- **Data:** 03/08/2026
- **Estado:** Definido
- **Escopo:** complementação tecnológica necessária ao WF-FT-01, sem implementação

## 2. Objetivo

Eliminar os impedimentos tecnológicos identificados pela WF-FT-01-REV para permitir a futura implementação integral do WF-FT-01, preservando as cinco camadas da ET-AR-001, os componentes da ET-CP-001, os modelos de dados, os fluxos técnicos e as decisões da Engenharia de Produto.

## 3. Fontes obrigatórias

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `ET-AR-002_ARQUITETURA_TECNOLOGICA_PETPASS_AI.md`.
- `WF-FT-01_ESPECIFICACAO_IMPLEMENTACAO_CADASTRO_VALIDO_PET.md`.
- `WF-FT-01-REV_PRONTIDAO_IMPLEMENTACAO.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md`.
- `ET-DD-002_MODELO_LOGICO_DADOS_PETPASS_AI.md`.
- `ET-IF-001_FLUXOS_TECNICOS_PETPASS_AI.md`.
- `ET-IM-001_PLANO_IMPLEMENTACAO_ENGENHARIA_TECNICA.md`.

## 4. Tecnologias oficializadas

| Camada ou integração | Tecnologia oficial | Aplicação no WF-FT-01 |
|---|---|---|
| CA-01 — Apresentação e Interação Institucional | Python com PySide6 | Materialização de CT-01 e CT-02 para receber os dados, encaminhar a solicitação e apresentar o resultado. |
| CA-02 — Coordenação de Aplicação | n8n | Materialização da coordenação de CT-05 e do workflow WF-FT-01. Decisão preservada da ET-AR-002. |
| CA-03 — Domínio e Regras do PetPass AI | Python | Materialização de CT-09 e CT-10, isolados da apresentação, da coordenação e do registro oficial. |
| CA-04 — Registro Oficial de Informações | SQLite, acessado exclusivamente por componente de registro em Python | Materialização de CT-13 e CT-15 e manutenção oficial de ED-01, ED-02 e ED-05, sem transferência de regras de domínio ao banco de dados. |
| Integração entre CA-01, CA-02, CA-03 e CA-04 | HTTP com conteúdo JSON | Transporte das solicitações e dos resultados entre as camadas, com o n8n coordenando as chamadas sem assumir responsabilidades das camadas integradas. |

As versões específicas das tecnologias não são definidas nesta atividade. Essa ausência não altera a escolha tecnológica nem autoriza adoção automática de versão fora de processo técnico posterior.

## 5. Responsabilidade tecnológica por camada

### 5.1 CA-01 — Python com PySide6

- Receber os valores dos campos autorizados por CT-01.
- Encaminhar a solicitação de conclusão à CA-02 pelo mecanismo oficial de integração.
- Receber o resultado coordenado.
- Apresentar por CT-02 a confirmação visual ou o retorno pertencente ao fluxo aplicável.
- Preservar a limitação de não validar regras por decisão própria e de não acessar diretamente CA-03 ou CA-04.

### 5.2 CA-02 — n8n

- Representar WF-FT-01 como workflow de coordenação.
- Receber a solicitação proveniente de CA-01.
- Coordenar a avaliação em CA-03.
- Coordenar o registro em CA-04 somente após resultado válido.
- Devolver o resultado a CA-01.
- Não executar regras de domínio, não manter o Registro Oficial e não apresentar interface.

### 5.3 CA-03 — Python

- Materializar CT-09 e CT-10.
- Aplicar exclusivamente as validações documentadas.
- Determinar ausência ou existência de violação impeditiva.
- Produzir o resultado de domínio consumido pela coordenação.
- Não manter estado oficial, não apresentar interface e não coordenar o processo.

### 5.4 CA-04 — SQLite com acesso por componente de registro em Python

- Materializar CT-13 e CT-15.
- Manter ED-01 associada a ED-02 após resultado válido.
- Manter ED-05 vinculada a ED-02 quando houver fotografia válida.
- Confirmar o armazenamento e disponibilizar os dados oficiais aos fluxos autorizados.
- Não decidir validações, não coordenar o workflow e não apresentar resultados ao usuário.
- O acesso ao SQLite permanece encapsulado na camada CA-04; CA-01 e o n8n não acessam diretamente o Registro Oficial.

## 6. Mecanismo oficial de integração

O mecanismo oficial entre CA-01, CA-02, CA-03 e CA-04 será **HTTP com conteúdo JSON**.

Aplicação arquitetural:

1. CA-01 encaminha a solicitação de cadastro a CA-02 por HTTP/JSON.
2. CA-02, por n8n, encaminha a solicitação de avaliação a CA-03 por HTTP/JSON.
3. CA-03 devolve o resultado de domínio a CA-02 por HTTP/JSON.
4. Quando o resultado for válido, CA-02 solicita a CA-04 o registro oficial por HTTP/JSON.
5. CA-04 devolve a confirmação do registro a CA-02 por HTTP/JSON.
6. CA-02 devolve o resultado oficial a CA-01 por HTTP/JSON.

Esta definição estabelece tecnologia de transporte e representação. Não define endpoints, métodos, cabeçalhos, códigos de estado, autenticação, endereço de rede, implantação física ou contratos adicionais aos campos e resultados já documentados.

## 7. Justificativas arquiteturais

### 7.1 Python com PySide6 na Apresentação

- Permite materializar CT-01 e CT-02 dentro da CA-01.
- Mantém a apresentação separada da coordenação oficial exercida pelo n8n.
- Não transfere validações ou manutenção do estado oficial para a interface.

### 7.2 Python no Domínio

- Permite materializar CT-09 e CT-10 separadamente da apresentação e do Registro Oficial.
- Mantém as regras subordinadas ao corpus documental, sem delegá-las ao n8n ou ao armazenamento.
- Preserva o limite de responsabilidade da CA-03.

### 7.3 SQLite no Registro Oficial

- Materializa a necessidade de armazenamento confirmável identificada pela WF-FT-01-REV.
- Permite manter as entidades e relações documentadas sem alterar o modelo conceitual ou lógico.
- O acesso encapsulado impede acesso direto da Apresentação e preserva CA-04 como responsável pelo estado oficial.

### 7.4 HTTP com JSON na integração

- Permite a comunicação tecnológica entre o n8n e as camadas materializadas sem fundir suas responsabilidades.
- Fornece transporte e representação comuns para solicitações e resultados do WF-FT-01.
- Mantém o n8n como coordenador e não como executor do Domínio ou proprietário do Registro Oficial.

## 8. Compatibilidade com o n8n

As tecnologias oficializadas são arquiteturalmente compatíveis com o papel aprovado para o n8n porque:

- CA-01, CA-03 e CA-04 expõem suas interações pelo mecanismo HTTP/JSON;
- o n8n permanece em CA-02 e coordena a sequência do WF-FT-01;
- o processamento das regras continua em CA-03;
- o estado oficial continua em CA-04;
- a interação visual continua em CA-01;
- nenhuma camada acessa outra por relação proibida na ET-AR-001.

A compatibilidade registrada é arquitetural. Nenhum endpoint, nó n8n, credencial ou configuração foi criado ou validado nesta atividade.

## 9. Verificação dos impedimentos da WF-FT-01-REV

| Impedimento identificado | Decisão desta atividade | Situação |
|---|---|---|
| Tecnologia da CA-01 não determinada | Python com PySide6 | Resolvido documentalmente. |
| Tecnologia da CA-03 não determinada | Python | Resolvido documentalmente. |
| Tecnologia da CA-04 não determinada | SQLite, acessado por componente de registro em Python | Resolvido documentalmente. |
| Integração CA-01 ↔ CA-02 não determinada | HTTP/JSON | Resolvido documentalmente. |
| Integração CA-02 ↔ CA-03 não determinada | HTTP/JSON | Resolvido documentalmente. |
| Integração CA-02 ↔ CA-04 não determinada | HTTP/JSON | Resolvido documentalmente. |
| Formato, transporte e serialização de entrada e saída não determinados | HTTP para transporte e JSON para representação | Resolvido documentalmente no nível tecnológico. |
| Mecanismo de armazenamento não determinado | SQLite encapsulado por CA-04 | Resolvido documentalmente. |
| Tratamento técnico de falha de armazenamento | Não pertence às decisões tecnológicas autorizadas nesta atividade | Permanece não determinado. |
| Tratamento técnico de indisponibilidade posterior dos dados | Não pertence às decisões tecnológicas autorizadas nesta atividade | Permanece não determinado. |
| Tratamento técnico de falha da confirmação visual | Não pertence às decisões tecnológicas autorizadas nesta atividade | Permanece não determinado. |

## 10. Impedimentos remanescentes

Permanecem fora da complementação tecnológica autorizada:

- comportamento técnico diante de falha de armazenamento;
- comportamento técnico diante de indisponibilidade posterior dos dados;
- comportamento técnico diante de falha da confirmação visual.

Essas ausências foram identificadas na WF-FT-01-REV como comportamentos de exceção não determinados. Não são tecnologias e não podem ser resolvidas nesta atividade sem ampliar seu escopo.

Também permanecem fora do escopo desta atividade:

- tecnologia da CA-05 — Limite com o Ambiente de Utilização, que não participa do WF-FT-01;
- versões específicas das tecnologias;
- infraestrutura física;
- endpoints, autenticação e detalhes de configuração;
- estrutura física do banco de dados.

## 11. Restrições tecnológicas

- O n8n permanece exclusivamente responsável pela Coordenação e Orquestração.
- Python com PySide6 permanece exclusivamente na Apresentação.
- Python na CA-03 não incorpora coordenação, apresentação ou persistência oficial.
- SQLite não executa regras de domínio e somente pode ser acessado por CA-04.
- HTTP/JSON não altera campos, validações, entidades, relações ou resultados documentados.
- Nenhuma tabela, coluna, chave, índice, endpoint, nó ou infraestrutura é definida.
- Nenhuma decisão desta atividade altera a Engenharia de Produto ou os artefatos técnicos anteriores.

## 12. Resultado da complementação

As ausências estritamente tecnológicas necessárias ao WF-FT-01 foram eliminadas. A implementação integral ainda não está autorizada porque permanecem três comportamentos técnicos de exceção não definidos, já registrados pela WF-FT-01-REV e não abrangidos pelo escopo tecnológico desta atividade.

## 13. Declaração de conformidade metodológica

A ET-AR-003 complementa exclusivamente a Arquitetura Tecnológica. Foram oficializados Python com PySide6 para CA-01, n8n para CA-02, Python para CA-03, SQLite com acesso encapsulado em Python para CA-04 e HTTP/JSON para integração. Nenhuma camada, componente, entidade, relacionamento, fluxo ou decisão da Engenharia de Produto foi alterado. Nenhum código, workflow, banco físico, API, infraestrutura ou implementação foi criado, e nenhuma atividade posterior foi iniciada.
