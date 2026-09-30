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

def contagem_vogais(texto):
    mensagem = texto.lower()
    contagem = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    for letra in mensagem:
        filtro = dict_acentos.get(letra, letra)
        if filtro in contagem:
            contagem[filtro] += 1

    return contagem


def resposta(contagem):
    texto = ""

    for vogal, quantidade in contagem.items():
        texto += f"{vogal}: {quantidade}\n"

    total = sum(contagem.values())
    texto += f"Total de vogais: {total}"

    return texto
