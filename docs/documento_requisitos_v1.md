# Documento de Requisitos (v1)

## 1. Introdução
Este documento descreve os requisitos funcionais e não funcionais para o desenvolvimento de um aplicativo de gerenciamento de finanças pessoais. O aplicativo tem como objetivo principal ajudar os usuários a registrar suas receitas e despesas, gerenciar suas finanças e gerar relatórios detalhados de suas transações.

## 2. Requisitos Funcionais

### 2.1. Cadastro de Transações
- **Descrição:** O sistema deve permitir que o usuário registre transações financeiras, sejam elas receitas ou despesas.
- **Entradas:**
  - Tipo de transação (Receita ou Despesa)
  - Categoria da transação (Ex: Alimentação, Transporte)
  - Valor da transação
  - Data (gerada automaticamente)
- **Saídas:** Confirmação de que a transação foi registrada com sucesso.
- **Regra de Negócio:** O sistema deve permitir a inserção de valores decimais no campo "Valor".

### 2.2. Visualização de Resumo Financeiro
- **Descrição:** O sistema deve exibir ao usuário um resumo financeiro com o saldo total, bem como a soma das receitas e despesas.
- **Entradas:** Nenhuma (dados são extraídos do banco de dados).
- **Saídas:** Exibição do resumo financeiro com:
  - Saldo total
  - Soma das receitas
  - Soma das despesas

### 2.3. Geração de Relatórios de Despesas
- **Descrição:** O sistema deve permitir que o usuário gere relatórios detalhados de suas despesas, categorizadas por tipo e data.
- **Entradas:**
  - Período de tempo para o relatório (Ex: Últimos 30 dias)
- **Saídas:** Relatório detalhado em formato texto, exibindo:
  - Categoria da despesa
  - Valor total gasto em cada categoria
  - Data das transações

### 2.4. Armazenamento Local
- **Descrição:** O sistema deve armazenar todas as transações localmente em um banco de dados SQLite.
- **Entradas:** Dados de transações (Receita ou Despesa).
- **Saídas:** Dados salvos no banco de dados.

## 3. Requisitos Não Funcionais

### 3.1. Usabilidade
- **Descrição:** O sistema deve ser simples e fácil de usar, com uma interface gráfica amigável, desenvolvida em Tkinter.
- **Critério de Aceitação:** Usuários devem ser capazes de registrar transações e visualizar o resumo financeiro sem dificuldade.

### 3.2. Desempenho
- **Descrição:** O sistema deve ser capaz de registrar transações e gerar relatórios sem atrasos perceptíveis para o usuário.
- **Critério de Aceitação:** O tempo de resposta para registrar uma transação ou gerar um relatório deve ser inferior a 2 segundos.

### 3.3. Segurança
- **Descrição:** Como o sistema utiliza armazenamento local, os dados financeiros dos usuários não devem ser enviados para servidores externos.
- **Critério de Aceitação:** Garantir que todas as transações e dados sejam armazenados localmente e não haja dependência de conexões de rede.

## 4. Casos de Uso

### Caso de Uso 1: Registrar uma Transação
- **Ator:** Usuário
- **Descrição:** O usuário registra uma transação financeira inserindo os dados necessários.
- **Fluxo Principal:**
  1. O usuário seleciona o tipo de transação (Receita ou Despesa).
  2. O usuário insere a categoria, valor e confirma.
  3. O sistema registra a transação no banco de dados e exibe uma mensagem de sucesso.
- **Fluxo Alternativo:** Se algum campo estiver vazio, o sistema exibirá uma mensagem de erro solicitando a inserção dos dados.

### Caso de Uso 2: Visualizar Resumo Financeiro
- **Ator:** Usuário
- **Descrição:** O usuário solicita a visualização do resumo financeiro.
- **Fluxo Principal:**
  1. O sistema calcula o saldo total com base nas transações cadastradas.
  2. O sistema exibe o saldo total, a soma das receitas e despesas.

### Caso de Uso 3: Gerar Relatório de Despesas
- **Ator:** Usuário
- **Descrição:** O usuário gera um relatório detalhado de suas despesas.
- **Fluxo Principal:**
  1. O usuário seleciona o período para o relatório.
  2. O sistema gera e exibe o relatório detalhado por categoria e data.
  
## 5. Restrições

- O sistema será desenvolvido para ambientes desktop, com suporte para Python e SQLite.
- O sistema deve ser utilizado localmente e não requer acesso à internet.
- O sistema não terá integração com serviços de nuvem ou servidores externos.

## 6. Versões Futuras
Em versões futuras, poderão ser implementadas funcionalidades como:
- **Exportação de Relatórios:** Exportar relatórios em formatos como PDF ou CSV.
- **Gráficos e Dashboards:** Exibição gráfica dos gastos e receitas para facilitar a análise visual.
- **Multiusuário:** Suporte a múltiplos perfis de usuário com separação de dados.

