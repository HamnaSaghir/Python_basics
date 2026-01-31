name= input("type your name")
print("Welcome to this adventure, "+name )
answer=input("You have come to make a choice of your path, you can either go left or right.Which way would you like to go? Choose left/right")
if answer=="left":
    answer= input (" You have come across a river, now it is upto you whether you want to walk around it or swim across? Type walk to walk around and swim to swim across.")
    if answer== "walk":
        answer=input("You have walked many miles, and found a bag and a trunk, you can choose only one.To choose the water type water and for the bag type bag")
        if answer=="trunk":
            print("There was a bomb BOOM, you have died and LOST yayy")
        elif answer=="bag":
            print(" Well, it is sad to inform you that you found some gold and got rich for the rest of your life. you WON")
        else:
            print("Not a valid option. YOU LOOSE")    
    elif answer=="swim": 
        print(" You met a pretty crocodile and it ate you. YOU LOOSE")
    else:
        print("Not a valid option. YOU LOOSE")
elif answer== "right":
    answer=input(" You see an elevator and stairs, you can only choose one to continue. For elevator type elevator and for the stairs type stairs.")
    if answer=="stairs":
        print("You were a hardworking personailty so you choosed the stairs, there was a man waiting for you who gave you a bag full of gold. Unfortunatley you WON")
    elif answer=="elevator":
        print(" Very well, a lazy person like you choose the elevator.I am glad to tell you that you have died as there was a bomb hidden in elevator. Boom you LOST you deserved it.")
    else:
        print("Not a valid option. YOU LOOSE")        
else:
    print("Not a valid option. YOU LOOSE")    

print("I hope you enjoyed the adventure.")    
