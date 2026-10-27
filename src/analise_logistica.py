"""Projeto junior: Logistics Analytics.

Execute a partir da pasta raiz:
    python src/analise_logistica.py

Os dados são FICTÍCIOS, para estudo. Não representam empresas reais.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# 1) Caminhos (funcionam no PyCharm e no VS Code)
PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = PASTA_PROJETO / "dados" / "entregas_simuladas.csv"
PASTA_RESULTADOS = PASTA_PROJETO / "resultados"
PASTA_GRAFICOS = PASTA_PROJETO / "graficos"
PASTA_RESULTADOS.mkdir(exist_ok=True)
PASTA_GRAFICOS.mkdir(exist_ok=True)


# 2) Carregar dados e converter datas
colunas_data = ["data_pedido", "data_prevista", "data_entrega"]
df = pd.read_csv(ARQUIVO_CSV, parse_dates=colunas_data)

# Verificações iniciais para evitar conclusões equivocadas
if df.empty:
    raise ValueError("O arquivo CSV está vazio.")
if df["pedido_id"].duplicated().any():
    raise ValueError("Existem IDs de pedido duplicados.")
if df.isna().any().any():
    raise ValueError("Existem valores ausentes. Corrija-os antes de continuar.")

print("\n=== PRIMEIRAS 5 ENTREGAS ===")
print(df.head().to_string(index=False))
print("\nDimensões (linhas, colunas):", df.shape)


# 3) Criar colunas para a análise
# Um pedido no prazo é aquele entregue ATÉ a data prevista.
df["atraso_dias"] = (df["data_entrega"] - df["data_prevista"]).dt.days
df["no_prazo"] = df["atraso_dias"] <= 0
df["mes_pedido"] = df["data_pedido"].dt.to_period("M").astype(str)


# 4) Indicadores de desempenho (KPIs)
total = len(df)
no_prazo = int(df["no_prazo"].sum())
atrasadas = total - no_prazo
taxa_no_prazo = 100 * no_prazo / total
atraso_medio = df.loc[df["atraso_dias"] > 0, "atraso_dias"].mean()
if pd.isna(atraso_medio):
    atraso_medio = 0.0

kpis = {
    "total_entregas": total,
    "entregas_no_prazo": no_prazo,
    "entregas_atrasadas": atrasadas,
    "taxa_no_prazo_pct": round(taxa_no_prazo, 2),
    "atraso_medio_entre_atrasadas_dias": round(float(atraso_medio), 2),
    "custo_frete_total_brl": round(df["custo_frete_brl"].sum(), 2),
    "custo_frete_medio_brl": round(df["custo_frete_brl"].mean(), 2),
}
print("\n=== INDICADORES GERAIS ===")
for nome, valor in kpis.items():
    print(f"{nome}: {valor}")
pd.DataFrame([kpis]).to_csv(PASTA_RESULTADOS / "indicadores_gerais.csv", index=False)


# 5) Comparar transportadoras
por_transportadora = (
    df.groupby("transportadora")
    .agg(
        entregas=("pedido_id", "count"),
        taxa_no_prazo_pct=("no_prazo", "mean"),
        frete_medio_brl=("custo_frete_brl", "mean"),
    )
    .reset_index()
)
por_transportadora["taxa_no_prazo_pct"] *= 100
por_transportadora = por_transportadora.round(2)
por_transportadora.to_csv(PASTA_RESULTADOS / "por_transportadora.csv", index=False)
print("\n=== DESEMPENHO POR TRANSPORTADORA ===")
print(por_transportadora.to_string(index=False))


# 6) Comparar regiões
por_regiao = (
    df.groupby("regiao")
    .agg(
        entregas=("pedido_id", "count"),
        taxa_no_prazo_pct=("no_prazo", "mean"),
        frete_medio_brl=("custo_frete_brl", "mean"),
    )
    .reset_index()
)
por_regiao["taxa_no_prazo_pct"] *= 100
por_regiao = por_regiao.round(2)
por_regiao.to_csv(PASTA_RESULTADOS / "por_regiao.csv", index=False)


# 7) Indicadores mensais (mês em que o pedido foi feito)
por_mes = (
    df.groupby("mes_pedido")
    .agg(entregas=("pedido_id", "count"), taxa_no_prazo_pct=("no_prazo", "mean"))
    .reset_index()
)
por_mes["taxa_no_prazo_pct"] *= 100
por_mes = por_mes.round(2)
por_mes.to_csv(PASTA_RESULTADOS / "por_mes.csv", index=False)


# 8) Gráficos - sem necessidade de abrir janelas interativas
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(por_transportadora["transportadora"], por_transportadora["taxa_no_prazo_pct"])
ax.set_title("Percentual de entregas no prazo por transportadora")
ax.set_ylabel("Entregas no prazo (%)")
ax.set_ylim(0, 100)
ax.grid(axis="y", alpha=0.2)
fig.tight_layout()
fig.savefig(PASTA_GRAFICOS / "entregas_no_prazo_transportadora.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(por_regiao["regiao"], por_regiao["frete_medio_brl"])
ax.set_title("Custo médio de frete por região")
ax.set_ylabel("Frete médio (R$)")
ax.tick_params(axis="x", rotation=15)
ax.grid(axis="y", alpha=0.2)
fig.tight_layout()
fig.savefig(PASTA_GRAFICOS / "frete_medio_regiao.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(por_mes["mes_pedido"], por_mes["taxa_no_prazo_pct"], marker="o")
ax.set_title("Evolução mensal de entregas no prazo")
ax.set_xlabel("Mês do pedido")
ax.set_ylabel("Entregas no prazo (%)")
ax.set_ylim(0, 100)
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(PASTA_GRAFICOS / "evolucao_mensal.png", dpi=160)
plt.close(fig)

print("\n✅ Pronto! Arquivos criados em 'resultados/' e 'graficos/'.")
