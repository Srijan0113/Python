#file handling
s="harry is a good boy"

# with open("test.txt","w") as f :
#     f.write(s)
#or you can do this 
# fp=open("test.txt","w")
# fp.write(s)
# fp.close


#Reading a file
with open("test.txt","r") as f :   
    a=f.read()
    print(a)

   #appending a file 
# with open("test.txt","w") as f :  
#     f.write("I am writing whatever i want ") 
with open("test.txt","a") as f :  
    f.write(" I am writing whatever i want ") 