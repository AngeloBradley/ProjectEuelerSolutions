#Special Pythogorean Triple in Python

def verify(a, b, c):
    if(a < b) and (b < c):
        return True
    else:
        return False

def pythag(a, b, c):
    if(a * a) + (b * b) == (c * c):
        return True
    else:
        return False


a = 0
b = 0
c = 0

for xa in range(1, 300):
    a = xa
    b = ((1000 * a) - 500000) / (a - 1000)
    c = 1000 - (a + b)
    if verify(a, b, c):
        if pythag(a, b, c):
            print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))
            print("product = " + str(a * b * c))
            break


   

