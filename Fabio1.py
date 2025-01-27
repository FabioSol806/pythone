ALIQUOTA_23=0.23
ALIQUOTA_35=0.35
ALIQUOTA_43=0.43
reddito=input("inserisci in tuo reddito: ")
reddito1= int(reddito)
result = reddito1*ALIQUOTA_23 if reddito1 <= 28000 else (28000*ALIQUOTA_23) 
result1= int(result)
print(result)
result2= (reddito1-28000)*ALIQUOTA_35 if result1 <= 50000 else (50000-28000) * ALIQUOTA_35
result3= int(result2)
print(result2)
result4= (reddito1-50000)*ALIQUOTA_43 if result2 > 50000 else (reddito1-50000) * ALIQUOTA_43
result5= int(result4)
print(result4)
print(result+result2+result4)
