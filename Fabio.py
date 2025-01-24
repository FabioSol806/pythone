def calcola_tassazione(reddito):
    if reddito <= 28000: tassazione = reddito * 0.23 
        
    elif reddito <= 50000:tassazione = 28000 * 0.23 + (reddito - 28000) * 0.35 
    
    else:tassazione = 28000 * 0.23 + 22000 * 0.35 + (reddito - 50000) * 0.43

    return tassazione

reddito = float(input("Inserisci il tuo reddito: "))
tassazione = calcola_tassazione(reddito)
print(f"La tassazione per un reddito di (reddito) è: {tassazione:.2f} euro")