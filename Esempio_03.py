player1 = "Giocatore 1"
player2 = "Giocatore 2"

def simulate_game(player1, player2):
    score_player1 = 0
    score_player2 = 0
    points = [0, 15, 30, 40, "ADV"]
    while True:
        winner = input(f"Chi ha vinto il punto? Inserisci '{player1}' o '{player2}': ")
        if winner == player1:
            score_player1 += 1
        elif winner == player2:
            score_player2 += 1
        else:
            print("Input non valido. Riprova.")
            continue
        if score_player1 >= 4 and score_player1 - score_player2 >= 2:
            return f"{player1} ha vinto il game!"
        elif score_player2 >= 4 and score_player2 - score_player1 >= 2:
            return f"{player2} ha vinto il game!"
        print(f"Punteggio: {player1} {points[min(score_player1, 4)]} - {player2} {points[min(score_player2, 4)]}")
print(simulate_game(player1, player2))