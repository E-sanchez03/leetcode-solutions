# 121. Best Time To Buy And Sell Stock

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
- **Dificultad:** Easy
- **Categorías:** `Array`, `Dynamic Programming`

---

## 1. Enunciado del Problema

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### Ejemplos

Example 1:

    **Input**: prices = [7,1,5,3,6,4]
    **Output**: 5
    **Explanation**: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

    **Input**: prices = [7,6,4,3,1]
    **Output**: 0
    **Explanation**: In this case, no transactions are done and the max profit = 0.

---

## 2. Análisis del Problema y Razonamiento

Hay varias formas de resolverlo. Por ejemplo, por fuerza bruta $O(n^2)$ sería con dos bucles anidados una solución trivial. Mi solución es de complejidad O(n) ya que recorremos el array una sola vez. El resultado óptimo será aquel que tenga el valor de compra más pequeño y el valor de venta más alto respecto al valor de compra.

---

## 3. Mi Solución


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying= prices[0]
        selling = 0
        for i in prices:
            buying = min(buying,i)
            selling = max(selling,i-buying)
        return selling
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Recorremos la lista una sola vez. Las demás operaciones se realizan en tiempo constante
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

Anota aquí tus métricas para tener una referencia de tu rendimiento.

- **Runtime:** `127 ms` (supera al `28.99%` de los envíos)
- **Memory:** `27.00 MB` (supera al `32.99%` de los envíos)


---


