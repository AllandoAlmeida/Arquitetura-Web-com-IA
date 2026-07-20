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

# Prompts - Aula 4

Você vai criar a versão final do servidor da API de álbum de figurinhas. Ele precisa liberar acesso ao frontend (CORS), listar as figurinhas e entregar a imagem de cada uma por um próprio endpoint.

Crie um arquivo main.py com um servidor FastAPI que:

Configure o middleware CORS para aceitar requisições de qualquer origem

Defina caminhos absolutos para a pasta de imagens usando: PASTA_BASE = os.path.dirname(os.path.abspath( file )) PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

Crie uma lista chamada figurinhascom as 30 figurinhas, cada uma com: id, nome, categoria, imagem_url O imagem_url deve apontar para "/figurinhas/{id}/imagem" Comente as figurinhas que ainda não estão disponíveis (ex: ids 3, 4, 5...) Deixe ativas apenas as figurinhas cujas imagens existem na pasta figurinhas/

Crie o endpoint GET "/figuras" que retorna a lista

Crie o endpoint GET "/figurinhas/{id}/imagem" que:

Use glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
Retornar 404 se não encontrar
Retorna FileResponse com o arquivo encontrado
Importações necessárias: from fastapi import FastAPI, HTTPException from fastapi.responses import FileResponse from fastapi.middleware.cors import CORSMiddleware import os import glob


## Prompt ajustado

Você vai **evoluir o arquivo `main.py` existente** de uma API de álbum de figurinhas feita com FastAPI.

Não recrie o projeto do zero e não substitua a lógica atual desnecessariamente. Preserve:

* A pasta física chamada `imagens`;
* As variáveis `PASTA_BASE` e `PASTA_IMAGENS`;
* A categoria padrão `CATEGORIA = "IA"`;
* A criação automática da lista `imagens`;
* O `for` que percorre os arquivos existentes na pasta;
* A extração automática do nome a partir do nome do arquivo;
* O endpoint atual `GET /images`;
* Os comentários existentes sempre que possível.

O código atual já percorre automaticamente os arquivos da pasta `imagens`, portanto **não crie manualmente uma lista com as 30 figurinhas e não comente IDs individualmente**.

Ajuste o arquivo existente para adicionar as seguintes funcionalidades:

### 1. Configurar CORS

Importe:

```python
from fastapi.middleware.cors import CORSMiddleware
```

Adicione o middleware CORS logo depois da criação da aplicação:

```python
app = FastAPI()
```

O CORS deve permitir:

* Requisições de qualquer origem;
* Todos os métodos HTTP;
* Todos os cabeçalhos;
* Credenciais.

### 2. Preservar os caminhos atuais

Continue utilizando:

```python
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "imagens")
```

Não altere o nome da pasta para `figurinhas`.

### 3. Manter a geração automática da lista

Continue preenchendo a lista `imagens` por meio de:

```python
for indice, arquivo in enumerate(
    sorted(os.listdir(PASTA_IMAGENS)),
    start=1
):
```

Apenas arquivos de imagem devem ser adicionados à lista.

Considere como imagens válidas as extensões:

```python
.jpg
.jpeg
.png
.webp
.avif
```

A extensão deve ser validada sem diferenciar letras maiúsculas e minúsculas.

### 4. Utilizar o número do arquivo como ID

Os arquivos possuem nomes como:

```text
01-alan-turing.jpg
02-john-mccarthy.jpg
13-Michael.webp
28-Vinicius.png
```

O campo `id` deve ser obtido a partir do número existente no início do nome do arquivo, e não pelo índice do `enumerate`.

Exemplo:

```python
id_figura = int(nome_sem_extensao.split("-", 1)[0])
```

Isso é importante porque podem existir números ausentes ou arquivos com extensões diferentes.

### 5. Ajustar a URL da imagem

No dicionário de cada item, altere:

```python
"imagem_url": f"/imgs/{arquivo}"
```

para:

```python
"imagem_url": f"/figurinhas/{id_figura}/imagem"
```

A estrutura de cada item deve continuar assim:

```python
{
    "id": id_figura,
    "nome": nome,
    "categoria": CATEGORIA,
    "imagem_url": f"/figurinhas/{id_figura}/imagem"
}
```

### 6. Manter o endpoint da lista

Preserve o endpoint:

```python
@app.get("/images")
def listar_figurinhas():
    return imagens
```

Não renomeie esse endpoint para `/figuras`, pois o frontend já utiliza `/images`.

### 7. Criar um endpoint próprio para cada imagem

Adicione o endpoint:

```python
GET /figurinhas/{id}/imagem
```

Ele deve:

1. Receber o ID como número inteiro;
2. Utilizar `glob` para procurar um arquivo cujo nome começa com o ID formatado com dois dígitos;
3. Procurar dentro de `PASTA_IMAGENS`;
4. Retornar erro HTTP 404 caso nenhuma imagem seja encontrada;
5. Retornar a imagem encontrada usando `FileResponse`.

Utilize um padrão que evite confundir:

```text
02-nome.jpg
```

com:

```text
020-nome.jpg
```

O padrão de busca deve ser:

```python
f"{id:02d}[!0-9]*"
```

Exemplo:

```python
padrao = os.path.join(
    PASTA_IMAGENS,
    f"{id:02d}[!0-9]*"
)

arquivos_encontrados = glob.glob(padrao)
```

### 8. Tratamento de erros

Caso não encontre a imagem, retorne:

```python
raise HTTPException(
    status_code=404,
    detail="Imagem não encontrada"
)
```

### 9. Importações necessárias

O arquivo deve possuir estas importações:

```python
import glob
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
```

Mantenha também:

```python
from fastapi.staticfiles import StaticFiles
```

e o seguinte código já existente:

```python
app.mount(
    "/imgs",
    StaticFiles(directory=PASTA_IMAGENS),
    name="imgs"
)
```

Mesmo que a nova propriedade `imagem_url` utilize o endpoint individual, a rota estática atual deve ser preservada para evitar quebrar funcionalidades existentes.

### 10. Resultado esperado

Entregue o conteúdo completo e atualizado do arquivo `main.py`.

Não altere nomes de variáveis, pastas ou endpoints já existentes sem necessidade. Adicione as novas funcionalidades de forma incremental e explique brevemente cada alteração realizada.

---

Uma melhoria importante nesse prompt é mandar usar o número presente no arquivo como ID. No seu código atual, o `enumerate` pode gerar IDs incorretos caso existam arquivos duplicados, números ausentes ou duas imagens com o mesmo prefixo, como:

```text
28-Vinicius.jpeg
28-Vinicius.png
```

Nesse caso, as duas imagens possuem o ID `28`, independentemente da posição delas na lista.
