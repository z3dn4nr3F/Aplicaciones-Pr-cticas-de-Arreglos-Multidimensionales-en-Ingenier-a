"""
Título: Resolución de Problemas de Ingeniería con Arreglos Multidimensionales
Autor: Estudiante de Ingeniería / Sistemas
Descripción: Implementación en Python de los 5 problemas prácticos solicitados,
utilizando matrices y tensores con NumPy, optimizado y libre de errores de linter.
"""

import numpy as np


# ==============================================================
# PROBLEMA 1: Análisis de Fuerzas en una Estructura (Matriz 3x3)
# ==============================================================
def problema_1_analisis_fuerzas():
    """
    Representa una estructura de nodos de 3x3 donde cada celda contiene
    la fuerza aplicada (en Newtons). Calcula las reacciones estáticas globales
    asumiendo equilibrio de fuerzas (Sumatoria de F_x = 0, Sumatoria de F_y = 0).
    """
    print("=" * 60)
    print("PROBLEMA 1: Análisis de Fuerzas en una Estructura (3x3)")
    print("=" * 60)

    # Matriz 3x3 que representa las fuerzas aplicadas en cada nodo
    matriz_fuerzas = np.array(
        [[120.5, 85.0, 95.2], [200.0, 150.4, 180.1], [90.3, 110.0, 75.6]]
    )

    print("Matriz de Fuerzas Aplicadas (N):\n", matriz_fuerzas)

    # Cálculo de estática: Reacciones en soportes basadas en equilibrio global
    fuerza_total = np.sum(matriz_fuerzas)
    reaccion_soporte_izq = fuerza_total / 2.0
    reaccion_soporte_der = fuerza_total / 2.0

    print(f"\n[Estatística] Fuerza total aplicada en la estructura: {fuerza_total:.2f} N")
    print(f"Reacción calculada en el Nodo de Soporte Izquierdo: {reaccion_soporte_izq:.2f} N")
    print(f"Reacción calculada en el Nodo de Soporte Derecho: {reaccion_soporte_der:.2f} N\n")


# =============================================================
# PROBLEMA 2: Simulación de Fluido en una Cuadrícula 3D (3x3x3)
# =============================================================
def problema_2_simulacion_fluido():
    """
    Utiliza un arreglo tridimensional (3x3x3) para modelar un volumen de fluido.
    Cada celda almacena tres propiedades físicas: [Presión, Temperatura, Velocidad].
    Simula la propagación de ondas de presión actualizando los valores con el promedio de vecinos.
    """
    print("=" * 60)
    print("PROBLEMA 2: Simulación de Fluido en una Cuadrícula 3D (3x3x3)")
    print("=" * 60)

    # Dimensiones: Z, Y, X, Propiedades (Presión, Temperatura, Velocidad)
    volumen_fluido = np.zeros((3, 3, 3, 3))
    volumen_fluido[:, :, :, 0] = 101.3  # Presión atmosférica base
    volumen_fluido[:, :, :, 1] = 298.15  # Temperatura en Kelvin
    volumen_fluido[:, :, :, 2] = 0.0    # Velocidad inicial

    # Perturbación de onda de presión en el nodo central (1, 1, 1)
    volumen_fluido[1, 1, 1, 0] = 150.0
    print("Estado inicial de presión en el centro (capa 1, fila 1, col 1):", volumen_fluido[1, 1, 1, 0])

    # Simulación de propagación por difusión con vecinos directos
    volumen_actualizado = volumen_fluido.copy()

    for z in range(1, 2):
        for y in range(1, 2):
            for x in range(1, 2):
                vecinos_presion = [
                    volumen_fluido[z+1, y, x, 0], volumen_fluido[z-1, y, x, 0],
                    volumen_fluido[z, y+1, x, 0], volumen_fluido[z, y-1, x, 0],
                    volumen_fluido[z, y, x+1, 0], volumen_fluido[z, y, x-1, 0]
                ]
                volumen_actualizado[z, y, x, 0] = np.mean(vecinos_presion)

    print(f"Presión propagada en el nodo central tras 1 ciclo: {volumen_actualizado[1, 1, 1, 0]:.2f} kPa\n")


# ====================================================================
# PROBLEMA 3: Análisis de Imágenes Médicas en 3D (Volumen y Suavizado)
# ====================================================================
def problema_3_imagenes_medicas():
    """
    Representa un volumen médico 3D (ej. tomografía de 3 capas de 4x4 píxeles).
    Aplica un filtro espacial de promedio (suavizado) capa por capa para reducir ruido.
    """
    print("=" * 60)
    print("PROBLEMA 3: Análisis de Imágenes Médicas en 3D")
    print("=" * 60)

    np.random.seed(42)
    volumen_medico = np.random.randint(50, 200, size=(3, 4, 4)).astype(float)

    print("Capa 0 original (con ruido de ejemplo):\n", volumen_medico[0])

    # Aplicar filtro de suavizado (promedio móvil 2D en cada capa)
    volumen_suavizado = np.zeros_like(volumen_medico)
    profundidad, alto, ancho = volumen_medico.shape

    for c in range(profundidad):
        capa = volumen_medico[c]
        capa_suave = capa.copy()
        for i in range(1, alto - 1):
            for j in range(1, ancho - 1):
                vecindario = capa[i-1:i+2, j-1:j+2]
                capa_suave[i, j] = np.mean(vecindario)
        volumen_suavizado[c] = capa_suave

    print("\nCapa 0 después del algoritmo de suavizado (reducción de ruido):\n", volumen_suavizado[0])
    print("\n[Éxito] Filtrado 3D completado correctamente.\n")


# ==========================================================
# PROBLEMA 4: Manejo de Datos en una Tabla de Sensores (5x5)
# ==========================================================
def problema_4_tabla_sensores():
    """
    Organiza datos de temperatura de 5 sensores en 5 momentos en el tiempo (matriz 5x5).
    Calcula la media y desviación estándar por sensor (columnas) y por momento temporal (filas).
    """
    print("=" * 60)
    print("PROBLEMA 4: Manejo de Datos en una Tabla de Sensores (5x5)")
    print("=" * 60)

    np.random.seed(100)
    datos_sensores = np.round(np.random.uniform(20.0, 35.0, size=(5, 5)), 2)

    print("Matriz de Sensores [Momentos x Sensores] (°C):\n", datos_sensores)

    # Análisis estadístico por columnas (Sensores) y filas (Momentos)
    medias_sensores = np.mean(datos_sensores, axis=0)
    desv_sensores = np.std(datos_sensores, axis=0)

    medias_tiempos = np.mean(datos_sensores, axis=1)
    desv_tiempos = np.std(datos_sensores, axis=1)

    print("\n--- Análisis por Sensor (Columnas) ---")
    for idx, (m, d) in enumerate(zip(medias_sensores, desv_sensores), start=1):
        print(f"Sensor S{idx} -> Media: {m:.2f} °C | Desviación Estándar: {d:.2f}")

    print("\n--- Análisis por Momento en el Tiempo (Filas) ---")
    print(f"Medias temporales: {np.round(medias_tiempos, 2)}")
    print(f"Desviaciones temporales: {np.round(desv_tiempos, 2)}\n")


# ==================================================================
# PROBLEMA 5: Transformación de Coordenadas en un Sistema Cartesiano
# ==================================================================
def problema_5_transformacion_coordenadas():
    """
    Representa un conjunto de puntos cartesianos en un arreglo 2D (N x 2)
    y aplica una transformación lineal (Rotación) mediante una matriz de transformación.
    """
    print("=" * 60)
    print("PROBLEMA 5: Transformación de Coordenadas en Sistema Cartesiano")
    print("=" * 60)

    puntos = np.array([
        [1.0, 1.0],
        [3.0, 1.0],
        [3.0, 3.0],
        [1.0, 3.0]
    ])
    print("Puntos originales (Cuadrado):\n", puntos)

    # Matriz de rotación de 90 grados en radianes
    angulo = np.pi / 2
    cos_t, sin_t = np.cos(angulo), np.sin(angulo)
    matriz_rotacion = np.array([
        [cos_t, -sin_t],
        [sin_t,  cos_t]
    ])

    # Aplicar transformación lineal
    puntos_transformados = np.dot(puntos, matriz_rotacion.T)
    print("\nPuntos después de Rotación de 90°:\n", np.round(puntos_transformados, 3))
    print("\n[Éxito] Transformación geométrica completada.\n")


# ===================
# EJECUCIÓN PRINCIPAL
# ===================
if __name__ == "__main__":
    print("\nINICIANDO EJECUCIÓN DE TAREAS - ARREGLOS MULTIDIMENSIONALES\n")
    problema_1_analisis_fuerzas()
    problema_2_simulacion_fluido()
    problema_3_imagenes_medicas()
    problema_4_tabla_sensores()
    problema_5_transformacion_coordenadas()
    print("¡Todas las simulaciones y análisis finalizaron exitosamente!")
    
    
