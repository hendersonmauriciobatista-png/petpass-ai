# WF-FT-01 — ESPECIFICAÇÃO DE IMPLEMENTAÇÃO DO CADASTRO VÁLIDO DO PET

## 1. Identificação

- **Atividade:** WF-FT-01
- **Projeto:** CASE-03 — PetPass AI
- **Fluxo de origem:** FT-01 — Cadastro válido do Pet
- **Workflow tecnológico correspondente:** WF-FT-01
- **Classificação:** Engenharia Técnica — Especificação de Implementação
- **Data:** 03/08/2026
- **Estado:** Especificado; não implementado

## 2. Fontes obrigatórias

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `ET-AR-002_ARQUITETURA_TECNOLOGICA_PETPASS_AI.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md`.
- `ET-DD-002_MODELO_LOGICO_DADOS_PETPASS_AI.md`.
- `ET-IF-001_FLUXOS_TECNICOS_PETPASS_AI.md`.
- `ET-IM-001_PLANO_IMPLEMENTACAO_ENGENHARIA_TECNICA.md`.
- `DP-PP-001_CAMPOS_CADASTRO_PET.md`.
- `DP-PP-002_CAMPOS_OBRIGATORIOS_OPCIONAIS_CADASTRO_PET.md`.
- `DP-PP-003_REGRAS_VALIDACAO_CADASTRO_PET.md`.
- `DP-PP-004_TRATAMENTO_FALHAS_CADASTRO_PET.md`.
- `DP-PP-005_CRITERIOS_SUCESSO_CADASTRO_PET.md`.

## 3. Objetivo do workflow

Coordenar o caminho de sucesso do Cadastro do Pet desde a solicitação de conclusão apresentada pelo usuário até a confirmação visual, permitindo o registro oficial somente quando todos os campos obrigatórios e todas as validações autorizadas forem satisfeitos.

O workflow não abrange o caminho de falha, a constituição da identidade digital ou qualquer funcionalidade posterior.

## 4. Entrada

### 4.1 Evento oficial de início

O usuário solicita a conclusão do Cadastro do Pet com os dados preenchidos.

### 4.2 Condições obrigatórias de entrada

- Deve existir uma solicitação de conclusão originada em CA-01 — Apresentação e Interação Institucional e encaminhada a CA-02 — Coordenação de Aplicação.
- A solicitação deve referir-se exclusivamente ao Cadastro do Pet.
- O conjunto submetido deve limitar-se aos campos autorizados:
  - Nome do Pet;
  - Espécie;
  - Raça;
  - Sexo;
  - Idade;
  - Peso;
  - Cor;
  - Foto.
- Nome do Pet, Espécie e Raça devem estar presentes para que o processamento possa alcançar o caminho de sucesso.
- Sexo, Idade, Peso, Cor e Foto permanecem opcionais.

### 4.3 Dados de entrada

| Campo | Classificação | Condição documental |
|---|---|---|
| Nome do Pet | Obrigatório | Não pode permanecer vazio. |
| Espécie | Obrigatório | Deve corresponder a Cão ou Gato. |
| Raça | Obrigatório | Não pode permanecer vazia. |
| Sexo | Opcional | Quando informado, deve corresponder a Macho, Fêmea ou Não informado. |
| Idade | Opcional | Quando informada, deve ser número inteiro positivo. |
| Peso | Opcional | Quando informado, deve ser número decimal positivo. |
| Cor | Opcional | Texto livre. |
| Foto | Opcional | Quando informada, deve ser arquivo de imagem. |

Formato técnico, contrato, transporte e serialização dos dados de entrada não estão determinados pelas fontes obrigatórias e não são inferidos nesta especificação.

## 5. Processamento

### 5.1 Camadas arquiteturais percorridas

1. CA-01 — Apresentação e Interação Institucional.
2. CA-02 — Coordenação de Aplicação.
3. CA-03 — Domínio e Regras do PetPass AI.
4. CA-04 — Registro Oficial de Informações.
5. Retorno por CA-02 para CA-01.

Não é permitido acesso direto de CA-01 a CA-03 ou CA-04.

### 5.2 Componentes participantes

| Componente | Participação exclusiva no workflow |
|---|---|
| CT-01 — Apresentação do Cadastro do Pet | Receber os dados e encaminhar a solicitação à Coordenação. |
| CT-02 — Apresentação de Retorno do Cadastro | Apresentar a confirmação visual recebida após a conclusão oficial. |
| CT-05 — Coordenação do Cadastro do Pet | Ordenar avaliação, registro e retorno sem decidir regras de domínio. |
| CT-09 — Avaliador das Regras do Cadastro | Aplicar exclusivamente campos, obrigatoriedades, valores permitidos e validações aprovadas. |
| CT-10 — Determinador do Resultado do Cadastro | Reconhecer a ausência de violação impeditiva e determinar o resultado válido. |
| CT-13 — Registro Oficial do Pet | Manter o Cadastro Oficial após resultado válido. |
| CT-15 — Registro da Fotografia Vinculada | Preservar a vinculação da fotografia quando ela tiver sido informada e validada. |

### 5.3 Entidades manipuladas

- **ED-01 — Pet:** conjunto de informações do pet submetido e validado.
- **ED-02 — Cadastro Oficial do Pet:** registro oficial que somente assume estado concluído após validação e armazenamento bem-sucedidos.
- **ED-05 — Fotografia do Pet:** manipulada exclusivamente quando uma Foto opcional tiver sido informada e validada.

Relações lógicas preservadas:

- RL-01 — Cadastro Oficial registra Pet.
- RL-04 — Cadastro Oficial vincula Fotografia do Pet, quando aplicável.

### 5.4 Sequência lógica completa

1. CT-01 recebe os dados preenchidos quando o usuário solicita a conclusão do Cadastro do Pet.
2. CA-01 encaminha a solicitação e os dados a CA-02.
3. CT-05 recebe a solicitação e solicita a CA-03 a avaliação dos dados.
4. CT-09 verifica exclusivamente:
   - se o conjunto de campos permanece dentro do escopo autorizado;
   - a presença e o não esvaziamento de Nome do Pet;
   - a presença de Espécie e sua correspondência a Cão ou Gato;
   - a presença e o não esvaziamento de Raça;
   - quando Sexo estiver informado, sua correspondência a Macho, Fêmea ou Não informado;
   - quando Idade estiver informada, se é número inteiro positivo;
   - quando Peso estiver informado, se é número decimal positivo;
   - quando Foto estiver informada, se é arquivo de imagem;
   - Cor, quando informada, como texto livre, sem validação adicional.
5. CT-10 reconhece que nenhuma regra de validação foi violada e determina que o processamento pode continuar pelo caminho válido.
6. CT-05 solicita a CA-04, por CT-13, o armazenamento do Cadastro Oficial do Pet.
7. CT-13 mantém ED-01 associado a ED-02.
8. Quando houver Foto informada e validada, CT-15 preserva ED-05 vinculada a ED-02. Quando não houver Foto, a ausência não impede o cadastro.
9. CA-04 confirma o armazenamento bem-sucedido e a disponibilidade dos dados para as funcionalidades subsequentes do MVP.
10. CT-05 recebe a confirmação oficial e encaminha o resultado a CA-01.
11. CT-02 apresenta a confirmação visual da conclusão do cadastro.
12. O workflow encerra-se com o resultado oficial de sucesso.

O mecanismo técnico de cada passagem entre camadas não está determinado pelas fontes obrigatórias e não é inferido nesta especificação.

## 6. Validações obrigatórias

| Identificador | Validação | Resultado necessário para continuidade |
|---|---|---|
| VAL-FT01-01 | Nome do Pet é obrigatório e não pode permanecer vazio. | Nome do Pet preenchido. |
| VAL-FT01-02 | Espécie é obrigatória e restrita a Cão ou Gato. | Uma das duas opções autorizadas selecionada. |
| VAL-FT01-03 | Raça é obrigatória e não pode permanecer vazia. | Raça preenchida. |
| VAL-FT01-04 | Sexo é opcional e, quando informado, admite somente Macho, Fêmea ou Não informado. | Ausência do campo ou valor autorizado. |
| VAL-FT01-05 | Idade é opcional e, quando informada, deve ser número inteiro positivo. | Ausência do campo ou valor válido. |
| VAL-FT01-06 | Peso é opcional e, quando informado, deve ser número decimal positivo. | Ausência do campo ou valor válido. |
| VAL-FT01-07 | Cor é opcional e corresponde a texto livre. | Nenhuma validação adicional autorizada. |
| VAL-FT01-08 | Foto é opcional e, quando informada, deve ser arquivo de imagem. | Ausência do campo ou arquivo de imagem. |

Nenhuma validação adicional está autorizada. Inteligência Artificial não poderá ser utilizada para validar ou corrigir os dados.

## 7. Exceções e condições de interrupção

O WF-FT-01 será interrompido antes do registro quando:

- Nome do Pet estiver ausente ou vazio;
- Espécie estiver ausente ou não corresponder a Cão ou Gato;
- Raça estiver ausente ou vazia;
- Sexo informado não corresponder aos valores autorizados;
- Idade informada não for número inteiro positivo;
- Peso informado não for número decimal positivo;
- Foto informada não for arquivo de imagem;
- houver campo não autorizado no escopo do Cadastro do Pet.

Nessas ocorrências:

- o WF-FT-01 não produz cadastro concluído;
- CA-04 não recebe solicitação de armazenamento de cadastro inválido;
- FT-03 não pode ser iniciado;
- o tratamento do caminho de falha pertence ao FT-02 e não é especificado nesta atividade.

O workflow também não pode ser declarado concluído quando:

- o armazenamento do registro não for confirmado;
- os dados não permanecerem disponíveis às funcionalidades subsequentes;
- a confirmação visual não for apresentada.

As fontes obrigatórias não determinam o tratamento técnico de falha de armazenamento, indisponibilidade posterior dos dados ou falha da confirmação visual. Esses comportamentos permanecem **NÃO DETERMINADOS — NÃO INFERIDOS**.

## 8. Saída

### 8.1 Resultado oficial produzido

O resultado oficial do WF-FT-01 é composto cumulativamente por:

- todos os campos obrigatórios preenchidos conforme as validações autorizadas;
- ausência de violação de regra de validação;
- ED-01 armazenada com sucesso no Cadastro Oficial ED-02;
- ED-05 vinculada ao cadastro quando a Foto opcional tiver sido informada;
- dados disponíveis para utilização nas funcionalidades subsequentes do MVP;
- confirmação visual da conclusão apresentada por CT-02.

### 8.2 Limite da saída

A saída não inclui:

- Key Pass;
- QR Code;
- Ficha de Emergência;
- contato externo;
- qualquer entidade, campo ou comportamento não pertencente ao FT-01.

## 9. Critério documental de conclusão

O WF-FT-01 somente poderá ser considerado documentalmente concluído quando houver evidência objetiva de que, em uma mesma execução:

1. a entrada foi recebida por CT-01 e encaminhada por CA-01 a CT-05;
2. CT-09 aplicou exclusivamente as oito validações documentadas;
3. CT-10 determinou ausência de violação impeditiva;
4. CT-13 confirmou o armazenamento de ED-01 em ED-02;
5. CT-15 preservou a vinculação de ED-05 quando havia Foto;
6. os dados permaneceram disponíveis às funcionalidades subsequentes;
7. CT-02 apresentou confirmação visual;
8. nenhuma responsabilidade de domínio, registro ou apresentação foi assumida pelo n8n além da coordenação autorizada.

A falta de qualquer uma dessas evidências impede a declaração de conclusão do workflow.

## 10. Dependências

### 10.1 Dependências para futura implementação do WF-FT-01

- Tecnologia da CA-01 — Apresentação e Interação Institucional: não determinada.
- Tecnologia da CA-03 — Domínio e Regras do PetPass AI: não determinada.
- Tecnologia da CA-04 — Registro Oficial de Informações: não determinada.
- Mecanismos de integração entre CA-01, CA-02, CA-03 e CA-04: não determinados.
- Formato técnico, contrato e transporte da entrada e da saída: não determinados.
- Infraestrutura física: fora do escopo e não definida.

O n8n permanece aprovado exclusivamente para CT-05 na CA-02 e para a orquestração do fluxo. Essas ausências impedem a construção do workflow, mas não impedem sua especificação documental.

### 10.2 Dependências para workflows posteriores

| Workflow posterior | Dependência produzida pelo WF-FT-01 |
|---|---|
| WF-FT-03 — Constituição da Identidade Digital | Cadastro oficial válido, armazenado e confirmado. |
| WF-FT-05 — Apresentação da Ficha de Emergência | Informações do pet disponíveis no Registro Oficial; fotografia vinculada quando informada. |

O WF-FT-01 não inicia esses workflows nesta atividade.

## 11. Limites de responsabilidade

- O workflow coordena exclusivamente o caminho de cadastro válido.
- O n8n não cria nem interpreta regras de domínio.
- CA-01 não valida por decisão própria nem acessa diretamente CA-04.
- CA-03 não apresenta interface nem mantém o estado oficial.
- CA-04 não cria validações nem apresenta confirmação visual.
- Nenhum mecanismo de persistência, API, protocolo, infraestrutura, nó ou gatilho n8n é definido.
- Nenhuma Key Pass ou representação QR Code é constituída no WF-FT-01.
- Nenhum tratamento não documentado é criado.

## 12. Declaração de conformidade metodológica

Esta especificação descreve exclusivamente o WF-FT-01 a partir das fontes obrigatórias. Foram preservados o evento de início, as camadas, os componentes, as entidades, as relações, as validações, os critérios de sucesso e as dependências documentadas. Ausências técnicas foram registradas sem inferência. Nenhum nó n8n, API, banco de dados, infraestrutura, código ou implementação foi criado; nenhum documento anterior foi alterado e nenhuma atividade posterior foi iniciada.
