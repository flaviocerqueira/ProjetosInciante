# 💰 Controle Financeiro Pessoal em Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Projeto desenvolvido em Python para controle financeiro pessoal via terminal, permitindo o registro de receitas e despesas, visualização de movimentações e cálculo automático de saldo, com persistência de dados em arquivo JSON.

## 📌 Funcionalidades

- Adicionar receitas
- Adicionar despesas
- Listar movimentações financeiras
- Calcular saldo atual
- Persistência de dados em arquivo (`JSON`)
- Validação de entradas do usuário

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Biblioteca padrão `json`

## 📂 Estrutura do projeto

* ├── main.py
* ├── menu.py
* ├── operacoes.py
* ├── dados.py
* ├── movimentacoes.json
* └── README.md


### Descrição dos arquivos

- **main.py**  
  Ponto de entrada da aplicação. Controla o fluxo principal e a interação entre os módulos.

- **menu.py**  
  Responsável pela interface com o usuário e validação das opções do menu.

- **operacoes.py**  
  Contém as regras de negócio: cadastro de receitas e despesas, listagem de movimentações e cálculo do saldo.

- **dados.py**  
  Responsável pela persistência dos dados, realizando leitura e gravação no arquivo JSON.

- **movimentacoes.json**  
  Arquivo onde as movimentações financeiras são armazenadas.

## ▶️ Como executar o projeto

1. Certifique-se de ter o Python 3 instalado:
   ```bash
   python --version
2. Clone ou baixe este repositório.
3. No terminal, navegue até a pasta do projeto e execute:
    ```bash
    python main.py

## 🚀 Melhorias futuras
* Relatórios mensais
* Filtro por categoria
* Geração de gráficos
* Exportação para Excel
* Interface gráfica

## 👨‍💻 Autor

Flávio Silva Cerqueira

Projeto desenvolvido com fins educacionais e de aprendizado em Python.