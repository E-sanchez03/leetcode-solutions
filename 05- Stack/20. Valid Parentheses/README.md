# 20. Valid Parentheses

- **Link al Problema:** [Enlace directo en LeetCode](https://leetcode.com/problems/valid-parentheses/)
- **Dificultad:** Easy
- **Categorías:** `String`, `Stack`

---

## 1. Enunciado del Problema

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Ejemplos

Example 1:

    Input: s = "()"

    Output: true

Example 2:

    Input: s = "()[]{}"

    Output: true

Example 3:

    Input: s = "(]"

    Output: false

Example 4:

    Input: s = "([])"

    Output: true

Example 5:

    Input: s = "([)]"

    Output: false

---

## 2. Análisis del Problema y Razonamiento

Para usar el concepto de pila vamos a ir añadiendo a una estructura de datos como una lista de Python todos los paréntesis que sean de apertura. Como tienen que estar en orden cada vez que encontremos uno de cierre miraremos el último elemento de la lista y comprobaremos que corresponde con uno válido. Entonces lo eliminaremos de la lisita, podemos ver que la estructura sigue un orden LIFO.

Al final haremos una última comprobación en la que la pila esté vacía. Es decir cada paréntesis de apertura ha tenido uno correspondiente de cierre.

---

## 3. Mi Solución


```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                open_stack.append(c)
            else:
                if open_stack == []:
                    return False
                if c == ")" and open_stack[-1] != "(":
                    return False
                if c == "]" and open_stack[-1] != "[":
                    return False
                if c == "}" and open_stack[-1] != "{":
                    return False
                open_stack.pop()
        return True if open_stack == [] else False
```

---

## 4. Análisis de Complejidad


### Complejidad Temporal (Time Complexity)
- **Análisis:** Recorremos el string una sola vez O(n) y accedemos continuamente a elementos del final de la pila O(1)
- **Complejidad:** `$O(n)$`

---

## 5. Resultados en LeetCode

- **Runtime:** `0 ms` (supera al `100.00%` de los envíos)
- **Memory:** `18 MB` (supera al `10.02%` de los envíos)


---


