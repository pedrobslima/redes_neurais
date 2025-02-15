# Projeto da disciplina de Redes Neurais (IF702)


## Informações:

Arquivos:
    `customer_churn_telecom_services.csv`: Arquivo do dataset
    `projet_rn.ipynb`: Arquivo do código executado para o projeto 

## Dicionário do Dataset:

Atributos de entrada:
- gender:	Customer's gender (Male/Female)
- SeniorCitizen:	Indicates if the customer is a senior citizen (1 = Yes, 0 = No)
- Partner:	Whether the customer has a partner (Yes/No)
- Dependents:	Whether the customer has dependents (Yes/No)
- tenure:	Number of months the customer has stayed with the company
- PhoneService:	Whether the customer has a phone service (Yes/No)
- MultipleLines:	Whether the customer has multiple phone lines (No, Yes, No phone service)
- InternetService:	Type of internet service (DSL, Fiber optic, No)
- OnlineSecurity:	Whether the customer has online security (Yes, No, No internet service)
- OnlineBackup:	Whether the customer has online backup (Yes, No, No internet service)
- DeviceProtection:	Whether the customer has device protection (Yes, No, No internet service)
- TechSupport:	Whether the customer has tech support (Yes, No, No internet service)
- StreamingTV:	Whether the customer has streaming TV (Yes, No, No internet service)
- StreamingMovies:	Whether the customer has streaming movies (Yes, No, No internet service)
- Contract:	Type of contract (Month-to-month, One year, Two year)
- PaperlessBilling:	Whether the customer has paperless billing (Yes/No)
- PaymentMethod:	Payment method used (Electronic check, Mailed check, Bank transfer, Credit card)
- MonthlyCharges:	Monthly charges the customer pays
- TotalCharges:	Total amount charged to the customer

Atributo alvo:
- Churn:	Whether the customer has churned (Yes/No)


## Descrição do projeto:

- Conjunto de classificadores disponíveis:
    - Perceptron multicamadas (MLP)
    - Kolmogorov Arnold Networks (KANs).
    - Modelo Baseado em Transformer (STab) 2024 (em preparação)
    - KAN Transformer (TabKANet) 2024 (em preparação)
    - Random Forest (usado para comparação)
    - Gradient Boosting (usado para comparação)

- Investigar diferentes topologias da rede e diferentes valores
    dos parâmetros (básico):
    - Número de camadas
    - Número de unidades intermediárias
    - Variação da taxa de aprendizagem
    - Função de ativação (logistica, tangent hiperbolica, Relu)
    - Otimização: Adam, Drop-out, Regularização
    - Usar método de amostragem básica (repetitive oversampling)

- Parâmetros adicionais que podem ser explorados:
    - Algoritmo de aprendizagem
    - Taxa de aprendizagem adaptativa
    - Outros

### Preparação de dados (divisão e balanceamento)
- Conjuntos de dados
- Treinamento
    - Validação (separar amostra do Treinamento)
    - Teste (separar amostra do Treinamento)
- Estatisticamente representativos e independentes
    - Nenhuma informação do conjunto de teste pode interferir nos conjuntos de treinamento e validação (ex: identificação do mínimo e máximo para normalização). (vazamento de dados)
    - Não pode haver sobreposição (contaminação)

### Avaliação de Desempenho
- Classificação
    - Teste estatístico Kolmogorov-Smirnov 
        - KS (principal) 
        - MSE (erro médio quadrado)
    - Matriz de confusão
    - Auroc (Área sob a Curva Roc)
    - Recall, Precision e F-Measure

### Experimentos
- Pré-processamento da base de dados
    - Tratamento de dados ausentes, se houver (missing data)
    - Remoção de ruídos (outliers), se houver
    - Remoção de inconsistências, se houver
    - Normalização
    - Codificação
    - Transformação de variáveis
    - Criação de variáveis agregadas
- Importante
    - Registrar o desempenho de forma evolutiva, a cada etapa. Não
    elimine váriáveis no primeiro modelo (a não ser identificadores)

- Recomendação:
    - Iniciar com um modelo MLP e um modelo
    Random Forest
    - Após bom desempenho com esses modelos,
    experimentar os demais
    - KANs, Transformer (tentativo), KAN
    Transformer (tentativo)
    - Gradient boosting.

### Ferramentas para o projeto

- Código em Python
    - https://github.com/RomeroBarata/IF702-redes-neurais

- Pode usar qualquer biblioteca, preocupando-se apenas de garantir que está executando corretamente os experimentos e análise de performance (exemplo, usar função do KS que meça corretamente os valores, comparar com os gráficos dos slides neste ppt)
- Conjuntos de dados do problema
    - Arquivo obtido do Kaggle

### Lições aprendidas

- Comece com uma rede pequena: 1 camada, 10 unidades (a melhor rede é a menor rede que resolve bem o problema: navalha de Occam)
- Definir numero de epocas maximo em 10mil! Usar o critério de parada baseado no Patience (Max Fail = 20)
- Taxas de aprendizagem menores requerem mais tempo mas tendem a gerar melhores resultados
- Fazer backup automático
- Começar cedo, se deixar para ultimo mês, não vai sair!
- Considerar Optuna pode ser uma boa estratégia, caso contrário use gridsearch

### Resultados do projeto

- Apresentação com todos do grupo com estrutura experimental e interpretação dos resultados
- Entrega no final do semestre (PPT e código)