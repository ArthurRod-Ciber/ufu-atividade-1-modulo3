dict_acentos = {
    "á": "a", 
    "à": "a",
    "â": "a",
    "ã": "a",
    "é": "e",
    "ê": "e",
    "í": "i",
    "õ": "o",
    "ô": "o",
    "ú": "u"
}




def inverter(palavra):
    palavra[::-1]

    return palavra[::-1]

def limpar(texto):
    texto_minusculo = texto.lower()
    resultado = ""
    for letra in texto_minusculo:
        filtro = dict_acentos.get(letra,letra)
        if filtro.isalnum():
            resultado += filtro

    return resultado

def eh_palidromo(texto):
    limpo = limpar(texto)
    return limpo == inverter(limpo)


def resposta(texto):
    invertido = inverter(texto)

    if eh_palidromo(texto):
        resultado = "É palíndromo!"

    else:
        resultado = "Não é palíndromo!. Tente 'arara'"

    return f"Invertido: {invertido}\n{resultado}"