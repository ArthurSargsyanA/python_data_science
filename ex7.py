def foo(arr) :
    res = []
    k = 0
    for i in arr:
        res.append(i ** 2)
        k += 1
    res.sort()
    return res

