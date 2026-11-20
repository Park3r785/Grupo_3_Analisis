Algoritmo RoboCasas_Dinamico
	Definir cantidad, k, gano, noGano, totalCasas Como Entero
	Definir botin, registro, rastro Como Entero
	Dimension botin[100], registro[100], rastro[100]
	
	Escribir "========================================="
	Escribir "   OPTIMIZACION DE ROBO (DINAMICA)     "
	Escribir "========================================="
	
	Repetir
		Escribir "¿Cuantas casas hay en la calle? (1 a 100):"
		Leer cantidad
	Hasta Que cantidad >= 1 Y cantidad <= 100
	
	Para k <- 1 Hasta cantidad Con Paso 1 Hacer
		Escribir "¿Cuanto dinero hay en la casa ", k, "?:"
		Leer botin[k]
		
		Mientras botin[k] <= 0 Hacer
			Escribir "Error: El dinero debe ser mayor a cero."
			Escribir "Ingrese de nuevo el dinero de la casa ", k, ":"
			Leer botin[k]
		FinMientras
	FinPara
	
	registro[1] <- botin[1]
	Si cantidad >= 2 Entonces
		Si botin[1] > botin[2] Entonces
			registro[2] <- botin[1]
		SiNo
			registro[2] <- botin[2]
		FinSi
	FinSi
	
	Para k <- 3 Hasta cantidad Con Paso 1 Hacer
		gano <- botin[k] + registro[k-2]
		noGano <- registro[k-1]
		Si gano > noGano Entonces
			registro[k] <- gano
		SiNo
			registro[k] <- noGano
		FinSi
	FinPara
	
	totalCasas <- 0
	k <- cantidad
	
	Mientras k >= 1 Hacer
		Si k = 1 Entonces
			Si botin[1] > 0 Entonces
				totalCasas <- totalCasas + 1
				rastro[totalCasas] <- 1
			FinSi
			k <- 0
		SiNo
			Si registro[k] = registro[k-1] Entonces
				k <- k - 1
			SiNo
				totalCasas <- totalCasas + 1
				rastro[totalCasas] <- k
				k <- k - 2
			FinSi
		FinSi
	FinMientras
	
	Escribir ""
	Escribir "=== TABLA DE CALCULOS (PROGRAMACION DINAMICA) ==="
	Escribir "Casa | Botin | Acumulado Maximo"
	Escribir "-----|-------|-----------------"
	Para k <- 1 Hasta cantidad Con Paso 1 Hacer
		Escribir "  ", k, "  |  S/", botin[k], "  |  S/", registro[k]
	FinPara
	
	Escribir ""
	Escribir "=== VEREDICTO FINAL ==="
	Escribir Sin Saltar "Ruta de robo optima (Casas): "
	Para k <- totalCasas Hasta 1 Con Paso -1 Hacer
		Si k > 1 Entonces
			Escribir Sin Saltar rastro[k], " -> "
		SiNo
			Escribir Sin Saltar rastro[k]
		FinSi
	FinPara
	
	Escribir ""
	Escribir "GANANCIA MAXIMA ASEGURADA: S/", registro[cantidad]
	Escribir "========================================="
	
FinAlgoritmo