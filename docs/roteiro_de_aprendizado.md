# Roteiro para quem começa do zero

## Semana 1 — Python e dados

**Meta:** executar o projeto e entender a entrada de dados.

- Dia 1: instalar/selecionar o Python 3 e executar `print("Olá, logística!")`.
- Dia 2: entender variáveis, números, textos e listas.
- Dia 3: conhecer `import`, `pandas as pd` e `pd.read_csv()`.
- Dia 4: testar `df.head()`, `df.shape` e `df.columns`.
- Dia 5: entender cada coluna pelo dicionário de dados.

**Checkpoint:** explicar com suas palavras o que uma linha e uma coluna representam.

## Semana 2 — Limpeza e criação de métricas

- Dia 1: revisar `df.isna().sum()` e `df.duplicated()`.
- Dia 2: compreender datas (`parse_dates`, `dt.days`).
- Dia 3: comparar números usando `<=`, `>`, `==`.
- Dia 4: calcular `len(df)`, `sum()` e `mean()`.
- Dia 5: modificar um pedido fictício para ficar atrasado e conferir a mudança da taxa.

**Checkpoint:** conseguir explicar como se calcula a taxa de entregas no prazo.

## Semana 3 — Tabelas e gráficos

- Dia 1: aprender `groupby()`.
- Dia 2: comparar transportadoras e regiões.
- Dia 3: entender gráficos de barras e eixos.
- Dia 4: verificar um gráfico de linha por mês.
- Dia 5: criar um gráfico adicional de volume mensal.

**Checkpoint:** identificar maior e menor taxa de pontualidade e explicar com cautela.

## Semana 4 — Conclusões e portfólio

- Dia 1: escrever objetivo, origem e limitações da base.
- Dia 2: incluir no README indicadores obtidos na sua execução.
- Dia 3: escrever três descobertas numéricas e duas hipóteses a investigar.
- Dia 4: revisar organização, comentários do código e nomes de arquivos.
- Dia 5: criar repositório no GitHub, adicionar código/dados simulados e screenshots.

**Checkpoint:** ter um projeto executável que outra pessoa consiga reproduzir.

## Exercícios extras

1. Quantas entregas há por região?
2. Qual transportadora tem a maior taxa de entregas no prazo?
3. Qual tem o menor custo médio? Coincide com a melhor pontualidade?
4. Qual mês teve a maior proporção de atraso?
5. Qual a diferença entre correlação e causa, neste caso?
6. O que muda nos resultados se você considerar atraso >= 2 dias como "atraso grave"?
