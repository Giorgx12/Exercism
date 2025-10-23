def square(number):
    
    n = number - 1
        
    square = 2 ** n
    if number == 1:
        return(1)
    elif number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return(square)

        

def total():
    tot = (2 ** 64) - 1
    return(tot)
