import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Tarefa(BaseModel):
    nome: Optional[str] = None
    status: Optional[str] = None

@app.get("/listar_tarefas")
def listar_tarefas():
    return abrir_json()

@app.post("/nova_tarefa")
def nova_tarefa(tarefa: Tarefa):
    dados = abrir_json()

    if dados:
        id = str(max(int(k) for k in dados.keys()) + 1)
    else:
        id = "1"

    # adiciona o novo item no dicionario da memoria
    dados[id] = tarefa.model_dump()

    #salva o dicionario inteiro de volta em arquivo
    salvar_json(dados)

    return {
        "mensagem": "criado com sucesso",
        "id": id,
        "tarefa": dados[id],
    }

@app.put("/atualizar_tarefa/{id}")
def atualizar_tarefa(id: str, nova_tarefa: Tarefa):
    dados = abrir_json()

    if id in dados:
        payload = nova_tarefa.model_dump(exclude_unset=True, exclude_none=True)
        dados[id].update(payload)
        salvar_json(dados)

        return{
            "mensagem": "atualizado com sucesso",
            "item": dados[id],
        }
    raise HTTPException(status_code = 404, detail = "Item não encontrado")

@app.delete("/deletar_tarefa/{id}")
def deletar_tarefa(id: str):
    dados = abrir_json()

    if id in dados:
        tarefa = dados.pop(id)

        salvar_json(dados)

        return{
            "mensagem": "Tarefa deletado com sucesso",
            "tarefa removida": tarefa,
        }
    raise HTTPException(status_code = 404, detail = "Item não encontrado")


def abrir_json():
    if not os.path.exists("src/tarefas.json"):
        return {}

    with open("src/tarefas.json", "r", encoding="utf-8") as arquivo:
        try:
            tarefas = json.load(arquivo)
        except json.JSONDecodeError:
             return {} # se falhar ao ler arquivo, devo reetornar uma lista vazia

    if not tarefas:
        return {} # se o arquivo estiver vazio, deve retornar uma lista vazia

    return tarefas

def salvar_json(dados):
    with open("src/tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)