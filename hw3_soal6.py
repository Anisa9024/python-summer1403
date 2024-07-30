n=input("number?").split()
nu=list(map(int,n))
x=sum(nu)

if x%2==0:
    n=eval(input("number?"))
    print(x+n)
else:
    x=x-nu[2]
    print(x)