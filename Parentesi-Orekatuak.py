# Egiaztatu (), [] eta {} dituen kate bat ondo orekatuta dagoen. Adibidea: "{[()]}", "[()(){()}]" → True, "{[(])}" → False.

def orekatua(katea):
    pila = []

    for k in katea:
        if k == "(" or k == "[" or k == "{":
            pila.append(k)

        elif k == ")":
            if len(pila) == 0 or pila.pop() != "(":
                return False
        elif k == "]":
            if len(pila) == 0 or pila.pop() != "[":
                return False
        elif k == "}":
            if len(pila) == 0 or pila.pop() != "{":
                return False

    return len(pila) == 0

katea = input("Sartu (), [] edo {} kate bat, nahi duzun ordenean, esateko orekatua dagoen ala ez: ")
print(f"Katea orekatua dago? {orekatua(katea)}")