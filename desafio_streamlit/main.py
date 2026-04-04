import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Funcionários",
    layout="wide"
)

@st.cache_data
def carregar_dados():
    dados = {
        "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
        "idade": [23, 35, 29, np.nan, 40],
        "cidade": ["SP", "RJ", "SP", "MG", "RJ"],
        "salario": [3000, 5000, 4000, 3500, np.nan],
        "data_contratacao": pd.to_datetime(["2020-01-10", "2019-03-15", "2021-07-22", "2022-11-01", "2018-05-20"])
    }

    df = pd.DataFrame(dados)

    df["idade"] = df["idade"].fillna(df["idade"].mean())
    df["salario"] = df["salario"].fillna(df["salario"].median())

    df["salario_anual"] = df["salario"] * 12
    df["ano_contratacao"] = df["data_contratacao"].dt.year
    df["categoria_salario"] = df["salario"].apply(
        lambda x: "Alto" if x > 4500 else "Médio" if x > 3000 else "Baixo"
    )

    return df

# DESAFIO DIFÍCIL: Faça o upload de CSV substituir os dados de exemplo e aplique os mesmos filtros no arquivo enviado.
st.sidebar.header("📂 Upload de CSV")
uploaded_file = st.sidebar.file_uploader(
    "Envie um CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = carregar_dados()

st.sidebar.header("🔎 Filtros")

cidades = st.sidebar.multiselect(
    "Selecione a cidade",
    options=df["cidade"].unique(),
    default=df["cidade"].unique()
)

faixa_salario = st.sidebar.slider(
    "Faixa salarial",
    float(df["salario"].min()),
    float(df["salario"].max()),
    (float(df["salario"].min()), float(df["salario"].max()))
)

# DESAFIO FÁCIL: Adicione um filtro de selectbox para a coluna categoria_salario na sidebar.
opcoes_categoria = ["Todas"] + list(df["categoria_salario"].unique())
categoria_selecionada = st.sidebar.selectbox(
    "Categoria Salarial",
    options=opcoes_categoria
)

df_filtrado = df[
    (df["cidade"].isin(cidades)) &
    (df["salario"] >= faixa_salario[0]) &
    (df["salario"] <= faixa_salario[1])
    ]

if categoria_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["categoria_salario"] == categoria_selecionada]

st.title("📊 Dashboard de Análise de Funcionários")

col1, col2, col3 = st.columns(3)

if not df_filtrado.empty:
    col1.metric("💰 Salário Médio", f"R$ {df_filtrado['salario'].mean():.2f}")
    col2.metric("👥 Total Funcionários", df_filtrado.shape[0])
    col3.metric("📈 Salário Máximo", f"R$ {df_filtrado['salario'].max():.2f}")
else:
    col1.metric("💰 Salário Médio", "R$ 0.00")
    col2.metric("👥 Total Funcionários", 0)
    col3.metric("📈 Salário Máximo", "R$ 0.00")

st.subheader("📋 Dados")
st.dataframe(
    df_filtrado,
    use_container_width=True
)

st.subheader("📊 Análises")

# DESAFIO MÉDIO: Substitua bar_chart por um gráfico Plotly com cores por categoria e tooltip customizado.
if not df_filtrado.empty:
    fig = px.bar(
        df_filtrado,
        x="cidade",
        y="salario",
        color="categoria_salario",
        title="Salário por Cidade e Categoria",
        barmode="group",
        hover_data={"salario": ':.2f', "nome": True, "cidade": False}
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("🔀 Tabela Dinâmica")

if not df_filtrado.empty:
    pivot = pd.pivot_table(
        df_filtrado,
        values="salario",
        index="cidade",
        columns="categoria_salario",
        aggfunc="mean"
    )
    st.dataframe(pivot)

st.divider()

if not df_filtrado.empty:
    csv = df_filtrado.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name="dados_filtrados.csv",
        mime="text/csv"
    )