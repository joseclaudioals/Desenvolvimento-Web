function geraAleatorio(){
    let n = parseInt(document.getElementById('n').value)
    let resultado = document.getElementById('resultado')

    if(isNaN(n)){
        resultado.innerHTML = 'Valor com input invalido'
        return
    }

    let list = []

    for(let i=0; i<6; i++){
        list.push(Math.floor(Math.random() * 20)+1)
    }

    let s = ""
    for(let i of list) s+= i + " "
    if(list.includes(n)){
        resultado.innerHTML = `VOCÊ ACERTOU <br/> <br/> 
                                Numero digitado ${n} <br/> 
                                Números sorteados: ${s}`
    }
    else{
        resultado.innerHTML = `VOCÊ ERROU! <br/> <br/> 
                                Número digitado: ${n} <br/> 
                                Números sorteados: ${s}`;
    }
    
}

document.getElementById('btn').addEventListener('click', geraAleatorio)