# GP-EVO-01 — PROCESSO FORMAL DE EVOLUÇÃO DO FRAMEWORK

## Adequação do ICFACTORY para Projetos Individuais

## 1. CONTROLE DO PROCESSO

- Identificador: GP-EVO-01.
  - Origem: Product Owner — GP-EVO-01.
- Objeto: avaliação institucional da possível lacuna normativa relacionada à aplicação do ICFACTORY em projetos conduzidos por um único Product Owner.
  - Origem: Product Owner — GP-EVO-01, “Objetivo” e “Fundamentação”.
- Natureza do ato de abertura: administrativa e processual.
  - Origem: Product Owner — GP-EVO-01, “Autorização”.
- Autor da autorização: Product Owner.
  - Origem: Product Owner — GP-EVO-01.
- Data de abertura: 29/07/2026.
  - Origem: contexto temporal da execução.
- Corpus normativo consultado: Governance Baseline v1.0 do ICFACTORY.
  - Origem: ICFACTORY — `docs/governance/FRAMEWORK_STATE_V1.md`.
- Commit do repositório oficial consultado: `eb64ad1031819c814934e52091d4a7eda0be9a3b`.
  - Origem: inspeção direta da referência `main` do repositório oficial indicado pelo Product Owner.

### Estado processual

**ABERTO — CONTRIBUIÇÃO REGISTRADA, AGUARDANDO TRIAGEM INSTITUCIONAL.**

Fundamento:

- qualquer colaborador humano pode registrar pesquisa, evidência e proposta de melhoria;
- uma contribuição é recebida sem promessa de incorporação;
- admissão em Research depende de triagem;
- triagem pode ser realizada pela Custódia Metodológica ou por responsável de Research formalmente delegado;
- admissão em Research não constitui aprovação metodológica.

Origem:

- ICFACTORY — `docs/governance/COMMUNITY_CONTRIBUTION_POLICY.md`, seções 2, 3, 5, 7 e 8.
- ICFACTORY — `docs/governance/METHODOLOGICAL_CUSTODY_MODEL.md`, seções 5 e 7.

### Limite da abertura

Este registro:

- abre e documenta a contribuição no início do Fluxo Oficial de Evolução;
- não declara admissão em Research;
- não atribui nível de maturidade Pesquisa (P);
- não autoriza experimento;
- não constitui validação;
- não constitui promoção;
- não constitui ato custodial;
- não modifica o método oficial.

Origem:

- ICFACTORY — `docs/governance/COMMUNITY_CONTRIBUTION_POLICY.md`, “Fluxo Oficial de Evolução”, “Recepção e triagem” e “Separação entre Conhecimento e Método”.
- ICFACTORY — `docs/governance/METHODOLOGICAL_CUSTODY_MODEL.md`, “Fluxo Oficial de Evolução”.

## 2. AUTORIZAÇÃO E LIMITES

### 2.1 Ato autorizado

Fica registrada a autorização do Product Owner para abertura administrativa do Processo Formal de Evolução do Framework ICFACTORY, decorrente da GP-RXX.

Origem:

- Product Owner — GP-EVO-01, “Autorização”.

### 2.2 Atos não autorizados

- Alteração da Constituição.
- Alteração dos templates.
- Alteração de documentos normativos.
- Criação de exceções.
- Flexibilização de princípios.
- Alteração de regras de governança.
- Promoção de proposta ao patrimônio normativo.

Origem:

- Product Owner — GP-EVO-01, “Autorização”.

### 2.3 Escopo autorizado

- Consolidar evidências.
- Identificar princípios constitucionais.
- Avaliar impactos arquiteturais.
- Verificar compatibilidade com a Constituição vigente.
- Produzir parecer técnico fundamentado.

Origem:

- Product Owner — GP-EVO-01, “Escopo do Processo”.

## 3. IDENTIFICAÇÃO DA POSSÍVEL LACUNA NORMATIVA

### PL-01 — Adoção do ICFACTORY por autoridade humana única

Descrição:

- A Constituição ICFACTORY não estabelece número mínimo de participantes nem trata explicitamente projetos individuais.
- O Project Constitution Template admite acumulação de funções, mas proíbe que a autoridade de validação valide ato ou conteúdo de sua própria autoria.
- O template também proíbe que uma autoridade institua ou designe a própria competência por simples declaração.
- O corpus normativo consultado não apresenta rito específico ou mecanismo compensatório para um projeto em que uma única pessoa seja autora e única autoridade humana disponível.

Efeito observado:

- uma Constituição de Projeto individual pode permanecer como rascunho controlado;
- sem autoridade competente distinta para validação do conteúdo autoral, não consegue atender ao requisito material de validação constitucional compatível;
- sem esse requisito, não adquire vigência.

Classificação:

- possível lacuna normativa de adoção;
- contribuição investigativa;
- sem maturidade atribuída;
- sem efeito normativo.

Origem:

- GP-RXX — Pesquisa Arquitetural: Adequação do ICFACTORY para Projetos Individuais.
- ICFACTORY — `CONSTITUTION.md`.
- ICFACTORY — `governance/PROJECT_CONSTITUTION_TEMPLATE.md`.
- ICFACTORY — `CONSTITUTIONAL_LEXICON.md`.

## 4. EVIDÊNCIAS CONSOLIDADAS

| ID | Evidência | Resultado sustentado | Fonte |
|---|---|---|---|
| EV-01 | A Constituição v0.2 não diferencia projetos por quantidade de participantes | Não existe pressuposto multiusuário textual explícito | `CONSTITUTION.md` |
| EV-02 | O template admite acumulação de funções | Não há segregação absoluta de todos os papéis | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| EV-03 | O validador não pode validar conteúdo de sua autoria | A separação autoria–validação é materialmente obrigatória | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| EV-04 | A acumulação não pode eliminar validação constitucional | Acúmulo de papéis não supre o gate de validação | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| EV-05 | Nenhuma autoridade pode autodesignar competência por declaração | Um Product Owner único não demonstra proveniência por ato próprio | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| EV-06 | Verificação de conformidade não substitui validação | Auditoria, checklist ou análise não produzem o mesmo efeito constitucional | `PROJECT_CONSTITUTION_TEMPLATE.md`; `CONSTITUTIONAL_LEXICON.md` |
| EV-07 | Inteligência não é autoridade | IA não pode ser presumida como autoridade constitucional compensatória | `CONSTITUTION.md`, Artigo XI |
| EV-08 | Não foi localizada regra específica para projetos individuais | Existe possível lacuna de adoção a avaliar | GP-RXX e corpus normativo consultado |
| EV-09 | O CASE-03 permaneceu bloqueado na FASE 0 pela acumulação elaboração–validação e pela proveniência circular | Existe impacto concreto em projeto real | `GP-PP-00_CASE-03_CONSTITUICAO_DO_PROJETO.md` |
| EV-10 | A GP-RXX concluiu pela possível lacuna e recomendou processo formal | Existe fundamentação investigativa para a abertura | `GP-RXX_PESQUISA_ADEQUACAO_ICFACTORY_PROJETOS_INDIVIDUAIS.md` |

### Limitações das evidências

- O conjunto contém observação direta de um único domínio de aplicação: CASE-03 — PetPass AI.
- Não demonstra recorrência multidomínio.
- Não demonstra estabilidade longitudinal.
- Não demonstra que a ausência seja deliberada ou acidental.
- Não demonstra que eventual tratamento alternativo seja constitucionalmente possível.
- Não contém experimento, implementação ou validação independente.

Origem:

- análise dos artefatos EV-01 a EV-10;
- ICFACTORY — `SCIENTIFIC_MATURITY_MODEL.md`, critérios de evolução por evidência;
- Product Owner — proibição de inferência e limites da GP-EVO-01.

## 5. PRINCÍPIOS CONSTITUCIONAIS ENVOLVIDOS

### Artigo III — A Autoridade Deve Ser Explícita

- Relação: competências de elaboração, validação, aprovação e custódia não podem permanecer implícitas.
- Risco avaliado: autoridade circular ou autodeclarada.

### Artigo IV — O Contexto Deve Ser Explícito

- Relação: o contexto individual do projeto e as condições de exercício da autoridade devem ser observáveis e rastreáveis.
- Risco avaliado: solução baseada em contexto oculto ou informal.

### Artigo V — A Governança Deve Ser Unificada

- Relação: eventual avaliação deve preservar a camada soberana de governança.
- Risco avaliado: criação de governança paralela para projetos individuais.

### Artigo VI — Observadores Não Governam

- Relação: verificação, auditoria e observação produzem conhecimento, não autoridade operacional.
- Risco avaliado: transformar mecanismo evidencial em autoridade de validação.

### Artigo X — Evolução Auditável

- Relação: contribuição, avaliação, decisões, rejeições e eventual evolução devem deixar rastros reconstruíveis.
- Risco avaliado: flexibilização informal sem histórico institucional.

### Artigo XI — Inteligência Não É Autoridade

- Relação: IA pode apoiar pesquisa e verificação, mas não adquire autoridade constitucional.
- Risco avaliado: usar IA como substituta de autoridade humana independente.

Origem:

- ICFACTORY — `CONSTITUTION.md`, Artigos III, IV, V, VI, X e XI.
- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, seção 3.

## 6. AVALIAÇÃO PRELIMINAR DE IMPACTOS

### 6.1 Impacto sobre a Constituição ICFACTORY

- Não foi identificada necessidade demonstrada de alterar a Constituição.
- Os princípios atuais explicam os limites de autoridade, auditabilidade e governança que devem ser preservados.
- A possível lacuna está, nesta etapa, localizada no tratamento normativo de adoção e não comprovada como lacuna dos princípios fundamentais.

Estado:

- avaliação preliminar;
- não constitui decisão sobre documento a alterar.

### 6.2 Impacto sobre a governança documental

- Qualquer tratamento futuro poderia afetar a relação entre elaboração, validação, aprovação, proveniência e vigência.
- O impacto é potencialmente material porque essas relações são requisitos obrigatórios do Project Constitution Template.
- A separação entre verificação e validação deve permanecer explícita.

### 6.3 Impacto sobre a Custódia Metodológica

- Evolução oficial permanece competência da Custódia Metodológica.
- Pesquisa, avaliação e recomendação podem ser preparadas por colaboradores, Research, auditores ou delegados.
- Eventual decisão oficial exige ato custodial com identidade, fundamento, escopo, evidências, revisões, data, vigência e documentos afetados.
- Caso o ocupante da Custódia seja autor primário da proposta ou evidência, revisão independente deve ser documentada antes da decisão.

Origem:

- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, seções 4 a 7 e 11.

### 6.4 Impacto sobre projetos existentes

- Uma eventual evolução pode afetar Constituições de Projeto, papéis, evidências, gates, versões e períodos de vigência.
- Compatibilidade retroativa, transição e preservação da autoridade anterior precisariam ser avaliadas antes de qualquer alteração.

Origem:

- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, “Compatibilidade Retroativa”.

### 6.5 Impacto científico

- A evidência atual é contextual e insuficiente para promoção metodológica ou constitucional.
- Abertura, triagem ou admissão em Research não atribui nível P, E, V ou C automaticamente.
- Não existe promoção tácita.

Origem:

- ICFACTORY — `COMMUNITY_CONTRIBUTION_POLICY.md`.
- ICFACTORY — `SCIENTIFIC_MATURITY_MODEL.md`.
- ICFACTORY — `KNOWLEDGE_EVOLUTION_LIFECYCLE.md`.

## 7. VERIFICAÇÃO PRELIMINAR DE COMPATIBILIDADE

### Resultado

**COMPATÍVEL PARA REGISTRO COMO CONTRIBUIÇÃO EM PRÉ-TRIAGEM.**

Fundamento:

- a política admite contribuição aberta;
- pesquisa e avaliação são atividades preparatórias permitidas;
- o processo preserva as fontes, evidências, limitações e conflitos;
- nenhuma alteração ou promoção foi praticada;
- a autoridade normativa continua pertencendo ao framework e à Custódia Metodológica.

Limite:

- este resultado não declara admissibilidade em Research;
- não atribui maturidade;
- não aprova proposta;
- não substitui triagem ou ato custodial.

## 8. RECOMENDAÇÃO TÉCNICA FUNDAMENTADA

Recomenda-se:

1. submeter este dossiê à triagem institucional prevista na Política Oficial de Contribuição da Comunidade;
2. verificar proveniência, completude, duplicidades, riscos e conflitos;
3. decidir entre admissão em Research, devolução para complemento ou rejeição fundamentada;
4. em caso de admissão, manter separação explícita entre pesquisa, avaliação, maturidade científica e evolução oficial;
5. exigir revisão independente caso o ocupante da Custódia seja autor primário da proposta ou das evidências;
6. manter o método vigente integralmente aplicável até eventual ato oficial posterior.

Esta recomendação:

- não propõe texto normativo;
- não determina documento a alterar;
- não cria papel;
- não cria exceção;
- não define mecanismo compensatório;
- não recomenda promoção;
- não antecipa resultado da triagem.

Origem:

- ICFACTORY — `COMMUNITY_CONTRIBUTION_POLICY.md`, seções 6, 8 e 9.
- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, seções 5, 7 e 13.

## 9. DECISÃO PENDENTE

### DE-GP-EVO-01-001 — Triagem e admissão institucional

- Autoridade requerida: Custódia Metodológica ou responsável de Research formalmente delegado para triagem.
- Decisão requerida:
  - admitir o processo em Research;
  - devolver para complemento; ou
  - rejeitar com fundamento.
- Evidências submetidas:
  - GP-RXX;
  - Constituição do CASE-03;
  - consolidação EV-01 a EV-10;
  - avaliação preliminar deste processo.
- Estado: PENDENTE.
- Efeito da pendência: o processo permanece no estágio Contribuição, sem admissão em Research e sem nível de maturidade.

Fundamento:

- ICFACTORY — `COMMUNITY_CONTRIBUTION_POLICY.md`, “Recepção e triagem”.
- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, “Delegação” e “Fluxo Oficial de Evolução”.

### Nota sobre a autoridade identificada no framework

O `FRAMEWORK_STATE_V1.md` identifica `CM-001`, Henderson Mauricio Batista, como Custodiante vigente. O GP-EVO-01 recebido registra a autorização na qualidade de Product Owner e não contém declaração de ato praticado no papel institucional de Custódia Metodológica, com os elementos formais exigidos para ato custodial.

Por isso:

- a identidade coincidente não foi interpretada como exercício automático da competência custodial;
- nenhuma decisão de triagem foi presumida;
- a decisão DE-GP-EVO-01-001 permanece pendente.

Origem:

- ICFACTORY — `FRAMEWORK_STATE_V1.md`, seção 1.
- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, “Natureza da autoridade” e “Atos oficiais da Custódia”.
- Product Owner — GP-EVO-01, que qualifica a autorização como administrativa e processual.

## 10. SITUAÇÃO NORMATIVA DO FRAMEWORK

- Constituição ICFACTORY: versão 0.2, ATIVA, inalterada.
- Project Constitution Template: versão 0.5, APROVADA, inalterada.
- Constitutional Lexicon: inalterado.
- Governance Architecture: inalterada.
- Governance Baseline v1.0: inalterada.
- Scientific Maturity Model: inalterado.
- Knowledge Evolution Lifecycle: inalterado.
- Methodological Custody Model: inalterado.
- Community Contribution Policy: inalterada.
- Nenhum conceito foi classificado, promovido, regredido ou institucionalizado por esta atividade.

Origem:

- inspeção direta dos documentos oficiais;
- limites expressos do GP-EVO-01.

## 11. DECLARAÇÃO DE NÃO ALTERAÇÃO NORMATIVA

**Nenhuma alteração normativa foi realizada.**

**A Constituição ICFACTORY vigente permanece integralmente inalterada.**

**Os templates oficiais permanecem integralmente inalterados.**

**O método oficial, sua governança, seus níveis de maturidade e seus estados de vigência permanecem inalterados.**

Este processo registra contribuição, evidência, avaliação preliminar e recomendação técnica. Nenhum desses elementos possui efeito de promoção ou institucionalização automática.

Origem:

- Product Owner — GP-EVO-01, “Autorização” e “Critérios de Conformidade”.
- ICFACTORY — `COMMUNITY_CONTRIBUTION_POLICY.md`, “Separação entre Conhecimento e Método”.
- ICFACTORY — `METHODOLOGICAL_CUSTODY_MODEL.md`, “Separação entre Conhecimento e Método”.
