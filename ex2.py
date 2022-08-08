with open("ex2_text.txt" , "r") as r_text:
    with open("ex2_res.txt" , "w") as w_text:
        for line in r_text:
            w_text.write(line.title())