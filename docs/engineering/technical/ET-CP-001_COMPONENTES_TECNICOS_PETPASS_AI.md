# ET-CP-001 — COMPONENTES TÉCNICOS DO PETPASS AI

## 1. Identificação

- Atividade: ET-CP-001.
- Projeto: CASE-03 — PetPass AI.
- Disciplina: Engenharia Técnica — Componentes Conceituais.
- Escopo: identificação, classificação e organização dos componentes nas camadas da ET-AR-001.
- Implementação e tecnologias: não definidas.

## 2. Fontes documentais

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `DP-PP-001_CAMPOS_CADASTRO_PET.md` a `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md`.
- `GP-PP-21_AUDITORIA_ENCERRAMENTO_FASE_DELIBERACOES_CASE03.md`.

## 3. Critérios de decomposição

- Cada componente materializa uma responsabilidade delimitada em sua camada de origem.
- Componentes de apresentação não aplicam regras de domínio nem acessam diretamente o registro oficial.
- Componentes de coordenação ordenam interações, mas não definem regras ou estado oficial.
- Componentes de domínio aplicam decisões normativas, mas não apresentam conteúdo nem mantêm estado físico.
- Componentes de registro mantêm conceitualmente o estado oficial sem definir mecanismo de armazenamento.
- O componente de limite ambiental apenas entrega a intenção de contato aos recursos externos disponíveis.
- As pendências técnicas e de medição registradas na GP-PP-21 não são preenchidas nesta decomposição.

## 4. CA-01 — Apresentação e Interação Institucional

### CT-01 — Apresentação do Cadastro do Pet

- **Camada:** CA-01 — Apresentação e Interação Institucional.
- **Objetivo:** apresentar e coletar exclusivamente os campos autorizados do Cadastro do Pet.
- **Responsabilidades:** apresentar Nome do Pet, Espécie, Raça, Sexo, Idade, Peso, Cor e Foto; distinguir os campos obrigatórios dos opcionais; preservar os valores informados durante a interação.
- **Entradas:** ações do usuário; campos e classificações normativas; resultados encaminhados pela coordenação.
- **Saídas:** solicitação de cadastro com os dados informados; estado visual preservado do preenchimento.
- **Dependências arquiteturais:** CA-02; DP-PP-001 e DP-PP-002.
- **Componentes com os quais poderá interagir:** CT-02 — Apresentação de Retorno do Cadastro; CT-05 — Coordenação do Cadastro do Pet.

### CT-02 — Apresentação de Retorno do Cadastro

- **Camada:** CA-01 — Apresentação e Interação Institucional.
- **Objetivo:** apresentar os resultados de falha ou sucesso recebidos da coordenação.
- **Responsabilidades:** destacar os campos obrigatórios com erro; apresentar motivo objetivo do bloqueio; preservar os dados preenchidos; apresentar confirmação visual de conclusão válida.
- **Entradas:** resultado de validação; campos inválidos; motivo do bloqueio; confirmação de registro.
- **Saídas:** indicação visual de erro; mensagem objetiva; confirmação visual de sucesso.
- **Dependências arquiteturais:** CA-02; DP-PP-004 e DP-PP-005.
- **Componentes com os quais poderá interagir:** CT-01 — Apresentação do Cadastro do Pet; CT-05 — Coordenação do Cadastro do Pet.

### CT-03 — Apresentação Institucional da Ficha de Emergência

- **Camada:** CA-01 — Apresentação e Interação Institucional.
- **Objetivo:** apresentar a representação documental oficial da Ficha de Emergência.
- **Responsabilidades:** preservar o Modelo 4, o cabeçalho, a identidade visual, a composição fixa e a hierarquia; apresentar os dados oficiais do pet, tutor e emergência; apresentar fotografia ou placeholder; apresentar Key Pass e QR Code nas áreas aprovadas.
- **Entradas:** conjunto oficial preparado pela coordenação; fotografia ou estado de ausência; Key Pass; QR Code ou estado de indisponibilidade.
- **Saídas:** Ficha de Emergência apresentada segundo as decisões institucionais.
- **Dependências arquiteturais:** CA-02; DP-PP-008 a DP-PP-014.
- **Componentes com os quais poderá interagir:** CT-07 — Coordenação da Ficha de Emergência; CT-04 — Acionador Visual do Contato de Emergência.

### CT-04 — Acionador Visual do Contato de Emergência

- **Camada:** CA-01 — Apresentação e Interação Institucional.
- **Objetivo:** receber a ação do usuário sobre o telefone oficialmente apresentado.
- **Responsabilidades:** disponibilizar o acionamento associado ao número apresentado; encaminhar exclusivamente a intenção do usuário à coordenação; não realizar comunicação própria.
- **Entradas:** ação do usuário; telefone de emergência apresentado na ficha.
- **Saídas:** solicitação de acionamento do contato oficial.
- **Dependências arquiteturais:** CA-02; DP-PP-012, DP-PP-013 e DP-PP-015.
- **Componentes com os quais poderá interagir:** CT-03 — Apresentação Institucional da Ficha de Emergência; CT-08 — Coordenação do Contato de Emergência.

## 5. CA-02 — Coordenação de Aplicação

### CT-05 — Coordenação do Cadastro do Pet

- **Camada:** CA-02 — Coordenação de Aplicação.
- **Objetivo:** coordenar o fluxo entre entrada do cadastro, aplicação das regras e manutenção do registro oficial.
- **Responsabilidades:** receber a solicitação de cadastro; solicitar validação; impedir a continuidade diante de falha; solicitar registro após resultado válido; devolver falha ou confirmação à apresentação.
- **Entradas:** solicitação e dados do cadastro; resultados das regras; confirmação conceitual de registro.
- **Saídas:** solicitação de validação; solicitação de registro; resultado destinado à apresentação; sinal de conclusão válida para coordenação da identidade digital.
- **Dependências arquiteturais:** CA-01, CA-03 e CA-04.
- **Componentes com os quais poderá interagir:** CT-01, CT-02, CT-09, CT-10, CT-13 e CT-06.

### CT-06 — Coordenação da Identidade Digital

- **Camada:** CA-02 — Coordenação de Aplicação.
- **Objetivo:** coordenar a associação da identidade digital após a conclusão válida do cadastro.
- **Responsabilidades:** receber a confirmação de conclusão válida; solicitar ao domínio a identidade conceitualmente válida; solicitar sua manutenção no registro oficial; disponibilizar Key Pass e sua relação com o QR Code para os fluxos autorizados.
- **Entradas:** confirmação de cadastro válido; regras de identidade; estado oficial da identidade digital.
- **Saídas:** solicitação de associação da identidade; identidade digital destinada ao registro ou à Ficha de Emergência.
- **Dependências arquiteturais:** CA-03 e CA-04; DP-PP-006, DP-PP-007 e DP-PP-014.
- **Componentes com os quais poderá interagir:** CT-05, CT-11 e CT-16.

### CT-07 — Coordenação da Ficha de Emergência

- **Camada:** CA-02 — Coordenação de Aplicação.
- **Objetivo:** reunir exclusivamente informações oficiais e encaminhá-las à apresentação como representação documental.
- **Responsabilidades:** receber a solicitação da ficha; consultar os registros oficiais necessários; solicitar verificação de consistência; organizar o conjunto destinado à apresentação sem criar dados; preservar estados aprovados de fotografia e QR Code indisponíveis.
- **Entradas:** solicitação da ficha; informações oficiais; regras de consistência; estados de fotografia e QR Code.
- **Saídas:** conjunto oficial destinado ao CT-03; solicitação de consulta aos componentes de registro.
- **Dependências arquiteturais:** CA-01, CA-03 e CA-04; DP-PP-011 a DP-PP-014.
- **Componentes com os quais poderá interagir:** CT-03, CT-12, CT-13, CT-14, CT-15 e CT-16.

### CT-08 — Coordenação do Contato de Emergência

- **Camada:** CA-02 — Coordenação de Aplicação.
- **Objetivo:** encaminhar a intenção de contato ao limite ambiental usando o número oficial apresentado.
- **Responsabilidades:** receber a solicitação de acionamento; preservar o número oficial; encaminhar a ação ao componente de limite ambiental; não definir ou executar comunicação própria.
- **Entradas:** intenção de contato; número de emergência oficial.
- **Saídas:** solicitação conceitual de entrega da ação ao ambiente.
- **Dependências arquiteturais:** CA-01, CA-04 e CA-05; DP-PP-013 e DP-PP-015.
- **Componentes com os quais poderá interagir:** CT-04, CT-14 e CT-17.

## 6. CA-03 — Domínio e Regras do PetPass AI

### CT-09 — Avaliador das Regras do Cadastro

- **Camada:** CA-03 — Domínio e Regras do PetPass AI.
- **Objetivo:** aplicar exclusivamente os campos, obrigatoriedades, valores permitidos e validações aprovadas.
- **Responsabilidades:** reconhecer somente os campos autorizados; validar Nome do Pet, Espécie e Raça; aplicar as regras autorizadas aos campos opcionais; rejeitar validação não prevista.
- **Entradas:** dados submetidos pelo cadastro.
- **Saídas:** resultado de validação; identificação dos campos inválidos; motivos objetivos de violação.
- **Dependências arquiteturais:** DP-PP-001, DP-PP-002 e DP-PP-003.
- **Componentes com os quais poderá interagir:** CT-05 e CT-10.

### CT-10 — Determinador do Resultado do Cadastro

- **Camada:** CA-03 — Domínio e Regras do PetPass AI.
- **Objetivo:** determinar bloqueio ou conclusão do cadastro segundo as decisões normativas.
- **Responsabilidades:** impedir conclusão quando houver violação; preservar a exigência de não limpeza dos dados; autorizar conclusão somente quando as validações forem satisfeitas e o registro puder ser confirmado.
- **Entradas:** resultado do CT-09; confirmação conceitual do registro oficial.
- **Saídas:** bloqueio com motivos; autorização de conclusão; resultado de sucesso.
- **Dependências arquiteturais:** DP-PP-004 e DP-PP-005.
- **Componentes com os quais poderá interagir:** CT-09, CT-05 e CT-13.

### CT-11 — Guardião das Regras da Identidade Digital

- **Camada:** CA-03 — Domínio e Regras do PetPass AI.
- **Objetivo:** preservar as invariantes normativas da Key Pass e de sua representação QR Code.
- **Responsabilidades:** reconhecer a Key Pass como identificador único e estável; permitir sua associação somente após cadastro válido; impedir alteração por mudança cadastral; preservar que QR Code representa a Key Pass, não a substitui e mantém a mesma identidade quando regenerado.
- **Entradas:** confirmação de cadastro válido; identidade digital associada; solicitação de verificação das invariantes.
- **Saídas:** identidade conceitualmente válida; confirmação ou violação das invariantes.
- **Dependências arquiteturais:** DP-PP-006, DP-PP-007 e DP-PP-014.
- **Componentes com os quais poderá interagir:** CT-06 e CT-16.

### CT-12 — Guardião da Consistência Documental

- **Camada:** CA-03 — Domínio e Regras do PetPass AI.
- **Objetivo:** preservar a correspondência entre cadastro oficial e Ficha de Emergência.
- **Responsabilidades:** assegurar que a ficha utilize somente dados do cadastro oficial; preservar a finalidade identificadora da fotografia; preservar a hierarquia e os limites conceituais da apresentação; impedir que a ficha seja tratada como fonte primária.
- **Entradas:** conjunto oficial destinado à ficha; regras de origem; estado da fotografia e identidade digital.
- **Saídas:** confirmação de consistência ou indicação objetiva de divergência conceitual.
- **Dependências arquiteturais:** DP-PP-011, DP-PP-012, DP-PP-013 e DP-PP-014.
- **Componentes com os quais poderá interagir:** CT-07, CT-13, CT-14, CT-15 e CT-16.

## 7. CA-04 — Registro Oficial de Informações

### CT-13 — Registro Oficial do Pet

- **Camada:** CA-04 — Registro Oficial de Informações.
- **Objetivo:** manter conceitualmente o cadastro oficial do pet após conclusão válida.
- **Responsabilidades:** aceitar somente cadastro validado; manter os campos oficiais do pet disponíveis; fornecer as informações de identificação para a Ficha de Emergência; confirmar conceitualmente o registro.
- **Entradas:** cadastro validado; solicitação coordenada de consulta.
- **Saídas:** confirmação de registro; informações oficiais do pet.
- **Dependências arquiteturais:** CA-02 e CA-03; DP-PP-001 a DP-PP-005 e DP-PP-013.
- **Componentes com os quais poderá interagir:** CT-05, CT-10, CT-07 e CT-12.

### CT-14 — Registro de Informações Associadas

- **Camada:** CA-04 — Registro Oficial de Informações.
- **Objetivo:** manter conceitualmente os dados oficiais associados ao pet utilizados nas áreas Tutor e Emergência.
- **Responsabilidades:** preservar a associação dos dados do tutor ao pet; preservar os contatos de emergência cadastrados para o pet; fornecer exclusivamente esses dados aos fluxos coordenados.
- **Entradas:** informações oficiais associadas ao cadastro; solicitações coordenadas de consulta.
- **Saídas:** dados oficiais do tutor; contato de emergência oficial.
- **Dependências arquiteturais:** CA-02 e CA-03; DP-PP-013 e DP-PP-015.
- **Componentes com os quais poderá interagir:** CT-07, CT-08 e CT-12.

### CT-15 — Registro da Fotografia Vinculada

- **Camada:** CA-04 — Registro Oficial de Informações.
- **Objetivo:** manter conceitualmente a vinculação permanente entre a fotografia original e o cadastro do pet.
- **Responsabilidades:** associar a fotografia selecionada ao respectivo cadastro; disponibilizar a fotografia vinculada; indicar a ausência de fotografia sem substituir o estado aprovado por imagem genérica.
- **Entradas:** fotografia original selecionada; identificação do cadastro; solicitação coordenada de consulta.
- **Saídas:** fotografia vinculada ou estado de ausência de fotografia.
- **Dependências arquiteturais:** CA-02 e CA-03; DP-PP-011 e DP-PP-013.
- **Componentes com os quais poderá interagir:** CT-07 e CT-12.

### CT-16 — Registro da Identidade Digital

- **Camada:** CA-04 — Registro Oficial de Informações.
- **Objetivo:** manter conceitualmente a Key Pass estável e sua relação com o QR Code correspondente.
- **Responsabilidades:** associar a identidade digital ao cadastro válido; preservar a Key Pass durante a existência do cadastro; fornecer Key Pass e estado do QR Code aos fluxos coordenados; preservar a relação entre identificador e representação.
- **Entradas:** identidade digital conceitualmente válida; cadastro correspondente; solicitação coordenada de consulta.
- **Saídas:** Key Pass oficial; QR Code correspondente ou estado de indisponibilidade.
- **Dependências arquiteturais:** CA-02 e CA-03; DP-PP-006, DP-PP-007 e DP-PP-014.
- **Componentes com os quais poderá interagir:** CT-06, CT-07, CT-11 e CT-12.

## 8. CA-05 — Limite com o Ambiente de Utilização

### CT-17 — Entrega da Ação de Contato ao Ambiente

- **Camada:** CA-05 — Limite com o Ambiente de Utilização.
- **Objetivo:** entregar a intenção de contato e o número oficial aos recursos disponíveis no ambiente de utilização.
- **Responsabilidades:** receber a ação coordenada; entregar a ação ao ambiente; preservar a neutralidade do produto quanto ao mecanismo de comunicação; não realizar comunicação própria.
- **Entradas:** solicitação de acionamento; número oficial apresentado.
- **Saídas:** entrega conceitual da ação ao ambiente.
- **Dependências arquiteturais:** CA-02; DP-PP-015.
- **Componentes com os quais poderá interagir:** CT-08 — Coordenação do Contato de Emergência.

## 9. Relações consolidadas entre componentes

| Origem | Destino permitido | Finalidade |
|---|---|---|
| CT-01, CT-02 | CT-05 | submissão do cadastro e apresentação de resultados |
| CT-05 | CT-09, CT-10, CT-13 | validação, determinação do resultado e registro oficial |
| CT-05 | CT-06 | sinalizar conclusão válida para identidade digital |
| CT-06 | CT-11, CT-16 | preservar e registrar a identidade digital |
| CT-03 | CT-07 | solicitar e receber a Ficha de Emergência |
| CT-07 | CT-12, CT-13, CT-14, CT-15, CT-16 | obter e verificar informações oficiais da ficha |
| CT-04 | CT-08 | encaminhar acionamento do usuário |
| CT-08 | CT-14, CT-17 | obter número oficial e entregar intenção ao ambiente |

Interações não relacionadas nesta matriz não são autorizadas por este documento.

## 10. Quantidade de componentes por camada

| Camada | Quantidade | Componentes |
|---|---:|---|
| CA-01 — Apresentação e Interação Institucional | 4 | CT-01 a CT-04 |
| CA-02 — Coordenação de Aplicação | 4 | CT-05 a CT-08 |
| CA-03 — Domínio e Regras do PetPass AI | 4 | CT-09 a CT-12 |
| CA-04 — Registro Oficial de Informações | 4 | CT-13 a CT-16 |
| CA-05 — Limite com o Ambiente de Utilização | 1 | CT-17 |
| **Total** | **17** | **CT-01 a CT-17** |

## 11. Limites da decomposição técnica

- Os componentes não representam classes, microsserviços, módulos físicos ou unidades de implantação.
- Não foram definidas interfaces técnicas, APIs, tabelas, bancos de dados ou contratos de comunicação.
- Não foram escolhidas tecnologias, linguagens, frameworks, protocolos ou infraestrutura.
- Não foram definidos mecanismos de persistência, geração da Key Pass, geração do QR Code ou comunicação externa.
- As pendências LD-002, LD-003, LD-005, LD-008, LD-010, LD-013 e LD-015 permanecem inalteradas.
- Nenhuma implementação foi iniciada.

## 12. Declaração de conformidade metodológica

Esta atividade limitou-se a identificar e organizar componentes conceituais nas camadas da ET-AR-001. Nenhuma classe, microsserviço, API, banco de dados, tabela, tecnologia, framework, protocolo, infraestrutura ou detalhe de implementação foi definido. Nenhum artefato existente foi modificado e nenhuma atividade posterior foi iniciada.
