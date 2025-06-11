# 1. Two Sum

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/two-sum/description/)
- **Dificultad:** Easy
- **Categorías:** `Array`, `Hash Table`

---

## 1. Enunciado del Problema

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

### Ejemplos

Example 1:

    **Input**: nums = [2,7,11,15], target = 9
    **Output**: [0,1]
    **Explanation**: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

    **Input**: nums = [3,2,4], target = 6
    **Output**: [1,2]

Example 3:

    **Input**: nums = [3,3], target = 6
    **Output**: [0,1]

---

## 2. Análisis del Problema y Razonamiento

- Se puede ver una clara solución por fuerza bruta, recorriendo para cada elemento los demás y ver si con alguna suma el target. Esto produciría dos bucles por tanto una complejidad $O(n^2)$. Sin embargo, podríamos recorrer la lista de manera más eficiente si la convertimos en un diccionario (Tabla Hash).

- Al recorrer la lista iremos añadiendo cada numero a un diccionario del tipo {núemero : índice}. Si el target que buscamos se encuentra ya en el hash_map paramos y devolvemos ambos índices.

---

## 3. Mi Solución


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,x in enumerate(nums):
            i_res = hash_map.get(target-x,-1)
            if i_res != -1:
                return i_res,i
            else:
                hash_map[x] = i
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Recorremos la lista una sola vez, hacemos dos operaciones, una de get y otra de inserción. Estas dos son de complejidad constante, O(1). Por tanto, el bucle for es el que limita la velocidad.
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `0 ms` (supera al `100.00%` de los envíos)
- **Memory:** `18.90 MB` (supera al `51.13%` de los envíos)


---
## 6. Notas y Puntos Clave Aprendidos

En este problema podemos entender como el acceso a diccionarios lleva menos tiempo que recorrer una lista. La fuerza bruta no sería la solución óptima si podemos fabricar nuestra propia tabla Hash.


