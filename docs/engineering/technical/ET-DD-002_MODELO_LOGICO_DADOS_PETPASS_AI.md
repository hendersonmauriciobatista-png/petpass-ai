# ET-DD-002 — MODELO LÓGICO DE DADOS DO PETPASS AI

## 1. Identificação

- Atividade: ET-DD-002.
- Projeto: CASE-03 — PetPass AI.
- Disciplina: Engenharia Técnica — Modelo Lógico de Dados.
- Escopo: relacionamentos, cardinalidades, dependências, agrupamentos e invariantes lógicas entre ED-01 e ED-08.
- Estruturas físicas, tecnologias e persistência: não definidas.

## 2. Fontes documentais

- `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `DP-PP-001_CAMPOS_CADASTRO_PET.md` a `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md`.

## 3. Convenções lógicas

- `1` indica uma ocorrência conceitualmente exigida pela relação documentada.
- `0..1` indica ocorrência opcional e singular expressamente sustentada.
- `NÃO DETERMINADA` registra ausência de evidência suficiente para estabelecer quantidade mínima ou máxima.
- Cardinalidade não determinada não é completada por convenção técnica.
- As relações descrevem o domínio, não mecanismos físicos de associação.

## 4. Entidades segundo seu papel lógico

### 4.1 Identificação e Cadastro Oficial

- ED-01 — Pet.
- ED-02 — Cadastro Oficial do Pet.
- ED-03 — Tutor.
- ED-04 — Contato de Emergência.
- ED-05 — Fotografia do Pet.

### 4.2 Identidade Digital

- ED-06 — Key Pass.
- ED-07 — QR Code.

### 4.3 Representação Institucional

- ED-08 — Ficha de Emergência.

## 5. Relações lógicas e cardinalidades

### RL-01 — Cadastro Oficial registra Pet

- **Origem:** ED-02 — Cadastro Oficial do Pet.
- **Destino:** ED-01 — Pet.
- **Relacionamento lógico:** registra o respectivo pet.
- **Cardinalidade conceitual:** cada Cadastro Oficial refere-se a `1` Pet; a quantidade de Cadastros Oficiais admissível para um mesmo Pet é **NÃO DETERMINADA** pelo corpus.
- **Dependência lógica:** ED-02 depende da identificação de ED-01 para representar o cadastro do respectivo animal.
- **Agrupamento ou composição:** ED-01 integra o agrupamento lógico Cadastro Oficial; nenhuma composição física é definida.
- **Restrições:** somente os campos autorizados em DP-PP-001 pertencem ao Cadastro do Pet; as obrigatoriedades e validações permanecem as de DP-PP-002 e DP-PP-003.
- **Invariantes:** um cadastro inválido não pode ser concluído; o pet do cadastro é o sujeito da identidade e da ficha.

### RL-02 — Cadastro Oficial associa Tutor

- **Origem:** ED-02 — Cadastro Oficial do Pet.
- **Destino:** ED-03 — Tutor.
- **Relacionamento lógico:** associa os dados oficiais do tutor ao pet cadastrado.
- **Cardinalidade conceitual:** **NÃO DETERMINADA** em ambos os sentidos; o corpus determina associação, mas não quantidade mínima ou máxima.
- **Dependência lógica:** ED-03 depende da associação com ED-02 para fornecer dados à Ficha de Emergência.
- **Agrupamento ou composição:** associação integrante do agrupamento Cadastro Oficial; composição não documentada.
- **Restrições:** os dados do Tutor apresentados devem vir exclusivamente do cadastro associado ao pet.
- **Invariantes:** a consistência entre o dado associado e sua apresentação deve ser preservada.

### RL-03 — Cadastro Oficial associa Contato de Emergência

- **Origem:** ED-02 — Cadastro Oficial do Pet.
- **Destino:** ED-04 — Contato de Emergência.
- **Relacionamento lógico:** associa o contato oficial ao respectivo pet.
- **Cardinalidade conceitual:** **NÃO DETERMINADA** em ambos os sentidos; a existência da associação é documentada, mas sua quantidade não.
- **Dependência lógica:** ED-04 depende de ED-02 para constituir o contato oficial apresentado.
- **Agrupamento ou composição:** associação integrante do agrupamento Cadastro Oficial; composição não documentada.
- **Restrições:** somente o contato cadastrado para o respectivo pet pode ser apresentado e acionado.
- **Invariantes:** o acionamento não pode alterar o número oficial nem transformar o produto em mecanismo próprio de comunicação.

### RL-04 — Cadastro Oficial vincula Fotografia do Pet

- **Origem:** ED-02 — Cadastro Oficial do Pet.
- **Destino:** ED-05 — Fotografia do Pet.
- **Relacionamento lógico:** vincula a fotografia original selecionada ao cadastro do respectivo pet.
- **Cardinalidade conceitual:** um Cadastro Oficial possui `0..1` Fotografia do Pet, pois Foto é campo opcional e singular; cada Fotografia cadastrada permanece vinculada ao respectivo cadastro.
- **Dependência lógica:** ED-05 depende de ED-02 para possuir vínculo oficial e integrar a ficha.
- **Agrupamento ou composição:** vínculo permanente no agrupamento Cadastro Oficial; nenhuma estrutura física é definida.
- **Restrições:** fotografia cadastrada não pode ser substituída por imagem ilustrativa ou genérica; ausência de fotografia produz estado de apresentação com placeholder institucional.
- **Invariantes:** proporção original preservada; distorção vedada; finalidade exclusivamente identificadora.

### RL-05 — Cadastro Oficial recebe Key Pass

- **Origem:** ED-02 — Cadastro Oficial do Pet.
- **Destino:** ED-06 — Key Pass.
- **Relacionamento lógico:** associa a identidade digital após conclusão válida do cadastro.
- **Cardinalidade conceitual:** antes da conclusão válida, `0` Key Pass; após a conclusão válida, `1` Key Pass para o animal cadastrado.
- **Dependência lógica:** ED-06 depende da conclusão válida de ED-02.
- **Agrupamento ou composição:** associação de identidade no agrupamento Cadastro Oficial; o corpus não define composição física.
- **Restrições:** cadastro inválido não recebe Key Pass; alterações cadastrais posteriores não modificam a identidade.
- **Invariantes:** Key Pass única, estável, exclusiva do ecossistema PetPass AI e coexistente com outros identificadores.

### RL-06 — Key Pass possui representação QR Code

- **Origem:** ED-06 — Key Pass.
- **Destino:** ED-07 — QR Code.
- **Relacionamento lógico:** é representada graficamente pelo QR Code correspondente.
- **Cardinalidade conceitual:** `1:1`; cada Key Pass possui exclusivamente um QR Code correspondente e cada QR Code representa a Key Pass do respectivo pet.
- **Dependência lógica:** ED-07 depende integralmente de ED-06 e não constitui identificador independente.
- **Agrupamento ou composição:** composição lógica da Identidade Digital: ED-06 constitui a identidade e ED-07 sua representação dependente. Nenhuma composição física é definida.
- **Restrições:** QR Code pode ser regenerado, mas deve preservar a mesma Key Pass; indisponibilidade visual utiliza placeholder institucional.
- **Invariantes:** regeneração ou substituição do QR Code não altera a identidade digital.

### RL-07 — Ficha de Emergência representa Cadastro Oficial

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-02 — Cadastro Oficial do Pet.
- **Relacionamento lógico:** representa documentalmente as informações oficiais do cadastro.
- **Cardinalidade conceitual:** cada Ficha de Emergência apresentada possui `1` Cadastro Oficial como origem; a quantidade de apresentações ou representações possíveis para um Cadastro Oficial é **NÃO DETERMINADA**.
- **Dependência lógica:** ED-08 depende de ED-02 como fonte primária.
- **Agrupamento ou composição:** projeção institucional do agrupamento Cadastro Oficial; ED-08 não compõe nem possui as entidades de origem.
- **Restrições:** nenhuma informação da ficha pode possuir origem externa ao cadastro oficial; a ficha não pode tornar-se fonte primária.
- **Invariantes:** consistência entre cadastro e ficha preservada; composição visual institucional mantida.

### RL-08 — Ficha de Emergência apresenta Pet

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-01 — Pet.
- **Relacionamento lógico:** apresenta a identificação do pet pertencente ao cadastro representado.
- **Cardinalidade conceitual:** cada Ficha de Emergência apresenta `1` Pet; a quantidade de fichas apresentáveis para um Pet é **NÃO DETERMINADA**.
- **Dependência lógica:** depende de RL-07 e RL-01; a ficha obtém o pet por meio do cadastro oficial.
- **Agrupamento ou composição:** relação de projeção; sem posse ou composição.
- **Restrições:** somente os dados oficiais autorizados podem ser apresentados.
- **Invariantes:** identificação do pet constitui a informação principal do documento.

### RL-09 — Ficha de Emergência apresenta Tutor

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-03 — Tutor.
- **Relacionamento lógico:** apresenta os dados oficiais do tutor associados ao pet.
- **Cardinalidade conceitual:** **NÃO DETERMINADA**; o corpus exige a origem oficial e a área Tutor, mas não determina quantidades.
- **Dependência lógica:** depende de RL-07 e RL-02.
- **Agrupamento ou composição:** relação de projeção; sem posse ou composição.
- **Restrições:** os dados devem permanecer contidos na área aprovada e vir exclusivamente do cadastro associado.
- **Invariantes:** dados de contato do tutor possuem prioridade operacional após a identificação do pet.

### RL-10 — Ficha de Emergência apresenta Contato de Emergência

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-04 — Contato de Emergência.
- **Relacionamento lógico:** apresenta o contato oficial e permite seu acionamento.
- **Cardinalidade conceitual:** **NÃO DETERMINADA**; nenhuma quantidade mínima ou máxima de contatos foi estabelecida.
- **Dependência lógica:** depende de RL-07 e RL-03.
- **Agrupamento ou composição:** relação de projeção; sem posse ou composição.
- **Restrições:** o acionamento utiliza exclusivamente o número apresentado e os recursos disponíveis no ambiente.
- **Invariantes:** a ficha não define, controla ou interfere no mecanismo tecnológico de comunicação.

### RL-11 — Ficha de Emergência apresenta Fotografia do Pet

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-05 — Fotografia do Pet.
- **Relacionamento lógico:** apresenta a fotografia vinculada ao cadastro ou o estado institucional de ausência.
- **Cardinalidade conceitual:** `0..1` Fotografia apresentada por ficha; quando não houver fotografia cadastrada, nenhuma ED-05 é projetada e aplica-se o placeholder de apresentação.
- **Dependência lógica:** depende de RL-07 e RL-04.
- **Agrupamento ou composição:** relação de projeção; placeholder não constitui entidade do modelo.
- **Restrições:** fotografia somente na área do Modelo 4; imagem cadastrada não pode ser substituída por imagem genérica.
- **Invariantes:** proporção preservada, sem distorção, e finalidade identificadora.

### RL-12 — Ficha de Emergência apresenta Key Pass

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-06 — Key Pass.
- **Relacionamento lógico:** apresenta a identidade digital estável do pet cadastrado.
- **Cardinalidade conceitual:** para cadastro validamente concluído, `1` Key Pass por ficha; antes da conclusão válida, a Key Pass não existe.
- **Dependência lógica:** depende de RL-07 e RL-05.
- **Agrupamento ou composição:** relação de projeção; ED-08 não possui ou altera ED-06.
- **Restrições:** apresentação somente na área oficial; a ficha não modifica a Key Pass.
- **Invariantes:** valor estável e exclusivo do PetPass AI.

### RL-13 — Ficha de Emergência apresenta QR Code

- **Origem:** ED-08 — Ficha de Emergência.
- **Destino:** ED-07 — QR Code.
- **Relacionamento lógico:** apresenta a representação institucional da Key Pass.
- **Cardinalidade conceitual:** `1` QR Code correspondente à Key Pass; sua impossibilidade de apresentação não elimina a relação lógica e produz exclusivamente o placeholder institucional aprovado.
- **Dependência lógica:** depende de RL-06, RL-07 e RL-12.
- **Agrupamento ou composição:** relação de projeção da composição lógica de Identidade Digital.
- **Restrições:** apresentação na área oficial; legibilidade preservada; QR Code não substitui a Key Pass.
- **Invariantes:** corresponde à mesma Key Pass mesmo após regeneração ou substituição.

## 6. Perspectiva lógica por entidade

### ED-01 — Pet

- **Relacionamentos lógicos:** RL-01 e RL-08; participa indiretamente de RL-04 e RL-05 como sujeito do cadastro.
- **Cardinalidades conceituais:** `1` Pet por Cadastro Oficial; `1` Pet apresentado por Ficha; quantidade inversa de cadastros ou fichas **NÃO DETERMINADA**.
- **Dependências lógicas:** regras do Cadastro do Pet e existência de ED-02 para identidade oficial.
- **Agregações ou composições:** integra o agrupamento Cadastro Oficial; nenhuma composição física.
- **Restrições de relacionamento:** somente dados autorizados; associações a Tutor, Contato, Fotografia e Key Pass mediadas pelo cadastro.
- **Invariantes lógicas:** campos, obrigatoriedade e validações preservados.

### ED-02 — Cadastro Oficial do Pet

- **Relacionamentos lógicos:** RL-01 a RL-05 e RL-07.
- **Cardinalidades conceituais:** `1` Pet; `0..1` Fotografia; `0` Key Pass antes da conclusão válida e `1` depois; Tutor e Contato com cardinalidade **NÃO DETERMINADA**; quantidade inversa de Fichas **NÃO DETERMINADA**.
- **Dependências lógicas:** resultado válido do domínio.
- **Agregações ou composições:** centro do agrupamento lógico Cadastro Oficial.
- **Restrições de relacionamento:** somente cadastro válido pode ser confirmado e receber identidade.
- **Invariantes lógicas:** origem primária e disponibilidade das informações oficiais.

### ED-03 — Tutor

- **Relacionamentos lógicos:** RL-02 e RL-09.
- **Cardinalidades conceituais:** **NÃO DETERMINADAS**.
- **Dependências lógicas:** associação ao cadastro do pet.
- **Agregações ou composições:** integrante associado do agrupamento Cadastro Oficial; sem composição documentada.
- **Restrições de relacionamento:** dados apresentados somente a partir da associação oficial.
- **Invariantes lógicas:** consistência com o cadastro.

### ED-04 — Contato de Emergência

- **Relacionamentos lógicos:** RL-03 e RL-10.
- **Cardinalidades conceituais:** **NÃO DETERMINADAS**.
- **Dependências lógicas:** associação oficial ao cadastro e apresentação na ficha para acionamento.
- **Agregações ou composições:** integrante associado do agrupamento Cadastro Oficial; sem composição documentada.
- **Restrições de relacionamento:** acionamento limita-se ao número oficial apresentado.
- **Invariantes lógicas:** origem oficial e neutralidade tecnológica da comunicação.

### ED-05 — Fotografia do Pet

- **Relacionamentos lógicos:** RL-04 e RL-11.
- **Cardinalidades conceituais:** `0..1` por Cadastro Oficial e `0..1` por Ficha.
- **Dependências lógicas:** vínculo ao cadastro oficial.
- **Agregações ou composições:** vínculo permanente no agrupamento Cadastro Oficial; projeção na ficha.
- **Restrições de relacionamento:** ausência não cria fotografia substituta; placeholder permanece estado visual.
- **Invariantes lógicas:** originalidade, proporção, ausência de distorção e finalidade identificadora.

### ED-06 — Key Pass

- **Relacionamentos lógicos:** RL-05, RL-06 e RL-12.
- **Cardinalidades conceituais:** `0` antes e `1` após cadastro válido; relação `1:1` com QR Code; `1` por Ficha de cadastro concluído.
- **Dependências lógicas:** conclusão válida do cadastro.
- **Agregações ou composições:** elemento principal do agrupamento Identidade Digital.
- **Restrições de relacionamento:** não substitui outros identificadores e não é modificada por alterações cadastrais.
- **Invariantes lógicas:** unicidade, estabilidade e finalidade exclusiva no PetPass AI.

### ED-07 — QR Code

- **Relacionamentos lógicos:** RL-06 e RL-13.
- **Cardinalidades conceituais:** `1:1` com Key Pass; `1` correspondente na ficha, sujeito a estado visual de indisponibilidade.
- **Dependências lógicas:** existência da Key Pass.
- **Agregações ou composições:** representação dependente na composição lógica Identidade Digital.
- **Restrições de relacionamento:** não constitui identidade independente.
- **Invariantes lógicas:** regeneração e substituição preservam a Key Pass.

### ED-08 — Ficha de Emergência

- **Relacionamentos lógicos:** RL-07 a RL-13.
- **Cardinalidades conceituais:** `1` Cadastro e `1` Pet por ficha; `0..1` Fotografia; `1` Key Pass e `1` QR Code para cadastro concluído; Tutor e Contato com quantidades **NÃO DETERMINADAS**.
- **Dependências lógicas:** todas as informações decorrem do cadastro oficial.
- **Agregações ou composições:** projeção institucional; não agrega por posse nem compõe as entidades de origem.
- **Restrições de relacionamento:** não cria, altera ou substitui dados oficiais; preserva composição e hierarquia.
- **Invariantes lógicas:** representação documental, nunca origem primária.

## 7. Agrupamentos lógicos

### AL-01 — Cadastro Oficial

- **Entidade central:** ED-02 — Cadastro Oficial do Pet.
- **Participantes:** ED-01, ED-03, ED-04, ED-05 e ED-06.
- **Justificativa documental:** ET-DD-001 registra o cadastro como origem primária e como associação conceitual do pet com dados relacionados, fotografia e identidade digital.
- **Limite:** o agrupamento não define posse física, ciclo técnico de persistência ou cardinalidades não documentadas.

### AL-02 — Identidade Digital

- **Entidade principal:** ED-06 — Key Pass.
- **Representação dependente:** ED-07 — QR Code.
- **Justificativa documental:** o QR Code representa a Key Pass, não constitui identificador independente e preserva a mesma identidade quando regenerado.
- **Limite:** não define conteúdo, padrão, geração, armazenamento ou leitura do QR Code.

### AL-03 — Representação Institucional

- **Entidade de representação:** ED-08 — Ficha de Emergência.
- **Entidades projetadas:** ED-01, ED-03, ED-04, ED-05, ED-06 e ED-07, sempre por meio da origem ED-02.
- **Justificativa documental:** a ficha representa exclusivamente dados oficiais cadastrados.
- **Limite:** projeção não constitui posse, composição ou nova origem de dados.

## 8. Dependências lógicas consolidadas

1. ED-02 depende de cadastro válido para assumir estado concluído.
2. ED-06 depende da conclusão válida de ED-02.
3. ED-07 depende integralmente de ED-06.
4. ED-03, ED-04 e ED-05 dependem de associação a ED-02 para integrarem ED-08.
5. ED-08 depende de ED-02 como origem e de ED-06/ED-07 para apresentar identidade digital.
6. O acionamento associado a ED-04 depende de sua apresentação em ED-08 e permanece fora do mecanismo próprio de dados.

## 9. Limites de responsabilidade do modelo lógico

- ED-01 representa o pet, mas não mantém associações oficiais por conta própria.
- ED-02 mantém o agrupamento oficial, mas não apresenta a ficha.
- ED-03, ED-04 e ED-05 não definem sua própria origem fora do cadastro.
- ED-06 constitui identidade; ED-07 apenas a representa.
- ED-08 apresenta informações, mas não as origina nem altera.
- Placeholders permanecem estados de apresentação, não entidades ou substitutos dos dados ausentes.
- Nenhuma relação lógica define mecanismo físico de armazenamento ou integração.

## 10. Consolidação quantitativa

| Categoria | Quantidade |
|---|---:|
| Entidades conceituais preservadas | 8 |
| Relacionamentos lógicos identificados | 13 |
| Agrupamentos lógicos | 3 |

## 11. Limites técnicos preservados

- Não são definidas tabelas, colunas, tipos de dados, chaves, índices ou estruturas físicas.
- Não são definidos banco de dados, ORM, tecnologia ou mecanismo de persistência.
- Não são definidas cardinalidades para Tutor ou Contato de Emergência sem evidência documental.
- Não são definidos formato ou algoritmo da Key Pass nem parâmetros técnicos do QR Code.
- Não é definida implementação.

## 12. Declaração de conformidade metodológica

Este documento estabelece exclusivamente relações lógicas entre as entidades da ET-DD-001. Nenhuma tabela, coluna, tipo de dado, chave, índice, banco de dados, ORM, tecnologia de persistência ou implementação foi definida. Nenhum artefato existente foi modificado e nenhuma atividade posterior foi iniciada.
