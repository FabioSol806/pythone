def giocata_utente(numero_giocatore):
    while True:
        mossa = input(f"Inserisci la giocata del giocatore {numero_giocatore} (sasso, carta, forbici): ")
        if mossa.lower() in ['sasso', 'carta', 'forbici']:
            return mossa
        else:
            print("Giocata non valida. Riprova.")


def vincitore(mossa1, mossa2):
    if mossa1.lower() == mossa2.lower():
        return 'parità'
    elif (mossa1.lower() == 'sasso' and mossa2.lower() == 'forbici') or (mossa1.lower() == 'carta' and mossa2.lower() == 'sasso') or (mossa1.lower() == 'forbici' and mossa2.lower() == 'carta'):
        return 'giocatore 1'
    else:
        return 'giocatore 2'

vittorie_g1 = 0
vittorie_g2 = 0

while (vittorie_g1 - vittorie_g2 < 3) and (vittorie_g2 - vittorie_g1 < 3):
    mossa1 = giocata_utente(1)
    mossa2 = giocata_utente(2)
    vinc = vincitore(mossa1, mossa2)
    if vinc == 'giocatore 1':
        vittorie_g1 += 1
    elif vinc == 'giocatore 2':
        vittorie_g2 += 1
    print(f"Giocatore 1: {mossa1}, Giocatore 2: {mossa2} -> {vinc}")

print(f"Il programma è terminato! Totale vittorie - Giocatore 1: {vittorie_g1}, Giocatore 2: {vittorie_g2}")