from stack import Stack

#   3. func que recibe un obj stack y la cadena
def reverse_string(stack, input_str):
    #   4. Longitud de la cadena iterando sobre un index para operar
    for i in range(len(input_str)):
    #   5. Por cada elemento de inptstr metemos al stack
        stack.push(input_str[i])
    rev_str = ""
    #   6. como el stack está lleno lo sacamos y concatenamos al rev
    #   mientras que pop hace el trabajo de sacarlos
    #   y quedan en orden ya que FiLo 
    #   FiLo para el string en reversa lo deja ordenado
    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str
#   1. Creamos el obj stack a partir de la clase
stack = Stack()
#   2. Cadena de ejemplo
input_str = "lleH ot emocleW"
print(reverse_string(stack, input_str))