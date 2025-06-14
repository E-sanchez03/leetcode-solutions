# 238. Product of Array Except Self

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/product-of-array-except-self/description/)
- **Dificultad:** Medium
- **Categorías:** `Array`, `Prefix Sum`

---

## 1. Enunciado del Problema

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

### Ejemplos

Example 1:

    **Input**: nums = [1,2,3,4]
    **Output**: [24,12,8,6]

Example 2:

    **Input**: nums = [-1,1,0,-3,3]
    **Output**: [0,0,9,0,0]

---

## 2. Análisis del Problema y Razonamiento

Vamos a hacer uso de Prefix and Suffix Product. 
Prefix product se puede definir como "In a prefix product array, ith term pref[i] = arr[i] * arr[i - 1] * ...... * arr[0] "
Suffix product se pude definir como "each element at index i contains the product of all elements to the right of i".

La idea es combinar ambos para excluir el elemento del índice. Por ejemplo para el índice 3, usaremos el término 4 en el array de sufijo junto con el término 2 de prefijo, de esta manera obtendremos el producto de todos sin contar el del índice 3.


---

## 3. Mi Solución

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = [nums[0]] * n
        suf_prod = [1] * n
        
        for i in range(n-2,-1,-1):
            suf_prod[i] = suf_prod[i+1]*nums[i+1]
        
        for i in range(1, n):
            pre_prod[i] = nums[i] * pre_prod[i-1]
            suf_prod[i] *= nums[i]
        output = [1]*n
        output[0] = suf_prod[1]
        for i in range(1,n-1):
            output[i] = suf_prod[i+1] * pre_prod[i-1]
        output[-1] = pre_prod[-2]
        return output
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** Se realizan tres bucles secuenciales, por tanto el tiempo es lineal
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `41 ms` (supera al `13.64%` de los envíos)
- **Memory:** `27.04 MB` (supera al `11.69%` de los envíos)

---
