# 📊 Dashboard de Análise de Funcionários

Este é um projeto prático de Dashboard construído 100% em Python utilizando o framework **Streamlit**. O aplicativo permite a visualização interativa, filtragem e exportação de dados de funcionários, além de suportar o upload de bases de dados customizadas.

## ✨ Funcionalidades

* **Upload de Dados:** Permite o envio de arquivos `.csv` para substituir os dados de exemplo em tempo real.
* **Filtros Interativos:** Barra lateral (sidebar) com múltiplos filtros integrados:
  * Seleção múltipla de Cidades.
  * Slider de faixa salarial.
  * Selectbox para Categoria Salarial (Alto, Médio, Baixo).
* **KPIs Dinâmicos:** Cartões de métricas mostrando Salário Médio, Total de Funcionários e Salário Máximo, que se atualizam automaticamente conforme os filtros aplicados.
* **Gráficos Avançados:** Utilização da biblioteca `Plotly Express` para renderizar gráficos de barras interativos (com tooltip customizado).
* **Tabela Dinâmica (Pivot Table):** Cruzamento automático de dados entre cidades e categorias salariais.
* **Exportação:** Botão para download dos dados filtrados em formato `.csv`.

## 🛠️ Tecnologias Utilizadas

* [Python 3.x](https://www.python.org/)
* [Streamlit](https://streamlit.io/) - Para a interface web e reatividade.
* [Pandas](https://pandas.pydata.org/) - Para manipulação e limpeza de dados.
* [NumPy](https://numpy.org/) - Para operações numéricas auxiliares.
* [Plotly](https://plotly.com/python/) - Para visualizações de dados interativas.

## 🚀 Como Instalar e Executar

1. **Clone ou baixe este repositório** para a sua máquina local.
2. **Abra o terminal** na pasta do projeto.
3. **Instale as dependências** necessárias executando o comando:
   ```bash
   pip install streamlit pandas numpy plotly
   ```
4. **Inicie o servidor do Streamlit** com o comando abaixo:
   ```bash
   streamlit run main.py
   ```
   *(O dashboard abrirá automaticamente no seu navegador padrão, geralmente no endereço `http://localhost:8501`)*

> **⚠️ Atenção:** Não utilize atalhos da sua IDE (como o `F5` no PyCharm ou VSCode) para rodar este arquivo como um script comum de Python. O Streamlit precisa ser inicializado via terminal para levantar o servidor web e criar o contexto de execução correto.

## 📁 Estrutura do Código

* **`main.py`**: Arquivo principal contendo toda a lógica do dashboard.
  * `carregar_dados()`: Função com cache (`@st.cache_data`) que gera os dados mockados, faz a limpeza de valores nulos (NaN) e cria colunas calculadas (Feature Engineering).
  * Construção da Sidebar (Upload e Filtros).
  * Renderização do Layout Principal (Métricas, Gráficos e Tabelas).
