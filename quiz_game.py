print("Welcome to the Quiz Game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("lETS PLAY")
playing = True

while playing == True:
    answer = input("What does CPU stand for? ")
    if answer == "central processing unit":
        print("You are correct")
        break
    else:
        print("You are wrong")
        playing == False

while playing == True:
    answer = input("What is the brain of CPU ")
    if answer == "motherboard":
        print("You are correct")
        print("Congragulations")
        break
    else:
        print("You are wrong")
        playing == False