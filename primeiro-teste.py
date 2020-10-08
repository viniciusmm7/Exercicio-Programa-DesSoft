# EP - Design de Software
# Equipe: Guilherme da Franca, Vinícius Matheus Morales
# Data: 18/10/2020

import random

# Nome e fichas:
nome=input('Digite seu nome: ')

fichas=int(input('Digite sua quantidade de fichas: '))

print('Nome: {}\nFichas: {}'.format(nome, fichas))

# Função para calcular o valor da carta:
def valor_carta (x, y):
  #sorteador (add e remover carta)
  if x[y]=='A':
    return 1

  elif x[y]=='10' or x[y]=='J' or x[y]=='Q' or x[y]=='K':
    return 0

  else:
    return int(x[y])

# Jogo:
while fichas>0:

  # Valor da aposta:
  aposta=int(input('Faça sua aposta: '))

  if aposta==0:
    break

  # Condição para a aposta ser válida:
  while aposta>fichas:
    print('Valor inválido')
    aposta=int(input('Faça sua aposta: '))

  # Local da aposta:
  escolha=input('Escolha entre "Jogador", "Banco" ou "Empate": ')

  # Condição do local ser válido:
  while escolha!='Jogador' and escolha!='Banco' and escolha!='Empate':
    print('Escolha inválida')
    escolha=input('Escolha entre "Jogador", "Banco" ou "Empate": ')

  # Cartas:
  cartas=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  cartas*=4
  
  pontos_jogador=0
  pontos_banco=0
  
  # Valor das cartas:

  """Par de cartas do Banco:"""
  i=0
  while i<2
    # Gerando uma carta:
    numero_carta=random.randint(0, len(cartas)-1)

    # Adicionando a pontuação:
    pontos_banco+=valor_carta(cartas, numero_carta)

    # Removendo a carta da lista:
    cartas.remove(cartas[numero_carta])
    i+=1

  """Par de cartas do Jogador:"""

  numero_carta=random.randint(0, 49)
  pontos_jogador+=valor_carta(cartas, numero_carta)
  cartas.remove(cartas[numero_carta])

  numero_carta=random.randint(0, 48)
  pontos_jogador+=valor_carta(cartas, numero_carta)
  cartas.remove(cartas[numero_carta])

  pontos_banco=str(pontos_banco)
  pontos_banco=pontos_banco[-1]
  pontos_banco=int(pontos_banco)
  print(pontos_banco)

  i=47
  if pontos_banco<6:
      # Gerando uma nova carta:
    numero_carta=random.randint(0, i)
    i-=1
      # Adicionando pontuação do banco:
    pontos_banco+=valor_carta(cartas, numero_carta)

      # Removendo a carta da lista:
    cartas.remove(cartas[numero_carta])

     

    pontos_banco=str(pontos_banco)
    pontos_banco=pontos_banco[-1]
    pontos_banco=int(pontos_banco)
  print(pontos_banco)

  while pontos_jogador<6:
    
    # Adicionando pontuação do jogador:
    pontos_jogador+=valor_carta(cartas, numero_carta)

      # Removendo a carta da lista:
    cartas.remove(cartas[numero_carta])

      # Gerando uma nova carta:
    numero_carta=random.randint(0, i)
    i-=1

    pontos_jogador=str(pontos_jogador)
    pontos_jogador=pontos_jogador[-1]
    pontos_jogador=int(pontos_jogador)
  print(pontos_jogador)

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

print(fichas)
