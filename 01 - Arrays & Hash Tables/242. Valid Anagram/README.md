# 242. Valid Anagram

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/valid-anagram/description/)
- **Dificultad:** Easy
- **Categorías:** `Hash Table`, `String`, `Sorting`

---

## 1. Enunciado del Problema

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

### Ejemplos

Example 1:

    **Input**: s = "anagram", t = "nagaram"
    **Output**: true

Example 2:

    **Input**: s = "rat", t = "car"
    **Output**: false
---

## 2. Análisis del Problema y Razonamiento

La primera idea que podríamos tener sería transformar las cadenas en conjuntos y ver si son iguales. SIn embargo, en casos como s='aa' y t='a'. Podríamos pensar que podemos comprobar primero la longitud de las cadenas y devolver falso directamente si no son iguales. Aún así, seguirá fallando para casos como s='aaca' t='ccac'. 

Por tanto, vamos a hacer uso de la librería collections y de su clase Counter(). Esta nos permite contar cada caracter de una string.

---

## 3. Mi Solución

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c = Counter(s)
        z = Counter(t)
        return c==z
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** Se realiza un recorrido de cada string para añadirla al Counter. La complejidad depende de la longitud de ambas cadenas. Por tanto sería O(len(s) + len(t)). Vamos a definir n=len(s) + len(t)
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `4 ms` (supera al `94.48%` de los envíos)
- **Memory:** `17.72 MB` (supera al `86.18%` de los envíos)

---


