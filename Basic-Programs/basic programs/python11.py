#match-case
a=int(input("Enter a number :  "))
match a :
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 10:
        print("Case is 10")
    case 11:
        print("Case is 11")
    case 21:
        print("Case is 21")
    case 41:
        print("Case is 41")
    case 51:
        print("Case is 51")
    case 61:
        print("Case is 81")
    case _:
         #default case
         print("No match found")
