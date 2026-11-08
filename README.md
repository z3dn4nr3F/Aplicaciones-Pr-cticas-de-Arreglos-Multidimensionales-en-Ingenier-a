# Tarea: Arreglos Multidimensionales y Aplicaciones de Ingeniería

Este repositorio contiene las soluciones algorítmicas y prácticas para cinco problemas de ingeniería donde se implementan arreglos multidimensionales (matrices y tensores) para modelar y resolver situaciones reales del ámbito físico, matemático y de procesamiento de datos.

## Descripción de Soluciones y Enfoque de Eficiencia

### 1. Análisis de Fuerzas en una Estructura (Problema 1)
Enfoque:Se implementó una matriz bidimensional ($3 \times 3$) modelando las cargas aplicadas en puntos nodales discretos. Utilizando operaciones de reducción vectorial (`np.sum`), se calcula la carga total distribuida y se derivan las reacciones estáticas basándose en las leyes de equilibrio de la estática ($\sum F = 0$).
  Eficiencia:Al utilizar estructuras contiguas en memoria y funciones vectorizadas de bajo nivel, el cálculo de las fuerzas opera en tiempo constante $O(1)$ para dimensiones fijas o $O(N \times M)$ en general, optimizando los recursos de procesamiento.

### 2. Simulación de Fluido en una Cuadrícula 3D (Problema 2)
Enfoque:Se modeló el espacio tridimensional mediante un tensor de 4 dimensiones de tamaño $(3 \times 3 \times 3 \times 3)$, abarcando las coordenadas espaciales $(Z, Y, X)$ y las variables físicas (Presión, Temperatura y Velocidad). La propagación de ondas de presión se simuló aplicando un filtro espacial tipo *stencil* de 6 vecinos adyacentes.
Eficiencia:El uso de arreglos multidimensionales permite acceder a celdas vecinas de forma directa mediante indexación de slices, evitando bucles anidados lentos y permitiendo escalar eficientemente a simulaciones numéricas más grandes.

### 3. Análisis de Imágenes Médicas en 3D (Problema 3)
Enfoque:Se estructuró un volumen tridimensional de datos de imagen médica donde cada capa corresponde a una matriz $2D$. Se implementó un algoritmo de suavizado espacial con un núcleo de ventana deslizante para mitigar el ruido aleatorio preservando las características principales del órgano modelado.
* **Eficiencia:** El procesamiento por capas vectorizadas minimiza la sobrecarga de memoria y acelera la aplicación de filtros convolucionales básicos sobre grandes conjuntos de datos volumétricos.

### 4. Manejo de Datos en una Tabla de Sensores (Problema 4)
Enfoque:Se utilizó una matriz de $5 \times 5$ donde los ejes representan de forma ortogonal las dimensiones temporales (filas) y espaciales/sensores (columnas). Se calcularon métricas estadísticas descriptivas (media y desviación estándar) aplicando reducciones a lo largo de los ejes específicos (`axis=0` y `axis=1`).
* **Eficiencia:** Las operaciones orientadas a ejes de NumPy eliminan la necesidad de iteraciones explícitas en Python, logrando tiempos de ejecución sumamente eficientes $O(N \times M)$ mediante procesamiento en bloques de CPU optimizados en C.

### 5. Transformación de Coordenadas Cartesianas (Problema 5)
Enfoque:Se representó un conjunto de vértices espaciales en un arreglo bidimensional de forma $(N \times 2)$ y se aplicó una matriz de transformación lineal (rotación geométrica de $90^\circ$ basada en funciones trigonométricas) mediante producto matricial directo.
* **Eficiencia:** El uso de álgebra lineal computacional con multiplicación de matrices optimiza la transformación simultánea de múltiples coordenadas en una sola instrucción de hardware vectorial.
