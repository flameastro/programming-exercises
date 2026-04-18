# palavra = "Zebra"

# for x in range(800000):
#     print(f"{x} Pulando")

#     if x == 799890:
#         print(f"Palavra encontrada: {x}")
#         break


# Uma maneira seria começar abrindo o dicionário ao meio, na sua parte central. Olhamos a palavra
# que se encontra no topo dessa página. Se for alfabeticamente “menor” que a palavra procurada, o que
# fazemos? Sabemos que, por conta da organização do dicionário, a palavra que buscamos não pode
# estar antes desta página, e que só pode estar depois. Deste modo, podemos ignorar todas as palavras
# da parte do dicionário que estão antes desta página. Observe que se tínhamos um universo de busca
# de 400 mil palavras, agora nosso universo de busca se reduziu a 200 mil palavras, a metade do
# universo original. Um ganho considerável! 
# Após esse primeiro passo, repetimos o processo de abrir o dicionário na página central. Novamente
# fazemos a escolha. Se a palavra da página for menor alfabeticamente, descartamos a metade anterior.
# Se for maior, devemos descartar a metade posterior. Vamos repetindo este processo até encontrar a
# palavra ou reduzirmos nosso universo de busca a apenas uma página e não a encontrarmos.
# Note que, segundo este algoritmo, cada vez que olhamos uma palavra, nosso universo de busca se
# reduz à metade do universo de busca anterior. Esse algoritmo é tão bom que tem até um nome: busca
# binária! Seu nome vem do fato de que a cada passo o universo de busca é dividido por 2
import time
import math


def busca_binaria(minimo, maximo, numero):
    tentativas = 0

    corte = maximo // 2

    if numero > corte:
        minimo = corte
    elif numero < corte:
        maximo = corte

    while True:
        tentativas += 1

        if numero < corte:
            maximo = corte
            corte = minimo + ((maximo - minimo) // 2)
        elif numero > corte:
            minimo = corte
            corte = corte + ((maximo - minimo) // 2)+1
        else:
            print(f"Tentativas finais: {tentativas}")
            break

        print(f"Máximo: {maximo} | Corte: {corte} | Mínimo: {minimo}")

busca_binaria(0, 400000, 2)
