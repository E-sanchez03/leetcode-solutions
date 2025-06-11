# 9. Palindrome Number

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/palindrome-number/)
- **Dificultad:** Easy
- **Categorías:** `Math`

---

## 1. Enunciado del Problema

Given an integer x, return true if x is a palindrome, and false otherwise.

### Ejemplos

Example 1:

    **Input**: x = 121
    **Output**: true
    **Explanation**: 121 reads as 121 from left to right and from right to left.

Example 2:

    **Input**: x = -121
    **Output**: false
    **Explanation**: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

    **Input**: x = 10
    **Output**: false
    **Explanation**: Reads 01 from right to left. Therefore it is not a palindrome.
---

## 2. Análisis del Problema y Razonamiento

La dificultad de este problema erradica en que es de tipo Math y no de tipo String. La solución tratando subcadenas es trivial, solo hay que revertir la cadena y comprobar ambas. Esta es la solución que hay ahora.

Este problema quedará en pendiente hasta hacerlo de manera matemática

---

## 3. Mi Solución

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```

---

## 4. Análisis de Complejidad

Esta sección es crucial para demostrar tu entendimiento.

### Complejidad Temporal (Time Complexity)
- **Análisis:** Recorrer una cadena una vez para revertirla
- **Complejidad:** `$O(n)$`


---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `3 ms` (supera al `88.42%` de los envíos)
- **Memory:** `17.68 MB` (supera al `88.83%` de los envíos)

---

