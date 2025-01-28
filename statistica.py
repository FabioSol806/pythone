contenitore =[]
for voti in range(10):
    valutazione = input()
    contenitore.append(int(valutazione))
contenitore.remove(min(contenitore))
print(contenitore)
print(sum(contenitore)/len(contenitore))