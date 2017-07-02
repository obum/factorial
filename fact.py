
def factorial(): 
    number = int(input())

    if number ==0:
        d1 = {0:1}
        result1 = 1,d1
        return tuple(result1)
    if number ==1:
        d2 ={1:1}
        result2 = 1,d2
        return tuple(result2)
    result = 1
    while(number >=2):
        result *= number
        number -= 1
        d ={}
        c = str(result)
        e = set(c)
        for key in e: 
            d[key] = c.count(key)
        result3 = (result, d)
        
        
    return (tuple (result3)
)
print(factorial())