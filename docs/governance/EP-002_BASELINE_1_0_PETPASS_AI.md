# EP-002 — BASELINE OFICIAL 1.0 DO PETPASS AI

## 1. Identificação

- **Atividade:** EP-002
- **Projeto:** CASE-03 — PetPass AI
- **Baseline:** 1.0
- **Data da consolidação:** 04/08/2026
- **Natureza:** manifesto documental de configuração
- **Classificação final:** A — Baseline 1.0 pronta para publicação

## 2. Objetivo

Consolidar os artefatos aprovados que formam a primeira versão oficial da documentação do PetPass AI, definir sua localização na estrutura da EP-001 e separar a baseline vigente das evidências históricas e dos materiais não integrantes.

Esta atividade não cria fisicamente a estrutura, não move arquivos, não publica a baseline e não inicia implementação.

## 3. Fontes obrigatórias

- `GP-ENG-001_AUDITORIA_PROFICIENCIA_ENGENHARIA_PETPASS_AI.md`.
- `ET-GOV-001_CONGELAMENTO_ARQUITETURA_TECNICA.md`.
- `EP-001_ESTRUTURA_REPOSITORIO_PETPASS_AI.md`.
- Documentos aprovados da Engenharia de Produto identificados neste manifesto.
- Documentos aprovados da Engenharia Técnica identificados neste manifesto.

## 4. Critério de composição

Integram a Baseline 1.0 somente artefatos que, no corpus vigente:

1. definem a fonte, o escopo, as regras ou a especificação da Engenharia de Produto;
2. materializam deliberações normativas vigentes do Product Owner;
3. definem a Engenharia Técnica congelada ou complementam suas condições de qualidade;
4. estabelecem a governança da baseline, a proficiência da engenharia ou a organização oficial do repositório;
5. constituem referências visuais aprovadas necessárias ao produto.

Auditorias intermediárias, pesquisas, investigações, rascunhos controlados, artefatos experimentais históricos e implementações anteriores não são promovidos à baseline por esta consolidação.

## 5. Artefatos integrantes da Baseline 1.0

### 5.1 Governança e configuração da baseline

| Artefato | Destino oficial segundo EP-001 | Função na baseline |
|---|---|---|
| `GP-ENG-001_AUDITORIA_PROFICIENCIA_ENGENHARIA_PETPASS_AI.md` | `docs/audits/implementation-readiness/` | Evidência de proficiência documental e condição de transição controlada. |
| `ET-GOV-001_CONGELAMENTO_ARQUITETURA_TECNICA.md` | `docs/governance/technical-baselines/` | Congelamento da Arquitetura Técnica. |
| `EP-001_ESTRUTURA_REPOSITORIO_PETPASS_AI.md` | `docs/governance/project/` | Estrutura oficial do repositório. |
| `EP-002_BASELINE_1_0_PETPASS_AI.md` | `docs/governance/technical-baselines/` | Manifesto da Baseline 1.0. |

### 5.2 Engenharia de Produto — constituição, origem, requisitos e especificação

| Artefato | Destino oficial segundo EP-001 | Função na baseline |
|---|---|---|
| `GP-PP-01_CONSTITUICAO_TECNICA_INICIAL_PETPASS_AI.md` | `docs/engineering/product/constitutions/` | Fundamentos técnicos iniciais do produto. |
| `GP-PP-09A_FONTE_PRIMARIA_REQUISITOS_PETPASS_AI.md` | `docs/engineering/product/requirements/` | Fonte primária dos requisitos. |
| `GP-PP-09B_MATRIZ_RASTREABILIDADE_REQUISITOS_MVP.md` | `docs/engineering/product/requirements/` | Rastreabilidade dos requisitos do MVP. |
| `GP-PP-09C_ESPECIFICACAO_FUNCIONAL_MVP.md` | `docs/engineering/product/specifications/` | Especificação funcional do MVP. |
| `GP-PP-09D_CONSOLIDADO_DELIBERACOES_PRODUCT_OWNER_MVP.md` | `docs/engineering/product/deliberations/` | Consolidado normativo das deliberações DP-PP-001 a DP-PP-005. |
| `ES-UI-001_ESPECIFICACAO_EXECUTAVEL_FICHA_EMERGENCIA.md` | `docs/engineering/product/specifications/` | Especificação documental da interface aprovada, complementada pelas decisões posteriores. |

### 5.3 Engenharia de Produto — deliberações normativas

| Artefato | Destino oficial segundo EP-001 |
|---|---|
| `DP-PP-001_CAMPOS_CADASTRO_PET.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-002_CAMPOS_OBRIGATORIOS_OPCIONAIS_CADASTRO_PET.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-003_REGRAS_VALIDACAO_CADASTRO_PET.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-004_TRATAMENTO_FALHAS_CADASTRO_PET.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-005_CRITERIOS_SUCESSO_CADASTRO_PET.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-006_IDENTIFICADOR_DIGITAL_KEY_PASS.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-007_REPRESENTACAO_GRAFICA_QR_CODE.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-008_IDENTIDADE_VISUAL_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-009_PARAMETROS_TECNICOS_INTERFACE_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-010_COMPORTAMENTO_INSTITUCIONAL_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-011_COMPORTAMENTO_FOTOGRAFIA_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-012_APRESENTACAO_CONTEUDO_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-013_ORIGEM_DADOS_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-014_COMPONENTE_QRCODE_FICHA_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |
| `DP-PP-015_COMPORTAMENTO_ACIONAMENTO_TELEFONE_EMERGENCIA.md` | `docs/engineering/product/deliberations/` |

### 5.4 Recursos visuais aprovados

| Artefato | Destino oficial segundo EP-001 | Função na baseline |
|---|---|---|
| `AV-PP-001_LOGOTIPO_OFICIAL_PROPOSTA_2.png` | `resources/visual/logos/` | Logotipo oficial aprovado. |
| `AV-PP-002_MODELO_4_FICHA_EMERGENCIA.png` | `resources/visual/reference-models/` | Referência visual oficial da Ficha de Emergência. |
| `AV-PP-003_REGISTRO_ARTEFATOS_VISUAIS_APROVADOS.md` | `docs/engineering/product/specifications/` | Registro e rastreabilidade dos artefatos visuais aprovados. |

### 5.5 Engenharia Técnica congelada

| Artefato | Destino oficial segundo EP-001 | Função na baseline |
|---|---|---|
| `ET-AR-001_ARQUITETURA_CONCEITUAL_PETPASS_AI.md` | `docs/engineering/technical/architecture/` | Camadas, relações e limites conceituais. |
| `ET-AR-002_ARQUITETURA_TECNOLOGICA_PETPASS_AI.md` | `docs/engineering/technical/architecture/` | Tecnologia de Coordenação e mapeamento inicial dos workflows. |
| `ET-AR-003_COMPLEMENTACAO_ARQUITETURA_TECNOLOGICA.md` | `docs/engineering/technical/architecture/` | Tecnologias complementares necessárias ao WF-FT-01. |
| `ET-CP-001_COMPONENTES_TECNICOS_PETPASS_AI.md` | `docs/engineering/technical/components/` | Dezessete componentes organizados por camada. |
| `ET-DD-001_MODELO_CONCEITUAL_DADOS_PETPASS_AI.md` | `docs/engineering/technical/data/` | Oito entidades conceituais. |
| `ET-DD-002_MODELO_LOGICO_DADOS_PETPASS_AI.md` | `docs/engineering/technical/data/` | Treze relações e três agrupamentos lógicos. |
| `ET-IF-001_FLUXOS_TECNICOS_PETPASS_AI.md` | `docs/engineering/technical/flows/` | Seis fluxos técnicos. |
| `ET-IM-001_PLANO_IMPLEMENTACAO_ENGENHARIA_TECNICA.md` | `docs/engineering/technical/implementation-plans/` | Quatro fases e ordem oficial da implementação. |
| `WF-FT-01_ESPECIFICACAO_IMPLEMENTACAO_CADASTRO_VALIDO_PET.md` | `docs/engineering/technical/workflow-specifications/` | Especificação do primeiro workflow. |
| `ET-QA-001_TRATAMENTO_EXCECOES_WF_FT_01.md` | `docs/engineering/technical/quality/` | Tratamento conceitual das três exceções do WF-FT-01. |

### 5.6 Consolidação quantitativa

| Grupo | Quantidade de artefatos |
|---|---:|
| Governança e configuração, incluindo este manifesto | 4 |
| Produto — constituição, origem, requisitos e especificação | 6 |
| Produto — deliberações normativas | 15 |
| Recursos visuais aprovados | 3 |
| Engenharia Técnica congelada e qualidade | 10 |
| **Total da Baseline 1.0** | **38** |

## 6. Artefatos históricos mantidos apenas como evidência

Os seguintes grupos permanecem versionáveis como evidência histórica, mas não definem a configuração vigente da Baseline 1.0:

### 6.1 Constituição e governança anteriores

- `GP-PP-00_CASE-03_CONSTITUICAO_DO_PROJETO.md` — Rascunho Controlado, não promovido à configuração vigente.
- `DE-CASE03-001_REGIME_OPERACIONAL_EXPERIMENTAL.md`.
- `DE-GP-EVO-01-002_ENCERRAMENTO_INVESTIGACAO_DOCUMENTAL.md`.
- `DO-CASE03-001_PLANO_GOVERNANCA_EXPERIMENTAL_PETPASS_AI.md`.

### 6.2 Auditorias e diagnósticos intermediários da Engenharia de Produto

- GP-PP-11, GP-PP-12, GP-PP-13, GP-PP-14, GP-PP-15, GP-PP-17, GP-PP-18, GP-PP-19, GP-PP-20 e GP-PP-21.

Esses documentos preservam a cadeia de diagnóstico e encerramento, mas não substituem as deliberações e especificações vigentes incluídas na baseline.

### 6.3 Pesquisa e evolução experimental do Framework

- `GP-RXX_PESQUISA_ADEQUACAO_ICFACTORY_PROJETOS_INDIVIDUAIS.md`.
- Documentos GP-EVO-01, GP-EVO-01A e fases experimentais correspondentes.
- ICF-EXP-001 a ICF-EXP-005.
- `GP-ICF-001_LICOES_APRENDIDAS_CASE03.md`.
- `GP-ICF-002_RELATORIO_ENCERRAMENTO_METODOLOGICO_CASE03.md`.
- `KL-001_LICAO_APRENDIDA_GOVERNANCA_PROJETOS_INDIVIDUAIS.md`.

Esses artefatos permanecem como pesquisa, governança experimental ou conhecimento histórico e não alteram a baseline normativa do produto.

### 6.4 Revisão anterior à complementação tecnológica

- `WF-FT-01-REV_PRONTIDAO_IMPLEMENTACAO.md`.

A revisão permanece como evidência histórica do impedimento então existente. ET-AR-003 e ET-QA-001 foram produzidos posteriormente e integram a configuração vigente.

## 7. Artefatos que não integram a Baseline 1.0

| Artefato ou grupo | Motivo documental da exclusão |
|---|---|
| `main.py` | Código existente; a Baseline 1.0 antecede o início autorizado da implementação arquitetural congelada. |
| `openai_service.py` | Código de integração anterior; não integra a configuração documental consolidada. |
| `requirements.txt` | Dependências executáveis anteriores; não integra a baseline documental. |
| `AV-PP-002_MODELO_4_FICHA_EMERGENCIA_CAO_REAL.png` | Variante não identificada no manifesto de artefatos visuais aprovados AV-PP-003. |
| `.icfactory-framework-reference/` | Referência local externa ao patrimônio específico do PetPass AI. |
| Definições executáveis de workflows n8n | Ainda não produzidas e implementação não iniciada. |
| Banco SQLite físico | Ainda não produzido e estrutura física fora da baseline documental. |
| Testes executáveis | Ainda não produzidos. |
| Credenciais, chaves e segredos | Não pertencem ao conteúdo versionável do repositório. |

A exclusão não apaga, modifica ou reclassifica o artefato; apenas registra que ele não compõe a Baseline 1.0.

## 8. Estado documental da Engenharia

- **Engenharia de Produto:** documentalmente concluída, conforme GP-ENG-001 e cadeia GP-PP/DP-PP vigente.
- **Engenharia Técnica:** consistente e congelada, conforme ET-GOV-001.
- **Arquitetura Tecnológica necessária ao WF-FT-01:** definida por ET-AR-002 e ET-AR-003.
- **Exceções técnicas do WF-FT-01:** tratadas documentalmente por ET-QA-001.
- **Proficiência:** A — Engenharia documentalmente proficiente, conforme GP-ENG-001.

## 9. Estado documental da Implementação

- **Estado:** não iniciada dentro da baseline arquitetural congelada.
- Não existem workflows n8n executáveis integrantes da Baseline 1.0.
- Não existe código Python autorizado como entrega da fase de implementação integrante da Baseline 1.0.
- Não existem testes executáveis integrantes da Baseline 1.0.
- A publicação desta baseline não constitui autorização para implementar.

## 10. Critérios para publicação da Baseline 1.0

A Baseline 1.0 estará apta à publicação física quando forem atendidos cumulativamente:

1. aprovação formal deste manifesto pelo Product Owner;
2. criação física da estrutura definida pela EP-001;
3. posicionamento dos 38 artefatos integrantes nos destinos definidos neste documento;
4. preservação integral dos nomes e conteúdos dos artefatos de origem;
5. verificação de presença e legibilidade de todos os integrantes;
6. separação dos artefatos históricos e dos itens excluídos;
7. registro versionado e identificável da configuração como Baseline 1.0;
8. ausência de código, workflow, infraestrutura, segredo ou implementação não autorizada na publicação.

Todos os 37 artefatos preexistentes selecionados para a baseline foram localizados no workspace. O trigésimo oitavo artefato é este próprio manifesto. A criação física e a publicação permanecem atividades posteriores não iniciadas.

## 11. Classificação final

**A — Baseline 1.0 pronta para publicação.**

Fundamentação documental:

- GP-ENG-001 classifica a Engenharia como documentalmente proficiente.
- ET-GOV-001 congela a Arquitetura Técnica.
- EP-001 define os destinos oficiais.
- Os 37 artefatos preexistentes integrantes foram localizados.
- Este manifesto completa a identificação da configuração com 38 artefatos.

A classificação “pronta para publicação” não significa “publicada” e não autoriza implementação.

## 12. Resumo executivo

A Baseline 1.0 consolida 38 artefatos: quatro de governança e configuração, seis de constituição/requisitos/especificação, 15 deliberações normativas, três recursos visuais e dez artefatos da Engenharia Técnica e Qualidade. Auditorias intermediárias, pesquisas e revisões superadas permanecem como evidência histórica. Código anterior, variante visual não registrada, referência externa, workflows, banco físico e testes não integram a baseline. A configuração está documentalmente pronta para publicação física, condicionada à aprovação do Product Owner e aos critérios desta consolidação.

## 13. Declaração de conformidade metodológica

A EP-002 realizou exclusivamente a consolidação documental da Baseline 1.0. Nenhum artefato existente foi alterado, movido, promovido por inferência ou implementado. Nenhum requisito, deliberação, arquitetura, componente, modelo, fluxo ou workflow foi criado ou modificado. A estrutura física não foi criada, a baseline não foi publicada e nenhuma atividade posterior foi iniciada.
