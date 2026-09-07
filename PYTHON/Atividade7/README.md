# Atividade 07 - Json

01. **Faça um programa que:**
- Converta o JSON para uma estrutura Python.
- Calcule a média de cada aluno.
- Mostre o nome e a média de cada aluno.
- Mostre somente os alunos com média maior ou igual a 7.
- Mostre qual aluno possui a maior média.
[ { "nome": "Ana", "idade": 20, "curso": "ADS", "notas": [8.0, 7.5, 9.0] } ]

Saída esperada parcialmente:
````
Ana - Média: 8.17
Carlos - Média: 6.17
Mariana - Média: 9.17
Pedro - Média: 7.17

Aprovados:
Ana
Mariana
Pedro

Maior média: Mariana - 9.17
````
02. **Considere:**
````
{ 
    "loja": "TechStore", 
    "produtos": [ {
        "id": 1, 
        "nome": "Teclado", 
        "categoria": "Periféricos", 
        "preco": 120.00, 
        "estoque": 15 
        }, 
        { 
        "id": 2, 
        "nome": "Mouse", 
        "categoria": "Periféricos", 
        "preco": 80.00, 
        "estoque": 5 
        }  
    ] 
}
        
````

Faça um programa que:

- Converta o JSON para Python.
- Mostre todos os produtos.
- Mostre os produtos com estoque menor que 6.
- Calcule o valor total armazenado no estoque de cada produto:
  - valor = preco × estoque
- Calcule o valor total de todos os produtos em estoque.
- Mostre o produto de maior valor total em estoque.
- Desafio adicional: permita que o usuário informe uma categoria e mostre apenas os produtos daquela categoria.