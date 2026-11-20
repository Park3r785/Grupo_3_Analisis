def ladron_programacion_dinamica(casas):
    n = len(casas)
    if n == 0:
        return 0, [], []
    if n == 1:
        return casas[0], [casas[0]], [1]

    tabla = [0] * n
    tabla[0] = casas[0]
    
    if casas[0] > casas[1]:
        tabla[1] = casas[0]
    else:
        tabla[1] = casas[1]

    paso_uno = 1
    paso_dos = 2

    for i in range(2, n):
        robar = casas[i] + tabla[i - paso_dos]
        no_robar = tabla[i - paso_uno]
        
        if robar > no_robar:
            tabla[i] = robar
        else:
            tabla[i] = no_robar

    elegidas = []
    pos = n - paso_uno
    
    while pos >= 0:
        if pos == 0:
            if casas[0] > 0:
                elegidas.append(1)
            pos = -1
        elif tabla[pos] == tabla[pos - paso_uno]:
            pos = pos - paso_uno
        else:
            elegidas.append(pos + paso_uno)
            pos = pos - paso_dos
            
    elegidas.reverse()

    return tabla[n - paso_uno], tabla, elegidas


print("=========================================")
print("   OPTIMIZACION DE ROBO (DINAMICA)     ")
print("=========================================")

n = int(input("Ingrese la cantidad de casas (1 a 100): "))

while n < 1 or n > 100:
    print("Error: La cantidad debe ser entre 1 y 100.")
    n = int(input("Ingrese de nuevo la cantidad de casas: "))

casas = []

for i in range(n):
    dinero = int(input(f"Dinero en la casa {i + 1}: "))
    
    while dinero <= 0:
        print("Error: El dinero debe ser mayor a cero.")
        dinero = int(input(f"Ingrese de nuevo el dinero en la casa {i + 1}: "))
        
    casas.append(dinero)

ganancia, tabla, elegidas = ladron_programacion_dinamica(casas)

print("\n=== TABLA DE CALCULOS (PROGRAMACION DINAMICA) ===")
print("Casa | Botin | Acumulado Maximo")
print("-----|-------|-----------------")
for i in range(len(tabla)):
    print(f"  {i + 1}  |  S/{casas[i]:<3} |  S/{tabla[i]}")

print("\n=== VEREDICTO FINAL ===")
print("Ruta de robo optima (Casas): ", end="")
for i in range(len(elegidas)):
    if i < len(elegidas) - 1:
        print(f"{elegidas[i]} -> ", end="")
    else:
        print(f"{elegidas[i]}")
        
print(f"GANANCIA MAXIMA ASEGURADA: S/{ganancia}")
print("=========================================")