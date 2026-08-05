# ET-IF-001 — FLUXOS TÉCNICOS DO PETPASS AI

## 1. Identificação

- Atividade: ET-IF-001.
- Projeto: CASE-03 — PetPass AI.
- Disciplina: Engenharia Técnica — Fluxos Técnicos Conceituais.
- Escopo: circulação lógica de informações entre camadas, componentes e entidades.
- Tecnologias, protocolos e implementação: não definidos.

## 2. Fontes documentais

- `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md`.
- `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md`.
- `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md`.
- `ET-DD-002_MODELO_LOGICO_DADOS_PETPASS_AI.md`.
- `DP-PP-001_CAMPOS_CADASTRO_PET.md` a `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md`.

## 3. Convenções dos fluxos

- O evento de início registrado é uma ação funcional documentada, não um evento técnico.
- A sequência descreve responsabilidades e circulação conceitual, sem mensagens técnicas, contratos ou mecanismos de transporte.
- Toda passagem pela apresentação ocorre por CA-02 — Coordenação de Aplicação.
- Toda validação ou invariante é determinada por CA-03 — Domínio e Regras do PetPass AI.
- Toda informação oficial é obtida por CA-04 — Registro Oficial de Informações.
- A comunicação externa limita-se à entrega conceitual da ação por CA-05.

## 4. Finalidade: Cadastro Oficial

### FT-01 — Cadastro válido do Pet

- **Nome do fluxo:** Cadastro válido do Pet.
- **Objetivo:** concluir o cadastro quando todos os campos obrigatórios e validações aprovadas forem satisfeitos e o registro oficial for confirmado.
- **Evento de início:** o usuário solicita a conclusão do Cadastro do Pet com os dados preenchidos.
- **Sequência de interação entre as camadas:**
  1. **CA-01** recebe os dados por CT-01 e encaminha a solicitação a **CA-02**.
  2. **CA-02**, por CT-05, solicita a **CA-03** a avaliação dos dados.
  3. **CA-03**, por CT-09, verifica campos, obrigatoriedades, valores permitidos e validações; CT-10 reconhece que não há violação impeditiva.
  4. **CA-02** solicita a **CA-04**, por CT-13, a manutenção do Cadastro Oficial do Pet.
  5. **CA-04** confirma conceitualmente o registro válido e mantém ED-01 no agrupamento ED-02; se houver fotografia, CT-15 preserva sua vinculação.
  6. **CA-02** recebe a confirmação, reconhece a conclusão e encaminha o resultado a **CA-01**.
  7. **CA-01**, por CT-02, apresenta a confirmação visual da conclusão.
- **Componentes participantes:** CT-01, CT-02, CT-05, CT-09, CT-10, CT-13 e, quando houver fotografia, CT-15.
- **Entidades manipuladas:** ED-01 — Pet; ED-02 — Cadastro Oficial do Pet; opcionalmente ED-05 — Fotografia do Pet.
- **Resultado esperado:** Cadastro Oficial concluído, informações disponíveis às funcionalidades subsequentes e confirmação visual apresentada.
- **Limites de responsabilidade:** o fluxo não acrescenta campos ou validações; não define armazenamento; não constitui ainda o mecanismo técnico da Key Pass; fotografia permanece opcional.

### FT-02 — Bloqueio do Cadastro por falha de validação

- **Nome do fluxo:** Bloqueio do Cadastro por falha de validação.
- **Objetivo:** impedir a conclusão quando um campo obrigatório ou uma validação aprovada não for satisfeito, preservando os dados informados.
- **Evento de início:** o usuário solicita a conclusão do cadastro e os dados submetidos contêm violação documentada.
- **Sequência de interação entre as camadas:**
  1. **CA-01**, por CT-01, encaminha os dados a **CA-02**.
  2. **CA-02**, por CT-05, solicita avaliação a **CA-03**.
  3. **CA-03**, por CT-09, identifica os campos inválidos e os motivos objetivos; CT-10 determina o bloqueio.
  4. **CA-02** interrompe a continuidade antes de qualquer solicitação de registro à **CA-04**.
  5. **CA-02** devolve o resultado a **CA-01**.
  6. **CA-01**, por CT-02, destaca os campos com erro, apresenta o motivo e mantém os dados já preenchidos.
- **Componentes participantes:** CT-01, CT-02, CT-05, CT-09 e CT-10.
- **Entidades manipuladas:** ED-01 — Pet apenas como conjunto de dados em avaliação; ED-02 — Cadastro Oficial do Pet não assume estado concluído.
- **Resultado esperado:** conclusão bloqueada, ausência de registro confirmado, dados preservados e falhas indicadas ao usuário.
- **Limites de responsabilidade:** o fluxo não limpa o formulário, não corrige dados, não utiliza IA, não cria tratamento adicional e não alcança CA-04 para manutenção de cadastro inválido.

## 5. Finalidade: Identidade Digital

### FT-03 — Constituição da Identidade Digital

- **Nome do fluxo:** Constituição da Identidade Digital.
- **Objetivo:** associar ao pet validamente cadastrado a Key Pass estável e sua representação QR Code correspondente.
- **Evento de início:** CT-05 reconhece a conclusão válida e confirmada do Cadastro Oficial do Pet.
- **Sequência de interação entre as camadas:**
  1. **CA-02**, por CT-05, encaminha a confirmação válida a CT-06.
  2. CT-06 solicita a **CA-03**, por CT-11, a aplicação das invariantes da identidade digital.
  3. **CA-03** confirma que a Key Pass somente pode ser associada após cadastro válido, deve ser única e permanecer estável.
  4. **CA-02**, por CT-06, solicita a **CA-04**, por CT-16, a manutenção da identidade associada ao ED-02.
  5. **CA-04** preserva ED-06 e sua relação `1:1` com ED-07 para o cadastro correspondente.
  6. CT-06 disponibiliza a identidade oficial aos fluxos autorizados, sem alterar suas invariantes.
- **Componentes participantes:** CT-05, CT-06, CT-11 e CT-16.
- **Entidades manipuladas:** ED-01 — Pet; ED-02 — Cadastro Oficial do Pet; ED-06 — Key Pass; ED-07 — QR Code.
- **Resultado esperado:** cadastro válido associado a uma Key Pass única e estável e ao QR Code que a representa.
- **Limites de responsabilidade:** não define formato, comprimento ou algoritmo da Key Pass; não define conteúdo, padrão, correção de erros, resolução ou mecanismo de geração do QR Code.

### FT-04 — Regeneração da representação QR Code

- **Nome do fluxo:** Regeneração da representação QR Code.
- **Objetivo:** preservar a mesma Key Pass quando sua representação QR Code precisar ser regenerada.
- **Evento de início:** necessidade funcional de regenerar o QR Code correspondente a uma Key Pass existente.
- **Sequência de interação entre as camadas:**
  1. **CA-02**, por CT-06, identifica a Key Pass oficial mantida em **CA-04** por CT-16.
  2. **CA-02** solicita a **CA-03**, por CT-11, a preservação das invariantes durante a regeneração.
  3. **CA-03** determina que ED-07 continue representando ED-06, sem alterar a identidade digital.
  4. **CA-04**, por CT-16, preserva a mesma Key Pass e a relação com o QR Code correspondente.
  5. **CA-02** disponibiliza o estado atualizado da representação aos fluxos de apresentação autorizados.
- **Componentes participantes:** CT-06, CT-11 e CT-16.
- **Entidades manipuladas:** ED-06 — Key Pass; ED-07 — QR Code.
- **Resultado esperado:** QR Code correspondente disponível como representação da mesma Key Pass, sem mudança da identidade do pet.
- **Limites de responsabilidade:** o fluxo não define gatilho de interface, tecnologia, conteúdo interno, padrão, versão, biblioteca, correção de erros, resolução ou mecanismo técnico de regeneração.

## 6. Finalidade: Representação Institucional

### FT-05 — Apresentação da Ficha de Emergência

- **Nome do fluxo:** Apresentação da Ficha de Emergência.
- **Objetivo:** apresentar a Ficha de Emergência como representação institucional das informações oficiais do cadastro.
- **Evento de início:** solicitação funcional de visualização da Ficha de Emergência do pet cadastrado.
- **Sequência de interação entre as camadas:**
  1. **CA-01**, por CT-03, encaminha a solicitação a **CA-02**.
  2. **CA-02**, por CT-07, solicita à **CA-04** as informações oficiais mantidas por CT-13, CT-14, CT-15 e CT-16.
  3. **CA-04** fornece ED-01 e ED-02, os dados associados ED-03 e ED-04, o estado de ED-05 e a identidade ED-06/ED-07.
  4. **CA-02** solicita à **CA-03**, por CT-12, a verificação da consistência e da origem oficial.
  5. **CA-03** confirma que ED-08 permanece representação de ED-02 e não cria ou altera informações.
  6. **CA-02** encaminha o conjunto oficial a **CA-01**.
  7. **CA-01**, por CT-03, apresenta ED-08 segundo o Modelo 4, a composição fixa, a hierarquia e as áreas institucionais.
  8. Se ED-05 estiver ausente, CT-03 apresenta exclusivamente o placeholder institucional da fotografia.
  9. Se ED-07 não puder ser apresentado, CT-03 apresenta exclusivamente o placeholder institucional do QR Code, preservando ED-06.
- **Componentes participantes:** CT-03, CT-07, CT-12, CT-13, CT-14, CT-15 e CT-16.
- **Entidades manipuladas:** ED-01 — Pet; ED-02 — Cadastro Oficial do Pet; ED-03 — Tutor; ED-04 — Contato de Emergência; ED-05 — Fotografia do Pet; ED-06 — Key Pass; ED-07 — QR Code; ED-08 — Ficha de Emergência.
- **Resultado esperado:** Ficha de Emergência apresentada com informações oficiais, identidade visual preservada e estados institucionais de ausência aplicados quando necessários.
- **Limites de responsabilidade:** a ficha não se torna fonte primária; o fluxo não altera cadastro; não define truncamento, quebra de linha, tamanhos tipográficos, códigos cromáticos ou parâmetros técnicos do QR Code; placeholders não se tornam entidades do domínio.

## 7. Finalidade: Contato de Emergência

### FT-06 — Acionamento do Contato de Emergência

- **Nome do fluxo:** Acionamento do Contato de Emergência.
- **Objetivo:** entregar ao ambiente de utilização a intenção de contato correspondente ao número oficial apresentado.
- **Evento de início:** o usuário aciona o telefone de emergência apresentado na Ficha de Emergência.
- **Sequência de interação entre as camadas:**
  1. **CA-01**, por CT-04, recebe a ação funcional associada a ED-04 e a encaminha a **CA-02**.
  2. **CA-02**, por CT-08, preserva o número oficial obtido do registro associado por CT-14.
  3. **CA-02** encaminha a intenção e o número a **CA-05**.
  4. **CA-05**, por CT-17, entrega a ação aos recursos disponíveis no ambiente de utilização.
  5. O PetPass AI encerra sua responsabilidade na entrega conceitual da ação ao ambiente.
- **Componentes participantes:** CT-04, CT-08, CT-14 e CT-17.
- **Entidades manipuladas:** ED-02 — Cadastro Oficial do Pet; ED-04 — Contato de Emergência; ED-08 — Ficha de Emergência.
- **Resultado esperado:** intenção de contato entregue ao ambiente usando exclusivamente o número oficial apresentado.
- **Limites de responsabilidade:** o produto não define, controla ou executa mecanismo próprio de comunicação; não define tecnologia de telefonia, protocolo, aplicativo, API ou integração; não altera o contato oficial.

## 8. Relações entre fluxos

| Fluxo de origem | Relação funcional | Fluxo relacionado | Restrição |
|---|---|---|---|
| FT-01 | conclusão válida permite | FT-03 | FT-03 não ocorre para cadastro inválido |
| FT-02 | exclui continuidade para | FT-03 | bloqueio não gera identidade digital |
| FT-03 | fornece identidade para | FT-05 | QR Code representa a Key Pass e não a substitui |
| FT-04 | atualiza somente a representação usada em | FT-05 | Key Pass permanece inalterada |
| FT-05 | disponibiliza o contato apresentado para | FT-06 | FT-06 utiliza exclusivamente o número oficial |

## 9. Matriz consolidada de participação

| Fluxo | Camadas | Componentes | Entidades |
|---|---|---|---|
| FT-01 | CA-01, CA-02, CA-03, CA-04 | CT-01, CT-02, CT-05, CT-09, CT-10, CT-13, CT-15 quando aplicável | ED-01, ED-02, ED-05 quando aplicável |
| FT-02 | CA-01, CA-02, CA-03 | CT-01, CT-02, CT-05, CT-09, CT-10 | ED-01; ED-02 sem conclusão |
| FT-03 | CA-02, CA-03, CA-04 | CT-05, CT-06, CT-11, CT-16 | ED-01, ED-02, ED-06, ED-07 |
| FT-04 | CA-02, CA-03, CA-04 | CT-06, CT-11, CT-16 | ED-06, ED-07 |
| FT-05 | CA-01, CA-02, CA-03, CA-04 | CT-03, CT-07, CT-12, CT-13, CT-14, CT-15, CT-16 | ED-01 a ED-08 |
| FT-06 | CA-01, CA-02, CA-04, CA-05 | CT-04, CT-08, CT-14, CT-17 | ED-02, ED-04, ED-08 |

## 10. Quantidade de fluxos por finalidade

| Finalidade funcional | Quantidade | Fluxos |
|---|---:|---|
| Cadastro Oficial | 2 | FT-01 e FT-02 |
| Identidade Digital | 2 | FT-03 e FT-04 |
| Representação Institucional | 1 | FT-05 |
| Contato de Emergência | 1 | FT-06 |
| **Total** | **6** | **FT-01 a FT-06** |

## 11. Limites globais

- Não são definidos APIs, endpoints, protocolos, mensagens técnicas, filas ou eventos técnicos.
- Não são definidos banco de dados, infraestrutura, tecnologias ou mecanismos de transporte.
- Não são definidos mecanismos de geração da Key Pass ou do QR Code.
- Não são definidos detalhes de renderização ou persistência.
- Nenhum fluxo modifica as entidades ou responsabilidades aprovadas nos modelos anteriores.
- Nenhuma implementação é iniciada.

## 12. Declaração de conformidade metodológica

Este documento registra exclusivamente fluxos técnicos conceituais sustentados pelo corpus. Nenhuma API, endpoint, protocolo, mensagem técnica, fila, evento técnico, banco de dados, infraestrutura, tecnologia ou implementação foi definida. Nenhum artefato existente foi modificado e nenhuma atividade posterior foi iniciada.
