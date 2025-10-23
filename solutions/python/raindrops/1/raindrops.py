def convert(number):
    list = []
    if number % 3 == 0:
        list.append("Pling")
        if number % 5 == 0:
            list.append("Plang")
            if number % 7 == 0:
               list.append("Plong")
        if number % 7 == 0 and number % 5 != 0:
            list.append("Plong")
    elif number % 5 == 0:
        list.append("Plang")
        if number % 7 == 0:
            list.append("Plong")
    elif number % 7 == 0:
        list.append("Plong")    
     
    else:
        list.append(number)
    return("".join(map(str, list)))
    
