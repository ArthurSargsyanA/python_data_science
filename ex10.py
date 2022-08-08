def odd(a , b) :
    res = 0
    if a % 2 != 0 :
        res += 1
    elif b % 2 != 0 :
        res += 1
    res += (b - a) // 2
    return res 
print(odd(1 , 9))  