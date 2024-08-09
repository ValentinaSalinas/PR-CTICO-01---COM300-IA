CREAR BASE DE DATOS PESO Y ALTURA

1. **Importar la biblioteca "random"**

Se utiliza para generar numeros aleatorios para generar estaturas y pesos aleatorios dentro de ciertos rangos

2. **Defino la funcion "generar_datos(n)"**

Genera **n** ejemplos de estaturas y pesos. Inicializo las listas vacias que llenare con valores de estaturas y pesos generados aleatoriamente.

3. **Bucle "for" para generar los datos**

Este bucle se ejecutará **n** veces (100 en este caso), para generar 100 ejemplos de estatura y peso.

4. **Bucle "for" para generar los datos**

Este bucle se ejecutará **n** veces (100 en este caso), para generar 100 ejemplos de estatura y peso.

5. **Bucle "while True"**

Se repetira hasta que se genere una combinacion correcta con la condicion que indique

6. **Generar estatura aleatoria**

random.uniform(1.50, 2.05) genera un número aleatorio con decimales entre 1.50 y 2.05 (estatura en metros) y round lo redondea a dos decimales.

7. **Asignar Peso Según la Estatura**

Dependiendo de la estatura generada, se asigna un rango de pesos adecuado y lo redondea a un decimal.

8. **Condición para Asegurar Combinaciones Realistas**

No se permite que una estatura de 2.00 metros o más tenga un peso menor a 70 kg.
No se permite que una estatura de 1.60 metros o menos tenga un peso mayor a 100 kg. Si la combinación es válida, se sale del bucle. Luego los valores se aniadia a las listas y se devuelven las dos listas.

9. **Llamo a la funcion y muestro los primeros 10 ejemplos para verificar si esta todo bien hecho**


PARA HACER LA REGRESION LINEAL

1. Inicializo valores para los coeficientes
mejor_m = None:

Inicializa la variable que almacenara la pendiente m encontrada durante el proceso de busqueda. None significa nada o sin valor, o sea que la variable no ha sido asignada a un valor importante.

best_b = None:

Eventualmente almacenará el mejor intercepto b encontrado.

min_error = float('inf'):

Esta línea inicializa la variable min_error, que almacenará el menor error cuadrático medio (MSE) encontrado durante la búsqueda de la mejor combinación de m y b.

2. Inicializo valores para los coeficientes
mejor_m = None:

Inicializa la variable que almacenara la pendiente m encontrada durante el proceso de busqueda. None significa nada o sin valor, o sea que la variable no ha sido asignada a un valor importante. float('inf') representa un valor de punto flotante que es equivalente a "infinito" en matemáticas.

Cualquier error calculado en las primeras iteraciones será menor que infinito, lo que permite actualizar min_error con ese valor. A medida que se encuentran combinaciones mejores, min_error se va actualizando con valores menores y menores, hasta que se encuentre el mínimo posible.

3. Estructuras repetitivas para m y b
El bucle for explora diferentes valores de m, que representa la pendiente de la línea que estás ajustando a los datos. Genera una secuencia de números enteros desde -5000 hasta 5001. Esta estructura de bucles anidados asegura que se prueben todas las combinaciones posibles dentro del rango especificado, lo que permite encontrar la combinación de m y b que minimiza el error cuadrático medio (MSE) para el modelo.

4. Conversion de valores enteros de m y b a valores de punto flotante
Trabajar con valores de punto flotante es importante para mantener precisión en los cálculos matemáticos, especialmente en la regresión lineal, donde las operaciones con decimales son comunes.

Al convertir los valores enteros en valores de punto flotante con la escala deseada (0.1 pasos), explorando combinaciones más finas de m y b, lo que aumenta las posibilidades de encontrar la mejor combinación para ajustar los datos.

Esto permite que los valores de m y b sean lo suficientemente pequeños o grandes como para ajustarse mejor a los datos, en lugar de limitarse a valores enteros grandes que podrían no ser tan efectivos.

m_float = m / 10.0: Convierte el valor entero de m en un valor de punto flotante con una escala adecuada para los cálculos de regresión. b_float = b / 10.0: Convierte el valor entero de b en un valor de punto flotante con una escala adecuada para los cálculos de regresión.

5. Calcular Error cuadrativo medio (MSE)
Inicializo la variable error en 0. Esta variable se usará para acumular el error cuadrático total para la combinación actual de m_float y b_float.

El bucle for itera sobre todos los datos generados (en este caso, 100 ejemplos de estatura y peso).

prediccion_peso = m_float * estaturas[i] + b_float

calcula el peso predicho (prediccion_peso) para el i-ésimo dato usando la fórmula de la regresión lineal:

y = m * x + b

El resultado es el peso predicho para esa estatura particular según la combinación

error += (pesos[i] - prediccion_peso) ** 2

calcula el error cuadrático para el i-ésimo dato y lo suma al error total acumulado.

error cuadratico = (yi - y^i)^2

Al elevar al cuadrado la diferencia entre el peso real y el predicho, se asegura que los errores positivos y negativos no se cancelen entre sí, y se da más peso a los errores grandes.

El error cuadrático para cada par de datos se suma al total (error). Después de que el bucle for ha terminado, error contendrá la suma de los errores cuadráticos para todos los datos. Este valor se utilizará para determinar qué combinación de m_float y b_float produce el menor error, lo que indica que esa combinación es la que mejor se ajusta a los datos.

El MSE es una medida estándar en la regresión lineal y otros modelos de predicción porque penaliza fuertemente los errores grandes, asegurando que el modelo se ajuste lo mejor posible a la mayor parte de los datos.

6. Encontrar la mejor combinacion de pendiente e intercepto
if error < min_error: Esta línea verifica si el error calculado para la combinación actual de m_float y b_float es menor que el error mínimo (min_error) encontrado hasta ese punto.

error es la suma de los errores cuadráticos calculados en el bucle anterior

min_error es la mejor (es decir, más baja) suma de errores cuadráticos encontrada hasta ahora.

Si error es menor que min_error, significa que la combinación actual de m_float y b_float es mejor (en términos de ajuste a los datos) que cualquier combinación anterior. Si la condición anterior es verdadera esta línea actualiza min_error con el valor de error.

Cuando eso sucede, el código actualiza min_error, best_m, y best_b para reflejar que esta nueva combinación es la mejor encontrada hasta ahora.

7. Mostrar resultados y predicciones para los primeros 10 Ejemplos
Mostrar los Resultados: Las primeras líneas imprimen los valores óptimos de m y b encontrados durante la búsqueda, junto con el menor error cuadrático medio.

Predicciones para los Primeros 10 Ejemplos: El bucle for calcula y muestra cómo se comporta el modelo en los primeros 10 ejemplos del conjunto de datos, comparando los pesos reales con los pesos predichos por el modelo ajustado.

TIEMPO DE EJECUCION
1 hora 11 minutos y 32 segundos

El tiempo de ejecución de 1 hora y 11 minutos. La razón principal de este tiempo de ejecución tan largo es que el código está realizando una búsqueda exhaustiva sobre una gran cantidad de combinaciones de m y b para encontrar la mejor combinación que minimice el error cuadrático medio (MSE).

Explorando un rango muy amplio de valores para m y b (de -500.0 a 500.0 con pasos de 0.1), lo que resulta en 10,001 posibles valores para m y 10,001 posibles valores para b.

Esto significa que se evalúan 100,020,001 combinaciones diferentes de m y b, lo cual es computacionalmente costoso.
