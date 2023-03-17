from stack import Stack

"""
Brackets y similares balanceados.
Determinar si están o no balanceados dado un conjunto de
elementos. 
"""
#   Func parametrizada que toma los dos elementos p1 y p2 
#   y los compara en mediante conjuncion (and operator)
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    
    elif p1 == "{" and p2 == "}":
        return True
    
    elif p1 == "[" and p2 == "]":
        return True
    
    else:
        return False

def is_items_balanced(items_string):
    s = Stack()
    is_balanced = True
    index = 0
    
    while index < len(items_string) and is_balanced:
        #   Creamos un objeto items_str y le asignamos el valor que tenga 
        #   el elemento en items_string en la pos del index
        items_str = items_string[index] 
        if items_str in "([{":
            s.push(items_str)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
            #   Creamos un obj llamado top (ultimo del stack)
            #   lo sacamos para evaluar el match
                top = s.pop()
                if not is_match(top, items_str):
                    is_balanced = False
                    break
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(is_items_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_items_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_items_balanced("[][]"))