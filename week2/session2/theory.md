# Distancia entre píxeles

## ¿Para qué sirve?

Cuando representamos imágenes en escala de grises o en color, cada píxel tiene una posición (coordenadas) y un valor de intensidad (o vector RGB).

Medir la "distancia" entre píxeles puede servir para:
- **Segmentación** (decidir si dos píxeles pertenecen al mismo objeto).
- **Filtros** (cuánto influye un píxel vecino).
- **Reconocimiento de patrones** (comparar patches o regiones de la imagen).
- **Clustering/KNN** (clasificar basándose en similitudes de intensidades o colores).

## Fórmula general de las métricas Lp

Todas son casos de la distancia de Minkowski:

$$
D(x,y) = \left( \sum_{i=1}^n |x_i - y_i|^p \right)^{1/p}
$$

donde:
- $x$ y $y$ son dos puntos (o píxeles, o vectores).
- $p$ determina el tipo de norma/distancia.

## Casos específicos

### Euclidiana ($p=2$)

$$
D(x,y) = \sqrt{ \sum_i (x_i - y_i)^2 }
$$

La distancia "geométrica normal", como con una regla.

### Manhattan ($p=1$)

$$
D(x,y) = \sum_i |x_i - y_i|
$$

Como caminar en calles de una cuadrícula (por eso también "distancia taxicab").

### Chebyshev ($p \to \infty$)

$$
D(x,y) = \max_i |x_i - y_i|
$$

Solo importa la diferencia máxima en una dimensión.  
En píxeles, equivale a decir: "la distancia es el mayor salto entre coordenadas".

**Ejemplo en 2D:**  
Entre $(1,1)$ y $(4,5)$:
- Euclidiana: $\sqrt{3^2+4^2}=5$
- Manhattan: $3+4=7$
- Chebyshev: $\max(3,4)=4$

En imágenes digitales, la distancia Chebyshev mide el número mínimo de movimientos de "rey" en ajedrez para ir de un píxel a otro.

## ¿Cuál usar?

- **Euclidiana** → cuando quieres la distancia real en el plano (bordes suaves, clustering).
- **Manhattan** → cuando importa la suma de diferencias (ej. redes en cuadrícula, movimiento 4-direcciones).
- **Chebyshev** → cuando lo relevante es la máxima diferencia (ej. movimiento 8-direcciones en píxeles, morfología matemática).

**Ejemplo práctico:** en procesamiento morfológico, si usas Chebyshev defines una vecindad cuadrada (8 vecinos). Si usas Manhattan defines vecindad en cruz (4 vecinos).
