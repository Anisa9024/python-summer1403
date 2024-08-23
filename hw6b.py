print("============MAIN MENU============")
print("1-Create new contact")
print("2-Edit Contact")
print("3-Delete Contact")
print("4-Block Contact")
print("5-Show contacts")
print("6-Call")
while True:
    item=input("choose an item:")
    if item=="1":
        x=open("phonebook.txt","a")
        name=input(" the name:")
        phone=input(" phone number:")
        x.write(f"\n{name}:{phone}\n")
        x.close()
    elif item=="2":
        x=input("you wanna edit phone or name?:")
        z=open("phonebook.txt","r")
        b=z.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        z.close()
        for i in c:
            q=i.split(":")
            name_1=q[0]
            phone_1=q[1]
            dictionary[name_1]=phone_1
        if x=="phone":
            e=input(" name:")
            r=input(" new phone number:")
            dictionary[e]=r
            a1=open("phonebook.txt","w")
            for i in dictionary:
                a1.write(f"\n{i}:{dictionary[i]}\n")
            a1.close()
        elif x=="name":
            name=input("new name:")
            phone=input(" phone number:")
            nam=input("enter the lastest name:")
            del dictionary[nam]
            dictionary[name]=phone
            a1=open("contacts.txt","w")
            for i in dictionary:
                a1.write(f"\n{i}:{dictionary[i]}\n")
            a1.close()
    elif item=="3":
        delete=input("name:")
        k=open("phonebook.txt","r")
        l=k.read()
        p=l.split("\n")
        for i in p:
            if i=="":
                p.remove(i)
        dictionary={}
        k.close()
        for i in p:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        del dictionary[delete]
        a1=open("contacts.txt","w")
        for i in dictionary:
            a1.write(f"\n{i}:{dictionary[i]}\n")
        a1.close()
    elif item=="4":
        name=input("name:")
        a=open("phonebooks.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        if name in dictionary:
            x=open("blocked.txt","a")
            x.write(f"\n{name}")
            x.close()
        else:
            pass
    elif item=="5":
        a=open("phonebook.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
            for i in dictionary:
                print(i,dictionary[i])
    elif item=="6":
        a=open("phonebook.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        dictionary={}
        a.close()
        for i in c:
            v=i.split(":")
            name_1=v[0]
            phone_1=v[1]
            dictionary[name_1]=phone_1
        a=open("blocked.txt","r")
        b=a.read()
        c=b.split("\n")
        for i in c:
            if i=="":
                c.remove(i)
        a.close()
        x=input("name:")
        if x in dictionary:
            if x in c:
                l=input("unblock it or no?")
                if l=="yes":
                    c.remove(x)
                    s=open("blocked.txt","w")
                    for i in c:
                        s.write(f"\n i")
                    print(f"calling {x}")
                else:
                    print("you can't call this contact because the contact is in blocking list ")
            else:
                print(f"calling {x}")
        else:
            print("you haven't got this contact")