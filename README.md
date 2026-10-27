# Logistics Analytics | Projeto Júnior em Ciência de Dados 📦

> Projeto educacional de análise exploratória de dados (EDA), voltado a iniciantes em Python.

## 1. Problema de negócio

Uma distribuidora fictícia quer identificar: (1) quantas entregas chegaram dentro do prazo; (2) quais transportadoras tiveram melhor pontualidade; (3) quais regiões apresentaram fretes médios mais altos; e (4) como a pontualidade mudou ao longo dos meses.

## 2. Origem dos dados

O arquivo `dados/entregas_simuladas.csv` contém **360 entregas fictícias**, geradas especificamente para fins de ensino. As transportadoras, centros e números não são de nenhuma empresa real. O dataset contém pedidos de janeiro a junho de 2026 (datas de entrega podem ultrapassar junho). Sem dados confidenciais.

**Limites:** a base traz apenas pedidos concluídos; não há cancelados ou entregas em andamento. As datas não possuem horários: um pedido entregue no mesmo dia da previsão é contado como **no prazo**. Comparações não provam causalidade.

## 3. Ferramentas

- Python 3.10+;
- pandas (leitura, limpeza e agrupamento);
- matplotlib (gráficos);
- csv (formato da base).

## 4. Como executar no Windows (sem precisar ativar o ambiente virtual)

Abra o terminal **dentro da pasta deste projeto** e execute, uma linha de cada vez:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\analise_logistica.py
```

Se `py` não funcionar, tente `python -m venv .venv` na primeira linha. No **PyCharm** ou **VS Code**, selecione como interpretador `.venv\Scripts\python.exe`. Não é preciso instalar Python por fora se você já tiver uma instalação funcional.

No macOS/Linux, use `python3 -m venv .venv`, `.venv/bin/python -m pip install -r requirements.txt` e `.venv/bin/python src/analise_logistica.py`.

## 5. Estrutura

```text
logistics_analytics_junior/
├── dados/
│   └── entregas_simuladas.csv
├── docs/
│   ├── dicionario_de_dados.md
│   └── roteiro_de_aprendizado.md
├── src/
│   └── analise_logistica.py
├── resultados/               # tabelas CSV criadas pelo script
├── graficos/                 # imagens PNG criadas pelo script
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. Indicadores

- **Entregas no prazo (%)** = entregas entregues até a data prevista / total de entregas x 100.
- **Entregas atrasadas** = entregas com data real posterior à previsão.
- **Atraso médio (dias)** = média de dias de atraso apenas dos pedidos atrasados.
- **Custo total de frete (R$)** = soma do frete de todas as entregas.
- **Frete médio (R$)** = média do valor de frete por entrega.

## 7. Resultados

Rode o script para gerar os indicadores em `resultados/` e os três gráficos em `graficos/`.

**Sua missão:** responda às perguntas de negócio com números específicos, escreva um parágrafo de conclusão e registre duas sugestões operacionais sem afirmar que encontrou causas definitivas.

## 8. Próximos passos

1. Entenda `pd.read_csv()`, `df.head()` e `df.shape()`.
2. Experimente `df["regiao"].value_counts()`.
3. Inclua uma análise de atraso médio por transportadora.
4. Adicione um gráfico comparando volumes de entrega por mês.
5. Publique o repositório no GitHub com seus gráficos e conclusões.

## 9. Portfólio (descrição curta)

> Análise exploratória de 360 entregas simuladas com Python, Pandas e Matplotlib. O projeto calcula KPIs logísticos, compara transportadoras e regiões e avalia tendências mensais, apresentando dados em gráficos e tabelas reproduzíveis.
