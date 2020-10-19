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
    x=valor_carta(baralho, numero_carta)
    pontos_player+=x # Adicionando a pontuação
    baralho.remove(baralho[numero_carta]) # Removendo a carta do baralho
    
    if pontos_player>=10:
        pontos_player-=10

    return pontos_player, x

def calcula_comissao(pagamento, num_baralhos, vencedor):
    comissao_j1=0.0129
    comissao_j6=comissao_j8=0.0124

    comissao_b1=0.0101
    comissao_b6=comissao_b8=0.0106

    comissao_e1=0.1575
    comissao_e6=0.1444
    comissao_e8=0.1436

    if num_baralhos==1:
        if vencedor=='Jogador':
            pagamento-=pagamento*comissao_j1
        elif vencedor=='Banco':
            pagamento-=pagamento*comissao_b1
        else:
            pagamento-=pagamento*comissao_e1

    elif num_baralhos==6:
        if vencedor=='Jogador':
            pagamento-=pagamento*comissao_j6
        elif vencedor=='Banco':
            pagamento-=pagamento*comissao_b6
        else:
            pagamento-=pagamento*comissao_e6

    else:
        if vencedor=='Jogador':
            pagamento-=pagamento*comissao_j8
        elif vencedor=='Banco':
            pagamento-=pagamento*comissao_b8
        else:
            pagamento-=pagamento*comissao_e8
    return pagamento

def player_fichas(num_player, fichas_player):
    dic_player_fichas={}
    for i in range(len(num_player)):
        dic_player_fichas[i]
    pass

def vitorioso(pontos_jogador, pontos_banco):
    if pontos_jogador>pontos_banco:
        vitoria='Jogador'
    elif pontos_banco>pontos_jogador:
        vitoria='Banco'
    else:
        vitoria='Empate'
    return vitoria

def jogo():
    
    # Quantidade de jogadores:
    jogadores=''
    i=1
    lista_jogadores=[]
    lista_fichas=[]
    while jogadores!='iniciar':
        nome=input('Digite seu nome, jogador {}: '.format(i)) # Nomes dos jogadores
        fichas=int(input('Digite sua quantidade de fichas com números, qualquer coisa diferente de um número dará um erro: ')) # Fichas de cada jogador
        print('\nNome jogador {}: {}\nFichas jogador {}: {}\n'.format(i, nome, i, fichas)) # Printando resultados obtidos
        lista_jogadores.append(nome)
        lista_fichas.append(fichas)
        jogadores=input('Digite "iniciar" para começar o jogo ou digite qualquer outra coisa para adicionar mais um jogador: ')
        i+=1
    
    # Quantidade de baralhos:
    if len(lista_jogadores)>1:
        qtd_baralhos=int(input('Quantos baralhos desejam usar? 1, 6 ou 8? ')) # Quantidade de baralhos desejadas
    else:
        qtd_baralhos=int(input('Quantos baralhos deseja usar? 1, 6 ou 8? '))

    while qtd_baralhos!=1 and qtd_baralhos!=6 and qtd_baralhos!=8: # Validando quantidade de baralhos
        print('Valor inválido, tente novamente')
        if len(lista_jogadores)>1:
            qtd_baralhos=int(input('Quantos baralhos desejam usar? 1, 6 ou 8? '))
        else:
            qtd_baralhos=int(input('Quantos baralhos deseja usar? 1, 6 ou 8? '))

    lista_apostas=[]
    lista_escolhas=[]
    lista_final=[]

    while len(lista_fichas)>0:
        z=0
        while len(lista_apostas)<len(lista_jogadores):
            aposta=int(input('Digite o valor que deseja apostar ou "0" para sair do jogo, {}: '.format(lista_jogadores[z]))) # Valor da aposta
            lista_apostas.append(aposta)
            if aposta==0:
                lista_final.append(lista_fichas[z])
                lista_apostas.pop(z)
                lista_jogadores.pop(z)
                lista_fichas.pop(z)
                continue

            while lista_apostas[z]>lista_fichas[z]: # Validando aposta
                lista_apostas.pop(z) # Removendo a aposta inválida
                print('Valor inválido, tente novamente')
                aposta=int(input('Digite o valor que deseja apostar ou "0" para sair do jogo: '))
                lista_apostas.append(aposta) # Adicionando uma nova aposta válida (ou não hehe)
                if aposta==0:
                    lista_final.append(lista_fichas[z])
                    lista_apostas.pop(z)
                    lista_jogadores.pop(z)
                    lista_fichas.pop(z)
                    continue
            z+=1
        y=0
        while len(lista_escolhas)<len(lista_jogadores):
            escolha=input('{}, escolha entre "Jogador", "Banco" ou "Empate": '.format(lista_jogadores[y])) # Escolhendo local da aposta
            lista_escolhas.append(escolha)

            while escolha!='Jogador' and escolha!='Banco' and escolha!='Empate': # Validando escolha de local
                lista_escolhas.pop(y)
                print('Escolha inválida, tente novamente')
                escolha=input('Escolha entre "Jogador", "Banco" ou "Empate": ')
                lista_escolhas.append(escolha)
            y+=1
            
        cartas=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4*qtd_baralhos # Definindo o tamanho do baralho que será utilizado no jogo

        pontos_jogador=0 # Pontuação inicial dos jogadores
        pontos_banco=0 # Pontuação inicial do banco

        # Pontuação banco no primeiro par de cartas:
        pontos_banco=(pontuacao(pontos_banco, cartas))[0]
        pontos_banco=(pontuacao(pontos_banco, cartas))[0]
        print('Pontos do banco no primeiro par de cartas: {}'.format(pontos_banco))

        # Pontuação dos jogadores no primeiro par de cartas:
        pontos_jogador=(pontuacao(pontos_jogador, cartas))[0]
        pontos_jogador=(pontuacao(pontos_jogador, cartas))[0]
        print('Pontos do(s) jogador(es) no primeiro par de cartas: {}'.format(pontos_jogador))

        # Adicionar regras adicionais para terceira carta aqui?
        # -----------------------------------------------------

        if pontos_banco==8 or pontos_banco==9 or pontos_jogador==8 or pontos_jogador==9:
            # Vitória:
            vitoria=vitorioso(pontos_jogador, pontos_banco)

        elif pontos_banco<6 or pontos_jogador<6: # Validando terceira carta

            if pontos_jogador<6: # Validando terceira carta jogador
                teste=pontuacao(pontos_jogador, cartas)
                pontos_jogador=teste[0]
                print('Pontos do jogador após a terceira carta: {}'.format(pontos_jogador))

                if pontos_banco<6: # Validando terceira carta banco
                    if pontos_banco==3 and teste[1]!=8:
                        pontos_banco=(pontuacao(pontos_banco, cartas))[0]
                        print('Pontos do banco após a terceira carta: {}'.format(pontos_banco))
                    
                    elif pontos_banco==4 and (teste[1] not in (0, 1, 8, 9)):
                        pontos_banco=(pontuacao(pontos_banco, cartas))[0]
                        print('Pontos do banco após a terceira carta: {}'.format(pontos_banco))
                    
                    elif pontos_banco==5 and (teste[1] not in (0, 1, 2, 3, 8, 9)):
                        pontos_banco=(pontuacao(pontos_banco, cartas))[0]
                        print('Pontos do banco após a terceira carta: {}'.format(pontos_banco))
                    
                    elif pontos_banco in (0, 1, 2):
                        pontos_banco=(pontuacao(pontos_banco, cartas))[0]
                        print('Pontos do banco após a terceira carta: {}'.format(pontos_banco))
            
            elif pontos_banco<6:
                pontos_banco=(pontuacao(pontos_banco, cartas))[0]
                print('Pontos do banco após a terceira carta: {}'.format(pontos_banco))

            # Vitória:
            vitoria=vitorioso(pontos_jogador, pontos_banco)

        # Pagamento das apostas:
        f=0
        while f<len(lista_escolhas):
            if lista_escolhas[f]=='Jogador':
                if vitoria=='Jogador':
                    lista_fichas[f]+=calcula_comissao(lista_apostas[f], qtd_baralhos, 'Jogador')//1
                else:
                    lista_fichas[f]-=lista_apostas[f]

            elif lista_escolhas[f]=='Banco':
                if vitoria=='Banco':
                    lista_fichas[f]+=calcula_comissao(0.95*lista_apostas[f], qtd_baralhos, 'Banco')//1
                else:
                    lista_fichas[f]-=lista_apostas[f]

            else:
                if vitoria=='Empate':
                    lista_fichas[f]+=calcula_comissao(lista_apostas[f]*8, qtd_baralhos, 'Empate')//1
                else:
                    lista_fichas[f]-=lista_apostas[f]
            f+=1
        print('Suas fichas após rodada do jogo: {}'.format(lista_fichas))
        lista_escolhas.clear() # Preparar para uma nova rodada
        lista_apostas.clear() # Preparar para uma nova rodada
        k=0
        while k<len(lista_jogadores):
            if lista_fichas[k]<=0:
                lista_jogadores.pop(k)
                lista_fichas.pop(k)
                k-=1
            k+=1

    print('Suas fichas após encerrar o jogo: {}'.format(lista_fichas))

jogo()
