# Mercado Livre Ofertas - ETL e Análise

O projeto consiste na extração dos dados das ofertas do mercado livre, no tratamento e na carga dos dados. Por fim, foi realizado uma análise dos dados com um dashboard interativo.

Os dados foram retirados da página de ofertas do site de comercio digital mercado livre. O conjunto de dados foi dividido em duas tabelas, produtos e categoria.

Na tabela de produtos possui informações como sua imagem, o link de acesso, o preço, descontos, etc. Na tabela de categorias possui informações como link de acesso para aquele filtro, total de itens e o título da categoria.

## Sobre os dados

A análise foi realizada retirando os dados do site **[mercado livre]("https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1)**.

## Dashboard:

No dashboard, pode-se conferir quais os indicadores existem para um melhor entendimento.

**[Clique para ver o dashboard](https://mercadolivreetlofertas.streamlit.app/)**

## Atualização dos dados

Os dados são atualizados 1x por dia.

## Ferramentas

- **Python**: Linguagem utilizada no projeto.
- **Beautiful Soup**: Biblioteca para realizar do webscraping.
- **Pandas**: Biblioteca utilizada para tratamento e manipulação da base.
- **Streamlit**: Biblioteca utilizada para desenvolvimento do dashboard.
- **SQLite**: Banco de dados utilizado para armazenamento dos dados.
- **Github Actions**: Automação do ETL do projeto.

## Como executar o projeto

Para executar o projeto, siga os passos:

1. Clonar o repositório

```
git clone https://github.com/LucasMarchesoni/mercado_livre_etl_ofertas.git
```

2. Criar um ambiente virtual e ativar:

```
python -m venv .venv
.venv\Scripts\activate
```

3. Instalação das dependências:

```
pip install  -r requirements.txt
```

4. Execução do ETL (recomendado fazer uma vez ao dia):

```
python etl/etl.py
```

5. Iniciar o Streamlit:

```
streamlit run 1_sobre.py
```
