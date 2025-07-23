# 📌 MonitoramentoApresenta – Sistema de Monitoramento de Sustentabilidade

## 📝 Descrição
Projeto integrador desenvolvido no 1º semestre de Engenharia de Software, que permite monitorar indicadores de sustentabilidade (água, energia, resíduos e transporte) com:

    - Cadastro de dados diários.

    - Classificação automática (Alta/Moderada/Baixa sustentabilidade).

    - Criptografia dos dados de classificação (matriz 2x2).

    - Relatórios e médias de consumo.

## ⚙️ Funcionalidades
### ✔ CRUD Completo:

    - Cadastro, alteração e exclusão de registros.
    
    - Persistência em banco de dados MySQL.

### ✔ Classificação Automática:

    - Consumo de água (<150L = Alta, 150-200L = Moderada, >200L = Baixa).
    
    - Consumo de energia (<5kWh = Alta, 5-10kWh = Moderada, >10kWh = Baixa).
    
    - Resíduos reciclados (>80% = Alta, 50-80% = Moderada, <50% = Baixa).
    
    - Transporte (prioriza veículos sustentáveis).

### ✔ Criptografia:

    - Usa matrizes 2x2 para cifrar classificações (ex: "Alta" → "KZ").

### ✔ Relatórios:
    
    - Médias de consumo.
    
    - Visualização de dados brutos e classificações descriptografadas.

## 🛠️ Tecnologias Utilizadas
### Área Tecnologias
    - Back-end	
        - Python 3.13
    - Banco de Dados 
        - MySQL (mysql-connector-python)
    - Criptografia
        - Matrizes 2x2 (Hill Cipher simplificado)
    - Interface	
        - Terminal (CLI)

## 📦 Estrutura do Código
📂 projeto-sustentabilidade/
├── database/
│   ├── CriacaoBancoDados.sql
│   └── scripts/ (opcional para futuros scripts SQL)
├── src/
│   ├── Cripto.py
│   ├── MonitoramentoApresenta.py
│   └── modules/ (opcional para módulos extras)
├── docs/
│   └── README.md
├── .gitignore
└── LICENSE

### Principais Funções

    - cripto(texto):
        - Cifra textos usando matriz [[4, 3], [1, 2]].
        - Ex: "Alta" → "KZ".
        
    - descriptografia(texto_cifrado):
    
        - Decifra textos com a matriz inversa.
    
    - Classificação:
    
        - Lógica baseada em thresholds pré-definidos.

## 🚀 Como Executar
### Pré-requisitos:

    - Python 3.13 + MySQL.

    - Bibliotecas: mysql-connector-python.
## 📦 Configure o Banco de Dados:
📂 ProjetoIntegrador/
└── database/
    ├── CriacaoBancoDados.sql
    └── scripts/ (opcional para futuros scripts SQL)

### Execute o Sistema:
    - python MonitoramentoApresenta.py

## 🖥️ Menu do Sistema
    =============================================================
                    Bem Vindo ao Sistema de                    
                        Sustentabibilidade                      
    =============================================================
    1. Cadastro de Parâmetros Diários.
    2. Alteração de Parâmetros.
    3. Exclusão de Parâmetros.
    4. Classificação da Sustentabilidade.
    5. Média de Sustentabilidade.
    6. Sair.
        
## 📌 Melhorias Futuras
    - Interface web (Flask/Django).

    - Gráficos com matplotlib.

    - Dashboard com métricas em tempo real.

## 📄 Licença
    GNU General Public License v3.0.

## ✉️ Contato
    [João Paulo Ferreira] - [jpauloferreira2006@gmail.com]
    https://www.linkedin.com/in/jo%C3%A3o-paulo-ferreira-6a1ab8328/
