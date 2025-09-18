#functions
def greetHello():
    print("Hello")
    
greetHello()

def greeting(name,ending):
    print("hello",name)
    print(ending)
greeting("srijan","How are you !!")
greeting("alue","tero bau sale")

def lettergenerator(name,date):
    str=f"hi mam,\n this is {name} and I will not come to school on {date}"
    print(str)

lettergenerator("Srian","12th june")
lettergenerator("Sriii","15th june")

def average(a,b):
    return (a+b)/2

print(average(4,9))
print(average(56,89))