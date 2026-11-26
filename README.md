# Jokenpô 🪨📄✂️

Jogo de pedra, papel e tesoura contra o computador, executado no terminal.

## Objetivo
Vencer 3 rodadas antes do computador (melhor de 5).

## Integrantes e contribuições
| Nome | Principais contribuições |
|---|---|
| (Giuliany) | |
| (Estefany) | |
| (Jacqueline) | |
| (Anna) | |

## Regras
- 🪨 Pedra vence ✂️ Tesoura, ✂️ Tesoura vence 📄 Papel e 📄 Papel vence 🪨 Pedra.
- Jogadas iguais dão empate, que não conta como vitória.
- Ganha a partida quem vencer 3 rodadas.

## Como executar
É preciso ter o Python 3.10 ou superior (por causa do `match case`).

    python main.py

No Linux ou macOS, use `python3 main.py`.

## Funcionalidades
- Menu: iniciar jogo, consultar regras, consultar resultados e sair.
- Identificação do jogador pelo nome.
- Validação das opções digitadas.
- Sorteio da jogada do computador.
- Placar de vitórias, derrotas e empates.
- Histórico das rodadas e resultados das partidas em listas.
- Possibilidade de jogar novamente sem reiniciar o programa.

## Exemplo de uso
    Escolha: 1 - 🪨 Pedra | 2 - 📄 Papel | 3 - ✂️ Tesoura | 0 - Desistir
    Sua opção: 1
    Rodada 1: 🪨 Pedra x ✂️ Tesoura = 🏆 Vitória
    Placar: Ana 1 x 0 Computador | Empates: 0

## Conceitos aplicados
Entrada de dados, operadores, if/elif/else, match case, while, while True, for, listas, dicionário e funções.

## Limitações conhecidas
- Os resultados são apagados quando o programa é fechado.
- Apenas um jogador por partida, contra o computador.