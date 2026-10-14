import streamlit as st


st.set_page_config(page_title="Prova Pratica 1 - Calculo IMC", layout="wide", page_icon="🤓")
with st.container(border=True):
    st.title("IMC Inteligente")
    st.write("Sua saúde começa com informação")

with st.container(border=True):
    st.markdown("""
                ### Calcule o seu IMC
                Preencha os campos abaixo para calcular seu índice de massa corporal
                """)

    with st.form(key='formulario'):
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input("Peso (kg)", min_value=0.0, max_value=400.0)
        with col2:
            altura = st.number_input("Altura (m)", min_value=0.0, max_value=3.0)

        bt = st.form_submit_button("Calcular meu IMC", type="primary", use_container_width=True)

    st.markdown("---")
    if bt:
        if peso <= 0 or altura <= 0:
            st.error("A altura e o peso devem ser maiores que zero")
        else:
            IMC = peso / (altura * altura)
            st.write("SEU RESULTADO")
            st.title(f"{IMC:.2f}")
            if IMC < 18.5:
                st.info(f"**Abaixo do peso**\n\nResultado abaixo da faica de preferencia para adultos")
            elif IMC < 25:
                st.success(f"**Peso normal**\n\nResultado dentro da faixa de referencia para adultos")
            elif IMC < 30:
                st.warning(f"**Sobrepeso**\n\nResultado um pouco acima da faixa de referencia para adultos")
            elif IMC >= 30:
                st.error(f"**Obesidade** \n\nResultado acima da faixa de referencia para adultos\nProcure um médico!")

        st.write("O IMC é um indicador geral e não substirui a avaliação de um profissional de saúde")