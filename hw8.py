def goorba(a,s):
    x=0
    for i in range(8):
        if a[i]=="1" and s[i]=="1":
            x=x+1
    return(x)
a=input("?").split()
s=input("?").split()
print(goorba(a,s))