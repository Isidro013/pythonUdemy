import random

chances = 7
tentativas = 1
jogador = ''

num_secreto = random.randint(1, 100)
print("Bem vindo, começa agora o jogo da adivinhação.")
print("Você tem 7 chances de acertar o número secreto.")

jogador = input("Digite seu nome: ")
print("Chute um número entre 1 e 100.")

while tentativas <= 7:
    numero = int(input("Escolha um Número: "))
    if numero < num_secreto:
        print ("Tentativa {} de {}.".format(tentativas, chances))
        print('{} você errou, seu número é menor que o sorteado.'
        'Tente novamente'.format(jogador))
    elif numero > num_secreto:
        print ("Tentativa {} de {}.".format(tentativas, chances))
        print('{} você errou, seu número é maior que o sorteado.'
        'Tente novamente'.format(jogador))
    elif numero == num_secreto:
        print("PARABÉNS, {}".format(jogador))
        print("{}, voce acertou com {} tentativas.".format(jogador, tentativas))
        break
    tentativas = tentativas + 1
    if tentativas > 7:
        print("GAME OVER. O número secreto era {}".format(num_secreto))
    