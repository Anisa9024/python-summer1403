def game(nx):
    x=int(nx[0])
    s=int(nx[1])
    if x>s:
        return x-s
    else:
        return s-x
nx=input("?")
print(game(nx))