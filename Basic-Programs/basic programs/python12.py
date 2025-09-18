#table of a number which is from 1 t0 10
i= int (input ("Enter a number : " ))
def table(x):
    for i in range(1,11):            
            print(x,"*",i ,"=",x*i)
    
match i :
    case 1 : 
          table(1)
    case 2: 
          table(2)
    case 3 : 
          table(3)
    case 4 : 
          table(4)
    case 5 : 
          table(5)
    case 6 : 
          table(6)
    case 7 : 
          table(7)
    case 8: 
          table(8)
    case 9 : 
          table(9)
    case 10 : 
          table(10)
    case _:
            print("no such choice")
          
        
        
        