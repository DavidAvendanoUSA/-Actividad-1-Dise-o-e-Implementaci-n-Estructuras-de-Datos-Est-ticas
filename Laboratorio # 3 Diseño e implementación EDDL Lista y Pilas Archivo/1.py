import random


corral1 = []  
corral2 = []  
corral3 = []  


for i in range(60):
    peso = random.randint(250, 600)
    corral1.append(peso)


total1 = len(corral1)
prom1 = sum(corral1) / total1 if total1 > 0 else 0
print(f"Corral #1 (antes): {total1} novillos, peso promedio = {prom1:.2f} kg")


i = 0
while i < len(corral1):
    peso = corral1[i]
    if 280 <= peso <= 400:
        corral2.append(peso)  
        corral1.pop(i)        
    elif 401 <= peso <= 500:
        corral3.append(peso)  
        corral1.pop(i)      
    else:
        i += 1  


total2 = len(corral2)
prom2 = sum(corral2) / total2 if total2 > 0 else 0
total3 = len(corral3)
prom3 = sum(corral3) / total3 if total3 > 0 else 0

print(f"Corral #2: {total2} novillos, peso promedio = {prom2:.2f} kg")
print(f"Corral #3: {total3} novillos, peso promedio = {prom3:.2f} kg")


camiones2 = []
camion = []
while corral2:
    peso = corral2.pop()  
    camion.append(peso)    
    if len(camion) == 10:
        camiones2.append(camion)
        camion = []
if camion:
    camiones2.append(camion)


camiones3 = []
camion = []
while corral3:
    peso = corral3.pop()  
    camion.append(peso)  
    if len(camion) == 10:
        camiones3.append(camion)
        camion = []
if camion:
    camiones3.append(camion)


print(f"Camiones requeridos Corral #2: {len(camiones2)}")
print(f"Camiones requeridos Corral #3: {len(camiones3)}")


total1_final = len(corral1)
prom1_final = sum(corral1) / total1_final if total1_final > 0 else 0
print(f"Corral #1 (final): {total1_final} novillos, peso promedio = {prom1_final:.2f} kg")