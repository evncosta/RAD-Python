# 🧮 API de Calculadora com FastAPI

Esta é uma API simples e intuitiva construída com [FastAPI](https://fastapi.tiangolo.com/) para realizar operações matemáticas básicas (soma, subtração, multiplicação e divisão). O projeto conta com rotas para cálculo via URL (GET) e tratamento de erros (como divisão por zero).

---

## 🚀 Tecnologias Utilizadas

* **Python 3.7+**
* **FastAPI:** Framework web rápido e moderno para construção da API.
* **Uvicorn:** Servidor de alta performance para rodar a aplicação.

---

## ⚙️ Como Instalar e Rodar o Projeto

1. **Clone ou baixe** este repositório para o seu computador.
2. Certifique-se de ter o Python instalado.
3. Abra o terminal na pasta do projeto e instale as dependências:
   ```bash
   pip install fastapi uvicorn
   ```
4. Salve o código principal em um arquivo chamado `main.py`.
5. Inicie o servidor local com o Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
6. O terminal indicará que o servidor está rodando, geralmente no endereço: `http://127.0.0.1:8000`.

---

## 🎮 Como Utilizar a Calculadora

Você tem duas formas de interagir com esta API:

### 1. Usando a Documentação Interativa (Swagger UI) - *Recomendado* ⭐

O FastAPI gera automaticamente uma página visual para você testar a sua API sem precisar escrever nenhuma linha de código extra ou usar ferramentas externas.

**Passo a passo:**

1. Com o servidor rodando, abra o seu navegador e acesse: **`http://127.0.0.1:8000/docs`**
2. Você verá a interface do Swagger. Clique na barra verde **`GET /`** para expandi-la.
3. No canto superior direito da caixa expandida, clique no botão **"Try it out"** (Testar).
4. As caixas de texto ficarão editáveis. Digite os valores para:
* `a` (ex: 10)
* `b` (ex: 5)
* `tipo` (ex: soma, subtração, multiplicação, divisão)


5. Clique no botão azul escrito **"Execute"**.
6. Role um pouco a página para baixo e você verá a resposta da API na seção **"Server response"** (Resposta do servidor), mostrando o resultado matemático em formato JSON.

### 2. Usando a URL Direta (Navegador)

Você pode fazer a requisição diretamente pela barra de endereços do navegador montando os parâmetros:
**`http://127.0.0.1:8000/?a=20&b=4&tipo=divisao`**

---

## 🛡️ Tratamento de Erros

A API é inteligente o suficiente para barrar operações inválidas e avisar o usuário. Ela valida:

* Se os parâmetros enviados são realmente números.
* Se os campos obrigatórios foram preenchidos.
* Prevenção contra erro de divisão por zero.
* Nomes de operações inválidos.
