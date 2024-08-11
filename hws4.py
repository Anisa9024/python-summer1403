from colorama import Fore
a=input("?").split()
s=input("?").split()
x=0
for i in range(8):
    if a[i]=="1" and s[i]=="1":
        x=x+1
print(Fore.RED + x)