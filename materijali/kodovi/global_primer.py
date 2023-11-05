
x = 0
y = 0

# ukoliko menjamo promeljivu izvan funkcije, moramo da stavimo global!!!
def uvecaj_x():
    global x
    x += 1

# iako izvan funkcije psotoji y, menja se y koji je prosledjen kao argument
def uvecaj_y(y):
    y += 1

uvecaj_x()
uvecaj_y(y)

print(f'{x = }')
print(f'{y = }')
