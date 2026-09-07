import json

texto_json = '[{"nome": "Ana", "idade": 20, "curso": "ADS", "notas": [8.0, 7.5, 9.0]},{"nome": "Beatriz","idade": 21,"curso": "ADS","notas": [7.0,8.5,9.2]},{"nome": "Rafael","idade": 19,"curso": "ADS","notas": [6.5,7.0,8.0]},{"nome": "Mariana","idade": 23,"curso": "ADS","notas": [ 9.0,9.5,8.8]},{"nome": "João","idade": 25,"curso": "ADS","notas": [10.0,8.5,9.5]}]'

maior_media = [-9999999, ""]
medias = []
dicionario = json.loads(texto_json)

for item in dicionario:
    media = (sum(item["notas"])/len(item["notas"]))
    if media > maior_media[0]:
        maior_media[0], maior_media[1] = media, item["nome"]
    medias.append(media)
    print(f"{item['nome']} - Média: {media:.2f}")

print(f"\nAprovados: ")
for i in range(len(medias)):
    if medias[i] >= 7.0: print(f"{dicionario[i]['nome']} - Aprovado")

print(f"\nMaior média: {maior_media[1]} - {maior_media[0]:.2f}")
