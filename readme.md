# Projeto de Coleta de Dados - Trabalho 2

Este projeto tem como objetivo coletar dados de campeões do jogo League of Legends e disponibilizá-los através de uma API. O projeto foi desenvolvido com base na disciplina de coleta de dados e tem como autores: Eduardo Tomacheski, Eduardo Rubin, Enzo Stefanello.

## Como Rodar o Projeto

1. Clone o repositório para sua máquina local.
2. Crie um ambiente virtual utilizando o conda:
    ```sh
    conda create --name meu_ambiente --file requirements.txt
    ```
3. Ative o ambiente:
    ```sh
    conda activate meu_ambiente
    ```
4. Execute o com o comando abaixo:
    ```sh
    flask --app app run
    ```

## Endereço Web

O projeto está disponível no seguinte endereço web: [https://api-champions-lol.onrender.com](https://api-champions-lol.onrender.com)

## Collection do Postman

Você pode encontrar a collection do Postman para testar a API no diretório `./Champios api.postman_collection`.

## Notebook de Utilização da API

Temos um notebook que consome a API criada, disponível em `./utilizando-api.ipynb`.