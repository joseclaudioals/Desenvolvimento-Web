import requests
import streamlit as st

st.title("Cartas de baralho API")

if st.button("Comprar cartas"):
    resposta = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=5") # crio meu monte de cartas
    deck_id = resposta.json()["deck_id"]

    # Compra as cartas
    draw = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
    cards = draw.json()["cards"]

    colunas = st.columns(len(cards))
    for col, card in zip(colunas, cards):
        with col:
            st.image(card["image"], caption=f"Valor da carta: {card['value']} Naipe: {card['suit']}")


