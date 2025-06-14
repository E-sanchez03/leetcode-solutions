# 15. 3Sum

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/3sum/description/)
- **Dificultad:** Medium
- **Categorías:** `Array`, `Two Pointers`, `Sorting`

---

## 1. Enunciado del Problema

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

### Ejemplos

Example 1:

    **Input**: nums = [-1,0,1,2,-1,-4]
    **Output**: [[-1,-1,2],[-1,0,1]]
    **Explanation**: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:

    **Input**: nums = [0,1,1]
    **Output**: []
    **Explanation**: The only possible triplet does not sum up to 0.

Example 3:

    **Input**: nums = [0,0,0]
    **Output**: [[0,0,0]]
    **Explanation**: The only possible triplet sums up to 0.

---

## 2. Análisis del Problema y Razonamiento

Usaremos la técnica de Two Pointers para resolverlo. Esta consiste en empezar en ambos extremos del array e ir recorriendolo tanto por el principio como por el final. Fijaremos un valor x y recorreremos la lista ordenada que queda a partir de ese valor. Cuando la suma sea mayor que 0 avanzaremos por el puntero de la derecha, cuando sea menor por la izquierda. Además comprobaremos algunos tests para evitar cálculos innecesarios.

---

## 3. Mi Solución


```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
    
        for x in range(len(nums)):
            if nums[x] > 0:
                break
            if x > 0 and nums[x] == nums[x-1]:
                continue
            left = x+1
            right = len(nums) -1
            while left < right:
                trip = [nums[x], nums[left], nums[right]]
                total = sum(trip)
                if total >0:
                    right -= 1
                elif total <0:
                    left +=1
                
                else:
                    triplets.append(trip)
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left += 1
           
        return triplets
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Realizamos un bucle for y un bucle while. Es dificil decir la complejidad del bucle while. Por tanto acotaremos por log(n)
- **Complejidad:** `$O(n log(n))$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `775 ms` (supera al `26.73%` de los envíos)
- **Memory:** `20.61 MB` (supera al `68.95%` de los envíos)


---



