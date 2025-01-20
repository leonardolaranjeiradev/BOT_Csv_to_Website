# Automação de Preenchimento de Formulário com PyAutoGUI

Este projeto utiliza a biblioteca `PyAutoGUI` para automatizar o processo de preenchimento de um formulário web, baseado em dados de um arquivo CSV. A automação simula ações como digitação, cliques e navegação, economizando tempo e reduzindo erros manuais.

## Tecnologias Utilizadas

- **Python**
- **PyAutoGUI**: Automação de tarefas
- **Pandas**: Manipulação e leitura de arquivos CSV
- **Time**: Controle de pausas durante a execução

## Objetivo

Automatizar o processo de login em um site e o preenchimento de campos de formulário com dados fornecidos em um arquivo `produtos.csv`. A automação realiza:
- Login no sistema.
- Preenchimento de campos como código, marca, tipo, categoria, preço unitário, custo e observações.
- Submissão de cada formulário e repetição para todos os registros do arquivo.

## Estrutura do Código

### 1. Configuração Inicial
- **Definição de pausas automáticas** com `pyautogui.PAUSE`.
- Navegação para o navegador e o site especificado.

### 2. Login Automático
- Preenchimento dos campos de login e senha utilizando coordenadas específicas de clique e ações de teclado.

### 3. Leitura do Arquivo CSV
- O arquivo `produtos.csv` contém os dados a serem inseridos no formulário.

### 4. Preenchimento Automático
- Para cada linha do arquivo, os campos são preenchidos automaticamente com as informações correspondentes, como:
  - Código do produto
  - Marca
  - Tipo
  - Categoria
  - Preço unitário
  - Custo
  - Observações (quando disponíveis)
- O formulário é submetido após o preenchimento.
