# ============================================
# JOGO DE ADIVINHAÇÃO DE NÚMEROS
# Desenvolvido com auxílio de Inteligência Artificial (Claude - Anthropic)
# ============================================

import random  # Biblioteca para gerar números aleatórios

# -------------------- VARIÁVEIS --------------------
# Variáveis para armazenar os limites do jogo
limite_inferior = 1
limite_superior = 50

# Variáveis para controle de pontuação e estatísticas
pontuacao = 0
rodadas_jogadas = 0
total_tentativas = 0

# Variável de controle do loop principal
jogando = True

# -------------------- INÍCIO DO JOGO --------------------
print("=" * 50)
print("   BEM-VINDO AO JOGO DE ADIVINHAÇÃO DE NÚMEROS!")
print("=" * 50)
print(f"Tente adivinhar o número entre {limite_inferior} e {limite_superior}.")
print("Você tem 7 tentativas por rodada.")
print("Boa sorte!\n")

# -------------------- ESTRUTURA DE REPETIÇÃO (while) --------------------
# Loop principal que mantém o jogo rodando até o jogador decidir parar
while jogando:
    # Gera um número aleatório (variável do número secreto)
    numero_secreto = random.randint(limite_inferior, limite_superior)
    tentativas = 0
    max_tentativas = 7
    acertou = False
    rodadas_jogadas += 1

    print(f"\n--- RODADA {rodadas_jogadas} ---")
    print(f"Um novo número foi gerado entre {limite_inferior} e {limite_superior}!")

    # -------------------- ESTRUTURA DE REPETIÇÃO (for) --------------------
    # Loop que controla as tentativas dentro de cada rodada
    for tentativa_atual in range(1, max_tentativas + 1):
        # Recebe o palpite do jogador
        try:
            palpite = int(input(f"\nTentativa {tentativa_atual}/{max_tentativas} - Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        tentativas += 1
        total_tentativas += 1

        # -------------------- ESTRUTURAS DE DECISÃO (if/elif/else) --------------------
        # Verifica se o palpite está correto, é maior ou menor
        if palpite == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você acertou o número {numero_secreto}!")
            print(f"Você usou {tentativas} tentativa(s).")

            # Cálculo de pontos baseado no número de tentativas
            if tentativas == 1:
                pontos_ganhos = 100
                print("INCRÍVEL! Acertou de primeira! +100 pontos!")
            elif tentativas <= 3:
                pontos_ganhos = 50
                print("Muito bom! +50 pontos!")
            elif tentativas <= 5:
                pontos_ganhos = 25
                print("Bom trabalho! +25 pontos!")
            else:
                pontos_ganhos = 10
                print("Ufa, quase! +10 pontos!")

            pontuacao += pontos_ganhos
            acertou = True
            break  # Sai do loop for ao acertar

        elif palpite < numero_secreto:
            print("📈 O número secreto é MAIOR que o seu palpite.")
            # Dica extra quando falta pouco
            if numero_secreto - palpite <= 5:
                print("   (Você está muito perto!)")

        else:
            print("📉 O número secreto é MENOR que o seu palpite.")
            # Dica extra quando falta pouco
            if palpite - numero_secreto <= 5:
                print("   (Você está muito perto!)")

    # Decisão: se não acertou após todas as tentativas
    if not acertou:
        print(f"\n😞 Suas tentativas acabaram! O número era {numero_secreto}.")

    # Exibe placar atual
    print(f"\n📊 PLACAR ATUAL: {pontuacao} pontos | Rodadas: {rodadas_jogadas}")

    # -------------------- DECISÃO: CONTINUAR OU PARAR --------------------
    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta in ['s', 'n']:
            break
        print("Por favor, digite 's' para sim ou 'n' para não.")

    if resposta == 'n':
        jogando = False  # Altera a variável de controle para encerrar o loop principal

# -------------------- RESUMO FINAL --------------------
print("\n" + "=" * 50)
print("   RESUMO FINAL DO JOGO")
print("=" * 50)
print(f"Rodadas jogadas: {rodadas_jogadas}")
print(f"Total de tentativas: {total_tentativas}")
print(f"Pontuação final: {pontuacao} pontos")

# Decisão final baseada na pontuação
if pontuacao >= 200:
    print("\n🏆 Você é um MESTRE da adivinhação!")
elif pontuacao >= 100:
    print("\n⭐ Excelente desempenho!")
elif pontuacao >= 50:
    print("\n👍 Bom jogo! Continue praticando!")
else:
    print("\n💪 Não desista! Tente novamente!")

print("\nObrigado por jogar! Até a próxima! 👋")
