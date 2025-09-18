# 🤖 Automação de Cadastro de Produtos com Python e PyAutoGUI

Este projeto demonstra como utilizar Python, a biblioteca PyAutoGUI e o Pandas para automatizar o processo de login em um sistema web e realizar o cadastro de produtos a partir de uma planilha CSV.

---

## 📌 Tecnologias utilizadas

- Python
- PyAutoGUI → automação de teclado e mouse.
- Pandas → leitura e manipulação da base de dados (csv).
- Time → controle de tempo e pausas entre ações.

---


## 🚀 Passos da Automação

### 🔹 Passo 1: Acessar o sistema da empresa
- O código abre o Google Chrome, digita a URL do sistema de login e aguarda alguns segundos para que a página carregue.

---

### 🔹 Passo 2: Realizar login
- Preenche o e-mail (pythonimpressionador@gmail.com).
- Preenche uma senha genérica.
- Clica no botão 'Logar' para acessar o sistema.

---

### 🔹 Passo 3: Importar a base de produtos
- Com a biblioteca *#Pandas* importamos a base csv 'produtos'.
- Cada linha da tabela representa um produto a ser cadastrado.

---

### 🔹 Passo 4: Cadastrar os produtos
- O cadastro é feito de forma automática e repetitiva utilizando um laço de repetição *#for*.
- O *#for* percorre todas as linhas da tabela.

- Para cada linha (ou seja, para cada produto):
  - O script clica no 1° campo do formulário,
  - Extrai os valores da planilha de forma ordenada,
  - Preenche cada campo automaticamente.

- Usamos também uma estrutura condicional *#if* para caso exista uma observação na base de dados que seja diferente de *#NaN*, a automação preencha o campo, caso contrário, pressiona *#tab*.

---

### ⚠️ Observações Importantes ⚠️

- As coordenadas *(x, y)* usadas no *pyautogui.click()* são específicas da tela do desenvolvedor. Ao executar em outro computador, pode ser necessário ajustar esses valores.

- O arquivo produtos.csv deve estar salvo na mesma pasta do script.

- Como a automação interage diretamente com a tela, não mova o mouse nem digite durante a execução para evitar erros.

- Pode ser necessário aumentar os tempos de espera *(time.sleep)* caso sua internet seja mais lenta.
