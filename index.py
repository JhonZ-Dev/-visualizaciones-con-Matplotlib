import numpy as np
import matplotlib.pyplot as plt


# Generar datos aleatorios para un conjunto de experimentos

for i in range(num_experimentos):
    tendencia = 0.5 * i * tiempo  # Tendencia lineal creciente
    ruido = np.random.normal(0, 0.1, num_puntos)  # Ruido gaussiano
    datos_experimento = tendencia + ruido
    datos_experimentos.append(datos_experimento)
    # Visualizar los datos
plt.figure(figsize=(10, 6))
for i in range(num_experimentos):
    plt.plot(tiempo, datos_experimentos[i], label=f'Experimento {i + 1}')

plt.title('Datos de Experimentos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()