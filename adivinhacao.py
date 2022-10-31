import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numerosecreto = random.randrange(1, 101) #gera um numero aleatorio entre 1 e 100
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1)-Fácil (2)-Médio (3)-Difícil")
    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: ")) #ja recebe como inteiro sem precisar converter

        if (chute < 1 or chute > 100):
            print("Número inválido! Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numerosecreto
        maior = chute > numerosecreto
        menor = chute < numerosecreto
        if (acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numerosecreto - chute)  # desconsidera sinais negativo ou positivo, a ordem da operaçao não muda o resultado,
            pontos = pontos - pontos_perdidos  # calcula a perda de pontos com numeros absolutos
            if (maior):
                print("Você errou! O seu chute foi MAIOR que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi MENOR que o número secreto.")

    print("O número secreto era: ", numerosecreto)
    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()