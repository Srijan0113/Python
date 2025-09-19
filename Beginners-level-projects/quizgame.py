print("Welcome to my computer quiz")

playing= input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :) ")
score=0

answer = input("What does CPU stand for ? ")#yaha pe vi .lower laga sakte hain
if answer.lower() == "central processing unit":
    print("Correct ! ")
    score += 1 
else:
    print("Incorrect")

print("You got " + str(score)+ " questions correct !") 
print("YOu got",score,"questions correct ")
#hum iska percentage vi nikal sakte hain
#we can add many questions like this 
