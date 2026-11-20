def ladron_fuerza_bruta(casas):
    n = len(casas)
    mejor_suma = 0
    mejor_seleccion = []
    combinaciones_validas = 0
    total_combinaciones = 2 ** n

    for mascara in range(total_combinaciones):
        # Convertir la máscara a binario: 1 = robar, 0 = no robar
        seleccion = []
        temp = mascara
        for i in range(n):
            seleccion.append(temp % 2)
            temp = temp // 2

        # Verificar que no haya dos casas vecinas robadas
        valida = True
        for i in range(1, n):
            if seleccion[i] == 1 and seleccion[i - 1] == 1:
                valida = False
                break

        # Si es válida, calcular su suma y compararla con la mejor
        if valida:
            combinaciones_validas += 1
            suma = 0
            for i in range(n):
                if seleccion[i] == 1:
                    suma += casas[i]
            if suma > mejor_suma:
                mejor_suma = suma
                mejor_seleccion = [i + 1 for i in range(n) if seleccion[i] == 1]

    return mejor_suma, mejor_seleccion, total_combinaciones, combinaciones_validas


# ---------------- PROGRAMA PRINCIPAL ----------------
while True:
    n = int(input("Ingrese la cantidad de casas (1 a 20): "))
    if 1 <= n <= 20:
        break
    print("Error: La cantidad de casas debe estar entre 1 y 20.")

casas = []
for i in range(n):
    while True:
        monto = int(input(f"Dinero en la casa {i + 1} (mayor a 0): "))
        if monto > 0:
            casas.append(monto)
            break
        print("Error: El monto debe ser mayor a 0.")

suma, seleccion, total, validas = ladron_fuerza_bruta(casas)

print("\n===== RESULTADO (FUERZA BRUTA) =====")
print(f"Combinaciones evaluadas: {total}")
print(f"Combinaciones válidas: {validas}")
print(f"Casas robadas: {seleccion}")
print(f"Ganancia máxima: S/ {suma}")