import random

#Lista de palavras pro jogo
palavras = ['maça', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    #Escolhe uma palavra aleatoria da lista
    palavra = random.choice(palavras)
    #Cria uma lista para armazenar as letras corretas
    letras_corretas = ['_'] * len(palavra)
    #Cria uma lista para armazenar as letras erradas
    letras_erradas = []
    #Defina o numero de tentativas
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Você tem 6 tentativas para advinhar a palavra.")

    while tentativas > 0 and '_' in letras_corretas:
        #Mostra a palavra com as letras corretas
        print(' '.join(letras_corretas))
        #Pede ao usuario para digitar uma letra
        letra = input("Digite uma letra:").lower()
        #verifica se a letra esta correta
        if letra in palavra:
            #substitui as letras corretas na lista
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_corretas[i] = letra 
        else:
            #adiciona a letra errada à lista
            letras_erradas.append(letra)
            #Diminui o numero de tentativas
            tentativas -= 1
            print(f"Tentativas restantes:{tentativas}")
            print(f"Letras erradas: {', '.join(letras_erradas)}")

#verifica se o usuario ganhou ou perdeu
            if '_' not in letras_corretas:
                print("Parabéns! Você ganhou!")
            else:
                print(f"Vocẽ perdeu! A palavra era {palavra}.")

#inicia o jogo
jogo_da_forca()