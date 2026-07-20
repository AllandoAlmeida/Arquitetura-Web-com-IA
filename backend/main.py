# Importa a classe FastAPI do framework fastapi
#from fastapi import FastAPI

# pyrefly: ignore [missing-import]
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define a rota para o método GET na raiz ("/") da API
@app.get("/")
def hello_world():
    # Retorna o JSON com a mensagem de boas-vindas solicitada
    return {"mensagem": "Olá, mundo! 🌍"}
