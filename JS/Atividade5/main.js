let votos = [0, 0, 0, 0]
let linguagens = ['python', 'php', 'java', 'c++']
let total = 0
let barra = []

barra.push(document.querySelector('#python-line'))
barra.push(document.querySelector('#php-line'))
barra.push(document.querySelector('#java-line'))
barra.push(document.querySelector('#c-line'))

let spans = []; 
spans.push(document.querySelector('#python_porc'));
spans.push(document.querySelector('#php_porc'));
spans.push(document.querySelector('#java_porc'));
spans.push(document.querySelector('#c_porc'));

function enquete(event){
    event.preventDefault()

    const x = document.querySelector('input[name="enquete"]:checked')

    if(!x){
        alert('selecione uma linguagem antes de votar')
        return
    }

    const opt = x.value

    let i = linguagens.indexOf(opt)
    if(i == -1)
        return

    total++
    votos[i]++    
    
    for(let j = 0; j<linguagens.length; j++){
        let porc = (votos[j]/total)*100

        barra[j].style.setProperty(`--tamanho_line`, `${porc}%`)

        spans[j].textContent = `${porc.toFixed(1)}%`
    }
}

document.getElementById('btn').addEventListener('click', enquete)