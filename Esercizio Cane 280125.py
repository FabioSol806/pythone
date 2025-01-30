def discount(prices, nItems):
    animal_present = False
    other_items_total = 0
    other_items_count = 0
    
    for i in range(nItems):
        if isPet[i]:
            animal_present = True
        else:
            other_items_total += prices[i]
            other_items_count += 1
            
    if animal_present and other_items_count >= 5:
        return other_items_total * 0.20
    else:
        return 0

prices = []
isPet = []

while True:
    price = float(input("Inserisci il prezzo (-1 per terminare): "))
    if price == -1:
        break

    while True:
        pet_status = input("Si tratta di un animale? (Y/N): ").upper()
        if pet_status == 'Y' or pet_status == 'N':
            break
        else:
            print("Inserimento non valido. Per favore, scrivi 'Y' o 'N'.")

    prices.append(price)
    isPet.append(pet_status == 'Y')

nItems = len(prices)
sconto = discount(prices, nItems)
print(f"Lo sconto applicato è: €{sconto:.2f}")

print("\n--- Scontrino ---")
for i in range(nItems):
        item_type = "Animale" if isPet[i] else "Articolo"
        print(f"Item {i+1}: {item_type}, Prezzo: €{prices[i]:.2f}")
        print(f"\nTotale articoli: {nItems}")
        print("-----------------\n")

totale_finale = sum(prices) - sconto
print(f"Totale articoli: {nItems}")
print(f"Totale finale da pagare: €{totale_finale:.2f}")
print(f"Sconto applicato: €{sconto:.2f}")