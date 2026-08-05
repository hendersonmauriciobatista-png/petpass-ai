# ET-DD-001 — MODELO CONCEITUAL DE DADOS DO PETPASS AI

## 1. Identificação

- Atividade: ET-DD-001.
- Projeto: CASE-03 — PetPass AI.
- Disciplina: Engenharia Técnica — Modelo Conceitual de Dados.
- Escopo: entidades, responsabilidades, relacionamentos, dependências e invariantes conceituais.
- Estruturas físicas e tecnologias: não definidas.

## 2. Fontes documentais

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `DP-PP-001_CAMPOS_CADASTRO_PET.md` a `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md`.

## 3. Critérios do modelo

- Entidade conceitual representa informação do domínio com responsabilidade própria documentada.
- Processo, validação, mensagem, placeholder e componente visual não são tratados como entidades do domínio.
- Relacionamentos são descritos conceitualmente, sem estrutura física ou mecanismo de associação.
- Quantidades e cardinalidades somente são registradas quando expressamente sustentadas pelas deliberações.
- Ausências técnicas não são preenchidas por inferência.

## 4. Papel: Identificação e Cadastro Oficial

### ED-01 — Pet

- **Nome:** Pet.
- **Objetivo:** representar o animal identificado no ecossistema PetPass AI.
- **Responsabilidades:** reunir exclusivamente as informações autorizadas de identificação do pet: Nome do Pet, Espécie, Raça, Sexo, Idade, Peso, Cor e Foto opcional; constituir o sujeito do cadastro oficial, da identidade digital e da Ficha de Emergência.
- **Relacionamentos:** é o sujeito do Cadastro Oficial do Pet; pode possuir Fotografia do Pet vinculada; recebe identidade por uma Key Pass após conclusão válida do cadastro; tem seus dados representados na Ficha de Emergência; possui dados de Tutor e Contato de Emergência associados por meio do cadastro oficial.
- **Dependências:** existência de cadastro válido para obtenção de identidade digital; regras de campos e validação das DP-PP-001 a DP-PP-005.
- **Componentes técnicos que a utilizam:** CT-01, CT-05, CT-09, CT-10, CT-12 e CT-13.
- **Invariantes documentais:** nenhum campo além dos oito autorizados integra o Cadastro do Pet; Nome do Pet, Espécie e Raça são obrigatórios; Espécie limita-se a Cão ou Gato; as demais validações são exclusivamente as registradas na DP-PP-003.
- **Limites:** não incorpora campos de tutor, contato de emergência, Key Pass ou QR Code como informações próprias do conjunto de campos autorizado.

### ED-02 — Cadastro Oficial do Pet

- **Nome:** Cadastro Oficial do Pet.
- **Objetivo:** representar o registro oficial que reúne e torna disponíveis as informações cadastradas do respectivo pet.
- **Responsabilidades:** preservar o resultado válido do cadastro; servir como origem primária das informações apresentadas na Ficha de Emergência; manter a associação conceitual do pet com dados relacionados, fotografia e identidade digital.
- **Relacionamentos:** registra ED-01 — Pet; associa ED-03 — Tutor, ED-04 — Contato de Emergência, ED-05 — Fotografia do Pet e ED-06 — Key Pass; fornece a origem de ED-08 — Ficha de Emergência.
- **Dependências:** conclusão válida segundo DP-PP-003 a DP-PP-005; coordenação e registro definidos por ET-AR-001 e ET-CP-001.
- **Componentes técnicos que a utilizam:** CT-05, CT-07, CT-10, CT-12, CT-13, CT-14, CT-15 e CT-16.
- **Invariantes documentais:** não pode ser considerado concluído quando houver violação de validação; o registro deve estar confirmado para caracterizar sucesso; os dados devem permanecer disponíveis às funcionalidades subsequentes; constitui origem primária, enquanto a ficha é somente representação documental.
- **Limites:** não define estrutura física, mecanismo de armazenamento, sincronização ou atualização.

### ED-03 — Tutor

- **Nome:** Tutor.
- **Objetivo:** representar conceitualmente os dados oficiais do tutor associados ao pet.
- **Responsabilidades:** permanecer associado ao respectivo cadastro; fornecer exclusivamente os dados oficiais destinados à área Tutor da Ficha de Emergência.
- **Relacionamentos:** associa-se ao ED-02 — Cadastro Oficial do Pet; seus dados são apresentados em ED-08 — Ficha de Emergência.
- **Dependências:** associação oficial ao pet determinada pela DP-PP-013; origem exclusiva no cadastro oficial.
- **Componentes técnicos que a utilizam:** CT-03, CT-07, CT-12 e CT-14.
- **Invariantes documentais:** os dados apresentados na área Tutor devem ser obtidos exclusivamente do cadastro associado ao pet; a consistência com o cadastro deve ser preservada.
- **Limites:** o corpus obrigatório não define, nesta atividade, novos campos, cardinalidades ou regras próprias do Tutor.

### ED-04 — Contato de Emergência

- **Nome:** Contato de Emergência.
- **Objetivo:** representar o contato oficial associado ao pet e apresentado para acionamento imediato.
- **Responsabilidades:** fornecer o número oficialmente cadastrado para apresentação e acionamento; preservar sua associação ao respectivo pet.
- **Relacionamentos:** associa-se ao ED-02 — Cadastro Oficial do Pet; é apresentado em ED-08 — Ficha de Emergência; pode originar a intenção de contato encaminhada ao ambiente externo.
- **Dependências:** origem oficial definida pela DP-PP-013; comportamento de acionamento definido pela DP-PP-015.
- **Componentes técnicos que a utilizam:** CT-03, CT-04, CT-07, CT-08, CT-12, CT-14 e CT-17.
- **Invariantes documentais:** deve corresponder exclusivamente às informações cadastradas para o respectivo pet; o acionamento limita-se ao número oficialmente apresentado; o PetPass AI não define ou controla o mecanismo tecnológico da comunicação.
- **Limites:** não define tecnologia, protocolo, aplicativo, mecanismo de integração ou recurso de comunicação.

### ED-05 — Fotografia do Pet

- **Nome:** Fotografia do Pet.
- **Objetivo:** representar a fotografia original selecionada pelo tutor e vinculada ao cadastro oficial do pet.
- **Responsabilidades:** identificar visualmente o pet; permanecer vinculada ao respectivo cadastro; fornecer a imagem oficial destinada à área fotográfica da Ficha de Emergência.
- **Relacionamentos:** vincula-se ao ED-02 — Cadastro Oficial do Pet e identifica ED-01 — Pet; é apresentada por ED-08 — Ficha de Emergência.
- **Dependências:** seleção durante o cadastro; regras da DP-PP-011; origem oficial preservada pela DP-PP-013.
- **Componentes técnicos que a utilizam:** CT-01, CT-03, CT-07, CT-12 e CT-15.
- **Invariantes documentais:** é opcional; quando cadastrada, nenhuma imagem ilustrativa ou genérica pode substituí-la; deve preservar sua proporção original e não sofrer distorção; sua finalidade é identificação visual; na ausência, a apresentação utiliza o placeholder institucional aprovado.
- **Limites:** não define formato de arquivo, tecnologia de armazenamento ou mecanismo físico de vinculação.

## 5. Papel: Identidade Digital

### ED-06 — Key Pass

- **Nome:** Key Pass.
- **Objetivo:** representar o identificador único do PetPass AI para um animal previamente cadastrado.
- **Responsabilidades:** identificar o pet exclusivamente no ecossistema PetPass AI; permanecer estável durante a existência do cadastro; servir de identidade representada pelo QR Code.
- **Relacionamentos:** associa-se ao ED-02 — Cadastro Oficial do Pet após conclusão válida; identifica ED-01 — Pet; possui ED-07 — QR Code como representação; é apresentada em ED-08 — Ficha de Emergência.
- **Dependências:** conclusão válida do cadastro; regras das DP-PP-006, DP-PP-007 e DP-PP-014.
- **Componentes técnicos que a utilizam:** CT-03, CT-06, CT-07, CT-11, CT-12 e CT-16.
- **Invariantes documentais:** é única para o animal previamente cadastrado; possui finalidade exclusiva no PetPass AI; não substitui outros identificadores; é gerada somente após conclusão válida; permanece inalterada durante a existência do cadastro; alterações cadastrais posteriores não a modificam.
- **Limites:** formato, comprimento e algoritmo de geração não estão definidos.

### ED-07 — QR Code

- **Nome:** QR Code.
- **Objetivo:** representar graficamente e institucionalmente a Key Pass do respectivo pet.
- **Responsabilidades:** tornar visualmente representável a Key Pass; preservar legibilidade na área oficial da ficha; manter a identidade da Key Pass quando regenerado ou substituído.
- **Relacionamentos:** representa ED-06 — Key Pass; integra ED-08 — Ficha de Emergência; corresponde à Key Pass do respectivo pet.
- **Dependências:** existência da Key Pass; regras das DP-PP-007, DP-PP-009 e DP-PP-014.
- **Componentes técnicos que a utilizam:** CT-03, CT-06, CT-07, CT-11, CT-12 e CT-16.
- **Invariantes documentais:** não constitui identificador independente; cada Key Pass possui exclusivamente um QR Code correspondente; pode ser regenerado preservando a mesma Key Pass; sua substituição não altera a identidade digital; quando indisponível, a apresentação utiliza exclusivamente o placeholder institucional aprovado.
- **Limites:** conteúdo interno, padrão, versão, correção de erros, margem silenciosa, resolução, geração e leitura não estão definidos.

## 6. Papel: Representação Institucional

### ED-08 — Ficha de Emergência

- **Nome:** Ficha de Emergência.
- **Objetivo:** representar documentalmente as informações oficiais cadastradas no PetPass AI segundo a identidade institucional aprovada.
- **Responsabilidades:** apresentar identificação do pet, fotografia, dados do tutor, contato de emergência, Key Pass e QR Code; preservar o Modelo 4, a hierarquia, a legibilidade e a composição institucional; permitir o acionamento do contato oficialmente apresentado sem realizar comunicação própria.
- **Relacionamentos:** representa informações de ED-01 a ED-07; depende do ED-02 — Cadastro Oficial do Pet como origem primária; apresenta ED-04 — Contato de Emergência para acionamento.
- **Dependências:** dados oficiais do cadastro; identidade visual e parâmetros das DP-PP-008 a DP-PP-010; comportamentos das DP-PP-011 a DP-PP-015.
- **Componentes técnicos que a utilizam:** CT-03, CT-04, CT-07, CT-08 e CT-12.
- **Invariantes documentais:** constitui Cartão Institucional oficial; não é fonte primária; sua composição permanece fixa e escala proporcionalmente; a relação espacial entre fotografia, QR Code, Key Pass e blocos informativos permanece inalterada; utiliza exclusivamente dados oficiais cadastrados.
- **Limites:** não define persistência, sincronização, atualização técnica, renderização de conteúdo excedente ou implementação do mecanismo de contato.

## 7. Relacionamentos conceituais consolidados

| Origem | Relação conceitual | Destino | Evidência principal |
|---|---|---|---|
| ED-02 — Cadastro Oficial do Pet | registra | ED-01 — Pet | DP-PP-001 a DP-PP-005 |
| ED-02 — Cadastro Oficial do Pet | associa | ED-03 — Tutor | DP-PP-013 |
| ED-02 — Cadastro Oficial do Pet | associa | ED-04 — Contato de Emergência | DP-PP-013 |
| ED-02 — Cadastro Oficial do Pet | vincula | ED-05 — Fotografia do Pet | DP-PP-011 e DP-PP-013 |
| ED-02 — Cadastro Oficial do Pet | recebe após conclusão válida | ED-06 — Key Pass | DP-PP-005 e DP-PP-006 |
| ED-06 — Key Pass | é representada por | ED-07 — QR Code | DP-PP-007 e DP-PP-014 |
| ED-08 — Ficha de Emergência | representa informações oficiais de | ED-02 — Cadastro Oficial do Pet | DP-PP-013 |
| ED-08 — Ficha de Emergência | apresenta | ED-01, ED-03, ED-04, ED-05, ED-06 e ED-07 | DP-PP-008 a DP-PP-015 |

## 8. Dependências conceituais consolidadas

1. ED-06 — Key Pass depende da conclusão válida de ED-02 — Cadastro Oficial do Pet.
2. ED-07 — QR Code depende de ED-06 — Key Pass e não existe conceitualmente como identificador independente.
3. ED-08 — Ficha de Emergência depende de ED-02 como origem primária de todas as informações apresentadas.
4. ED-03, ED-04 e ED-05 dependem de sua associação ao cadastro do respectivo pet para integrarem a ficha.
5. O acionamento de ED-04 depende de sua apresentação oficial na ED-08 e dos recursos disponíveis no ambiente externo ao produto.

## 9. Invariantes documentais transversais

- Nenhuma informação da Ficha de Emergência pode possuir origem distinta do cadastro oficial.
- A Ficha de Emergência não pode tornar-se origem primária dos dados.
- Cadastro inválido não pode ser concluído ou receber Key Pass.
- A Key Pass permanece estável e não é substituída pelo QR Code.
- A regeneração ou substituição do QR Code não altera a identidade digital.
- Fotografia cadastrada não pode ser substituída por imagem ilustrativa ou genérica.
- Ausência de fotografia ou QR Code utiliza o respectivo placeholder institucional aprovado na apresentação.
- A identidade visual e a composição institucional não podem ser alteradas pelo conteúdo apresentado.

## 10. Quantidade de entidades por papel

| Papel no domínio | Quantidade | Entidades |
|---|---:|---|
| Identificação e Cadastro Oficial | 5 | ED-01 a ED-05 |
| Identidade Digital | 2 | ED-06 e ED-07 |
| Representação Institucional | 1 | ED-08 |
| **Total** | **8** | **ED-01 a ED-08** |

## 11. Limites do modelo conceitual

- Não são definidas tabelas, colunas, tipos de dados, chaves, índices ou estruturas físicas.
- Não são definidos banco de dados, ORM, tecnologia ou mecanismo de persistência.
- Não são estabelecidas cardinalidades não expressamente sustentadas pelas deliberações.
- Não são criados campos para Tutor ou Contato de Emergência.
- Não são definidos formato e algoritmo da Key Pass ou parâmetros técnicos do QR Code.
- Validações, placeholders, mensagens e resultados permanecem regras ou estados de apresentação, não entidades autônomas.
- Nenhuma implementação é iniciada.

## 12. Declaração de conformidade metodológica

Este documento define exclusivamente o modelo conceitual do domínio. Nenhum banco de dados, tabela, coluna, tipo de dado, chave, índice, ORM, tecnologia, persistência física ou implementação foi definido. Nenhum artefato existente foi modificado e nenhuma atividade posterior foi iniciada.
