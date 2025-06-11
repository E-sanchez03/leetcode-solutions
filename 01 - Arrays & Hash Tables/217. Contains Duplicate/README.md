# 217. Contains Duplicate

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/contains-duplicate/)
- **Dificultad:** Easy
- **Categorías:** `Array`, `Hash Table`, `Sorting`

---

## 1. Enunciado del Problema

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Ejemplos

Example 1:

    **Input**: nums = [1,2,3,1]
    **Output**: true
    **Explanation**: The element 1 occurs at the indices 0 and 3.

Example 2:

    **Input**: nums = [1,2,3,4]
    **Output**: false
    **Explanation**: All elements are distinct.

Example 3:

    **Input**: nums = [1,1,1,3,3,4,3,2,4,2]
    **Output**: true
---

## 2. Análisis del Problema y Razonamiento

Solución trivial al convertir la lista de números en un conjunto. Los conjuntos no pueden contener duplicados, por tanto habría que comparar la longitud de ambos.

---

## 3. Mi Solución

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** Crear el conjunto y calcular su longitud son procesos de complejidad O(n).
- **Complejidad:** `$O(n)$`


---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `9 ms` (supera al `81.25%` de los envíos)
- **Memory:** `31.59 MB` (supera al `53.44%` de los envíos)

---



