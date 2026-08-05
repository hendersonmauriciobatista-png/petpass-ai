# EP-001 — ESTRUTURA OFICIAL DO REPOSITÓRIO PETPASS AI

## 1. Identificação

- **Atividade:** EP-001
- **Projeto:** CASE-03 — PetPass AI
- **Objeto:** organização oficial do repositório
- **Data:** 04/08/2026
- **Estado:** Definido

## 2. Objetivo

Estabelecer a organização oficial destinada ao versionamento da Engenharia de Produto, Engenharia Técnica, Auditorias, Governança, Base de Conhecimento, workflows n8n, código Python, testes e recursos do PetPass AI.

Esta atividade define a estrutura documental. Não cria fisicamente os diretórios, não move os artefatos existentes e não inicia implementação.

## 3. Fontes obrigatórias

- `ET-GOV-001_CONGELAMENTO_ARQUITETURA_TECNICA.md`.
- `GP-ENG-001_AUDITORIA_PROFICIENCIA_ENGENHARIA_PETPASS_AI.md`.

## 4. Princípios de organização

1. O repositório constitui a fonte única de verdade versionada do PetPass AI.
2. Engenharia, Governança, Auditorias, Conhecimento, Workflows, Código, Testes e Recursos permanecem separados por responsabilidade.
3. A separação do código Python preserva as camadas congeladas na ET-GOV-001.
4. O n8n permanece separado do código Python e restrito à Coordenação e Orquestração.
5. Especificações de workflows permanecem separadas de suas futuras definições executáveis.
6. Artefatos normativos e documentos de governança não se misturam com código ou recursos executáveis.
7. A estrutura não altera a identificação canônica dos documentos existentes.

## 5. Estrutura oficial completa

```text
PetPass AI/
├── docs/
│   ├── engineering/
│   │   ├── product/
│   │   │   ├── constitutions/
│   │   │   ├── requirements/
│   │   │   ├── specifications/
│   │   │   └── deliberations/
│   │   └── technical/
│   │       ├── architecture/
│   │       ├── components/
│   │       ├── data/
│   │       ├── flows/
│   │       ├── implementation-plans/
│   │       ├── workflow-specifications/
│   │       └── quality/
│   ├── audits/
│   │   ├── product/
│   │   ├── technical/
│   │   ├── methodological/
│   │   └── implementation-readiness/
│   ├── governance/
│   │   ├── project/
│   │   ├── technical-baselines/
│   │   ├── decisions/
│   │   └── experimental/
│   └── knowledge/
│       ├── discoveries/
│       └── lessons-learned/
├── workflows/
│   └── n8n/
│       ├── definitions/
│       ├── configurations/
│       └── verification-evidence/
├── src/
│   └── petpass_ai/
│       ├── presentation/
│       ├── domain/
│       ├── official_registry/
│       └── integration/
├── tests/
│   ├── presentation/
│   ├── domain/
│   ├── official_registry/
│   ├── integration/
│   └── workflows/
└── resources/
    ├── visual/
    │   ├── logos/
    │   ├── reference-models/
    │   └── placeholders/
    ├── pet-images/
    └── styles/
```

## 6. Finalidade dos diretórios

### 6.1 `docs/`

Diretório exclusivo para documentos versionados do projeto. Não contém código executável, workflows executáveis ou recursos binários de operação.

### 6.2 `docs/engineering/product/`

Armazena a Engenharia de Produto e suas fontes documentais.

| Diretório | Finalidade |
|---|---|
| `constitutions/` | Constituições e documentos de definição inicial do produto. |
| `requirements/` | Fonte primária, matrizes de requisitos e documentos de rastreabilidade do MVP. |
| `specifications/` | Especificações funcionais aprovadas. |
| `deliberations/` | Documentos DP-PP que materializam decisões normativas do Product Owner. |

### 6.3 `docs/engineering/technical/`

Armazena os artefatos que compõem ou detalham a Engenharia Técnica congelada.

| Diretório | Finalidade |
|---|---|
| `architecture/` | Arquitetura Conceitual, Arquitetura Tecnológica e suas complementações. |
| `components/` | Identificação e organização dos componentes técnicos. |
| `data/` | Modelos Conceitual e Lógico de Dados. |
| `flows/` | Fluxos Técnicos conceituais FT-01 a FT-06. |
| `implementation-plans/` | Plano oficial e ordenação das fases de implementação. |
| `workflow-specifications/` | Especificações documentais de implementação de cada workflow, incluindo WF-FT-01. |
| `quality/` | Tratamentos de exceções e demais documentos técnicos de qualidade. |

### 6.4 `docs/audits/`

Armazena documentos verificatórios. Auditorias registram evidências e classificações, sem substituir os artefatos auditados.

| Diretório | Finalidade |
|---|---|
| `product/` | Auditorias de requisitos, deliberações e cobertura da Engenharia de Produto. |
| `technical/` | Auditorias de consistência ou cobertura da Engenharia Técnica. |
| `methodological/` | Auditorias e relatórios restritos ao comportamento metodológico do CASE-03. |
| `implementation-readiness/` | Revisões de prontidão, incluindo WF-FT-01-REV e auditorias de proficiência para transição. |

### 6.5 `docs/governance/`

Armazena documentos responsáveis por autoridade, estado, baseline e controle institucional do projeto.

| Diretório | Finalidade |
|---|---|
| `project/` | Constituição, regime operacional e documentos de governança geral do CASE-03. |
| `technical-baselines/` | Congelamentos e declarações oficiais de baseline, incluindo ET-GOV-001. |
| `decisions/` | Deliberações de governança que não pertencem às deliberações funcionais DP-PP. |
| `experimental/` | Governança e controle dos artefatos classificados como EXPERIMENTAL ou EM VALIDAÇÃO. |

### 6.6 `docs/knowledge/`

Armazena conhecimento observável produzido durante o projeto sem conferir caráter normativo automático ao seu conteúdo.

| Diretório | Finalidade |
|---|---|
| `discoveries/` | Descobertas documentais, técnicas ou experimentais registradas durante o projeto. |
| `lessons-learned/` | Lições aprendidas sustentadas pelo corpus, incluindo os artefatos KL e GP-ICF correspondentes. |

### 6.7 `workflows/n8n/`

Armazena exclusivamente os futuros artefatos executáveis e evidências dos workflows coordenados pelo n8n. As especificações permanecem em `docs/engineering/technical/workflow-specifications/`.

| Diretório | Finalidade |
|---|---|
| `definitions/` | Definições versionadas dos workflows n8n autorizados. |
| `configurations/` | Configurações versionáveis dos workflows que não constituam credenciais ou segredos. |
| `verification-evidence/` | Evidências produzidas pela verificação técnica dos workflows. |

Credenciais, chaves e segredos não pertencem ao conteúdo versionado desses diretórios.

### 6.8 `src/petpass_ai/`

Armazena o futuro código Python do produto, separado conforme as responsabilidades arquiteturais congeladas.

| Diretório | Correspondência arquitetural | Finalidade |
|---|---|---|
| `presentation/` | CA-01 | Código Python/PySide6 responsável exclusivamente por apresentação e interação. |
| `domain/` | CA-03 | Código Python responsável exclusivamente pelas regras documentadas do domínio. |
| `official_registry/` | CA-04 | Código Python responsável pelo acesso encapsulado ao Registro Oficial SQLite. |
| `integration/` | Relação entre CA-01, CA-02, CA-03 e CA-04 | Código de integração HTTP/JSON sem absorver responsabilidades de domínio, apresentação, coordenação ou registro. |

Não existe diretório Python próprio para CA-02, pois a tecnologia oficial de Coordenação é o n8n. CA-05 não recebe diretório de implementação enquanto sua tecnologia permanecer não determinada.

### 6.9 `tests/`

Armazena os futuros testes e suas evidências executáveis, organizados pelo objeto arquitetural verificado.

| Diretório | Finalidade |
|---|---|
| `presentation/` | Testes da responsabilidade de CA-01. |
| `domain/` | Testes das regras e resultados de CA-03. |
| `official_registry/` | Testes da manutenção e disponibilidade do Registro Oficial em CA-04. |
| `integration/` | Testes das relações HTTP/JSON autorizadas entre as camadas. |
| `workflows/` | Testes das sequências coordenadas pelos workflows n8n. |

A estrutura não define ferramentas, bibliotecas, cenários ou código de teste.

### 6.10 `resources/`

Armazena recursos não executáveis utilizados pelo produto, preservando a origem e a identidade visual documentadas.

| Diretório | Finalidade |
|---|---|
| `visual/logos/` | Logotipos institucionais aprovados. |
| `visual/reference-models/` | Modelos visuais oficiais utilizados como referência. |
| `visual/placeholders/` | Placeholders institucionais aprovados. |
| `pet-images/` | Fotografias de pet utilizadas exclusivamente conforme as regras documentadas; dados reais não são presumidos como conteúdo versionável. |
| `styles/` | Recursos visuais derivados das decisões oficiais, sem definir tecnologia de implementação adicional. |

## 7. Organização dos artefatos existentes por classe

| Classe documental | Destino oficial |
|---|---|
| Constituição e definição inicial GP-PP | `docs/engineering/product/constitutions/` |
| Fonte, matrizes e rastreabilidade de requisitos | `docs/engineering/product/requirements/` |
| Especificações funcionais | `docs/engineering/product/specifications/` |
| DP-PP | `docs/engineering/product/deliberations/` |
| ET-AR | `docs/engineering/technical/architecture/` |
| ET-CP | `docs/engineering/technical/components/` |
| ET-DD | `docs/engineering/technical/data/` |
| ET-IF | `docs/engineering/technical/flows/` |
| ET-IM | `docs/engineering/technical/implementation-plans/` |
| WF-FT em forma de especificação | `docs/engineering/technical/workflow-specifications/` |
| ET-QA | `docs/engineering/technical/quality/` |
| ET-GOV | `docs/governance/technical-baselines/` |
| GP-PP de natureza auditável | Subdiretório aplicável de `docs/audits/` |
| GP-ENG e revisões de prontidão | `docs/audits/implementation-readiness/` |
| ICF-EXP e pesquisas experimentais | `docs/governance/experimental/` ou `docs/knowledge/discoveries/`, conforme sua classificação documental vigente |
| KL e lições consolidadas | `docs/knowledge/lessons-learned/` |
| AV-PP aprovados | Subdiretório correspondente de `resources/visual/` |

Esta tabela determina destino organizacional. Nenhum arquivo é movido por esta atividade.

## 8. Limites da estrutura

- Não define infraestrutura, implantação, integração contínua ou hospedagem.
- Não cria código Python, workflow n8n ou teste.
- Não define estrutura física do SQLite.
- Não define tecnologia da CA-05.
- Não autoriza versionamento de credenciais, chaves, segredos ou dados pessoais reais.
- Não altera nomes, conteúdo, classificação ou autoridade dos documentos existentes.
- Não inicia a fase de implementação.

## 9. Resumo executivo

A estrutura oficial separa documentos, workflows, código, testes e recursos. A Engenharia de Produto e a Engenharia Técnica possuem subdivisões próprias; Auditorias, Governança e Conhecimento permanecem independentes. O código Python reflete CA-01, CA-03 e CA-04, enquanto a Coordenação permanece em `workflows/n8n/`. A definição estabelece organização e rastreabilidade sem realizar migração física ou iniciar desenvolvimento.

## 10. Declaração de conformidade metodológica

A EP-001 foi produzida exclusivamente a partir de ET-GOV-001 e GP-ENG-001. Nenhum código, workflow, infraestrutura, teste ou diretório físico foi criado; nenhum documento existente foi alterado ou movido; nenhuma implementação foi iniciada e nenhuma atividade posterior foi iniciada.
