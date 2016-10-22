print("\n                                Bem-vindo ao Jogo de Damas!!!(Multiplayer)\n\n")
tutorial= input("Deseja ler as regras?(s/n)")
print("")
regras= '''
1°: Você combina com seu amigo para quem vai se o |X| e o |O|.
2º: O jogador da vez deve escolher a posição que deseja jogar de acordo com a tabela ao lado.
3º: Ganha aquele que conseguir 3 |X| ou 3 |O| de forma ininterrupta nas verticais, horizontais ou diagonais
4º: Caso o item 3º não seja alcançado o jogo da Velha, ou seja, Empate.
'''

if tutorial=="s":
    print(regras)


velha="""               Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""
# Uma lista de posições (linha e coluna) para cada posição válida do jogo
# Um elemento extra foi adicionado para facilitar a manipulação
# dos índices e para que estes tenham o mesmo valor da posição
#
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3













