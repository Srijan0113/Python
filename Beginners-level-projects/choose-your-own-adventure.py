name=input('Type you name : ')
print("Welcome",name,"to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right . Which way would you like to go ? : ")

if answer.lower()=="left":
    answer=input("Ok now you have come to a river , you can walk around it or swim across. Choose between (Walk/Swim) ").lower()

    if answer=="swim":
        print("Oh o ....You were eaten by the Piranas ")
    elif answer=="walk":
        print("You walked for many miles , ran out of water and you have died of dehydration ")
    else:
        print("Not a Valid option . You lose ! ")    


elif answer=="right":
    answer=input('You have came to a bridge . You can go straight or jump from it using umbrella to go to the main road .Which option do you choose (Straight/Jump) : ').lower()
    if answer=="straight":
        print("You have come to a village of vampires .")

    elif answer =="jump":
        answer=input("You have come to the main road and someone has come to pick you up . Do you want to go with him : ").lower()
        if answer=="Yes":
            print("He take you the treasure land . You won ....")
        if answer=="No":
            print ("The bridge collapsed and you were crushed under it . You lose .... ")
        else:
            print("Not a valid option. You lose ... ")

else:
    print("Not a valid option . You lose !!")

print("Thank you for trying ...... ")
