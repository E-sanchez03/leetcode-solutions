# 11. Container With Most Water

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/container-with-most-water/description/)
- **Dificultad:** Medium
- **Categorías:** `Array`, `Two Pointers`, `Greedy`

---

## 1. Enunciado del Problema

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

### Ejemplos

Example 1:

    **Input**: height = [1,8,6,2,5,4,8,3,7]
    **Output**: 49
    **Explanation**: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

    **Input**: height = [1,1]
    **Output**: 1

---

## 2. Análisis del Problema y Razonamiento

Usaremos la técnica de Two Pointers para resolverlo. Esta consiste en empezar en ambos extremos del array e ir recorriendolo tanto por el principio como por el final. Sabemos que el área será el ancho que hay entre los punteros por el puntero  más pequeño. Por tanto hay que maximizar ese valor. Iremos acortando el ancho moviendo los punteros, siempre siendo el más pequeño el que cambiará.

---

## 3. Mi Solución


```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1

        max_area = 0
        while left<right:
            wide = right-left
            area = min(height[left],height[right]) * wide
            max_area = max(max_area,area)
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return max_area
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Realizamos un bucle while solo. Las demás operaciones son de complejidad O(1)
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

- **Runtime:** `103 ms` (supera al `55.22%` de los envíos)
- **Memory:** `28.45 MB` (supera al `67.41%` de los envíos)


---



