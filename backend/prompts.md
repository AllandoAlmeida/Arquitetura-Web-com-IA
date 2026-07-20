# Prompts - Aula 1 (chat-1)

1. De forma resumida explique para mim o que cada um destes arquivos faz

2. Crie um readme.md do projeto que explique o seu objetivo e as funcionalidades dos arquivos envolvidos

3. Em que parte do projeto estâo definidas as cores utilizadas?

4. Dentro do bloco root do arquivo @[style.css] modifique o esquema de cores para variações da cor magenta


# Prompts - Aula 2

1. Crie um ambiente virtual em Python usando a venv e faça a ativação

2. Instale o uvicorn na venv deste projeto

3. Você vai criar o primeiro servidor de uma API de álbum de figurinhas.

   Crie um arquivo main.py com um servidor FastAPI que tenha apenas 1 endpoint:

   1. GET "/" → retorna o JSON {"mensagem": "Olá, mundo! 🌍"}
      (use uma função chamada hello_world)

   Requisitos:
   - Use apenas Python com FastAPI (import: from fastapi import FastAPI)
   - Crie a aplicação com app = FastAPI()
   - Adicione comentários em português explicando cada parte
   - Não adicione nenhum outro endpoint

4. No mesmo arquivo main.py, adicione um segundo endpoint, mantendo o endpoint "/" que já existe:

   2. GET "/figurinhas" → retorna uma lista com 2 figurinhas de exemplo
      (use uma função chamada listar_figurinhas)
      Cada figurinha é um objeto com os campos:
        - id (número inteiro)
        - nome (texto)
        - categoria (texto)
      Use estas duas figurinhas:
        - {id: 1, nome: "Alan Turing",   categoria: "IA"}
        - {id: 2, nome: "John McCarthy", categoria: "IA"}

   Requisitos:
   - Mantenha tudo que já existe no arquivo
   - Adicione comentários em português
   - Não adicione nenhum endpoint além desses dois

# Prompts - Aula 3

1. Evolua o servidor da API de álbum de figurinhas para também servir
   as imagens das figurinhas como arquivos estáticos.

   Atualize o arquivo main.py com um servidor FastAPI que:

   1. Use a aplicação com app = FastAPI()

   2. Defina o caminho absoluto da pasta de imagens (para o servidor encontrar
      a pasta independente de onde for executado):
        PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
        PASTA_IMAGENS = os.path.join(PASTA_BASE, "imagens")

   3. Configure os arquivos estáticos: "monte" a pasta PASTA_IMAGENS na rota "/imgs"
      usando StaticFiles, com name="imgs".
      Assim, "figurinhas/01-alan-turing.jpg" fica acessível em "/imgs/01-alan-turing.jpg".

   4. Tenha uma lista chamada "imagens" com 2 itens, cada um com os campos
      id, nome, categoria e imagem_url:
        - {id: 1, nome: "Alan Turing",   categoria: "IA", imagem_url: "/imgs/01-alan-turing.jpg"}
        - {id: 2, nome: "John McCarthy", categoria: "IA", imagem_url: "/imgs/02-john-mccarthy.jpg"}

   5. Tenha apenas um endpoint: GET "/figurinhas" (função listar_figurinhas)
      que retorna a lista de figurinhas.

   Requisitos:
   - Use Python com FastAPI
   - Adicione comentários em português explicando cada parte
   - Imports necessários:
       from fastapi import FastAPI
       from fastapi.staticfiles import StaticFiles
       import os