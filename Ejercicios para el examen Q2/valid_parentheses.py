# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

#primero defino mi variable para almacenar llaves abiertas
#defino un diccionario para ver con cual llave abre y cierra
#recorro el string con for normal
    #valido si son llaves abriendo las meto al stack
    #si no primero veo si el stack no esta vacio si no son puras llaves cerrando
    #luego obtengo y elimino la ultima pocicion del stack con pop
    #comparo la ultima posicion del stack con la llave que esta cerrando en mi diccionario
#retorno si el stack esta vacio todas las llaves cerraron correctamente

def is_valid(s):
    stack = []
    mapeo = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            
            last = stack.pop()

            if last != mapeo[i]:
                return False
            
    return len(stack) == 0


s = "()"
s = "()[]{}"
s = "(]"
s = "([])"
s = "([)]"
print(is_valid(s))