# EP - Design de Software
# Equipe: Guilherme da Franca, Vinícius Matheus Morales
# Data: 18/10/2020

import random

def valor_carta(baralho:list, posicao_carta:int): # Função para determinar o valor de cada carta
    if baralho[posicao_carta]=='A':
        return 1
    elif baralho[posicao_carta]=='10' or baralho[posicao_carta]=='J' or baralho[posicao_carta]=='Q' or baralho[posicao_carta]=='K':
        return 0
    else:
        return int(baralho[posicao_carta])

def pontuacao(pontos_player, baralho:list): # Função para calcular a pontuação do player
    numero_carta=random.randint(0, len(baralho)-1) # Gerando uma carta nova
    pontos_player+=valor_carta(baralho, numero_carta) # Adicionando a pontuação
    baralho.remove(baralho[numero_carta]) # Removendo a carta do baralho
    
    pontos_player=str(pontos_player)
    pontos_player=pontos_player[-1]
    pontos_player=int(pontos_player)

    return pontos_player

def jogo():
    nome=input('Digite seu nome: ')
    fichas=int(input('Digite sua quantidade de fichas: '))
    print('Nome: {}\nFichas: {}'.format(nome, fichas))
    qtd_baralhos=int(input('Quantos baralhos deseja usar? 1, 6 ou 8? '))

    while qtd_baralhos!=1 and qtd_baralhos!=6 and qtd_baralhos!=8:
        print('Valor inválido, tente novamente')
        qtd_baralhos=int(input('Quantos baralhos deseja usar? 1, 6 ou 8? '))

    while fichas>0:
        aposta=int(input('Faça sua aposta: '))
        if aposta==0:
            break

        while aposta>fichas:
            print('Valor inválido, tente novamente')
            aposta=int(input('Faça sua aposta: '))
        
        escolha=input('Escolha entre "Jogador", "Banco" ou "Empate": ')

        while escolha!='Jogador' and escolha!='Banco' and escolha!='Empate':
            print('Escolha inválida, tente novamente')
            escolha=input('Escolha entre "Jogador", "Banco" ou "Empate": ')
        
        cartas=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4*qtd_baralhos

        pontos_jogador=0
        pontos_banco=0

        # Pontuação banco no primeiro par de cartas:
        pontos_banco=pontuacao(pontos_banco, cartas)
        pontos_banco=pontuacao(pontos_banco, cartas)
        print('Pontos do banco no primeiro par de cartas: {}'.format(pontos_banco))

        # Pontuação jogador no primeiro par de cartas:
        pontos_jogador=pontuacao(pontos_jogador, cartas)
        pontos_jogador=pontuacao(pontos_jogador, cartas)
        print('Pontos do jogador no primeiro par de cartas: {}'.format(pontos_jogador))

        if pontos_banco<6:
            pontos_banco=pontuacao(pontos_banco, cartas)
            print('Pontos do banco após a terceira carta: {}'.format(pontos_banco))
        
        if pontos_jogador<6:
            pontos_jogador=pontuacao(pontos_jogador, cartas)
            print('Pontos do jogador após a terceira carta: {}'.format(pontos_jogador))
        
        # Vitória:
        if pontos_jogador>pontos_banco:
            vitoria='Jogador'
        elif pontos_banco>pontos_jogador:
            vitoria='Banco'
        else:
            vitoria='Empate'

        # Pagamento das apostas:
        if escolha=='Jogador':
            if vitoria=='Jogador':
                fichas+=aposta
            else:
                fichas-=aposta

        elif escolha=='Banco':
            if vitoria=='Banco':
                fichas+=0.95*aposta
            else:
                fichas-=aposta

        else:
            if vitoria=='Empate':
                fichas+=int(aposta*8)
            else:
                fichas-=aposta
        print('Suas fichas após rodada do jogo: {}'.format(fichas))
    
    print('Suas fichas após encerrar o jogo: {}'.format(fichas))

jogo()
