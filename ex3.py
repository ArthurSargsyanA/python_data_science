from collections import Counter
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7 , 7]

counts = dict(Counter(numbers))
res = {key:value for key, value in counts.items() if value > 0}

print(res)