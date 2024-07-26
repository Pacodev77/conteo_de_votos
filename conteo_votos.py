
a = b = c = d = e = 0
i = 1

while i != 0:  
    i = int(input("Ingresa una opción 1, 2, 3, 4, 5, 0: "))

    if i == 1:
        a += 1
    elif i == 2:
        b += 1
    elif i == 3:
        c += 1
    elif i == 4:
        d += 1
    elif i == 5:
        e += 1

total_votos = a + b + c + d + e

if total_votos > 0:
    porcentaje_a = 100 * a / total_votos
    porcentaje_b = 100 * b / total_votos
    porcentaje_c = 100 * c / total_votos
    porcentaje_d = 100 * d / total_votos
    porcentaje_e = 100 * e / total_votos 
else:
    porcentaje_a = porcentaje_b = porcentaje_c = porcentaje_d = porcentaje_e = 0

print(f"Votaciones del candidato 1: {a} ({porcentaje_a:.2f}%)")
print(f"Votaciones del candidato 2: {b} ({porcentaje_b:.2f}%)")
print(f"Votaciones del candidato 3: {c} ({porcentaje_c:.2f}%)")
print(f"Votaciones del candidato 4: {d} ({porcentaje_d:.2f}%)")
print(f"Votaciones del candidato 4: {e} ({porcentaje_e:.2f}%)")