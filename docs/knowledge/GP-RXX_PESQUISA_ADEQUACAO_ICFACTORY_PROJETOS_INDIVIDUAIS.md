# GP-RXX — PESQUISA ARQUITETURAL

## Adequação do ICFACTORY para Projetos Individuais

## 1. CONTROLE DA PESQUISA

- Natureza: exclusivamente investigativa.
  - Origem: Product Owner — GP-RXX, “IMPORTANTE”.
- Objeto: aplicabilidade da Constituição e dos mecanismos de governança do ICFACTORY a projetos conduzidos por um único Product Owner.
  - Origem: Product Owner — GP-RXX, “Objetivo”.
- Escopo documental: Constituição vigente e documentos normativos oficiais.
  - Origem: Product Owner — GP-RXX, “LIMITES DA PESQUISA”.
- Commit do repositório oficial consultado: `eb64ad1031819c814934e52091d4a7eda0be9a3b`.
  - Origem: inspeção direta da referência `main` do repositório `hendersonmauriciobatista-png/icfactory-framework`.
- Alterações normativas realizadas: nenhuma.
  - Origem: limite da pesquisa e verificação desta execução.
- Alterações no CASE-03 realizadas por esta pesquisa: nenhuma.
  - Origem: limite da pesquisa e verificação desta execução.

## 2. CORPUS DOCUMENTAL

### 2.1 Documentos normativos principais

1. `CONSTITUTION.md`
   - Versão: 0.2.
   - Status: ATIVA.
   - Função: princípios fundamentais e não negociáveis do ICFACTORY.
2. `governance/GOVERNANCE_ARCHITECTURE.md`
   - Versão: 1.0.
   - Status: FUNDACIONAL.
   - Função: hierarquia entre Constituição ICFACTORY, Constituição do Projeto, ALO e sistema.
3. `governance/PROJECT_CONSTITUTION_TEMPLATE.md`
   - Versão: 0.5.
   - Status: APROVADA.
   - Função: baseline oficial para criação e governança documental de Constituições de Projeto.
4. `CONSTITUTIONAL_LEXICON.md`
   - Função: referência semântica oficial dos conceitos constitucionais.
5. `docs/governance/FRAMEWORK_STATE_V1.md`
   - Status: estado institucional oficial da Governance Baseline v1.0.
   - Função: identificação do corpus normativo vigente e da autoridade metodológica oficial.

### 2.2 Regra de autoridade documental

O `DOCUMENT_MAP.md` classifica:

- `CONSTITUTION.md` como documento normativo dos princípios fundamentais;
- `PROJECT_CONSTITUTION_TEMPLATE.md` como template normativo para adoção em projetos;
- `GOVERNANCE_ARCHITECTURE.md` como documento da hierarquia e do fluxo de autoridade;
- `PROJECT_CONSTITUTION_ALFA_DRAFT.md` apenas como exemplo não aprovado para uso operacional.

O exemplo alfa não foi utilizado como fonte normativa.

## 3. INTERPRETAÇÃO FUNDAMENTADA

### 3.1 Alcance da Constituição ICFACTORY

A Constituição v0.2 estabelece princípios universais relacionados a:

- infraestrutura;
- observação anterior à intervenção;
- autoridade explícita;
- contexto explícito;
- governança unificada;
- separação entre observação e governo;
- explicabilidade;
- investigação de causa-raiz;
- especialização coordenada;
- evolução auditável;
- separação entre inteligência e autoridade.

Ela não declara:

- quantidade mínima de participantes humanos;
- obrigatoriedade de ambiente multiusuário;
- categoria específica de “projeto individual”;
- exceção ou rito alternativo para projetos conduzidos por uma única pessoa;
- mecanismo compensatório para autovalidação.

Evidência:

- ICFACTORY — `CONSTITUTION.md`, Preâmbulo, Artigos I a XI e Disposição Fundadora.

### 3.2 Alcance do Project Constitution Template

O template aprovado impõe requisitos materiais a qualquer Constituição de Projeto:

- autoridades identificadas;
- validação constitucional compatível;
- aprovação explícita;
- identidade inequívoca do conteúdo integral aprovado;
- proveniência verificável das competências;
- vigência somente após atendimento dos requisitos materiais.

O template permite acumulação de funções, mas condiciona essa acumulação:

- cada papel acumulado deve possuir proveniência verificável;
- a proveniência de um papel não presume competência para outro;
- a acumulação não pode eliminar a validação constitucional;
- a autoridade de validação não pode validar ato ou conteúdo de sua própria autoria;
- nenhuma autoridade pode instituir ou designar a própria competência por simples declaração, interpretação ou registro.

Consequência documental:

- elaboração, aprovação e custódia não são declaradas absolutamente incompatíveis com acumulação;
- elaboração e validação do mesmo conteúdo pela mesma autoridade são expressamente incompatíveis;
- um único Product Owner que seja simultaneamente autor e única autoridade disponível não consegue produzir sozinho a validação constitucional exigida para vigência;
- a autodeclaração de competência não supre a proveniência exigida.

Evidência:

- ICFACTORY — `governance/PROJECT_CONSTITUTION_TEMPLATE.md`, “GOVERNANÇA DOCUMENTAL”, “AUTORIDADES CONSTITUCIONAIS” e “APROVAÇÃO E VIGÊNCIA”.

### 3.3 Distinção entre verificação e validação

O framework separa Verificação de Conformidade de Validação Constitucional:

- verificação examina evidências e pode concluir conformidade, não conformidade ou indeterminação;
- verificação não constitui nem substitui validação constitucional;
- validação exige autoridade competente e resultado explícito.

Consequência:

- uma revisão documental, checklist, auditoria automatizada ou verificação executada durante a pesquisa não adquire, apenas por sua qualidade evidencial, o efeito jurídico-documental de validação constitucional;
- inteligência ou automação não adquire autoridade de validação por produzir análise.

Evidência:

- ICFACTORY — `governance/PROJECT_CONSTITUTION_TEMPLATE.md`, “CONFORMIDADE E REMEDIAÇÃO CONSTITUCIONAL”, “Separação Funcional”.
- ICFACTORY — `CONSTITUTIONAL_LEXICON.md`, TUX-41 e TUX-67.
- ICFACTORY — `CONSTITUTION.md`, Artigo XI.

## 4. RESPOSTAS ÀS PERGUNTAS DE PESQUISA

### 4.1 A segregação de funções é obrigatória para qualquer categoria de projeto?

Resposta:

- A segregação absoluta de todas as funções não é exigida.
- O template admite expressamente acumulação de funções.
- A separação entre autoria e validação do mesmo conteúdo é obrigatória.
- A validação constitucional não pode ser eliminada pela acumulação.
- As regras não apresentam distinção por categoria, natureza, porte ou número de participantes do projeto.

Fundamento:

- ICFACTORY — `PROJECT_CONSTITUTION_TEMPLATE.md`, regras obrigatórias de proveniência e relacionamento entre autoridades.

### 4.2 A Constituição pressupõe obrigatoriamente ambiente multiusuário?

Resposta:

- A Constituição v0.2 não contém pressuposto textual explícito de ambiente multiusuário.
- O template, entretanto, produz necessidade funcional de autoridade distinta do autor para validar o mesmo conteúdo.
- Essa necessidade funcional não equivale a uma declaração constitucional de que todo projeto deve ser multiusuário.

Fundamento:

- ausência de disposição correspondente em `CONSTITUTION.md`;
- proibição expressa de autovalidação em `PROJECT_CONSTITUTION_TEMPLATE.md`.

### 4.3 Existe previsão normativa para projetos individuais?

Resposta:

- Não foi localizada previsão normativa específica para projetos individuais no corpus consultado.
- Também não foi localizada exclusão explícita desses projetos.
- Não existe rito alternativo, perfil constitucional específico ou mecanismo compensatório normativo identificado para o caso em que uma única pessoa concentra autoria e toda autoridade disponível.

Fundamento:

- pesquisa textual e análise integral dos documentos listados na seção 2.

### 4.4 A ausência representa decisão arquitetural ou lacuna normativa?

Resposta:

- A independência entre autoria e validação é uma decisão normativa explícita do template.
- A ausência de tratamento específico para adoção por uma única pessoa não é classificada pelos documentos como decisão arquitetural deliberada.
- Também não existe registro normativo que classifique formalmente essa ausência como lacuna.
- Diante da combinação entre aplicabilidade geral do template, proibição de autovalidação e ausência de rito para projetos individuais, existe evidência de possível lacuna normativa de adoção.

Limite da conclusão:

- “Possível lacuna normativa” é resultado investigativo.
- Não constitui alteração, exceção, flexibilização nem promoção automática ao patrimônio normativo.

### 4.5 Quais princípios constitucionais motivam a segregação?

Princípios diretamente relacionados:

- Artigo III — A Autoridade Deve Ser Explícita.
  - Relação: exige origem identificável e impede autoridade crítica implícita.
- Artigo VI — Observadores Não Governam.
  - Relação: separa produção de conhecimento de autoridade operacional.
- Artigo XI — Inteligência Não É Autoridade.
  - Relação: capacidade de interpretar ou recomendar não confere autoridade.
- Artigo V — A Governança Deve Ser Unificada.
  - Relação: impede estruturas paralelas de autoridade e preserva camada soberana.
- Artigo X — Evolução Auditável.
  - Relação: exige rastros observáveis das mudanças significativas.
- Artigo IV — O Contexto Deve Ser Explícito.
  - Relação: exige que o contexto das decisões seja observável e rastreável.

Qualificação:

- A regra concreta de não autovalidação está no template, não no texto literal dos Artigos III, VI ou XI.
- A relação acima é uma interpretação sistemática entre os princípios constitucionais e a regra normativa do template.

### 4.6 Existem mecanismos compensatórios vigentes?

Resposta:

- Não foi identificado mecanismo compensatório vigente que autorize a mesma autoridade a elaborar e validar o mesmo conteúdo.
- Proveniência, registro, custódia, verificação de integridade, verificação de conformidade e evidência preservam auditabilidade, mas não substituem validação constitucional.
- Aprovação também não substitui validação.
- IA, automação ou observadores podem produzir conhecimento e evidência, mas não recebem autoridade por essa capacidade.

Fundamento:

- ICFACTORY — `PROJECT_CONSTITUTION_TEMPLATE.md`, regras de relacionamento entre autoridades, “APROVAÇÃO E VIGÊNCIA” e “Separação Funcional”.
- ICFACTORY — `CONSTITUTIONAL_LEXICON.md`, TUX-41, TUX-45, TUX-67 e TUX-68.
- ICFACTORY — `CONSTITUTION.md`, Artigos VI e XI.

### 4.7 Um perfil constitucional futuro para projetos individuais violaria princípios fundamentais?

Resposta:

- A mera existência futura de um perfil específico não é proibida textualmente pela Constituição vigente.
- Sua compatibilidade dependeria do conteúdo e do processo formal de evolução.
- Um perfil que tornasse autoridade implícita, atribuísse autoridade à inteligência, eliminasse auditabilidade ou permitisse autovalidação em conflito com a baseline vigente seria incompatível com as normas atuais.
- A pesquisa não determina formato, mecanismo, papel, exceção ou proposta para esse eventual perfil.

Fundamento:

- ICFACTORY — `CONSTITUTION.md`, Artigos III, VI, X e XI.
- ICFACTORY — `GOVERNANCE_ARCHITECTURE.md`, princípio de subordinação à Constituição ICFACTORY.
- ICFACTORY — `PROJECT_CONSTITUTION_TEMPLATE.md`, compatibilidade obrigatória e regras de autoridade.

## 5. EVIDÊNCIAS DOCUMENTAIS

| Evidência | Resultado sustentado | Fonte |
|---|---|---|
| A Constituição contém onze princípios e não diferencia projetos por quantidade de participantes | Ausência de pressuposto multiusuário explícito | `CONSTITUTION.md` |
| Toda Constituição de Projeto permanece subordinada à Constituição ICFACTORY | Perfil futuro não poderia contrariar princípios superiores | `GOVERNANCE_ARCHITECTURE.md`; `PROJECT_CONSTITUTION_TEMPLATE.md` |
| Acumulação de funções é admitida sob condições | Não existe segregação absoluta de todos os papéis | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| Validador não pode validar conteúdo de sua autoria | Separação autoria–validação é obrigatória | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| Autoridade não pode autodesignar competência | Product Owner único não supre proveniência por declaração própria | `PROJECT_CONSTITUTION_TEMPLATE.md` |
| Verificação não substitui validação | Controles compensatórios evidenciais não resolvem o ato constitucional | `PROJECT_CONSTITUTION_TEMPLATE.md`; `CONSTITUTIONAL_LEXICON.md` |
| Inteligência não é autoridade | IA não pode ser presumida como validadora constitucional | `CONSTITUTION.md`, Artigo XI |
| Nenhuma regra específica para projeto individual foi localizada | Possível lacuna normativa de adoção | Corpus listado na seção 2 |

## 6. POSSÍVEL LACUNA IDENTIFICADA

### PL-01 — Adoção por autoridade humana única

Descrição:

- O framework estabelece requisitos gerais de validação e proveniência.
- O framework admite acumulação de funções, mas proíbe autovalidação.
- O corpus não define tratamento específico para projeto conduzido por uma única pessoa nem mecanismo normativo alternativo para obtenção da validação exigida.

Efeito observado:

- um projeto individual pode elaborar um rascunho controlado;
- não consegue, apenas pela atuação da mesma pessoa, demonstrar validação constitucional compatível e adquirir vigência;
- a barreira decorre da regra normativa vigente, não de limitação técnica.

Classificação desta pesquisa:

- possível lacuna normativa de adoção;
- não constitui defeito constitucional confirmado;
- não constitui autorização para flexibilização;
- exige processo formal do Framework para qualquer evolução.

## 7. RISCOS DE EVENTUAL FLEXIBILIZAÇÃO

- Autovalidação material: a mesma autoridade produzir e certificar o conteúdo elimina independência avaliativa.
- Autoridade circular: competência fundamentada apenas na declaração de quem pretende exercê-la.
- Confusão entre evidência e autoridade: tratar checklist, auditoria, IA ou registro como ato de validação.
- Concentração opaca: acumular funções sem proveniência verificável para cada papel.
- Perda de auditabilidade: impossibilidade de distinguir autoria, verificação, validação, aprovação e custódia.
- Deriva normativa: criar exceção local que passe a operar como regra sem validação do Framework.
- Autoridade implícita: permitir que conveniência operacional substitua ato formal de competência.
- Precedente incompatível: aplicar solução do CASE-03 a outros projetos sem processo formal de evolução.

Origem:

- interpretação sistemática de `CONSTITUTION.md`, Artigos III, VI, X e XI;
- regras expressas de autoridade, proveniência, validação e vigência de `PROJECT_CONSTITUTION_TEMPLATE.md`.

## 8. NECESSIDADE DE FUTURA EVOLUÇÃO ARQUITETURAL

Foi identificada necessidade de avaliação futura pelo processo formal de evolução do ICFACTORY.

Objeto da avaliação futura:

- determinar institucionalmente se projetos individuais pertencem ao escopo de adoção do framework;
- determinar se a impossibilidade atual de autovalidação é suficiente e intencional para esse contexto ou se existe lacuna de adoção;
- preservar integralmente os princípios constitucionais e a separação entre evidência, validação, aprovação e autoridade.

Esta seção:

- não propõe alteração normativa;
- não cria perfil;
- não cria papel;
- não cria exceção;
- não define mecanismo compensatório;
- não modifica o CASE-03.

## 9. CONCLUSÃO AUTORIZADA

**Foi identificada possível lacuna normativa, recomendando abertura de processo formal de evolução do Framework.**
