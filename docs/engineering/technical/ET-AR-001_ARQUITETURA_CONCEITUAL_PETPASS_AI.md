# ET-AR-001 — ARQUITETURA CONCEITUAL DO PETPASS AI

## 1. Identificação

- Atividade: ET-AR-001.
- Projeto: CASE-03 — PetPass AI.
- Disciplina: Engenharia Técnica — Arquitetura Conceitual.
- Escopo: camadas, responsabilidades, relações, dependências e limites conceituais.
- Tecnologias, linguagens, frameworks, protocolos e infraestrutura: não definidos.

## 2. Objetivo arquitetural

Estabelecer a separação conceitual das responsabilidades necessárias para receber interações do usuário, coordenar os comportamentos autorizados, aplicar as regras normativas do PetPass AI, manter o cadastro oficial e apresentar a Ficha de Emergência com sua identidade institucional.

A arquitetura preserva a distinção documental entre:

- apresentação institucional;
- coordenação dos comportamentos do produto;
- regras e identidade do domínio;
- estado oficial dos cadastros;
- acionamento de recurso externo ao produto para contato de emergência.

## 3. Fontes normativas e documentais

- `DP-PP-001_CAMPOS_CADASTRO_PET.md`.
- `DP-PP-002_CAMPOS_OBRIGATORIOS_OPCIONAIS_CADASTRO_PET.md`.
- `DP-PP-003_REGRAS_VALIDACAO_CADASTRO_PET.md`.
- `DP-PP-004_TRATAMENTO_FALHAS_CADASTRO_PET.md`.
- `DP-PP-005_CRITERIOS_SUCESSO_CADASTRO_PET.md`.
- `DP-PP-006_IDENTIFICADOR_DIGITAL_KEY_PASS.md`.
- `DP-PP-007_REPRESENTACAO_GRAFICA_QR_CODE.md`.
- `DP-PP-008_IDENTIDADE_VISUAL_FICHA_EMERGENCIA.md`.
- `DP-PP-009_PARAMETROS_TECNICOS_INTERFACE_FICHA_EMERGENCIA.md`.
- `DP-PP-010_COMPORTAMENTO_INSTITUCIONAL_FICHA_EMERGENCIA.md`.
- `DP-PP-011_COMPORTAMENTO_FOTOGRAFIA_FICHA_EMERGENCIA.md`.
- `DP-PP-012_APRESENTACAO_CONTEUDO_FICHA_EMERGENCIA.md`.
- `DP-PP-013_ORIGEM_DADOS_FICHA_EMERGENCIA.md`.
- `DP-PP-014_COMPONENTE_QRCODE_FICHA_EMERGENCIA.md`.
- `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md`.
- `GP-PP-21_AUDITORIA_ENCERRAMENTO_FASE_DELIBERACOES_CASE03.md`.
- `GP-ICF-002_RELATORIO_ENCERRAMENTO_METODOLOGICO_CASE03.md`.

## 4. Camadas arquiteturais

### CA-01 — Apresentação e Interação Institucional

- **Nome:** Apresentação e Interação Institucional.
- **Objetivo:** apresentar as informações e receber as ações do usuário sem assumir regras de domínio ou autoridade sobre o cadastro oficial.
- **Responsabilidades:**
  - apresentar o Cadastro do Pet com os campos autorizados;
  - indicar campos inválidos, mensagens objetivas e confirmação visual conforme resultados recebidos;
  - preservar os dados preenchidos quando houver falha de validação;
  - apresentar a Ficha de Emergência segundo sua composição, nomenclaturas, hierarquia e identidade institucional;
  - apresentar a fotografia cadastrada ou o placeholder institucional previsto;
  - apresentar Key Pass e QR Code em suas áreas oficiais;
  - receber a ação do usuário sobre o telefone de emergência e encaminhá-la para coordenação.
- **Entradas:** ações do usuário; dados destinados ao cadastro; resultados de validação e conclusão; informações oficiais preparadas para apresentação; estados de disponibilidade de fotografia e QR Code.
- **Saídas:** solicitações de cadastro e acionamento; apresentação visual do resultado; mensagens de falha ou sucesso; Ficha de Emergência apresentada.
- **Dependências:** CA-02 — Coordenação de Aplicação; decisões visuais DP-PP-008 a DP-PP-012 e DP-PP-014.
- **Limites de responsabilidade:**
  - não valida regras de negócio por decisão própria;
  - não cria ou altera Key Pass;
  - não determina a origem oficial dos dados;
  - não mantém o cadastro oficial;
  - não realiza comunicação por meios próprios;
  - não redefine o Modelo 4 ou seus componentes.

### CA-02 — Coordenação de Aplicação

- **Nome:** Coordenação de Aplicação.
- **Objetivo:** coordenar as ações autorizadas do produto e ordenar a colaboração entre apresentação, domínio, registro oficial e limite ambiental.
- **Responsabilidades:**
  - receber solicitações oriundas da apresentação;
  - solicitar validação do Cadastro do Pet à camada de domínio;
  - impedir a conclusão quando o domínio informar violação das regras aprovadas;
  - coordenar o registro após validação bem-sucedida;
  - solicitar a associação da identidade digital após conclusão válida do cadastro;
  - obter do registro oficial as informações necessárias à Ficha de Emergência;
  - coordenar a preparação da representação documental sem transformar a ficha em fonte primária;
  - encaminhar a intenção de contato de emergência ao limite ambiental usando exclusivamente o número oficial apresentado.
- **Entradas:** solicitações de cadastro; solicitações de apresentação da ficha; ação de contato de emergência; resultados do domínio; informações recuperadas do cadastro oficial.
- **Saídas:** comandos conceituais para validação e registro; resultados de sucesso ou falha; conjunto oficial destinado à apresentação; solicitação conceitual de acionamento externo.
- **Dependências:** CA-03 — Domínio e Regras do PetPass AI; CA-04 — Registro Oficial de Informações; CA-05 — Limite com o Ambiente de Utilização.
- **Limites de responsabilidade:**
  - não define regras de validação;
  - não decide os campos autorizados;
  - não mantém diretamente o estado oficial;
  - não modifica a identidade institucional;
  - não define nem executa o mecanismo tecnológico de comunicação.

### CA-03 — Domínio e Regras do PetPass AI

- **Nome:** Domínio e Regras do PetPass AI.
- **Objetivo:** representar e aplicar exclusivamente as decisões normativas que definem o Cadastro do Pet, a identidade digital e as relações conceituais da Ficha de Emergência.
- **Responsabilidades:**
  - reconhecer exclusivamente os campos autorizados para o Cadastro do Pet;
  - aplicar obrigatoriedade, valores permitidos e validações aprovadas;
  - determinar sucesso ou falha do cadastro segundo os critérios normativos;
  - definir a Key Pass como identificador único, estável e exclusivo do ecossistema PetPass AI;
  - preservar a Key Pass diante de alterações cadastrais posteriores;
  - preservar a relação conceitual segundo a qual o QR Code representa a Key Pass e não constitui identificador independente;
  - preservar a finalidade identificadora da fotografia;
  - preservar as regras conceituais de origem e consistência entre cadastro oficial e Ficha de Emergência.
- **Entradas:** dados do cadastro submetidos à validação; estado de conclusão do cadastro; identidade e informações oficiais do pet; solicitações conceituais de verificação de consistência.
- **Saídas:** resultado de validação; motivos objetivos de bloqueio; autorização conceitual de conclusão; identidade digital conceitualmente válida; regras de consistência a serem preservadas.
- **Dependências:** exclusivamente as DP-PP-001 a DP-PP-007 e DP-PP-011 a DP-PP-015 como fontes normativas; não depende das camadas de apresentação ou do ambiente externo para definir suas regras.
- **Limites de responsabilidade:**
  - não apresenta interface;
  - não decide tecnologia de armazenamento;
  - não define formato, comprimento ou algoritmo da Key Pass;
  - não define parâmetros técnicos de geração do QR Code;
  - não inicia comunicação externa;
  - não acrescenta validações ou campos.

### CA-04 — Registro Oficial de Informações

- **Nome:** Registro Oficial de Informações.
- **Objetivo:** manter conceitualmente o estado oficial dos cadastros e disponibilizá-lo às ações coordenadas do PetPass AI.
- **Responsabilidades:**
  - manter o registro do pet após conclusão válida;
  - manter disponíveis os dados para funcionalidades subsequentes do MVP;
  - manter a vinculação entre pet, dados associados, fotografia e identidade digital;
  - preservar a estabilidade da Key Pass durante a existência do cadastro;
  - disponibilizar exclusivamente as informações oficiais requeridas para a Ficha de Emergência;
  - preservar a distinção entre cadastro oficial como origem primária e ficha como representação documental.
- **Entradas:** cadastro validado; identidade digital autorizada; fotografia e dados associados ao cadastro; solicitações de consulta coordenadas.
- **Saídas:** confirmação conceitual do registro; informações oficiais do pet; dados associados do tutor e contatos de emergência; fotografia vinculada; Key Pass e relação correspondente com sua representação gráfica.
- **Dependências:** CA-03 para validade e invariantes do domínio; CA-02 para coordenação das operações.
- **Limites de responsabilidade:**
  - não valida regras de negócio por conta própria;
  - não apresenta a Ficha de Emergência;
  - não transforma a ficha em origem primária;
  - não define tecnologia, estrutura física ou mecanismo de armazenamento;
  - não define sincronização ou atualização técnica.

### CA-05 — Limite com o Ambiente de Utilização

- **Nome:** Limite com o Ambiente de Utilização.
- **Objetivo:** demarcar a entrega da intenção de contato de emergência aos recursos disponíveis fora das responsabilidades próprias do PetPass AI.
- **Responsabilidades:**
  - receber da coordenação a solicitação de contato e o número oficialmente apresentado;
  - entregar a ação ao recurso disponível no ambiente de utilização;
  - preservar a neutralidade do PetPass AI quanto ao mecanismo que realizará a comunicação.
- **Entradas:** solicitação de acionamento do contato de emergência; número oficial apresentado na ficha.
- **Saídas:** entrega conceitual da ação ao ambiente.
- **Dependências:** CA-02 — Coordenação de Aplicação; disponibilidade externa ao PetPass AI, conforme DP-PP-015.
- **Limites de responsabilidade:**
  - não cria funcionalidade própria de comunicação;
  - não define tecnologia de telefonia, protocolo, aplicativo, API ou mecanismo de integração;
  - não seleciona ou altera o número de emergência;
  - não pertence ao domínio de regras do cadastro ou da identidade digital.

## 5. Relações permitidas entre as camadas

| Origem | Destino | Relação permitida | Limite |
|---|---|---|---|
| CA-01 | CA-02 | encaminhar ações do usuário e receber resultados destinados à apresentação | CA-01 não acessa diretamente domínio, registro ou ambiente externo |
| CA-02 | CA-03 | solicitar validação e aplicação das regras normativas | CA-02 não substitui decisões do domínio |
| CA-02 | CA-04 | solicitar registro ou consulta após os resultados aplicáveis do domínio | CA-02 não define o mecanismo de manutenção do estado |
| CA-02 | CA-05 | encaminhar intenção de contato e número oficial | CA-02 e CA-05 não realizam comunicação própria nem definem sua tecnologia |
| CA-04 | CA-03 | preservar invariantes e identidade definidos pelo domínio ao manter o estado oficial | CA-04 não cria regras de domínio |
| CA-02 | CA-01 | devolver falhas, confirmações e informações oficiais preparadas para apresentação | CA-02 não altera a identidade visual |

## 6. Relações não permitidas

- CA-01 não acessa diretamente CA-04.
- CA-01 não aciona diretamente recursos externos de comunicação.
- CA-01 não cria regras pertencentes a CA-03.
- CA-03 não depende de CA-01 para determinar regras normativas.
- CA-03 não executa comunicação por meio de CA-05.
- CA-04 não apresenta componentes institucionais e não decide regras de validação.
- CA-05 não acessa o cadastro oficial nem altera informações do pet, tutor ou emergência.
- Nenhuma camada pode preencher as pendências técnicas ou de medição registradas na GP-PP-21 por inferência.

## 7. Dependências conceituais

1. A apresentação depende da coordenação para qualquer ação que envolva regra, estado oficial ou ambiente externo.
2. A coordenação depende do domínio para determinar validade, sucesso e invariantes.
3. O registro oficial depende do resultado válido do domínio para aceitar o cadastro.
4. A Ficha de Emergência depende exclusivamente das informações disponibilizadas pelo registro oficial.
5. A fotografia apresentada depende da fotografia vinculada ao cadastro ou do estado institucional de ausência aprovado.
6. A representação QR Code depende conceitualmente da Key Pass correspondente e não a substitui.
7. A Key Pass depende da conclusão válida do cadastro e permanece estável durante sua existência.
8. O contato de emergência depende do número oficial do cadastro e dos recursos disponíveis no ambiente de utilização.

## 8. Fluxos conceituais autorizados

### 8.1 Cadastro do Pet

CA-01 recebe os dados → CA-02 coordena a solicitação → CA-03 aplica campos, obrigatoriedade e validações → em caso de falha, CA-02 devolve o resultado a CA-01 → em caso de sucesso, CA-02 solicita manutenção a CA-04 → CA-04 confirma o registro → CA-02 devolve confirmação visual a CA-01.

### 8.2 Ficha de Emergência

CA-01 solicita a ficha → CA-02 solicita a CA-04 as informações oficiais → CA-04 fornece cadastro, dados associados, fotografia e identidade digital → CA-02 preserva a representação documental → CA-01 apresenta o conteúdo segundo a identidade institucional.

### 8.3 Contato de emergência

CA-01 recebe o acionamento do usuário → CA-02 utiliza o número oficial apresentado → CA-02 encaminha a intenção a CA-05 → CA-05 entrega a ação aos recursos disponíveis no ambiente, sem mecanismo próprio de comunicação.

## 9. Limites globais da arquitetura conceitual

- Não define tecnologia, linguagem, framework, banco de dados, serviço, API, protocolo ou infraestrutura.
- Não define mecanismo de persistência, sincronização ou atualização.
- Não define formato ou algoritmo da Key Pass.
- Não define geração técnica, correção de erros, margem silenciosa ou resolução do QR Code.
- Não define tamanhos tipográficos, limites dimensionais, truncamento, quebra de linha ou códigos cromáticos ainda pendentes.
- Não inclui definição de Inteligência Artificial nesta atividade.
- Não cria requisitos, campos, regras de negócio ou componentes funcionais além dos documentados.
- Não inicia implementação.

## 10. Rastreabilidade arquitetural consolidada

| Responsabilidade conceitual | Fontes principais |
|---|---|
| Cadastro, obrigatoriedade, validação, falhas e sucesso | DP-PP-001 a DP-PP-005 |
| Key Pass e relação com QR Code | DP-PP-006, DP-PP-007, DP-PP-014 |
| Identidade e estrutura institucional da ficha | DP-PP-008, DP-PP-009, DP-PP-010, DP-PP-012 |
| Fotografia oficial | DP-PP-008, DP-PP-011 |
| Origem oficial das informações | DP-PP-013 |
| Acionamento do telefone de emergência | DP-PP-015 |
| Encerramento das deliberações e pendências técnicas | GP-PP-21 |
| Limites do encerramento metodológico | GP-ICF-002 |

## 11. Declaração de conformidade metodológica

Esta arquitetura é exclusivamente conceitual. Nenhuma tecnologia, linguagem, framework, banco de dados, API, protocolo, infraestrutura, mecanismo de IA ou implementação foi definido. Nenhum artefato existente foi modificado e nenhuma atividade posterior foi iniciada.
