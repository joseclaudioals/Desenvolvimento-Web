def estatistica(*args):
    dicionario ={
    "soma": 0,
    "media": 0,
    "maior": -999999999999999,
    "menor": 999999999999999,
    }

    for n in args:
        dicionario["soma"] = dicionario["soma"] + n
        if n > dicionario["maior"]: dicionario["maior"] = n
        if n < dicionario["menor"]: dicionario["menor"] = n

    dicionario["media"] = dicionario["soma"]/len(args)

    return dicionario

print(estatistica(1,2,3,4,5))
