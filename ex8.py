def sum_numbers(num):
    res = 0
    while num > 0 :
        res += num % 10
        num = num // 10
    return res
print(sum_numbers(782004))
