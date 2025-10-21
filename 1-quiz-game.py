# https://youtu.be/NpmFbWO6HPU?si=h_8zXJfaW2ZtIsoW&t=120

print("Welcome to my computer quiz!")

playing = input("Do you want to play? (y/n): ")

if len(playing) == 0:
    quit()

if playing[0].lower() != "y":
    quit()

print("Ok let's play! 🎉")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! 🧠")
    score += 1
else:
    print("Incorrect 😭")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! 🧠")
    score += 1
else:
    print("Incorrect 😭")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct! 🧠")
    score += 1
else:
    print("Incorrect 😭")

answer = input("Did you subscribe to the channel? ")
if answer.lower() == "maybe":
    print("Correct! 🧠")
    score += 1
else:
    print("Incorrect 😭")

print("All done!")
print("You got " + str(score) + " questions correct!")
print("That's " + str((score / 4)  * 100) + "%!")