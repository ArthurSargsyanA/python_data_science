with open("ex4_text.txt") as f:
    r = f.read()
    res = 0
    for i in range(len(r)):
        if r[i].isalpha() == True :
            res += 1
    print(res)