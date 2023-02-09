# Boas-vindas ao repositório do TING (Trybe is not Google)!
 - Implementa um programa que simula um algoritmo de indexação de documentos similar ao do Google.
 - Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT).
 - Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

## Ferramentas e bibliotecas utilizadas

- [![Python Badge](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)](https://docs.python.org/3/)

## Features

- [x] Implementa uma fila para armazenar os arquivos que serão lidos.
- [x] Implementa uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
- [x] Implementa a função process. Essa função é capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue.
- [x] Implementa uma função "remove" dentro do módulo file_process capaz de remover o primeiro arquivo processado.
- [x] Implementa uma função file_metadata dentro do módulo file_process capaz de apresentar as informações superficiais de um arquivo processado.
- [x] Implementa uma função exists_word, dentro do módulo word_search, que verifique a existência de uma palavra em todos os arquivos processados.
- [x] Implementa uma função search_by_word dentro do módulo word_search, que busque uma palavra em todos os arquivos processados.

## Pré-requisitos para rodar a aplicação

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: [![Python Badge](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)](https://docs.python.org/3/)

- Clone o repositório
~~~Java
git@github.com:DeividBorges93/project-TING.git
~~~

- Crie o ambiente virtual para o projeto
~~~Java
python3 -m venv .venv && source .venv/bin/activate
~~~

- Instale as dependências
~~~Java
python3 -m pip install -r dev-requirements.txt
~~~


:construction: README customizado em construção ! :construction:
