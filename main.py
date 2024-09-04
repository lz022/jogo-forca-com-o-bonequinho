import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

def desenho(tentativas_falhas):
    if tentativas_falhas == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif tentativas_falhas == 1:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif tentativas_falhas == 2:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif tentativas_falhas == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif tentativas_falhas == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
    elif tentativas_falhas == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|   / ")
        print("|      ")
        print("_      ")
        print()
    elif tentativas_falhas == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|   / \\ ")
        print("|      ")
        print("_      ")
        print()

def game():
    print("Bem-Vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo: ")
    print()

    # Lista de frutas
    frutas = [
        "abacate", "amora", "ameixa", "acerola", "abacaxi", "açai", "banana",
        "caju", "cereja", "cacau", "caqui", "cupuaçu", "damasco",
        "goiaba", "groselia", "guarana", "jaca", "kiwi", "laranja", "limao",
        "lima", "lixia", "melancia", "mamao", "melao", "maracuja", "manga", "maça",
    ]

    # Escolha da fruta aleatória
    fruta_escolhida = random.choice(frutas)

    # Inicialização
    length = len(fruta_escolhida)
    chances = 6
    letras_erradas = []
    letras_certas = ['_'] * length  # Inicia com todos os tracinhos

    tentativas_falhas = 0
    while chances > 0 and '_' in letras_certas:
        limpa_tela()  # Limpa a tela antes de cada nova tentativa
        print(' '.join(letras_certas))  # Mostrar o estado atual da palavra
        print(f"Chances restantes: {chances}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        desenho(tentativas_falhas)  # Exibir o desenho atual do enforcado

        letra = input("Digite uma letra: ").lower()

        if letra in fruta_escolhida:
            # Atualizar letras certas
            for i, char in enumerate(fruta_escolhida):
                if char == letra:
                    letras_certas[i] = letra
        else:
            # Atualizar letras erradas e diminuir chances
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                tentativas_falhas += 1
                chances -= 1

    # Finalizar o jogo
    limpa_tela()  # Limpa a tela antes de mostrar o resultado
    desenho(tentativas_falhas)  # Mostrar o desenho final

    if '_' not in letras_certas:
        print(f"Você venceu! A palavra era: {fruta_escolhida}")
    else:
        print(f"Você perdeu! A palavra era: {fruta_escolhida}")

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")