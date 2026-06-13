def sum_number(a):
    if a==0:
        return 0
    
    return sum_number(a-1) +a


print(sum_number(5))