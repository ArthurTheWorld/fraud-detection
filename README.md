# Sistema de Deteccao de Fraudes Bancarias

Modelo de machine learning para deteccao de transacoes fraudulentas, com interface interativa construida em Streamlit. O projeto atingiu 94% de acuracia na identificacao de fraudes em transacoes financeiras.

---

## Sobre o Projeto

Este projeto aplica tecnicas de ciencia de dados e aprendizado de maquina para identificar padroes suspeitos em transacoes bancarias. A partir de um dataset real com milhoes de transacoes, foram realizadas etapas de pre-processamento, feature engineering, selecao e avaliacao de modelos, resultando em um pipeline treinado e servido via interface web.

---

## Funcionalidades

- Classificacao de transacoes como fraude ou legitima em tempo real
- Interface web interativa via Streamlit
- Suporte a 5 tipos de transacao: Pagamento, Transferencia, Saque, Debito e Deposito
- Pipeline de ML serializado com joblib para inferencia rapida

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3.x | Linguagem principal |
| Pandas | Manipulacao e analise de dados |
| Scikit-learn | Treinamento do modelo e pipeline |
| Matplotlib | Visualizacao exploratoria |
| Streamlit | Interface web |
| Joblib | Serializacao do modelo |

---

## Estrutura do Projeto

```
ProjetoFraude/
├── app.py                          # Interface Streamlit
├── pipeline_detecçao_fraude.pkl    # Modelo treinado
├── notebook.ipynb                  # Analise exploratoria e treinamento
├── requirements.txt                # Dependencias do projeto
└── README.md
```

O dataset nao esta incluido no repositorio por exceder o limite de tamanho do GitHub (470 MB). Faca o download pelo link abaixo.

---

## Dataset

Fraud Detection Dataset — disponivel no Kaggle:

https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

Apos o download, coloque o arquivo CSV na pasta `Dataframe/` na raiz do projeto.

---

## Como Executar

1. Clone o repositorio:
```bash
git clone https://github.com/ArthurTheWorld/ProjetoFraude.git
cd ProjetoFraude
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependencias:
```bash
pip install -r requirements.txt
```

4. Execute a aplicacao:
```bash
streamlit run app.py
```

---

## Resultados

- Precisão: 94%
- Modelo treinado com tecnicas de balanceamento de classes e feature engineering sobre diferencas de saldo (balanceDiffOrig, balanceDiffDest)




