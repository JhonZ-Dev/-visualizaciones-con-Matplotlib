import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios para un conjunto de experimentos
np.random.seed(42)
# Número de experimentos
num_experimentos = 5
# Número de puntos de datos por experimento
num_puntos = 100
# Crear datos de tiempo (en segundos)
tiempo = np.linspace(0, 1, num_puntos)
# Crear datos de experimentos con diferentes tendencias y ruido
datos_experimentos = []
for i in range(num_experimentos):
    tendencia = 0.5 * i * tiempo  # Tendencia lineal creciente
    ruido = np.random.normal(0, 0.1, num_puntos)  # Ruido gaussiano
    datos_experimento = tendencia + ruido
    datos_experimentos.append(datos_experimento)