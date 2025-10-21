# https://www.youtube.com/watch?v=NpmFbWO6HPU

print("Welcome to the quiz game!")

playing = input("Do you want to play? (y/n): ")

if len(playing) == 0:
    quit()

if playing[0].lower() != "y":
    quit()

print("Ok let's play! 🎉")
score = 0
playing = True

qas = [
    ("What does CPU stand for?", "central processing unit", 1),
    ("What does GPU stand for?", "graphics processing unit", 1),
    ("What does PSU stand for?", "power supply unit", 1),
    ("Did you subscribe the channel?", "maybe", 1)
    ("Did you like the video?", "Nahhhh", 100),
]

for qa in qas:
    answer = input(f"{qa[0]}: ").lower()
    if answer == "q":
        break
    if answer == qa[1]:
        score += qa[2]
        print("Correct! 🧠")
    else:
        print("WRONG! ❌")
    print("(respond Q to quit early)")

print("Score is", score)
pct_correct = int(score / 4 * 100)

print(f"All done! Your score was {str(score)}! That's {pct_correct}%!")