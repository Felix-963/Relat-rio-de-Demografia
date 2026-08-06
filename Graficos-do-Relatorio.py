import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ==============================================================================
# CONFIGURAÇÕES GERAIS DOS GRÁFICOS
# ==============================================================================

plt.style.use("ggplot")

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 15,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "figure.dpi": 300,
    "savefig.dpi": 300
})

# ==============================================================================
# DADOS
# ==============================================================================

faixas = [
    '0-4', '5-9', '10-14', '15-19', '20-24', '25-29',
    '30-34', '35-39', '40-44', '45-49', '50-54',
    '55-59', '60-64', '65-69', '70-74', '75-79', '80+'
]

# Dados simulados (% da população)

masc_2010 = np.array([
    5.1,5.2,5.3,4.9,4.5,4.0,3.5,3.1,
    2.7,2.3,1.9,1.5,1.2,0.9,0.6,0.4,0.3
])

fem_2010 = np.array([
    4.9,5.0,5.1,4.8,4.6,4.2,3.7,3.3,
    2.9,2.5,2.0,1.6,1.3,1.0,0.7,0.5,0.4
])

masc_2022 = np.array([
    3.8,3.9,4.1,4.4,4.5,4.3,4.0,3.8,
    3.4,2.8,2.4,2.0,1.6,1.2,0.9,0.6,0.4
])

fem_2022 = np.array([
    3.7,3.8,4.0,4.3,4.6,4.5,4.2,4.1,
    3.7,3.1,2.6,2.2,1.8,1.4,1.1,0.8,0.6
])

anos = ["2010", "2022"]

razao_dependencia = [60.2, 51.0]
indice_envelhecimento = [23.2, 42.0]

urbana = np.array([63.1, 68.5])
rural = np.array([36.9, 31.5])

periodos = ["1991-2000", "2000-2010", "2010-2022"]
taxas = [1.38, 1.17, 0.25]

# ==============================================================================
# GRÁFICO 1 - PIRÂMIDE ETÁRIA
# ==============================================================================

fig, ax = plt.subplots(figsize=(10,8))

ax.barh(
    faixas,
    -masc_2022,
    color="#4E79A7",
    edgecolor="black",
    label="Homens (2022)"
)

ax.barh(
    faixas,
    fem_2022,
    color="#E15759",
    edgecolor="black",
    label="Mulheres (2022)"
)

ax.plot(
    -masc_2010,
    faixas,
    linestyle="--",
    linewidth=2,
    color="black",
    label="2010"
)

ax.plot(
    fem_2010,
    faixas,
    linestyle="--",
    linewidth=2,
    color="black"
)

ax.axvline(0, color="black", linewidth=1)

ticks = ax.get_xticks()
ax.set_xticklabels([abs(round(x,1)) for x in ticks])

ax.set_xlabel("Percentual da população (%)")
ax.set_title("Pirâmide Etária Comparativa - Maranhão (2010 x 2022)")
ax.grid(axis="x", alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("grafico_piramide.png")
plt.close()

# ==============================================================================
# GRÁFICO 2 - INDICADORES DEMOGRÁFICOS
# ==============================================================================

fig, ax = plt.subplots(figsize=(8,5))

x = np.arange(len(anos))
largura = 0.35

b1 = ax.bar(
    x-largura/2,
    razao_dependencia,
    largura,
    color="#4E79A7",
    label="Razão de Dependência"
)

b2 = ax.bar(
    x+largura/2,
    indice_envelhecimento,
    largura,
    color="#F28E2B",
    label="Índice de Envelhecimento"
)

ax.bar_label(b1, fmt="%.1f")
ax.bar_label(b2, fmt="%.1f")

ax.set_xticks(x)
ax.set_xticklabels(anos)

ax.set_ylabel("Valor do indicador")
ax.set_title("Indicadores Demográficos")
ax.legend()
ax.grid(axis="y", alpha=.3)

plt.tight_layout()
plt.savefig("grafico_indicadores.png")
plt.close()

# ==============================================================================
# GRÁFICO 3 - POPULAÇÃO URBANA E RURAL
# ==============================================================================

fig, ax = plt.subplots(figsize=(7,5))

ax.bar(
    anos,
    urbana,
    color="#4E79A7",
    edgecolor="white",
    label="Urbana"
)

ax.bar(
    anos,
    rural,
    bottom=urbana,
    color="#59A14F",
    edgecolor="white",
    label="Rural"
)

for i in range(len(anos)):
    ax.text(
        i,
        urbana[i]/2,
        f"{urbana[i]}%",
        ha="center",
        va="center",
        color="white",
        fontsize=11,
        fontweight="bold"
    )

    ax.text(
        i,
        urbana[i]+rural[i]/2,
        f"{rural[i]}%",
        ha="center",
        va="center",
        color="white",
        fontsize=11,
        fontweight="bold"
    )

ax.set_ylim(0,100)
ax.set_ylabel("Percentual (%)")
ax.set_title("Distribuição da População Urbana e Rural")
ax.legend()

plt.tight_layout()
plt.savefig("grafico_urbano_rural.png")
plt.close()

# ==============================================================================
# GRÁFICO 4 - TAXA DE CRESCIMENTO POPULACIONAL
# ==============================================================================

fig, ax = plt.subplots(figsize=(8,5))

cores = ["#76B7B2", "#59A14F", "#E15759"]

barras = ax.bar(
    periodos,
    taxas,
    color=cores,
    width=0.5
)

ax.bar_label(barras, fmt="%.2f%%")

ax.set_ylabel("Taxa (%) ao ano")
ax.set_title("Taxa Geométrica de Crescimento Populacional")
ax.grid(axis="y", alpha=.3)

plt.tight_layout()
plt.savefig("grafico_crescimento.png")
plt.close()

# ==============================================================================
# GRÁFICO 5 - GRANDES GRUPOS ETÁRIOS
# ==============================================================================

grupos = ["0-14 anos", "15-59 anos", "60 anos ou mais"]

grupo2010 = [30.6, 62.3, 7.1]
grupo2022 = [23.3, 68.0, 8.7]

fig, ax = plt.subplots(figsize=(8,5))

x = np.arange(len(grupos))
largura = 0.35

b1 = ax.bar(
    x-largura/2,
    grupo2010,
    largura,
    color="#4E79A7",
    label="2010"
)

b2 = ax.bar(
    x+largura/2,
    grupo2022,
    largura,
    color="#E15759",
    label="2022"
)

ax.bar_label(b1, fmt="%.1f%%")
ax.bar_label(b2, fmt="%.1f%%")

ax.set_xticks(x)
ax.set_xticklabels(grupos)

ax.set_ylabel("Percentual da população")
ax.set_title("Estrutura Etária da População")
ax.legend()

plt.tight_layout()
plt.savefig("grafico_estrutura_etaria.png")
plt.close()

# ==============================================================================
# TABELA 1 - PIRÂMIDE ETÁRIA
# ==============================================================================

tabela_piramide = pd.DataFrame({
    "Faixa Etária": faixas,
    "Homens 2010 (%)": masc_2010,
    "Mulheres 2010 (%)": fem_2010,
    "Homens 2022 (%)": masc_2022,
    "Mulheres 2022 (%)": fem_2022
})

print("\n")
print("="*80)
print("TABELA 1 - PIRÂMIDE ETÁRIA")
print("="*80)
print(tabela_piramide)

tabela_piramide.to_excel("tabela_piramide.xlsx", index=False)

# ==============================================================================
# TABELA 2 - INDICADORES DEMOGRÁFICOS
# ==============================================================================

tabela_indicadores = pd.DataFrame({
    "Ano": anos,
    "Razão de Dependência": razao_dependencia,
    "Índice de Envelhecimento": indice_envelhecimento,
    "População Urbana (%)": urbana,
    "População Rural (%)": rural
})

print("\n")
print("="*80)
print("TABELA 2 - INDICADORES")
print("="*80)
print(tabela_indicadores)

tabela_indicadores.to_excel("tabela_indicadores.xlsx", index=False)

# ==============================================================================
# TABELA 3 - CRESCIMENTO POPULACIONAL
# ==============================================================================

tabela_crescimento = pd.DataFrame({
    "Período": periodos,
    "Taxa Geométrica (% ao ano)": taxas
})

print("\n")
print("="*80)
print("TABELA 3 - CRESCIMENTO POPULACIONAL")
print("="*80)
print(tabela_crescimento)

tabela_crescimento.to_excel("tabela_crescimento.xlsx", index=False)

# ==============================================================================
# TABELA 4 - VARIAÇÃO ENTRE 2010 E 2022
# ==============================================================================

tabela_variacao = pd.DataFrame({
    "Faixa Etária": faixas,
    "Variação Homens": np.round(masc_2022-masc_2010,2),
    "Variação Mulheres": np.round(fem_2022-fem_2010,2)
})

print("\n")
print("="*80)
print("TABELA 4 - VARIAÇÃO ENTRE 2010 E 2022")
print("="*80)
print(tabela_variacao)

tabela_variacao.to_excel("tabela_variacao.xlsx", index=False)

# ==============================================================================
# TABELA 5 - GRANDES GRUPOS ETÁRIOS
# ==============================================================================

tabela_grupos = pd.DataFrame({
    "Grupo Etário": grupos,
    "2010 (%)": grupo2010,
    "2022 (%)": grupo2022,
    "Variação": np.round(np.array(grupo2022)-np.array(grupo2010),2)
})

print("\n")
print("="*80)
print("TABELA 5 - GRANDES GRUPOS ETÁRIOS")
print("="*80)
print(tabela_grupos)

tabela_grupos.to_excel("tabela_grupos_etarios.xlsx", index=False)

print("\n")
print("="*80)
print("TODOS OS GRÁFICOS E TABELAS FORAM GERADOS COM SUCESSO!")
print("="*80)

print("""
Arquivos criados:

✓ grafico_piramide.png
✓ grafico_indicadores.png
✓ grafico_urbano_rural.png
✓ grafico_crescimento.png
✓ grafico_estrutura_etaria.png

✓ tabela_piramide.xlsx
✓ tabela_indicadores.xlsx
✓ tabela_crescimento.xlsx
✓ tabela_variacao.xlsx
✓ tabela_grupos_etarios.xlsx
""")