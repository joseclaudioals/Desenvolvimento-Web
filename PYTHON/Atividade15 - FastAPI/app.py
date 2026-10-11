import streamlit as st
import pandas as pd
import requests as rqt
import time

BASE_URL = "http://127.0.0.1:8000"

def listar_tarefas():
    rota = f"{BASE_URL}/listar_tarefas"

    resposta = rqt.get(rota)
    if resposta.status_code == 200:
        return resposta.json()

    return []

def criar_tarefas(nome, status):
    rota = f"{BASE_URL}/nova_tarefa"

    payload = {"nome": nome, "status": status}
    resposta = rqt.post(rota, json = payload) # é necessário indicar que o corpo da requisição é json

    return resposta

def atualizar_tarefa(id, payload):
    rota = f"{BASE_URL}/atualizar_tarefa/{id}"

    resposta = rqt.put(rota, json=payload)

    return resposta

def deletar_tarefa(id):
    rota = f"{BASE_URL}/deletar_tarefa/{id}"

    resposta = rqt.delete(rota)

    return resposta

def criar_dataframe():
    dados = listar_tarefas()
    if isinstance(dados, dict):
        # Transforma {id: {...}} em DataFrame
        # Trata as chaves externas (os id) como uma linha em indice
        # Após isso, tranforma esse indice em uma coluna normal
        # em seguida, renomeamos "index" para "id"
        df = pd.DataFrame.from_dict(dados, orient="index").reset_index()
        return df.rename(columns={"index": "id"})
    else:
        return pd.DataFrame(dados)

st.set_page_config(page_title = "To-do Lista", page_icon = "✏️")

st.title("To-do Lista")
st.subheader("Tarefas")

df = criar_dataframe()
st.dataframe(df)

tab1, tab2, tab3 = st.tabs(["Nova tarefa", "Editar Tarefa", "Excluir tarefa"])

with tab1:
    with st.form(key="criar_tarefa"):
        nome = st.text_input("Nome da tarefa")
        status = st.selectbox("Status", ("A fazer", "Em desenvolvimento", "Concluido"))

        if st.form_submit_button("Criar tarefa"):
            if not nome:
                    st.error("Campo nome está vazio")
            else:
                resposta = criar_tarefas(nome, status)
                if resposta.ok:
                    st.success("Tarefa criada com sucesso")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error(f"Erro {resposta.status_code} ao criar a tarefa")


with tab2:

    with st.form(key="atualizar_tarefa"):
        id_tarefa = st.number_input("ID da tarefa", min_value=1)
        campo = st.selectbox("Campo a editar", ["nenhum", "nome", "status"])

        novo_valor = None

        if campo == "status":
            novo_valor = st.selectbox("Status", ("A fazer", "Em desenvolvimento", "Concluido"))
        elif campo == "nome":
            novo_valor = st.text_input("Nome tarefa")

        enviar = st.form_submit_button("Atualizar tarefa")

    if enviar:
        if campo == "nenhum":
            st.error("nenhum campo selecionado")
        elif campo == "nome" and not novo_valor:
            st.error("O campo de nome está vazio")
        else:
            resposta = atualizar_tarefa(id_tarefa, {campo: novo_valor})
            if resposta.ok:
                st.success("Tarefa atualizada com sucesso")
                time.sleep(2)
                st.rerun()
            elif resposta.status_code == 404:
                st.error(f"Tarefa não existente. Erro {resposta.status_code}")

with tab3:
    with st.form(key="excluir_tarefa"):
        id_tarefa = st.number_input("ID da tarefa", min_value=1)

        enviar = st.form_submit_button("Deletar tarefa")

    if enviar:
        resposta = deletar_tarefa(id_tarefa)
        if resposta.ok:
            st.success("Tarefa deletada com sucesso")
            time.sleep(2)
            st.rerun()
        elif resposta.status_code == 404:
            st.error(f"Tarefa nãoe xistente. Erro {resposta.status_code}")
