def foo(str) :
    res = ""
    for i in range(len(str)):
        if (i + 1) % 3 == 0:
            continue
        res += str[i]
    return res

