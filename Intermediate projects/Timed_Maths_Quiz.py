import random 
import time
OPERATORS = ['+','-','*']# it is a Constant
MIN_OPERAND=int(input("Enter the minimum operand you want : "))
MAX_OPERAND = int(input("Enter the maximum operand you want : "))

print("This is a simplication problems program . Solve as many questions as you want")

TOTAL_PROBLEMS=int(input("How many problems do you want to solve : "))



def generate_problem():
    a=random.randint(MIN_OPERAND,MAX_OPERAND)
    b=random.randint(MIN_OPERAND,MIN_OPERAND)
    c=random.randint(MIN_OPERAND,MIN_OPERAND)
    d=random.randint(MIN_OPERAND,MIN_OPERAND)
   # operator=random.choice(OPERATORS) #randomly choose from a list

    expr=str(a) + " " + random.choice(OPERATORS) + " " +str(b) + " " + random.choice(OPERATORS) + " " + str(c) + " " + random.choice(OPERATORS) + " " + str(d)
    answer=eval(expr)
    return expr,answer
wrong=0
input("Press Enter to start ! ")
print("-------------------------")

start_time=time.time()
correct=0

for i in range(TOTAL_PROBLEMS):
    expr,answer=generate_problem()
    while True:
     guess=input("Problem #"+ str(i+1)+ " : " + expr + " = ")
     if guess==str(answer):
        correct+=1
        break
     
     wrong+=1


end_time=time.time()
total_time=round(end_time-start_time,2)
print("---------------------------------")
print("Nice work! You finished the problems in ",total_time, "seconds")
print("Overall Correct answer with multiple attempts : ",correct)
print("Incorrect answer : ", wrong)







