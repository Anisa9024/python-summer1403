def calculate_floor(string):
    x=string.split()
    z=0
    for i in x:
        if i=="U":
            z=z+1
        elif i=="D":
            z=z-1
    return z
string=input("?")
print(calculate_floor(string))