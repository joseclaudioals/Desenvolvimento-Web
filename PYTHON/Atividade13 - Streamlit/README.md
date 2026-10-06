Atividade: Desafio do Número Secreto
Objetivo
Criar uma aplicação web em Streamlit na qual o computador sorteia um número e o usuário precisa descobri-lo.

O sistema deve informar se o palpite é:

- 🔼 Maior que o número secreto
- 🔽 Menor que o número secreto
- 🎯 Igual ao número secreto
Além disso, o aluno deverá desenvolver uma interface visual organizada.

## Regras
O programa deve:

1. Sortear um número entre 1 e 100.
2. Permitir que o usuário informe um palpite.
3. Comparar o palpite com o número secreto.
   4. Informar uma dica:
   5. "Tente um número maior!"
   6. "Tente um número menor!"
7. "Parabéns! Você acertou!"
9. Contar quantas tentativas o jogador utilizou.
10. Possuir um botão "Novo Jogo".
11. Utilizar elementos visuais do Streamlit.
## 🎨 Requisitos de Design
O aluno deverá utilizar pelo menos:

`st.title()`
`st.write()` ou `st.markdown()`
`st.number_input()`
`st.button()`
`st.success()`
`st.warning()` ou `st.error()`
`st.sidebar()`
Pode criar um título como:

> 🎮 DESAFIO DO NÚMERO SECRETO