#dictionary and methods 
#dictionary is key:value pairs
#mutable
dict1={}
print(type(dict1))
dict2={"good":"Something pleasant","fetch":"to bring","1":"the number 1"}
dict2["good"]
marks={"harry":45,"Srijan":56,"karun":98,"karuna":89,"Mohan":67}
print(marks)
marks["Manish"]=100
print(marks)
print(marks.get("Karun Poudel"))
print(marks.get("Karun"))
print(marks.get("karun"))
print(marks["karun"])
#print(marks["karun poudel"]) #Error will occur here
print(marks.keys())
print(marks.values)
print(marks.items())