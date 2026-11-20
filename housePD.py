def ladron_programacion_dinamica(botines):
    cantidad_casas = len(botines)
    if cantidad_casas == 0:
        return 0, [], []
    if cantidad_casas == 1:
        return botines[0], [botines[0]], [1]

    # ganancia_acumulada[i] = mejor ganancia posible considerando hasta la casa i
    ganancia_acumulada = [0] * cantidad_casas
    ganancia_acumulada[0] = botines[0]

    if botines[0] > botines[1]:
        ganancia_acumulada[1] = botines[0]
    else:
        ganancia_acumulada[1] = botines[1]

    una_casa_atras = 1
    dos_casas_atras = 2

    for indice in range(2, cantidad_casas):
        ganancia_si_robo = botines[indice] + ganancia_acumulada[indice - dos_casas_atras]
        ganancia_si_no_robo = ganancia_acumulada[indice - una_casa_atras]

        if ganancia_si_robo > ganancia_si_no_robo:
            ganancia_acumulada[indice] = ganancia_si_robo
        else:
            ganancia_acumulada[indice] = ganancia_si_no_robo

    # Reconstrucción de la ruta, recorriendo desde la última casa hacia atrás
    casas_robadas = []
    posicion = cantidad_casas - una_casa_atras

    while posicion >= 0:
        if posicion == 0:
            if botines[0] > 0:
                casas_robadas.append(1)
            posicion = -1
        elif ganancia_acumulada[posicion] == ganancia_acumulada[posicion - una_casa_atras]:
            posicion = posicion - una_casa_atras
        else:
            casas_robadas.append(posicion + una_casa_atras)
            posicion = posicion - dos_casas_atras

    casas_robadas.reverse()

    return ganancia_acumulada[cantidad_casas - una_casa_atras], ganancia_acumulada, casas_robadas


def main():
    print("=========================================")
    print("   OPTIMIZACION DE ROBO (DINAMICA)     ")
    print("=========================================")

    cantidad_casas = int(input("Ingrese la cantidad de casas (1 a 100): "))

    while cantidad_casas < 1 or cantidad_casas > 100:
        print("Error: La cantidad debe ser entre 1 y 100.")
        cantidad_casas = int(input("Ingrese de nuevo la cantidad de casas: "))

    botines = []

    for indice in range(cantidad_casas):
        botin = int(input(f"Dinero en la casa {indice + 1}: "))

        while botin <= 0:
            print("Error: El dinero debe ser mayor a cero.")
            botin = int(input(f"Ingrese de nuevo el dinero en la casa {indice + 1}: "))

        botines.append(botin)

    ganancia_maxima, ganancia_acumulada, casas_robadas = ladron_programacion_dinamica(botines)

    print("\n=== TABLA DE CALCULOS (PROGRAMACION DINAMICA) ===")
    print("Casa | Botin | Acumulado Maximo")
    print("-----|-------|-----------------")
    for indice in range(len(ganancia_acumulada)):
        print(f"  {indice + 1}  |  S/{botines[indice]:<3} |  S/{ganancia_acumulada[indice]}")

    print("\n=== VEREDICTO FINAL ===")
    print("Ruta de robo optima (Casas): ", end="")
    for indice in range(len(casas_robadas)):
        if indice < len(casas_robadas) - 1:
            print(f"{casas_robadas[indice]} -> ", end="")
        else:
            print(f"{casas_robadas[indice]}")

    print(f"GANANCIA MAXIMA ASEGURADA: S/{ganancia_maxima}")
    print("=========================================")


if __name__ == "__main__":
    main()