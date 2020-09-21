import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença:  "))
    pal = float(input("Entre o tamanho medio de frase:"))
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print ()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print ()

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''

    sentencas = re.split(r'[.?!]+', texto)
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

#################################################################################################################################

def tam_medio_palavras (palavras, quantas_palavras):
    '''Pega cada palavra da lista, calcula o seu tamanho, soma e divide pela quantidade de palavras'''
    soma = 0

    for i in palavras:
        tamanho_atual = len(i)
        soma = soma + tamanho_atual

    media = soma/quantas_palavras  
    return media

def type_token (quantas_palavras, diferentes):
    '''Recebe quantas palavras diferentes tem e divide pelo total de palavras'''
    razao = diferentes/quantas_palavras
    return razao

def hapax_legomana (quantas_palavras, unicas):
    razao = unicas/quantas_palavras
    return razao

def tamanho_medio_sentencas (sentecas, quantas_sentencas):
    soma = 0

    for i in sentecas:
        tamanho = len(i)
        soma = soma + tamanho

    razao = soma/quantas_sentencas

    return razao

def complexidade (frases, sentencas):
    razao = frases/sentencas

    return razao

def tamanho_medio_frase (frase, quantas_frases):
    soma = 0

    for i in frase:
        tamanho = len(i)
        soma = soma + tamanho

    razao = soma/quantas_frases

    return razao

###############################################################################################################################################3

def calcula_assinatura (texto):
    sentencas = []
    marcador = 0

    sentencas = separa_sentencas(texto)
    #print('sentencas = ', sentencas)

    '''vetor com as sentencas
    while marcador < len(textos): #vou pegar cada item da lista, colocar numa lista aux as sentencas separadas e depois append na sent
        aux = separa_sentencas(texto)
        print(aux)
        sentencas = sentencas + aux
        marcador += 1'''

    #vetor com as frases
    frases = []
    marcador = 0
    while marcador < len(sentencas):
        aux = separa_frases(sentencas[marcador])
        frases = frases + aux
        marcador += 1
    #print ('frases = ', frases)

    #vetor com as palavras
    palavras = []
    marcador = 0
    while marcador < len(frases):
        aux = separa_palavras(frases[marcador])
        palavras = palavras + aux
        marcador += 1
    #print ('palavras = ', palavras)

    #quantas palavras unicas tem o texto?
    unicas = n_palavras_unicas(palavras)

    #quantas palavras diferentes?
    diferentes = n_palavras_diferentes(palavras)
    #print ('unicas = ', unicas, 'diferentes = ', diferentes)

    '''PRONTO, chamou todas as funções dadas. Agora tem que calcular a assinatura.'''

    #valores auxiliares
    quantas_palavras = len(palavras)
    quantas_frases = len(frases)
    quantas_sentencas = len(sentencas)

    #assinatura do texto
    assinatura = []
    wal = tam_medio_palavras (palavras, quantas_palavras)
    assinatura.append(wal)

    ttr = type_token (quantas_palavras, diferentes)
    assinatura.append(ttr)

    hlr = hapax_legomana (quantas_palavras, unicas)
    assinatura.append(hlr)

    sal = tamanho_medio_sentencas (sentencas, quantas_sentencas)
    assinatura.append(sal)

    sac = complexidade (quantas_frases, quantas_sentencas)
    assinatura.append(sac)

    #print (assinatura)

    pal = tamanho_medio_frase (frases, quantas_frases)
    assinatura.append(pal)
    #print (assinatura)

    return assinatura

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    '''grau de similaridade = S'''
    '''f_ib é dado como entrada, f_ia é obtido do texto'''

    diferenca = []

    for i in range (0,6):
        #calcular a diferenca de cada um e coloca no vetor
        aux = as_a[i] - as_b[i]
        diferenca.append(abs(aux))

    soma = 0
    
    for i in diferenca:
        soma = soma + i

    return (soma/6)


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o
    numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = []
    comparacao = []
    copia = 100000000

    for i in range (len(textos)):
        #calcula a assinatura do texto i
        assinaturas = calcula_assinatura(textos[i])
        #ja calcula a similaridade com a ass_cp
        comparacao = compara_assinatura(ass_cp,assinaturas)

        #print('texto', i, 'comparacao', comparacao)

        if comparacao < copia:
            copia = comparacao
            aux = i + 1

    return aux

'''MAIN'''

ass_cp = le_assinatura()
textos = le_textos()
copiao = avalia_textos (textos, ass_cp)
print('O autor do texto', copiao,'está infectado com COH-PIAH')




