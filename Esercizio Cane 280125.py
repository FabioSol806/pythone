def discount(prices, isPet, nItems):
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

prices = [] lista
isPet = [] lista 

while True:
    price = float(input("Inserisci il prezzo (-1 per terminare): "))
    if price == -1:
        confronto con -1
        break
    pet_status = input("Si tratta di un animale? (Y/N): ")
    prices.append(price)
    isPet.append(pet_status.upper() == 'Y')
    Controllo lettera

nItems = len(prices)
sconto = discount(prices, isPet, nItems)
riporto della funzione 
print(f"Lo sconto applicato è: €{sconto:.2f}")