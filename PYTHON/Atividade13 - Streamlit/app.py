import random
import streamlit as st
import time

if 'numero_secreto' not in st.session_state:
    st.session_state.numero_secreto = None
if 'jogo_ativo' not in st.session_state:
    st.session_state.jogo_ativo = False
if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0

st.title("Desafio do Numero Secreto")
st.write("Clique no botão abaixo para gerar um numero aleatorio")

if st.button("Gerar numero"):
    st.session_state.numero_secreto  = random.randint(1,100)
    st.session_state.jogo_ativo  = True

    with st.spinner('Gerando numero...'):
        time.sleep(2)

    st.success("Numero gerado")

if st.session_state.jogo_ativo:
    st.write("Adivinhe o numero")
    chute = st.number_input("chute", min_value=1, max_value=100, value=None, key=f'numero_{st.session_state.tentativas}')

    if chute is not None:
        st.session_state.tentativas += 1

        if chute != st.session_state.numero_secreto:
            st.error("chute incorreto")
            if chute > st.session_state.numero_secreto:
                st.warning("chute maior que o numero")
            elif chute < st.session_state.numero_secreto:
                st.warning("chute menor que o numero")
        elif chute == st.session_state.numero_secreto:
            st.success("chute acertado")
            st.write(f"Quantidade de chutes: {st.session_state.tentativas}")

            st.session_state.jogo_ativo = False
            st.session_state.numero_secreto = None
            st.session_state.tentativas = 0


