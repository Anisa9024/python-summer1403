def separator(x):
    en=[]
    odd=[]
    for i in x:
        if i%2==0:
            en.append(i)
        else:
            odd.append(i)
    return f"even:{en},odd:{odd}"
s=input("numbers:")
ln=s.split(",")
it=list(map(int,ln))
print(separator(it))