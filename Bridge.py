import random

# Definizione delle carte e dei semi
SEMI = ['Cuori', 'Quadri', 'Fiori', 'Picche']
VALORI = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
PUNTEGGIO = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Carta:
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def __repr__(self):
        return f"{self.valore} di {self.seme}"

class Mazzo:
    def __init__(self):
        self.carte = [Carta(seme, valore) for seme in SEMI for valore in VALORI]
        random.shuffle(self.carte)

    def distribuisci(self):
        return [self.carte[i::4] for i in range(4)]

def stampa_mano(mano):
    for carta in mano:
        print(carta)

# Fase di dichiarazione
def dichiarazione():
    dichiarazioni = ['Passa', '1 Cuori', '2 Cuori', '3 Cuori', '1 Quadri', '2 Quadri', '3 Quadri', '1 Fiori', '2 Fiori', '3 Fiori', '1 Picche', '2 Picche', '3 Picche']
    dichiarazioni_giocatori = []
    for i in range(4):
        dichiarazione_giocatore = random.choice(dichiarazioni)
        dichiarazioni_giocatori.append(dichiarazione_giocatore)
        print(f"Dichiarazione del giocatore {i + 1}: {dichiarazione_giocatore}")
    return dichiarazioni_giocatori

# Fase di gioco delle carte
def gioco_delle_carte(mani, seme_trionfo):
    punteggio_giocatori = [0, 0, 0, 0]
    for turno in range(13):
        tavolo = []
        seme_giocato = None
        for i in range(4):
            carta_giocata = mani[i].pop(0)
            tavolo.append((carta_giocata, i))
            if seme_giocato is None:
                seme_giocato = carta_giocata.seme
            print(f"Il giocatore {i + 1} gioca: {carta_giocata}")
        vincitore_turno = determinare_vincitore(tavolo, seme_trionfo, seme_giocato)
        punteggio_giocatori[vincitore_turno] += 1
        print(f"Carte sul tavolo: {[carta[0] for carta in tavolo]}")
        print(f"Vincitore del turno: Giocatore {vincitore_turno + 1}")
        print()
    return punteggio_giocatori

# Determinare il vincitore del turno
def determinare_vincitore(tavolo, seme_trionfo, seme_giocato):
    carte_giocabili = [carta for carta in tavolo if carta[0].seme == seme_giocato or carta[0].seme == seme_trionfo]
    carta_vincente = max(carte_giocabili, key=lambda x: (x[0].seme == seme_trionfo, PUNTEGGIO[x[0].valore]))
    return carta_vincente[1]

# Creazione e mescolamento del mazzo
mazzo = Mazzo()
mani = mazzo.distribuisci()

# Stampa delle mani dei giocatori
for i, mano in enumerate(mani):
    print(f"Mano del giocatore {i + 1}:")
    stampa_mano(mano)
    print()

# Fase di dichiarazione
print("Fase di dichiarazione:")
dichiarazioni = dichiarazione()
print()

# Supponiamo che il seme trionfo sia Cuori
seme_trionfo = 'Cuori'

# Fase di gioco delle carte
print("Fase di gioco delle carte:")
punteggio_giocatori = gioco_delle_carte(mani, seme_trionfo)

# Stampa del punteggio finale
print("Punteggio finale:")
for i, punteggio in enumerate(punteggio_giocatori):
    print(f"Giocatore {i + 1}: {punteggio} punti")