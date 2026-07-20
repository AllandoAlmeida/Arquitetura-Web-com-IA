# Importa as classes e módulos necessários
# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.staticfiles import StaticFiles
import os

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Definição dos caminhos absolutos para a pasta de imagens
# PASTA_BASE obtém o diretório atual onde o arquivo main.py está localizado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# PASTA_IMAGENS combina o caminho base com a pasta "imagens"
PASTA_IMAGENS = os.path.join(PASTA_BASE, "imagens")

# Configura o FastAPI para servir arquivos estáticos.
# "Montamos" a pasta física PASTA_IMAGENS na rota virtual "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista chamada "imagens" contendo duas figurinhas de exemplo e suas respectivas URLs
imagens = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/imgs/01-alan-turing.jpg"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/imgs/02-john-mccarthy.jpg"
    }
]

# Define a única rota da API: GET "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas (imagens) definida acima
    return imagens
