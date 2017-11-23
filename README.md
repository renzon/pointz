# pointz
Prova de conceito para geração de relatório com BigQuery

## Como usar

Instalação
1. Instale python >= 3.6
2. Instale a lib com
    
   pip install pointz

## Variáveis de ambiente   
3. Sete as variáveis de ambiente BIGQUERY_SECRET_JSON com path para chave secreta do BigQuery
4. Sete as variáveis de ambiente DATABASE_URL com url do seu banco SQL Server

Opcionalmente vc pode criar um arquivo .env na raiz do projeto. Confira contrib/env-sample com exemplo

## Gerando DREs

5. Rode generate_dre para gerar os relatórios
6. Rode load_data para carregar dados do SQL Server no BigQuery e gerar os relatórios   
   
    
