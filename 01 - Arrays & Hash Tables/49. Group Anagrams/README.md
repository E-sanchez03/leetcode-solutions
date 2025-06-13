# 49. Group Anagrams

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/group-anagrams/description/)
- **Dificultad:** Medium
- **Categorías:** `Hash Table`, `Array`, `String`, `Sorting`

---

## 1. Enunciado del Problema

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

### Ejemplos

Example 1:

    **Input**: strs = ["eat","tea","tan","ate","nat","bat"]
    **Output**: [["bat"],["nat","tan"],["ate","eat","tea"]]
    **Explanation**:There is no string in strs that can be rearranged to form "bat".
        The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

    **Input**: strs = [""]
    **Output**: [[""]]

Example 3:

    **Input**: strs = ["a"]
    **Output**: [["a"]]

---

## 2. Análisis del Problema y Razonamiento

Vamos a crear una tabla Hash usando un defaultdict de la librería collections. Ordenaremos las cadenas de caracteres y en el diccionario accederemos a la clave que es la string ordenada y añadiremos cada string sin ordenar que corresponda.

La base está en que los anagramas ordenados son iguales, por tanto tendrán la misma clave.

---

## 3. Mi Solución

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for i in strs:
            d[''.join(sorted(i))].append(i)

        return list(d.values())
```

---

## 4. Análisis de Complejidad

### Complejidad Temporal (Time Complexity)
- **Análisis:** La complejidad principal está en el bucle y luego dentro del bucle la longitud de las cadenas de caracteres y la función sorted.
- **Complejidad:** `$O(nlog(n))$`


---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `9 ms` (supera al `90.31%` de los envíos)
- **Memory:** `20.48 MB` (supera al `95.83%` de los envíos)

---
