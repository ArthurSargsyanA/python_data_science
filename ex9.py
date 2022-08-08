def foo(num) :
    sum = 0
    p = 1
    while num > 0 :
        sum += num % 10
        p *= num % 10
        num = num // 10
    return p - sum
