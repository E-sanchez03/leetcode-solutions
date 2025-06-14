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

Implemento el algoritmo de divide y vencerás para resolver el problema. Comprueba si existe para cierto n el número anterior n-1. Cada vez que existe un elemento más se suma uno a la cuenta. Luego se escoge la cuenta más grande

---

## 3. Mi Solución

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        counts = []
        def check(n):
            suma = 1
            if n in nums:
                suma += check(n-1)
            return suma
        for n in nums:
            if n+1 in nums:
                continue
            count = check(n-1)
            counts.append(count)
        
        return max(counts)
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** No es la solución óptima pédida.
- **Complejidad:** `$O(n log n)$`


---

## 5. Resultados en LeetCode

- **Runtime:** `64 ms` (supera al `29.11%` de los envíos)
- **Memory:** `65.35 MB` (supera al `5.00%` de los envíos)

---
