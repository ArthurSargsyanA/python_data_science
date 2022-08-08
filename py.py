with open("text.txt") as f:
    r = f.readlines()
    res = ''''''
    for i in range(len(r)):
        r[i] = r[i].replace("tpel" , "print")
        r[i] = r[i].replace("_if" , "if") 
        r[i] = r[i].replace("_else" , "else")
        r[i] = r[i].replace("elseif" , "elif")
        res += r[i]
    exec(res)





