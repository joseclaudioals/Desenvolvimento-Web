from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ler_raiz():
    return {"hello" : "world"}

@app.get("/produtos/{produto_id}")
def ler_produto(produto_id: int):
    return {"produto_id" : produto_id}