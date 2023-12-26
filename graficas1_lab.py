import numpy as np

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

import matplotlib.pyplot as plt

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)

# Crear gráfico de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(matematicas, ciencias, color='blue', alpha=0.7)
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.grid(True)
plt.tight_layout()
plt.show()

#import matplotlib.pyplot as plt

# Datos de calificaciones de los estudiantes
# (¡Asegúrate de haber generado estos datos previamente!)
# matematicas, ciencias, literatura = ...

# Datos de errores para el gráfico de barras de error
errores_matematicas = [1.5, 3.5]  # Sustituye con los datos reales
errores_ciencias = [1.2, 3.8]  # Sustituye con los datos reales
errores_literatura = [2.7, 5.2]  # Sustituye con los datos reales

# Calcular calificaciones promedio
promedio_matematicas = np.mean(matematicas)
promedio_ciencias = np.mean(ciencias)
promedio_literatura = np.mean(literatura)

# Etiquetas para las materias
materias = ['Matemáticas', 'Ciencias', 'Literatura']

# Valores de calificaciones promedio
calificaciones_promedio = [promedio_matematicas, promedio_ciencias, promedio_literatura]

# Valores de errores para las barras de error
errores = [errores_matematicas, errores_ciencias, errores_literatura]

# Crear gráfico de barras de error
plt.figure(figsize=(8, 6))

plt.bar(materias, calificaciones_promedio, yerr=errores, capsize=7, color='skyblue', alpha=0.7)

plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')
plt.title('Calificaciones Promedio y Errores por Materia')
plt.legend(['Calificaciones Promedio'])

plt.tight_layout()
plt.show()


#import matplotlib.pyplot as plt

# Datos de calificaciones de matemáticas (asegúrate de tener estos datos)
# matematicas = ...

# Crear histograma de calificaciones de matemáticas
plt.figure(figsize=(8, 6))

plt.hist(matematicas, bins=10, edgecolor='black', alpha=0.7)

plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones de Matemáticas')

plt.tight_layout()
plt.show()
