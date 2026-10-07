import streamlit as st

pages = ["pages/p1.py",
         "pages/p2.py",
         "pages/p3.py",
         "pages/p4.py,"
         "pages/p5.py",
         "pages/p6.py"]

sidebar_logo = "img/img_1.png"
st.logo(sidebar_logo, size="large")
st.sidebar.markdown("Conheça a nossa cidade")
st.title("Portal Turistico")



with st.container(horizontal_alignment="center"):
    st.image("img/img.png")

    st.markdown("""
        Parnaíba é um município brasileiro do Estado do Piauí, o segundo mais populoso do estado, com uma população estimada em 2025 pelo IBGE em 172 mil. É a principal cidade pertencente à Região Metropolitana de Parnaíba. Situado no litoral piauiense, é um dos quatro municípios litorâneos do estado (além de Ilha Grande, Luís Correia e Cajueiro da Praia). Parnaíba é conurbada com Luís Correia, e também o portal de entrada para o Delta do Parnaíba, sendo único delta em mar aberto das Américas, tornando-se popularmente conhecido como a "Capital do Delta".[7] A cidade apresenta grande valor histórico para o Piauí, com inúmeros monumentos históricos tombados pelo IPHAN, principalmente nas proximidades do Porto das Barcas.[8][9]
    """)

st.write("Conheça os melhores destinos!!")
if st.button("Destinos"):
    st.switch_page(pages[0])

if st.button("Galeria"):
    st.switch_page(pages[1])

if st.button("Materiais"):
    st.switch_page(pages[2])

if st.button("Links"):
    st.switch_page(pages[3])

if st.button("Contato"):
    st.switch_page(pages[4])

if st.button("Avaliação"):
    st.switch_page(pages[5])


