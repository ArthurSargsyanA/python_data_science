with open("text.txt") as f:
    r = f.readlines()
    res = "print("
    for i in range(len(r)):
        r[i] = r[i].replace(" " , "+")
        if i > 0:
            res += "+" + r[i]
        else :
            res += r[i]
        print(res)
    res += ")"
    exec(res)
