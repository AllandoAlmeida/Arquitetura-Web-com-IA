# Importa as classes e módulos necessários
import glob
import os

# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
# pyrefly: ignore [missing-import]
from fastapi.responses import FileResponse
# pyrefly: ignore [missing-import]
from fastapi.staticfiles import StaticFiles

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configuração do Middleware CORS para permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definição dos caminhos absolutos para a pasta de imagens
# PASTA_BASE obtém o diretório atual onde o arquivo main.py está localizado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
# PASTA_IMAGENS combina o caminho base com a pasta "imagens"
PASTA_IMAGENS = os.path.join(PASTA_BASE, "imagens")

# Configura o FastAPI para servir arquivos estáticos.
# "Montamos" a pasta física PASTA_IMAGENS na rota virtual "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Categoria padrão para as figurinhas
CATEGORIA = "IA"

# Lista que conterá as figurinhas geradas dinamicamente a partir dos arquivos
imagens = []

# Extensões de imagem válidas permitidas
EXTENSOES_VALIDAS = {".jpg", ".jpeg", ".png", ".webp", ".avif"}

# Percorre todos os arquivos da pasta imagens e os ordena para obter uma ordenação consistente
for indice, arquivo in enumerate(sorted(os.listdir(PASTA_IMAGENS)), start=1):
    # Ignora se não for um arquivo
    if not os.path.isfile(os.path.join(PASTA_IMAGENS, arquivo)):
        continue

    # Separa o nome do arquivo da extensão
    nome_sem_extensao, ext = os.path.splitext(arquivo)

    # Valida se a extensão do arquivo (em minúsculas) é permitida
    if ext.lower() not in EXTENSOES_VALIDAS:
        continue

    # Extrai o ID da figurinha a partir do número inicial presente no nome do arquivo (ex: "01" de "01-alan-turing")
    try:
        id_figura = int(nome_sem_extensao.split("-", 1)[0])
    except (ValueError, IndexError):
        # Caso o nome do arquivo não siga o padrão esperado de começar com número seguido de hífen, pula o arquivo
        continue

    # Remove o número inicial (01-, 02-, etc.) e obtém o nome
    nome = nome_sem_extensao.split("-", 1)[1]

    # Converte para um nome bonito (substitui hifens por espaços e coloca iniciais em maiúsculo)
    nome = nome.replace("-", " ").title()

    # Adiciona a figurinha à lista imagens com a nova estrutura de imagem_url
    imagens.append({
        "id": id_figura,
        "nome": nome,
        "categoria": CATEGORIA,
        "imagem_url": f"/images/{id_figura}/imagem"
    })

# Define a rota para listar todas as figurinhas disponíveis
@app.get("/images")
def listar_figurinhas():
    # Retorna a lista de figurinhas (imagens) populada dinamicamente
    return imagens

# Define a rota para obter uma imagem individual pelo ID da figurinha
@app.get("/images/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Constrói o padrão de busca com o ID formatado com dois dígitos seguido de caractere não numérico
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    
    # Realiza a busca no sistema de arquivos usando glob
    arquivos_encontrados = glob.glob(padrao)
    
    # Se nenhum arquivo for encontrado, levanta uma exceção HTTP 404
    if not arquivos_encontrados:
        raise HTTPException(
            status_code=404,
            detail="Imagem não encontrada"
        )
    
    # Retorna o arquivo de imagem encontrado usando FileResponse
    return FileResponse(arquivos_encontrados[0])
