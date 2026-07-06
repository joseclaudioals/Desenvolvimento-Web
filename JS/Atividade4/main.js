const imagem1 = document.getElementById('imagem1')
const imagem2 = document.getElementById('imagem2')

function mudarImagem(){
    let temp = imagem1.src
    imagem1.src = imagem2.src
    imagem2.src = temp
}

document.getElementById('btn').addEventListener('click', mudarImagem)