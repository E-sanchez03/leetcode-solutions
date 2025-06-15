# 3. Longest Substring Without Repeating Characters

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
- **Dificultad:** Medium
- **Categorías:** `Hash Table`, `String`, `Sliding Window`

---

## 1. Enunciado del Problema

Given a string s, find the length of the longest substring without duplicate characters.


### Ejemplos

Example 1:

    **Input**: s = "abcabcbb"
    **Output**: 3
    **Explanation**: The answer is "abc", with the length of 3.

Example 2:

    **Input**: s = "bbbbb"
    **Output**: 1
    **Explanation**: The answer is "b", with the length of 1.

Example 3:

    **Input**: s = "pwwkew"
    **Output**: 3
    **Explanation**: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

## 2. Análisis del Problema y Razonamiento

Para encontrar la solución recorreremos todo el array una sola vez creando una substring. Cuando vayamos a añadir un elemento que ya está iremos moviendo la ventana hasta eliminar ese elemento. Cada vez que añadimos un nuevo elemento comprobamos si el tamaño es mayor que antes o no.

---

## 3. Mi Solución


```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        first_letter = s[0]
        sub = s[0]
        output = 1
        for i in s[1:]:
            if i in sub:
                sub = sub[sub.index(i)+1:]
            sub += i
            output = max(output, len(sub))

        return output
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Recorremos la lista una sola vez. Sin embargo, en el peor de los casos encontrar el índice puede ser de complejidad O(n). 
- **Complejidad:** `$O(n^2)$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `19 ms` (supera al `56.09%` de los envíos)
- **Memory:** `18.00 MB` (supera al `34.23%` de los envíos)


---


