# 128. Longest Consecutive Sequence

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)
- **Dificultad:** Medium
- **Categorías:** `Array`, `Hash Table`, `Union Find`

---

## 1. Enunciado del Problema

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

### Ejemplos

Example 1:

    **Input**: nums = [100,4,200,1,3,2]
    **Output**: 4
    **Explanation**: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

    **Input**: nums = [0,3,7,2,5,8,4,6,0,1]
    **Output*: 9

Example 3:

    **Input**: nums = [1,0,1,2]
    **Output**: 3

---

## 2. Análisis del Problema y Razonamiento

Usaremos una comprobación directa de si existe un número posterior a él para evitar cálculos repetidos. Cuando tengamos un número que no tiene siguiente inmediato comprobaremos cuantos inferiores tiene. La cuenta más grande será el resultado

---

## 3. Mi Solución

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        counts = 0
        for n in nums:
            if n+1 in nums:
                continue
            count =1
            c = n-1
            while c in nums:
                count+=1
                c-=1
            counts = max(counts,count)
        return counts
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** No es la solución óptima pédida.
- **Complejidad:** `$O(n log n)$`


---

## 5. Resultados en LeetCode

- **Runtime:** `43 ms` (supera al `90.22%` de los envíos)
- **Memory:** `34.08 MB` (supera al `71.89%` de los envíos)

---
