def aps(x):
    if x >= 0:
        return x
    else:
        return -x
    
def povrsina_pravougaonika(a, b):
    return a * b

def maksimum(a, b):
    if a >= b:
        return a
    else:
        return b
    
print(f'{aps(5)=}')
print(f'{aps(-2)=}')
print(f'{maksimum(3, 4) = }')
print(f'{maksimum(5, -2) = }')