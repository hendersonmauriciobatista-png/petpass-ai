# DP-PP-009 — PARÂMETROS TÉCNICOS DA INTERFACE DA FICHA DE EMERGÊNCIA

## Identificação

- Documento: DP-PP-009.
- Projeto: CASE-03 — PetPass AI.
- Classificação: NORMATIVO.
- Assunto: parâmetros técnicos oficiais da interface da Ficha de Emergência.
- Finalidade: consolidar exclusivamente decisões aprovadas pelo Product Owner e parâmetros já documentados nas fontes obrigatórias.

## Fontes normativas e técnicas

- `DP-PP-006_IDENTIFICADOR_DIGITAL_KEY_PASS.md`.
- `DP-PP-007_REPRESENTACAO_GRAFICA_QR_CODE.md`.
- `DP-PP-008_IDENTIDADE_VISUAL_FICHA_EMERGENCIA.md`.
- `AV-PP-001_LOGOTIPO_OFICIAL_PROPOSTA_2.png`.
- `AV-PP-002_MODELO_4_FICHA_EMERGENCIA.png`.
- `ES-UI-001_ESPECIFICACAO_EXECUTAVEL_FICHA_EMERGENCIA.md`.
- `GP-PP-17_AUDITORIA_LACUNAS_DESIGN_IMPLEMENTACAO.md`.
- Deliberações aprovadas neste ciclo, conforme declaração do Product Owner na atividade DP-PP-009.

## 1. Referência visual oficial

- A Proposta 2 constitui a identidade visual institucional aprovada.
- O arquivo de referência do logotipo é `AV-PP-001_LOGOTIPO_OFICIAL_PROPOSTA_2.png`.
- O Modelo 4 constitui a referência oficial da identidade visual da Ficha de Emergência.
- O arquivo de referência da ficha é `AV-PP-002_MODELO_4_FICHA_EMERGENCIA.png`.
- A dimensão documentada do Modelo 4 é `735 × 475 px`, a `96 × 96 DPI`.
- O sistema de coordenadas possui origem `(0, 0)` no canto superior esquerdo do bitmap.
- Coordenadas aferidas no bitmap admitem variação de até `±2 px` nas bordas antialiasadas.

Origem: DP-PP-008; AV-PP-001; AV-PP-002; ES-UI-001, seção 1.

## 2. Família tipográfica oficial

- Família tipográfica oficial: **Inter**.
- Aplicação: conteúdo textual da interface da Ficha de Emergência.
- Pesos visualmente documentados: peso forte para títulos, cabeçalhos e rótulos; o Modelo 4 permanece como referência visual obrigatória da hierarquia.
- Tamanhos tipográficos nominais em pontos: **NÃO DETERMINADOS PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDOS.**

Origem da família: deliberação aprovada neste ciclo — Família tipográfica Inter.

Origem da hierarquia observável e da ausência de tamanhos nominais: ES-UI-001, seções 3.2, 5, 6, 7, 8, 9, 10, 11 e 12; GP-PP-17, LD-001 e LD-002.

## 3. Hierarquia tipográfica

| Nível documentado | Conteúdo | Tratamento documentado |
|---|---|---|
| Identidade principal | `PETPASS AI` | Caixa alta, peso forte; `PETPASS` em azul-escuro e `AI` em verde-azulado; altura observável aproximada dos glifos: `29 px` |
| Identidade da ficha | `FICHA DE EMERGÊNCIA` | Caixa alta, peso forte, verde-azulado; altura observável aproximada dos glifos: `12 px`; nomenclatura imutável |
| Identificação do modelo | `MODELO 4 – IDENTIDADE OFICIAL` | Caixa alta, peso forte, texto branco, centralizado em faixa verde-azulada |
| Cabeçalhos de seção | `INFORMAÇÕES DO PET`, `TUTOR`, `EMERGÊNCIA`, `QR CODE`, `KEY PASS` | Caixa alta, peso forte; azul-escuro, exceto `KEY PASS`, em branco sobre faixa verde-azulada |
| Rótulos de campos | Rótulos documentados no Modelo 4 | Peso forte, azul-escuro |
| Mensagem institucional | Texto do rodapé | Caixa alta, peso forte, azul-escuro |
| Valores | Dados apresentados nas áreas documentadas | Alinhamentos definidos nas seções próprias; tamanhos nominais não determinados |

Origem: DP-PP-008; AV-PP-002; ES-UI-001, seções 3, 5 a 10.

## 4. Paleta cromática oficial

A paleta cromática oficial é a paleta visual do Modelo 4, composta pelas seguintes cores documentadas:

- azul-escuro;
- verde-azulado;
- azul-claro;
- branco.

Aplicações documentadas:

- azul-escuro: `PETPASS`, cabeçalhos, rótulos, borda principal e mensagem institucional;
- verde-azulado: `AI`, subtítulo institucional, ícones, detalhes internos, faixas e valor da Key Pass;
- azul-claro: padrão linear orgânico, linhas pontilhadas, fundos e elementos de baixa opacidade;
- branco: fundo predominante e textos sobre faixas verde-azuladas.

Códigos cromáticos exatos: **NÃO DETERMINADOS PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDOS.**

Origem: deliberação aprovada neste ciclo — Paleta oficial; AV-PP-001; AV-PP-002; ES-UI-001, seções 3, 5 a 11; GP-PP-17, LD-003.

## 5. Estrutura institucional do cartão

| Bloco | Posição aproximada `(x, y)` | Dimensão aproximada `(L × A)` |
|---|---:|---:|
| Tela completa de referência | `(0, 0)` | `735 × 475 px` |
| Faixa `MODELO 4 – IDENTIDADE OFICIAL` | `(82, 14)` | `284 × 30 px` |
| Contêiner principal | `(26, 55)` | `709 × 420 px` |
| Borda interna decorativa | `(34, 62)` | `700 × 405 px` |
| Cabeçalho institucional | `(54, 66)` | `488 × 70 px` |
| Fotografia | `(55, 152)` | `176 × 183 px` |
| Informações do Pet | `(262, 145)` | `280 × 183 px` |
| QR Code e Key Pass | `(570, 114)` | `145 × 228 px` |
| Bloco inferior | `(53, 354)` | `662 × 111 px` |
| Tutor | `(53, 354)` | `225 × 111 px` |
| Emergência | `(278, 354)` | `180 × 111 px` |
| Rodapé institucional | `(458, 354)` | `257 × 111 px` |

A estrutura institucional é composta por:

1. faixa de identificação do Modelo 4;
2. cabeçalho com logotipo, `PETPASS AI` e `FICHA DE EMERGÊNCIA`;
3. corpo superior dividido entre fotografia, Informações do Pet e painel de QR Code/Key Pass;
4. bloco inferior dividido entre Tutor, Emergência e rodapé institucional.

Origem: DP-PP-008; AV-PP-002; ES-UI-001, seções 2, 3 e 10; deliberações aprovadas neste ciclo — Hierarquia das informações e Natureza institucional do cartão.

## 6. Área oficial da fotografia

- Posição aproximada do limite externo: `(55, 152)`.
- Dimensão aproximada: `176 × 183 px`.
- Moldura: polígono de oito lados, com contorno externo azul, contorno interno verde-azulado e base branca.
- Recuo documentado da imagem interna: aproximadamente `8 px`.
- Alinhamento: centralizado na moldura.
- Origem da imagem: fotografia original do pet de cada tutor.
- Finalidade: exclusivamente identificadora.
- A fotografia ilustrativa do Modelo 4 deverá ser substituída pela fotografia original do pet.
- Método de ajuste da fotografia: **NÃO DETERMINADO PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDO.**
- Comportamento quando não houver fotografia: **NÃO DETERMINADO PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDO.**

Origem: DP-PP-008; AV-PP-002; ES-UI-001, seção 4; GP-PP-17, LD-006 e LD-007; deliberação aprovada neste ciclo — Comportamento da fotografia.

## 7. Área oficial do QR Code

- Painel conjunto de QR Code e Key Pass: posição aproximada `(570, 114)`, dimensão aproximada `145 × 228 px`.
- Área gráfica do QR Code: posição aproximada `(583, 149)`, dimensão aproximada `119 × 119 px`.
- Margem interna lateral do painel: aproximadamente `12 px`.
- Título literal: `QR CODE`.
- Alinhamento: título e representação gráfica centralizados horizontalmente no painel.
- O QR Code representa graficamente a Key Pass.
- O QR Code não constitui identificador independente.
- O QR Code poderá ser regenerado sempre que necessário.
- A regeneração preservará integralmente a mesma Key Pass.
- A substituição do QR Code não altera a identidade digital do pet.
- Regra de geração visual, correção de erro, margem silenciosa e resolução: **NÃO DETERMINADA PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDA.**
- Comportamento quando o QR Code não estiver disponível: **NÃO DETERMINADO PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDO.**

Origem: DP-PP-007; AV-PP-002; ES-UI-001, seção 6; GP-PP-17, LD-013 e LD-014; deliberação aprovada neste ciclo — Comportamento do QR Code.

## 8. Área oficial da Key Pass

- Faixa de título: posição aproximada `(579, 280)`, dimensão aproximada `127 × 28 px`.
- Conteúdo literal da faixa: `KEY PASS`.
- Tratamento: texto branco, caixa alta, peso forte e centralizado em faixa verde-azulada com cantos arredondados.
- Área do valor: posição aproximada `(579, 313)`, dimensão aproximada `127 × 22 px`.
- Alinhamento do valor: centralizado horizontalmente.
- A Key Pass constitui o identificador único do PetPass AI para animal previamente cadastrado.
- Coexiste com outros identificadores sem substituí-los.
- Possui finalidade exclusiva no ecossistema PetPass AI.
- É gerada automaticamente somente após a conclusão válida do cadastro.
- Permanece inalterada durante toda a existência do cadastro.
- Alterações cadastrais posteriores não modificam a Key Pass.
- Formato, comprimento e algoritmo de geração: **NÃO DETERMINADOS PELAS DECISÕES DISPONÍVEIS — NÃO INFERIDOS.**

Origem: DP-PP-006; AV-PP-002; ES-UI-001, seção 7; GP-PP-17, LD-015; deliberação aprovada neste ciclo — Natureza da Key Pass.

## 9. Margens externas

- Margem esquerda do contêiner principal em relação ao bitmap: aproximadamente `26 px`.
- Margem superior do contêiner principal em relação ao bitmap: aproximadamente `55 px`.
- As demais margens externas não foram individualizadas como parâmetros independentes nas fontes disponíveis.

Origem: ES-UI-001, seção 2.2.

## 10. Margens internas

- Recuo da borda interna decorativa em relação à borda externa: aproximadamente `8 px`.
- Margem interna lateral do painel QR Code/Key Pass: aproximadamente `12 px`.
- Recuo da fotografia em relação ao limite externo de sua moldura: aproximadamente `8 px`.
- Outras margens internas não foram individualizadas como parâmetros independentes nas fontes disponíveis.

Origem: ES-UI-001, seções 2.2, 4 e 6.

## 11. Espaçamento entre blocos

Os blocos obedecem às posições e dimensões oficiais da seção 5. A partir dos limites documentados na ES-UI-001, são observáveis os seguintes intervalos aproximados:

- entre Fotografia e Informações do Pet: `31 px`;
- entre Informações do Pet e painel QR Code/Key Pass: `28 px`;
- entre o término vertical da Fotografia e o início do bloco inferior: `19 px`;
- entre o término vertical de Informações do Pet e o início do bloco inferior: `26 px`;
- entre o término vertical do painel QR Code/Key Pass e o início do bloco inferior: `12 px`.

Tutor, Emergência e Rodapé compartilham o mesmo bloco inferior e são separados por linhas verticais, sem espaçamento independente documentado entre os painéis.

Os intervalos são resultados aritméticos das coordenadas e dimensões aproximadas registradas na ES-UI-001 e conservam a mesma tolerância de `±2 px` em cada limite aferido.

Origem: ES-UI-001, seções 2.1 e 2.2.

## 12. Alinhamentos oficiais

- Logotipo à esquerda; título e subtítulo alinhados em coluna à direita do símbolo.
- Fotografia centralizada em sua moldura.
- Informações do Pet dispostas verticalmente, com rótulos à esquerda e áreas de valor à direita.
- QR Code centralizado horizontalmente em seu painel.
- Faixa `KEY PASS` e valor centralizados horizontalmente.
- Tutor e Emergência organizados verticalmente, com rótulos à esquerda e áreas de valor à direita.
- Texto do rodapé alinhado à esquerda e centralizado verticalmente no painel.
- Faixa `MODELO 4 – IDENTIDADE OFICIAL`: texto centralizado horizontal e verticalmente.

Origem: AV-PP-002; ES-UI-001, seções 3 a 10.

## 13. Hierarquia visual e das informações

A ordem visual documentada é:

1. identidade institucional: logotipo, `PETPASS AI` e `FICHA DE EMERGÊNCIA`;
2. identificação do pet: fotografia e Informações do Pet;
3. identidade digital: QR Code e Key Pass;
4. identificação do Tutor;
5. contato de Emergência;
6. mensagem institucional do rodapé.

O bloco superior concentra identidade institucional, identificação do pet e identidade digital. O bloco inferior concentra Tutor, Emergência e instrução institucional de localização do tutor.

Origem: DP-PP-006; DP-PP-007; DP-PP-008; AV-PP-002; ES-UI-001, seções 2 a 10; deliberação aprovada neste ciclo — Hierarquia das informações.

## 14. Natureza institucional do cartão

- O cartão constitui a Ficha de Emergência do PetPass AI.
- Sua identidade institucional é composta por `PETPASS AI` e `FICHA DE EMERGÊNCIA`.
- A identidade visual oficial baseia-se na Proposta 2.
- O Modelo 4 constitui a referência oficial da identidade visual.
- A identidade visual representa proteção, identificação, confiança, simplicidade institucional e aderência ao escopo do desafio da DIO.
- A alteração é exclusivamente visual e institucional e não altera requisitos funcionais ou regras de negócio.

Origem: DP-PP-008; deliberação aprovada neste ciclo — Natureza institucional do cartão.

## 15. Regras de preservação da identidade visual

- Não alterar o nome `FICHA DE EMERGÊNCIA`.
- Não alterar o Modelo 4.
- Não alterar requisitos funcionais.
- Não modificar regras de negócio.
- Não criar novos componentes ou funcionalidades.
- A identidade visual oficial permanece baseada na Proposta 2.
- Alterações conceituais dependem de nova Deliberação do Product Owner.
- Ajustes futuros ficam limitados à natureza técnica já autorizada: vetorização, resolução, tipografia e adaptação de mídia.
- A fotografia ilustrativa deve ser substituída pela fotografia original do pet, sem modificar requisitos, regras de negócio ou funcionalidades do MVP.
- O QR Code permanece representação da Key Pass e não identificador independente.
- A Key Pass permanece a identidade digital estável do pet no ecossistema PetPass AI.

Origem: DP-PP-006; DP-PP-007; DP-PP-008; AV-PP-001; AV-PP-002.

## 16. Comportamentos previamente deliberados

### 16.1 Fotografia

- utilizar a fotografia original do pet de cada tutor;
- finalidade exclusivamente identificadora;
- substituição da fotografia ilustrativa sem alteração funcional.

### 16.2 QR Code

- representar graficamente a Key Pass;
- não constituir identificador independente;
- admitir regeneração;
- preservar a mesma Key Pass em cada regeneração;
- não alterar a identidade digital quando substituído.

### 16.3 Key Pass

- identificar unicamente, no PetPass AI, animal previamente cadastrado;
- coexistir com outros identificadores sem substituí-los;
- possuir finalidade exclusiva no ecossistema PetPass AI;
- ser gerada somente após cadastro válido;
- permanecer inalterada durante a existência do cadastro;
- não ser modificada por alterações cadastrais posteriores.

Origem: DP-PP-006; DP-PP-007; DP-PP-008; deliberações aprovadas neste ciclo — Comportamento da fotografia, Comportamento do QR Code e Natureza da Key Pass.

## 17. Parâmetros ainda não determinados

Permanecem sem conteúdo concreto nas fontes e não foram preenchidos neste documento:

- tamanhos tipográficos nominais;
- códigos cromáticos exatos;
- comportamento de redimensionamento e limites mínimo e máximo da janela;
- método de ajuste da fotografia e estado sem fotografia;
- apresentação, truncamento e quebra de valores extensos;
- origem dos dados de Tutor e Emergência;
- comportamento de acionamento do telefone de Emergência;
- regra de geração visual, correção de erro, margem silenciosa e resolução do QR Code;
- estado da área quando o QR Code não estiver disponível;
- formato, comprimento e algoritmo de geração da Key Pass.

Origem: ES-UI-001, seção 12; GP-PP-17, LD-002 a LD-015. A lacuna LD-001 foi resolvida exclusivamente quanto à família tipográfica pela deliberação deste ciclo que aprovou Inter; os tamanhos nominais permanecem não determinados.

## 18. Restrições e preservação

- Nenhum componente foi criado.
- Nenhuma funcionalidade foi criada.
- O Modelo 4 não foi alterado.
- Nenhuma DP anterior foi alterada.
- Nenhuma decisão do Product Owner foi reinterpretada.
- Nenhuma regra de negócio foi modificada.
- Nenhuma tecnologia de implementação foi definida.
- Nenhum parâmetro ausente foi preenchido por inferência.
