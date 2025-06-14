# 125. Valid Palindrome

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/valid-palindrome/description/)
- **Dificultad:** Easy
- **Categorías:** `Two Pointers`, `String`

---

## 1. Enunciado del Problema

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

### Ejemplos

Example 1:

    **Input**: s = "A man, a plan, a canal: Panama"
    **Output**: true
    **Explanation**: "amanaplanacanalpanama" is a palindrome.

Example 2:

    **Input**: s = "race a car"
    **Output**: false
    **Explanation**: "raceacar" is not a palindrome.

Example 3:

    **Input**: s = " "
    **Output**: true
    **Explanation**: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

---

## 2. Análisis del Problema y Razonamiento

Usaremos la técnica de Two Pointers para resolverlo. Esta consiste en empezar en ambos extremos del array e ir recorriendolo tanto por el principio como por el final. Si el string es un palindrómo ambos punteros serán iguales. Antes de eso normalizaremos el string eliminando carácteres no alfanuméricos y poniéndolo todo en minúsculas.

---

## 3. Mi Solución


```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(s)-1

        for i in range(len(s)//2):
            if s[left] != s[right]:
                return False
            left +=1
            right -= 1
        return True
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Hacemos dos bucles, uno para normalizar, un bucle de longitud n, y luego un bucle de longitud n/2 para comprobar los punteros.
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `8 ms` (supera al `52.74%` de los envíos)
- **Memory:** `23.31 MB` (supera al `6.37%` de los envíos)


---



