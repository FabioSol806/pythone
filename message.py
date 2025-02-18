class Message:
    def __init__(self, sender, recipient):
        # Inizializza il mittente, il destinatario e il testo del messaggio
        self._sendersender = sender
        self._recipient = recipient
        self._text = ""

    def append(self, line):
        # Aggiunge una riga alla fine del testo del messaggio
        if self._text:
            self._text += "\n"  # Aggiunge una nuova riga se il testo non è vuoto
        self._text += line

    def toString(self):
        # Trasforma il messaggio in un'unica, lunga stringa
        return f"Da: {self._sendersender}\nA: {self._recipient}\n\n{self._text}"
# Richiedi l'inserimento dei dati da parte dell'utente
mittente = input("Inserisci l'indirizzo email del mittente: ")
destinatario = input("Inserisci l'indirizzo email del destinatario: ")

# Crea un nuovo messaggio con i dati inseriti
msg = Message(mittente, destinatario)

# Aggiungi righe di testo al messaggio
print("Inserisci il testo del messaggio. Digita 'fine' per terminare.")
while True:
    riga = input()
    if riga.lower() == 'fine':
        break
    msg.append(riga)

# Stampa il messaggio completo
print("\nMessaggio completo:")
print(msg.toString())