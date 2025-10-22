def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c:
        return(False)
    if a + c < b:
        return(False)
    if b + c < a:
        return(False)
    if a == b == c == c and a != 0 and b != 0 and c != 0:
        return(True)
    else:
        return(False)

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c:
        return(False)
    if a + c < b:
        return(False)
    if b + c < a:
        return(False)    
    if a == b or a == c or b == c and a != 0 and b != 0 and c != 0:
        return(True)
    else:
        return(False)


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c:
        return(False)
    if a + c < b:
        return(False)
    if b + c < a:
        return(False)
    if a != b and a != c and b != c:
        return(True)
    else:
        return(False)
    
