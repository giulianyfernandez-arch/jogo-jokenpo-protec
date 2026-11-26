# Jokenpô - UC 4: Desenvolver Algoritmos
import os
import random

os.system("")

VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
CIANO = "\033[96m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

OPCOES = ["Pedra", "Papel", "Tesoura"]
EMOJIS = {"Pedra": "🪨", "Papel": "📄", "Tesoura": "✂️"}

# cada jogada (chave) vence o seu valor
VENCE = {"Pedra": "Tesoura", "Papel": "Pedra", "Tesoura": "Papel"}

VITORIAS_PARA_GANHAR = 3  # melhor de 5


def mostrar_menu():
    print(f"\n{CIANO}{NEGRITO}===== JOKENPÔ 🪨📄✂️ ====={RESET}")
    print("1 - Iniciar jogo")
    print("2 - Consultar regras")
    print("3 - Consultar resultados")
    print("4 - Sair")


def mostrar_regras():
    print(f"\n{CIANO}{NEGRITO}--- REGRAS ---{RESET}")
    print("🪨 Pedra vence ✂️ Tesoura.")
    print("✂️ Tesoura vence 📄 Papel.")
    print("📄 Papel vence 🪨 Pedra.")
    print("Jogadas iguais dão empate.")
    print("Ganha a partida quem vencer", VITORIAS_PARA_GANHAR, "rodadas.")


def pedir_nome():
    nome = input("Digite seu nome: ").strip()
    while nome == "":
        nome = input(f"{VERMELHO}O nome não pode ficar vazio.{RESET} Digite seu nome: ").strip()
    return nome


def pedir_jogada():
    print("\nEscolha: 1 - 🪨 Pedra | 2 - 📄 Papel | 3 - ✂️ Tesoura | 0 - Desistir")
    escolha = input("Sua opção: ").strip()
    while escolha not in ["0", "1", "2", "3"]:
        escolha = input(f"{VERMELHO}Opção inválida!{RESET} Digite 0, 1, 2 ou 3: ").strip()
    return escolha


def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif VENCE[jogador] == computador:
        return "Vitória"
    else:
        return "Derrota"


def mostrar_historico(historico):
    print(f"\n{CIANO}{NEGRITO}--- HISTÓRICO DE RODADAS ---{RESET}")
    if len(historico) == 0:
        print("Nenhuma rodada jogada.")
    for rodada in historico:
        print(rodada)


def jogar_partida(nome):
    vitorias = 0
    derrotas = 0
    empates = 0
    historico = []  # uma frase para cada rodada

    while vitorias < VITORIAS_PARA_GANHAR and derrotas < VITORIAS_PARA_GANHAR:
        escolha = pedir_jogada()
        if escolha == "0":
            break

        jogador = OPCOES[int(escolha) - 1]
        computador = random.choice(OPCOES)
        resultado = verificar_vencedor(jogador, computador)

        if resultado == "Vitória":
            vitorias += 1
            cor_res = f"{VERDE}Vitória 🏆{RESET}"
        elif resultado == "Derrota":
            derrotas += 1
            cor_res = f"{VERMELHO}Derrota ❌{RESET}"
        else:
            empates += 1
            cor_res = f"{AMARELO}Empate 🤝{RESET}"

        rodada = (
            f"Rodada {len(historico) + 1}: "
            f"{EMOJIS[jogador]} {jogador} x {EMOJIS[computador]} {computador} = {cor_res}"
        )
        historico.append(rodada)

        print(rodada)
        print(
            f"Placar: {nome} {VERDE}{vitorias}{RESET} x {VERMELHO}{derrotas}{RESET} Computador "
            f"| Empates: {AMARELO}{empates}{RESET}"
        )

    if vitorias == VITORIAS_PARA_GANHAR:
        final = f"{VERDE}ganhou{RESET}"
    elif derrotas == VITORIAS_PARA_GANHAR:
        final = f"{VERMELHO}perdeu{RESET}"
    else:
        final = f"{AMARELO}desistiu{RESET}"

    mostrar_historico(historico)
    resumo = f"{nome} {final} | Vitórias: {vitorias} | Derrotas: {derrotas} | Empates: {empates}"
    print("\nFim da partida:", resumo)
    return resumo


def mostrar_resultados(resultados):
    print(f"\n{CIANO}{NEGRITO}--- RESULTADOS DAS PARTIDAS ---{RESET}")
    if len(resultados) == 0:
        print("Nenhuma partida jogada ainda.")
    for resultado in resultados:
        print(resultado)


def main():
    resultados = []  # guarda o resumo de cada partida

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                nome = pedir_nome()
                mostrar_regras()
                resultados.append(jogar_partida(nome))
            case "2":
                mostrar_regras()
            case "3":
                mostrar_resultados(resultados)
            case "4":
                print(f"{CIANO}Até a próxima!{RESET}")
                break
            case _:
                print(f"{VERMELHO}Opção inválida! Tente novamente.{RESET}")


main()