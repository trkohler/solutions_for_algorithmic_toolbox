def euclid_algo(a, b): 
    if b == 0:
        return a
    
    _a = a % b
    return euclid_algo(b, _a)

a = 357
b = 234

answer = euclid_algo(a, b)
print(answer)
