import random

# Paso 1: Generar los datos de estatura y peso
def generar_datos(n):
    estaturas = []
    pesos = []

    for _ in range(n):
        while True:
            estatura = round(random.uniform(1.50, 2.05), 2)  # Genera estatura entre 1.50 y 2.05 metros
            if estatura < 1.60:
                peso = round(random.uniform(50, 70), 1)  # Peso entre 50 y 70 kg para estatura < 1.60
            elif estatura < 1.75:
                peso = round(random.uniform(55, 85), 1)  # Peso entre 55 y 85 kg para estatura < 1.75
            elif estatura < 1.90:
                peso = round(random.uniform(65, 100), 1)  # Peso entre 65 y 100 kg para estatura < 1.90
            else:
                peso = round(random.uniform(75, 120), 1)  # Peso entre 75 y 120 kg para estatura >= 1.90

            if not (estatura >= 2.00 and peso < 70) and not (estatura <= 1.60 and peso > 100):
                break

        estaturas.append(estatura)
        pesos.append(peso)

    return estaturas, pesos

# Paso 2: Inicializar valores para los coeficientes
best_m = None
best_b = None
min_error = float('inf')

# Generar los datos
n = 100
estaturas, pesos = generar_datos(n)

# Paso 3: Exploración más fina de `m` y `b`
for m in range(-1000, 1001):  # Pendiente variando de -100 a 100 con pasos de 0.1
    for b in range(-1000, 1001):  # Intercepto variando de -100 a 100 con pasos de 0.1
        m_float = m / 10.0
        b_float = b / 10.0

        # Paso 4: Calcular el error cuadrático medio
        error = 0
        for i in range(n):
            prediccion_peso = m_float * estaturas[i] + b_float
            error += (pesos[i] - prediccion_peso) ** 2

        # Si el error actual es menor que el mínimo, actualizar m, b y min_error
        if error < min_error:
            min_error = error
            best_m = m_float
            best_b = b_float

# Mostrar los resultados
print(f"La mejor pendiente (m): {best_m}")
print(f"El mejor intercepto (b): {best_b}")
print(f"Error mínimo: {min_error}")

# Mostrar los primeros 10 ejemplos generados
print("\nPrimeros 10 ejemplos generados:")

pesos_predichos = []
for i in range(10):
    prediccion_peso = best_m * estaturas[i] + best_b
    pesos_predichos.append(prediccion_peso)
    print(f"Estatura: {estaturas[i]} m, Peso real: {pesos[i]} kg, Peso predicho: {pesos_predichos[i]} kg")

import numpy as np
import matplotlib.pyplot as plt

# Crear un rango continuo de estaturas para graficar la recta
estaturas_rango = np.linspace(min(estaturas), max(estaturas), 100)

# Calcular los pesos predichos usando la mejor pendiente e intercepto para todo el rango de estaturas
pesos_predichos = [best_m * x + best_b for x in estaturas_rango]

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar los puntos de datos originales
plt.scatter(estaturas, pesos, color='blue', label='Datos Originales')

# Graficar la recta de regresión
plt.plot(estaturas_rango, pesos_predichos, color='red', label='Recta de Regresión')

# Configurar los títulos y las etiquetas de los ejes
plt.title('Regresión Lineal: Estatura vs Peso')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()

# Convertir las listas a arrays de numpy para facilitar el manejo matemático
estaturas_np = np.array(estaturas)
pesos_np = np.array(pesos)

# Ajustar un modelo polinómico de grado 2 (parábola)
coeficientes = np.polyfit(estaturas_np, pesos_np, 2)
polinomio = np.poly1d(coeficientes)

# Crear un rango de estaturas para graficar la curva
estaturas_rango = np.linspace(min(estaturas), max(estaturas), 100)

# Calcular los pesos predichos usando el modelo polinómico
pesos_predichos = polinomio(estaturas_rango)

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar los puntos de datos originales
plt.scatter(estaturas, pesos, color='blue', label='Datos Originales')

# Graficar la curva polinómica
plt.plot(estaturas_rango, pesos_predichos, color='red', label='Curva de Regresión Polinómica')

# Configurar los títulos y las etiquetas de los ejes
plt.title('Regresión Polinómica: Estatura vs Peso')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
