numero_righe = int(input("Inserisci il numero di righe dell'albero: "))
lettera = input("Inserisci una lettera: ")

def costruisci_albero(numero_righe, lettera):
    for i in range(0, numero_righe):
        print(" " * (numero_righe-i-1) + lettera * (1+i*2))

costruisci_albero(numero_righe, lettera)