#importo a biblioteca random para fazer o random dos arrays
import random
import os

#Aqui criei as duas arrays de dois temas diferentes 
palavras = ["cobra", "macaco", "urso", "tartaruga", "porco"]
palavras2 = ["abacate", "laranja", "banana", "pessego", "tomate"]

# Aqui uso o random para sortear as palavras com tema1
def escolherPalavra1():
    return random.choice(palavras)

# Aqui uso o random para sortear as palavras com tema2
def escolherPalavra2():
    return random.choice(palavras2)



#Função para jogar o jogo se for o tema1
def jogarForca():
    palavraTema1 = escolherPalavra1()
    letrasCorretas = set()
    tentativasMaximas = 6
    tentativas = 0

    #Aqui peço ao usuário uma palavra e adiciono a lista com o append()
    novaPalavra = input("Digite uma nova palavra para dicionar com o tema (animais): ")
    palavras.append(novaPalavra)

    #Aqui criei um while para o jogo continuar até chegar ao numero de tentativas máximas
    while tentativas < tentativasMaximas:
                    

            # Mostra a palavra com as letras adivinhadas
            palavra_exibida = "".join(letra if letra in letrasCorretas else "_" for letra in palavraTema1)
            print(f"Palavra: {palavra_exibida}")

            # Pede a letra
            letra = input("Escreve uma letra: ").lower()

            # Ve se a letra ja foi tentada
            if letra in letrasCorretas:
                print("Já tentaste esta letra, tenta outra.")
                continue

            # Ve se a letra está na palavra
            if letra in palavraTema1:
                print("Letra correta!")
                letrasCorretas.add(letra)
    
            else:
                print("Letra errada.")
                tentativas += 1

            # vê se a palavra que escreveste esta certa
            if set(palavraTema1) == letrasCorretas:
                print(f"\033[32Parabéns! Acertaste pro player: \033[m \033[36{palavraTema1}[m")
                return

    #Se chegar ao numero de tentativas máximas faz este print
    print(f"\033[31mJá atingiste o numero maximo de erros, a palavra era:\033[m \033[32m{palavraTema1}\033[m")

#Aqui é a função para jogar com o tema 2
def jogarForca2():
    palavraTema2 = escolherPalavra2()
    letrasCorretas = set()
    tentativasMaximas = 6
    tentativas = 0

    #Aqui peço ao usuário uma palavra e adiciono a lista com o append()
    novaPalavra = input("Digite uma nova palavra para dicionar com o tema (frutas): ")
    palavras2.append(novaPalavra)

    #Aqui criei um while para o jogo continuar até chegar ao numero de tentativas máximas
    while tentativas < tentativasMaximas:
                    
    

            # Mostra a palavra com as letras adivinhadas
            palavra_exibida = "".join(letra if letra in letrasCorretas else "_" for letra in palavraTema2)
            print(f"Palavra: {palavra_exibida}")

            # Pede a letra
            letra = input("Escreve uma letra: ").lower()

            # Ve se a letra ja foi tentada
            if letra in letrasCorretas:
                print("Já tentaste esta letra, tenta outra.")
                continue

            # Ve se a letra está na palavra
            if letra in palavraTema2:
                print("Letra correta!")
                letrasCorretas.add(letra)
    
            else:
                print("Letra errada.")
                tentativas += 1

            # vê se a palavra que escreveste esta certa
            if set(palavraTema2) == letrasCorretas:
                print(f"\033[32Parabéns! Acertaste pro player: \033[m \033[36{palavraTema2}[m")
                return

    #Se chegar ao numero de tentativas máximas faz este print    
    print(f"\033[31mJá atingiste o numero maximo de erros, a palavra era:\033[m \033[32m {palavraTema2}\033[m")

#Aqui é a função main, faz o usuário escolher o tema
def main():
    nome = input("\033[32mNickname:\033[m ")
    
    with open("Jogo Da Forca PT.txt", "a") as f:
        f.write('Nome - ' + nome + '\n')
    
    #f = open("Jogo Da Forca PT.txt", "w")
    #f.write(nome)
    #f = open("Jogo Da Forca PT.txt", 'r')
    #f.close()

    print("")

    print("1-animais")
    print("2-frutas")
    tema:int = int(input("Escolhe um tema: "))

    #Se o tema for 1 executa a função jogarForca()
    if tema == 1:
        jogarForca()

    #Se o tema for 2 executa a função jogarForca2()
    elif tema == 2:
        jogarForca2()

    #Aqui é uma verificação se for um numero sem tema
    else:
        print("METE UM NUMERO QUE TEJA UM TEMA ASSOCIADO")

#Aqui é o main em si
if __name__ == "__main__":
    print("")
    print("\033[35mJOGO DA FORCA\033[m")
    print("")
    main()
    