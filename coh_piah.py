import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i = i + 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    assinatura_a = as_a
    assinatura_b = as_b
    diferencas = 0
    diferencastotal = 0
    i = 0
    while i < len(assinatura_a):
        diferencas = abs(assinatura_a[i]-assinatura_b[i])
        diferencastotal = diferencastotal+diferencas
        i += 1
    similaridade = (diferencastotal/6)
    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    todas_palavras = []
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        for fr in novas_frases:
            novas_palavras = separa_palavras(fr)
            todas_palavras.extend(novas_palavras)

    lpt = 0
    for palavra in todas_palavras:
        lp = len(palavra)
        lpt = lpt+lp
    len_palavras_total = lpt
    wal_text = (len_palavras_total/len(todas_palavras))
    lista_palavras = todas_palavras
    sem_palavras_repetidas = n_palavras_diferentes(lista_palavras)
    ttr_text = (sem_palavras_repetidas/len(todas_palavras))
    sem_palavras_que_repetem = n_palavras_unicas(lista_palavras)
    hlr_text = (sem_palavras_que_repetem/len(todas_palavras))
    caracteres = 0
    for caracter in texto:
        if caracter != '.' and caracter != '?' and caracter != '!':
            caracteres = len(caracter)+caracteres
    numero_sentencas = separa_sentencas(texto)
    numero_sentencas = len(sentencas)
    sal_text = (caracteres/numero_sentencas)
    frases = re.split(r'[,:;?.!]+', texto)
    if frases[-1] == '':
        del frases[-1]
    numero_frases = len(frases)
    sac_text = (numero_frases/numero_sentencas)
    caracteres = 0
    for caracter in frases:
        caracteres = len(caracter)+caracteres
    pal_text = (caracteres/numero_frases)
    return [wal_text, ttr_text, hlr_text, sal_text, sac_text, pal_text]


def avalia_textos(textos, ass_cp):
    n_texto = 1
    similaridade_textual_1 = 10**5
    for texto in textos:
        as_b = ass_cp
        parametros = calcula_assinatura(texto)
        as_a = parametros
        similaridade_textual_2 = compara_assinatura(as_a, as_b)
        if similaridade_textual_2 < similaridade_textual_1:
            similaridade_textual_1 = similaridade_textual_2
            texto_infectado = n_texto
        n_texto += 1
    return texto_infectado


ass_cp = le_assinatura()
textos = le_textos()
avaliacao = avalia_textos(textos, ass_cp)
print("O autor do texto", avaliacao, "está infectado com COH-PIAH.")
