Algoritmo LadronCasas_FuerzaBruta
	Definir n, i, mascara, totalCombinaciones, temp, suma, mejorSuma, validas Como Entero
	Definir valida Como Logico
	Definir casas, seleccion, mejorSeleccion Como Entero
	Dimension casas[20], seleccion[20], mejorSeleccion[20]
	
	// Lectura de cantidad de casas (1 a 20)
	Repetir
		Escribir "Ingrese la cantidad de casas (1 a 20):"
		Leer n
		Si n < 1 O n > 20 Entonces
			Escribir "Error: La cantidad de casas debe estar entre 1 y 20."
		FinSi
	Hasta Que n >= 1 Y n <= 20
	
	// Lectura del dinero por casa (solo valores mayores a 0)
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Repetir
			Escribir "Dinero en la casa ", i, " (mayor a 0):"
			Leer casas[i]
			Si casas[i] <= 0 Entonces
				Escribir "Error: El monto debe ser mayor a 0."
			FinSi
		Hasta Que casas[i] > 0
	FinPara
	
	// Calcular 2^n = total de combinaciones posibles
	totalCombinaciones <- 1
	Para i <- 1 Hasta n Con Paso 1 Hacer
		totalCombinaciones <- totalCombinaciones * 2
	FinPara
	
	mejorSuma <- 0
	validas <- 0
	Para i <- 1 Hasta n Con Paso 1 Hacer
		mejorSeleccion[i] <- 0
	FinPara
	
	// Probar TODAS las combinaciones
	Para mascara <- 0 Hasta totalCombinaciones - 1 Con Paso 1 Hacer
		
		// Convertir la mascara a binario: 1 = robar, 0 = no robar
		temp <- mascara
		Para i <- 1 Hasta n Con Paso 1 Hacer
			seleccion[i] <- temp MOD 2
			temp <- trunc(temp / 2)
		FinPara
		
		// Verificar que no haya dos casas vecinas robadas
		valida <- Verdadero
		Para i <- 2 Hasta n Con Paso 1 Hacer
			Si seleccion[i] = 1 Y seleccion[i-1] = 1 Entonces
				valida <- Falso
			FinSi
		FinPara
		
		// Si la combinacion es valida, calcular su suma
		Si valida Entonces
			validas <- validas + 1
			suma <- 0
			Para i <- 1 Hasta n Con Paso 1 Hacer
				Si seleccion[i] = 1 Entonces
					suma <- suma + casas[i]
				FinSi
			FinPara
			
			// Guardar la mejor combinacion encontrada
			Si suma > mejorSuma Entonces
				mejorSuma <- suma
				Para i <- 1 Hasta n Con Paso 1 Hacer
					mejorSeleccion[i] <- seleccion[i]
				FinPara
			FinSi
		FinSi
	FinPara
	
	// Mostrar resultados
	Escribir ""
	Escribir "===== RESULTADO (FUERZA BRUTA) ====="
	Escribir "Combinaciones evaluadas: ", totalCombinaciones
	Escribir "Combinaciones validas: ", validas
	Escribir Sin Saltar "Casas robadas: "
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Si mejorSeleccion[i] = 1 Entonces
			Escribir Sin Saltar i, " "
		FinSi
	FinPara
	Escribir ""
	Escribir "Ganancia maxima: S/ ", mejorSuma
FinAlgoritmo
