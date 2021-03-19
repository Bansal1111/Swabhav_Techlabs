import random
min = 1
max = 6
turn=0
user_sum=0
play="Y"
while(user_sum<20) :
    turn+=1
    if(turn!=1):
        print()
    print("Turn "+str(turn))
    user_input="r"
    turn_sum=0
    flag=0
    while(user_input!="h"):
        print("Roll or hold? (r/h): ",end="")
        user_input=input()
        if(user_input=="r"):
            upper_face_value=(random.randint(min, max))
            print("Die "+str(upper_face_value))
            if(upper_face_value==1):
                print("Turn over. No score.")
                flag=1
                break
            turn_sum+=upper_face_value
        else:
            break
    if(flag==0):
        user_sum+=turn_sum
        print("Score for turn :"+str(turn_sum))
        print("Total score :"+str(user_sum))
print()
print()
print("You finished in "+str(turn)+" turns.")
print("Game over !!")