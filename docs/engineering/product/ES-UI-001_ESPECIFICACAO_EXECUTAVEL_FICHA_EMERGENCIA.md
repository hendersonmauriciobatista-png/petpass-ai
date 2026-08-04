# ES-UI-001 — ESPECIFICAÇÃO EXECUTÁVEL DA FICHA DE EMERGÊNCIA

## 1. Identificação e autoridade

- Projeto: CASE-03 — PetPass AI.
- Atividade: ES-UI-001.
- Natureza: especificação técnica da interface aprovada.
- Referência visual obrigatória: `AV-PP-002_MODELO_4_FICHA_EMERGENCIA.png`.
- Deliberações normativas obrigatórias:
  - `DP-PP-008_IDENTIDADE_VISUAL_FICHA_EMERGENCIA.md`;
  - `DP-PP-006_IDENTIFICADOR_DIGITAL_KEY_PASS.md`;
  - `DP-PP-007_REPRESENTACAO_GRAFICA_QR_CODE.md`.
- Sistema de coordenadas: origem `(0, 0)` no canto superior esquerdo do bitmap; coordenadas e dimensões expressas em pixels.
- Dimensão aferida do artefato: `735 × 475 px`, resolução declarada no arquivo de `96 × 96 DPI`.

## 2. Estrutura da janela

### 2.1 Dimensões e limites observáveis

| Elemento | Posição aproximada `(x, y)` | Dimensão aproximada `(L × A)` | Alinhamento observável |
|---|---:|---:|---|
| Tela completa da referência | `(0, 0)` | `735 × 475` | Plano integral |
| Faixa “MODELO 4 – IDENTIDADE OFICIAL” | `(82, 14)` | `284 × 30` | Superior, deslocada à esquerda |
| Contêiner principal da ficha | `(26, 55)` | `709 × 420` | Abaixo da faixa do modelo |
| Borda interna decorativa | `(34, 62)` | `700 × 405` | Inserida no contêiner principal |
| Cabeçalho institucional | `(54, 66)` | `488 × 70` | Superior esquerdo |
| Fotografia | `(55, 152)` | `176 × 183` | Coluna esquerda do corpo |
| Informações do Pet | `(262, 145)` | `280 × 183` | Centro do corpo |
| QR Code e Key Pass | `(570, 114)` | `145 × 228` | Coluna direita do corpo |
| Bloco inferior | `(53, 354)` | `662 × 111` | Base da ficha |
| Tutor | `(53, 354)` | `225 × 111` | Esquerda do bloco inferior |
| Emergência | `(278, 354)` | `180 × 111` | Centro do bloco inferior |
| Rodapé informativo | `(458, 354)` | `257 × 111` | Direita do bloco inferior |

As coordenadas acima são aferições do bitmap raster e admitem variação de até `±2 px` nas bordas antialiasadas.

### 2.2 Margens e divisões

- Margem esquerda do contêiner principal em relação ao bitmap: aproximadamente `26 px`.
- Margem superior do contêiner principal: aproximadamente `55 px`.
- Recuo da borda interna em relação à borda externa: aproximadamente `8 px`.
- O cabeçalho é separado do corpo por linha horizontal azul-petróleo, de aproximadamente `(54, 135)` a `(542, 135)`.
- O corpo superior divide-se em fotografia, informações do pet e painel de QR Code/Key Pass.
- O bloco inferior é contornado por cantos arredondados e dividido por linhas verticais próximas a `x = 278` e `x = 458`.
- Comportamento de redimensionamento da janela: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Largura ou altura mínima e máxima da janela: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 3. Cabeçalho

### 3.1 Faixa de identificação do modelo

- Posição aproximada: `(82, 14)`.
- Dimensão aproximada: `284 × 30 px`.
- Conteúdo literal: `MODELO 4 – IDENTIDADE OFICIAL`.
- Forma: retângulo horizontal com cantos arredondados.
- Preenchimento: verde-azulado.
- Texto: branco, caixa alta, peso visual forte, centralizado horizontal e verticalmente.

### 3.2 Identidade institucional

- Área aproximada: `(82, 68)` a `(392, 121)`.
- Logotipo: símbolo institucional à esquerda, ocupando aproximadamente `(82, 68)` a `(190, 119)`.
- Título literal: `PETPASS AI`.
- Posição aproximada do título: `(204, 77)`.
- Subtítulo literal e imutável: `FICHA DE EMERGÊNCIA`.
- Posição aproximada do subtítulo: `(219, 106)`.
- Alinhamento: símbolo à esquerda; título e subtítulo alinhados em coluna à direita do símbolo.
- Título: fonte visualmente sem serifa, caixa alta e peso forte; `PETPASS` em azul-escuro e `AI` em verde-azulado.
- Subtítulo: fonte visualmente sem serifa, caixa alta, peso forte e cor verde-azulada; linhas horizontais decorativas nas laterais.
- Família tipográfica exata: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Tamanho tipográfico nominal em pontos: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Altura observável aproximada dos glifos do título: `29 px`.
- Altura observável aproximada dos glifos do subtítulo: `12 px`.

## 4. Área da fotografia

- Posição aproximada do limite externo: `(55, 152)`.
- Dimensão aproximada: `176 × 183 px`.
- Moldura: polígono de oito lados, com contorno externo azul e contorno interno verde-azulado sobre base branca.
- Imagem interna: fotografia recortada pelo mesmo contorno poligonal, com recuo aproximado de `8 px` em relação ao limite externo.
- Alinhamento: centralizado na moldura.
- Origem normativa da imagem: fotografia original do pet de cada tutor, conforme DP-PP-008.
- Finalidade: exclusivamente identificadora, conforme DP-PP-008.
- A fotografia ilustrativa do Modelo 4 não integra os dados definitivos e deverá ser substituída pela fotografia original do pet.
- Método de ajuste da fotografia — corte, encaixe, preenchimento ou preservação de proporção: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Comportamento quando não houver fotografia: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 5. Área Informações do Pet

- Área aproximada: `(262, 145)` a `(542, 328)`.
- Cabeçalho da seção: ícone de pata seguido do texto literal `INFORMAÇÕES DO PET`.
- Posição aproximada do cabeçalho: `(262, 146)`.
- Texto do cabeçalho: azul-escuro, caixa alta, peso forte.
- Campos dispostos verticalmente, com rótulo à esquerda e linha pontilhada para valor à direita.

| Campo | Posição aproximada do rótulo `(x, y)` | Início aproximado da área de valor | Alinhamento |
|---|---:|---:|---|
| Nome | `(265, 179)` | `x = 318` | Horizontal |
| Espécie | `(265, 202)` | `x = 318` | Horizontal |
| Raça | `(265, 225)` | `x = 318` | Horizontal |
| Sexo | `(265, 248)` | `x = 318` | Horizontal |
| Idade | `(265, 270)` | `x = 318` | Horizontal |
| Peso | `(265, 293)` | `x = 318` | Horizontal |
| Pelagem / Cor | `(265, 315)` | `x = 350` | Horizontal |

- Espaçamento vertical aproximado entre linhas: `22–23 px`.
- Rótulos: azul-escuro, fonte visualmente sem serifa e peso forte.
- Valores: conteúdo proveniente do cadastro do pet; apresentação, truncamento e quebra de linha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 6. Área QR Code

- Painel conjunto QR Code/Key Pass: posição aproximada `(570, 114)`, dimensão aproximada `145 × 228 px`.
- Margem interna lateral aproximada: `12 px`.
- Título literal: `QR CODE`, centralizado, na região aproximada `(614, 130)`.
- Área gráfica do QR Code: posição aproximada `(583, 149)`, dimensão aproximada `119 × 119 px`.
- A área possui fundo claro e cantos arredondados.
- O QR Code é centralizado horizontalmente no painel.
- Comportamento normativo: representa graficamente a Key Pass; não constitui identificador independente; pode ser regenerado; sua regeneração preserva a mesma Key Pass; sua substituição não altera a identidade digital do pet, conforme DP-PP-007.
- Regra de geração visual, correção de erro, margem silenciosa e resolução do QR Code: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Comportamento quando o QR Code ainda não estiver disponível: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 7. Área Key Pass

- Faixa de título: posição aproximada `(579, 280)`, dimensão aproximada `127 × 28 px`.
- Forma: retângulo horizontal com cantos arredondados e preenchimento verde-azulado.
- Conteúdo literal: `KEY PASS`, branco, caixa alta, peso forte e centralizado.
- Área do valor: posição aproximada `(579, 313)`, dimensão aproximada `127 × 22 px`.
- Valor centralizado horizontalmente, em cor verde-azulada e peso forte.
- Comportamento normativo: identificador único de animal previamente cadastrado; gerado automaticamente somente após cadastro válido; permanece inalterado durante a existência do cadastro; alterações cadastrais posteriores não o modificam, conforme DP-PP-006.
- Formato, comprimento e algoritmo de geração da Key Pass: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 8. Área Tutor

- Posição aproximada: `(53, 354)`.
- Dimensão aproximada: `225 × 111 px`.
- Cabeçalho: ícone de pessoa seguido do texto literal `TUTOR`.
- Posição aproximada do cabeçalho: `(61, 363)`.
- Componentes, em disposição vertical:

| Campo | Posição aproximada do rótulo `(x, y)` | Área de valor observável |
|---|---:|---|
| Nome | `(61, 388)` | Linha pontilhada até aproximadamente `x = 264` |
| Telefone | `(61, 411)` | Linha pontilhada até aproximadamente `x = 264` |
| E-mail | `(61, 433)` | Linha pontilhada até aproximadamente `x = 264` |
| Endereço | `(61, 456)` | Linha pontilhada até aproximadamente `x = 264` |

- Cabeçalho e rótulos: azul-escuro; ícone em verde-azulado.
- Origem dos valores, regras de apresentação, truncamento e quebra de linha: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 9. Área Emergência

- Posição aproximada: `(278, 354)`.
- Dimensão aproximada: `180 × 111 px`.
- Cabeçalho: ícone de telefone seguido do texto literal `EMERGÊNCIA`.
- Posição aproximada do cabeçalho: `(289, 363)`.
- Componentes, em disposição vertical:

| Campo | Posição aproximada do rótulo `(x, y)` | Área de valor observável |
|---|---:|---|
| Nome | `(289, 388)` | Linha pontilhada até aproximadamente `x = 445` |
| Telefone | `(289, 412)` | Linha pontilhada até aproximadamente `x = 445` |

- Cabeçalho e rótulos: azul-escuro; ícone em verde-azulado.
- Origem dos valores e comportamento de acionamento do telefone: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 10. Rodapé

- Posição aproximada: `(458, 354)`.
- Dimensão aproximada: `257 × 111 px`.
- Separação à esquerda por linha vertical.
- Ícone circular de pata: posição aproximada `(474, 388)`, dimensão aproximada `39 × 46 px`.
- Conteúdo literal, em caixa alta:

  `SE VOCÊ ENCONTROU ESTE PET,`

  `UTILIZE O QR CODE PARA`

  `LOCALIZAR SEU TUTOR.`

- Bloco textual: posição aproximada `(523, 390)` a `(695, 432)`.
- Alinhamento: texto à esquerda, centralizado verticalmente no painel.
- Cor do texto: azul-escuro; fonte visualmente sem serifa e peso forte.
- O rodapé não contém controles interativos observáveis no Modelo 4.

## 11. Elementos visuais transversais

- Fundo: branco com padrão linear orgânico em azul-claro de baixa opacidade.
- Cores predominantes observáveis: azul-escuro, verde-azulado, azul-claro e branco.
- Cantos externos e painéis: arredondados.
- Borda principal: azul-escuro com detalhes internos verde-azulados nos cantos.
- Há marca gráfica de escudo e pata em baixa opacidade atrás da área de informações do pet.
- Códigos exatos de cor: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**
- Família tipográfica exata: **AUSÊNCIA DE INFORMAÇÃO — NÃO INFERIDA.**

## 12. Limites de executabilidade documental

Esta especificação materializa as dimensões, posições, alinhamentos, conteúdos e relações visualmente comprováveis no Modelo 4, juntamente com os comportamentos expressamente estabelecidos nas DP-PP-006, DP-PP-007 e DP-PP-008.

Permanecem não determinados pelas fontes obrigatórias: família tipográfica, tamanhos nominais em pontos, códigos exatos de cor, comportamento de redimensionamento, política de ajuste e ausência da fotografia, apresentação de valores extensos, origem de determinados dados de tutor e emergência e parâmetros técnicos de geração do QR Code e da Key Pass. Esses pontos foram registrados sem inferência e não receberam decisão técnica nesta atividade.

## 13. Declaração de preservação

- Nenhum componente foi criado.
- O layout aprovado não foi alterado.
- O Modelo 4 não foi reinterpretado.
- Nenhuma funcionalidade foi criada.
- Nenhuma regra de negócio foi alterada.
- Nenhum código foi produzido ou modificado.
