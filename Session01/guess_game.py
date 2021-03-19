import random
min = 1
max = 15
user=0
play="Y"
while(play!="N") :
    moves=0
    print("Think and guess a value from 1 to 15")
    upper_face_value=(random.randint(min, max))
    while(user!=1):
        print("Guess a value :",end=" ")
        user_input=int(input())
        moves+=1
        if(user_input>upper_face_value):
            print("Your guessed value is high.")
            continue
        elif(user_input<upper_face_value):
            print("Your guessed value is low.")
            continue
        else:
            print("You guessed correctly in "+str(moves)+" tries")
            break
    print("Do you want to play again(Y/N) :",end=" ")
    play=input()

