#JOKENPO ✂️ 📄 🪨

jogo = "Menu do jogo JOKENPO"
op1 = "Pedra = 1"
op2 = "Tesoura = 2"
op3 = "Papel = 3"

print(jogo)
print(op1)
print(op2)
print(op3)

nome = str(input("Digite seu nome: "))

opcoes = ["Pedra", "Papel", "Tesoura"]
historico = []

def mostrar_menu():
    print("\n1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("0 - Sair")

def verificar_vencedor(usuario, maquina):
    if usuario == maquina:
        return "Empate"
    elif (usuario == 1 and maquina == 3) or (usuario == 2 and maquina == 1) or (usuario == 3 and maquina == 2):
        return "Jogador"
    else:
        return "Maquina"

while True:
    vitorias_jogador = 0
    vitorias_maquina = 0
    empates = 0
    contador = 0
    historico.clear()
    sair = False

    while vitorias_jogador < 3 and vitorias_maquina < 3:
        mostrar_menu()
        escolha = int(input("Digite sua escolha: "))

        match escolha:
            case 0:
                sair = True
                break
            case 1 | 2 | 3:
                pass
            case _:
                print("Opção inválida!")
                continue

        maquina = (contador % 3) + 1
        contador += 1

        print(f"você jogou {opcoes[escolha - 1].lower()}")

        resultado = verificar_vencedor(escolha, maquina)

        if resultado == "Empate":
            empates += 1
            print("Empate! Repita a rodada.")
            historico.append("Empate")
        elif resultado == "Jogador":
            vitorias_jogador += 1
            print("Você venceu a rodada!")
            historico.append(f"Vitória de {nome}")
        else:
            vitorias_maquina += 1
            print("A máquina venceu a rodada!")
            historico.append("Vitória da máquina")

        print(f"Placar: {nome} {vitorias_jogador} x {vitorias_maquina} Máquina (Empates: {empates})")

    if sair:
        print("Saindo do jogo...")
        break

    if vitorias_jogador == 3:
        print(f"\n{nome} venceu o jogo!🏆")
    else:
        print("\nA máquina venceu o jogo!🏆")

    print("\nResultados das rodadas:")
    for item in historico:
        print("-", item)

    novamente = input("\nJogar novamente? (s/n): ").lower()
    if novamente != "s":
        print("Programa encerrado.")
        break