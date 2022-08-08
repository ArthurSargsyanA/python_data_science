from collections import Counter
with open("ex6_text.txt") as f:
    r = f.read()
    arr = r.split()
    print(arr)
    counts = dict(Counter(arr))
    res = {key:value for key, value in counts.items() if value > 0}
    print(res)