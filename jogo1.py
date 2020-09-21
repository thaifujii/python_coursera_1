def quem_comeca (n,m):
    if n % (m+1) == 0:
        return 0
    else:
        return 1
 
def computador_escolhe_jogada (n,m):
    numero_de_pecas = -1
    x = 1

    if n >= m:
        while x <= m:
            if (n-x)%(m+1) == 0: #a quantidade que sobra ao tirar x peças é multiplo de m+1
                numero_de_pecas = x
            x += 1
      
        if numero_de_pecas == -1:
            return m
        else:
            return numero_de_pecas
 
    else:
        return n

def analise_jogada (n,m,jogada):
    if jogada <= 0:
        return False
    elif jogada > n:
        return False
    elif n >= m and jogada > m:
        return False
    else:
        return True
 
def usuario_escolhe_jogada (n,m):
    jogada = int(input('Quantas peças você vai tirar? '))

    deu_bom = analise_jogada (n,m,jogada)

    if deu_bom:
        return jogada

    else:
        while not deu_bom:
            print ()
            print ('Oops! Jogada inválida! Tente de novo.')
            print()
            jogada = int(input('Quantas peças você vai tirar? '))
            deu_bom = analise_jogada (n,m,jogada)
        return jogada

 
def partida ():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
 
    jogada_inicial = quem_comeca(n,m)
 
    if jogada_inicial == 1:
        #o computador começa
        print ("Computador começa!")
 
        while n != 0:
            computador = computador_escolhe_jogada (n,m)
            n = n - computador
            print()
            if computador == 1:
                print ('O computador tirou uma peça')
            else:
                print ('O computador tirou', computador, 'peças.')
 
            if n == 0:
                print ("Fim de jogo! O computador ganhou!")
                break
            else:
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print ("Agora restam", n, 'peças no tabuleiro.')
    
            print ()
            jogador = usuario_escolhe_jogada (n,m)
            n = n - jogador
            print ()

            if jogador == 1:
                print ('Você tirou uma peça')
            else:
                print ('Você tirou', jogador, 'peças.')

            if n == 1:
                print ("Agora resta apenas uma peça no tabuleiro.")
            else:
                print ("Agora restam", n, 'peças no tabuleiro.')
 
    else:
        print ("Você começa!")
        print ()
        while n != 0:
            jogador = usuario_escolhe_jogada (n,m)
            n = n - jogador

            if jogador == 1:
                print ('Você tirou uma peça')
            else:
                print ('Você tirou', jogador, 'peças.')

                
            if n == 1:
                print ("Agora resta apenas uma peça no tabuleiro.")
            else:
                print ("Agora restam", n, 'peças no tabuleiro.')
     
            print ()
     
            computador = computador_escolhe_jogada (n,m)
            #retorna o numero de peças retiradas
            n = n - computador
     
            if computador == 1:
                print ('O computador tirou uma peça')
            else:
                print ('O computador tirou', computador, 'peças.')

            if n == 0:
                print ("Fim de jogo! O computador ganhou!")
            else:
                if n == 1:
                    print ("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print ("Agora restam", n, 'peças no tabuleiro.')   
 
def campeonato ():
    print("Bem-vindo ao jogo NIM! Escolha:")
    print()
    print("1 - para jogar partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    print()
 
    if escolha == 1:
        print ("Voce escolheu uma partida isolada!")
        print()
        partida()
    else:
        print ("Voce escolheu um campeonato!")
        contador = 1
 
        while contador != 4:
            print()
            print ("**** Rodada", contador, '****')
            print()
            partida()
            contador += 1
  
        print()
        print ("**** Final do campeonato! ****")
        print ()
        print("Placar: Você 0 X 3 Computador")
 
campeonato()
