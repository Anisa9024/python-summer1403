List=input("question?").split()
num_1=int(List[0])
num_2=int(List[2])
match List[1]:
    case "+":
        print(num_1+num_2)
    case "-":
        print(num_1+num_2)
    case "*":
        print(num_1*num_2)
    case "//":
        print(num_1//num_2)
    case "*":
        print(num_1**num_2)