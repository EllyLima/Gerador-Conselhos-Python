# Gerador de Conselhos Aleatórios (Python) 🐍💡

Este é um script Python simples que consome uma **API pública** (Application Programming Interface) para buscar e exibir conselhos aleatórios no terminal.

## 🎯 Objetivo

Demonstrar conhecimentos fundamentais em Python, especificamente:
* Realizar requisições HTTP (GET) para serviços externos.
* Manipular dados no formato **JSON**.
* Tratamento básico de erros (try/except).

## ⚙️ Como Funciona

O script utiliza a API gratuita [Advice Slip JSON API](https://api.adviceslip.com/).
1.  O código faz uma requisição `GET` para a URL da API.
2.  A API retorna um objeto JSON contendo um ID e o texto do conselho.
3.  O script converte esse JSON para um dicionário Python e extrai apenas a frase do conselho para exibir ao usuário.

## 🚀 Como Rodar (Em sua máquina)

### Pré-requisitos
* Python instalado (versão 3.x).
* Biblioteca `requests` instalada.

### Passo a passo
1.  Clone este repositório.
2.  Instale a dependência:
    ```bash
    pip install requests
    ```
3.  Execute o script pelo terminal na pasta do projeto:
    ```bash
    python app.py
    ```

## 📂 Arquivo

* `app.py`: O código fonte principal em Python.

---
*Desenvolvido por Elly Lima como parte de estudos práticos em Python e APIs.*
