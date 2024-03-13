#importo a biblioteca random para fazer o random dos arrays
import random

#Aqui criei as duas arrays de dois temas diferentes 
palavras = ["cobra", "macaco", "urso", "tartaruga", "porco"]
palavras2 = ["abacate", "laranja", "banana", "pessego", "tomate"]

# Aqui uso o random para sortear as palavras com tema1
def escolherPalavra1():
    return random.choice(palavras)

def escolherPalavra2():
    return random.choice(palavras2)



def jogarForca():
    palavraTema1 = escolherPalavra1()
    letrasCorretas = set()
    tentativasMaximas = 6
    tentativas = 0

    novaPalavra = input("Digite uma nova palavra para dicionar com o tema (animais): ")
    palavras.append(novaPalavra)

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
                print(f"Parabéns! Acertaste pro player: {palavraTema1}")
                return


    print(f"\033[31mJá atingiste o numero maximo de erros, a palavra era:\033[m \033[32m{palavraTema1}\033[m")

def jogarForca2():
    palavraTema2 = escolherPalavra2()
    letrasCorretas = set()
    tentativasMaximas = 6
    tentativas = 0

    novaPalavra = input("Digite uma nova palavra para dicionar com o tema (frutas): ")
    palavras2.append(novaPalavra)

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
                print(f"Parabéns! Acertaste pro player: {palavraTema2}")
                return

         
    print(f"\033[31mJá atingiste o numero maximo de erros, a palavra era:\033[m \033[32m {palavraTema2}\033[m")

def main():
    print("1-animais")
    print("2-frutas")
    tema:int = int(input("Escolhe um tema: "))

    if tema == 1:
        jogarForca()

    elif tema == 2:
        jogarForca2()

    else:
        print("METE UM NUMERO QUE TEJA UM TEMA ASSOCIADO")


if __name__ == "__main__":
    print("JOGO DA FORCA")
    print("")
    main()
    