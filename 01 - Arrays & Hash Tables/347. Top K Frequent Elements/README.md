# 347. Top K Frequent Elements

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
- **Dificultad:** Medium
- **Categorías:** `[Array`, `Hash Table`, `Divide and Conquer`, `Sorting`,`Heap`,`Bucket Sort`,`Counting`, `Quick Select`

---

## 1. Enunciado del Problema

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

### Ejemplos

Example 1:

    **Input**: nums = [1,1,1,2,2,3], k = 2
    **Output**: [1,2]

Example 2:

    **Input**: nums = [1], k = 1
    **Output**: [1]

---

## 2. Análisis del Problema y Razonamiento

En este problema podemos hacer uso de la librería collections y su clase Counter. Esta tiene un método llamada most_common con el que podemos trabajar. Esta devuelve para cada valor una lista con el valor y la cantidad de veces que aparece. Tendriamos que quedarnos solo con el valor del número.

---

## 3. Mi Solución

```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [x[0]for x in c.most_common(k)]
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** El contador tiene un tiempo O(n). Para calcular los más frecuentes se usa un sorting con complejidad U(log(k)) siendo U el tamaño del contador.
- **Complejidad:** `$O(N + Ulog(k))$`


---

## 5. Resultados en LeetCode

- **Runtime:** `3 ms` (supera al `91.10%` de los envíos)
- **Memory:** `21.38 MB` (supera al `40.34%` de los envíos)

---

