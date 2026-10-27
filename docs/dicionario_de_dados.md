# Dicionário de dados

| Coluna | Tipo | O que significa |
|---|---|---|
| `pedido_id` | texto | Identificador único do pedido, ex.: PED0001 |
| `data_pedido` | data AAAA-MM-DD | Dia em que o pedido foi realizado |
| `data_prevista` | data AAAA-MM-DD | Data limite prometida de entrega |
| `data_entrega` | data AAAA-MM-DD | Dia da entrega efetiva |
| `centro_distribuicao` | texto | Centro de distribuição fictício |
| `transportadora` | texto | Prestador de transporte fictício |
| `regiao` | texto | Macrorregião brasileira de destino |
| `distancia_km` | inteiro | Distância simulada em quilômetros |
| `peso_kg` | número decimal | Peso simulado em quilogramas |
| `custo_frete_brl` | número decimal | Custo simulado do frete, em reais |

**Colunas que o Python cria:**

- `atraso_dias` = `data_entrega - data_prevista` em dias. É negativo para adiantadas e zero para no prazo exatamente na data.
- `no_prazo` = verdadeiro se `atraso_dias <= 0`.
- `mes_pedido` = mês de `data_pedido`, formato `AAAA-MM`.

**Atenção:** não tratar a base simulada como prova sobre prazos, custos ou produtividade de transportadoras reais.
