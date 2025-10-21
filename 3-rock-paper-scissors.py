import random
from typing import List

choices = ["rock", "scissors", "paper"]
user_wins = 0
pc_wins = 0

def check_win2(usr: str, pc: str, choices: List[str]):
    uidx = choices.index(usr)
    pidx = choices.index(pc)
    win = uidx + 1 == pidx
    if not win and uidx == len(choices) - 1:
        win = pidx == 0
    return win

def check_win1(usr: str, pc: str):
    win_conditions = []
    win_conditions.push(usr == "rock" and pc == "scissors")
    win_conditions.push(usr == "scissors" and pc == "paper")
    win_conditions.push(usr == "paper" and pc == "rock")
    return any(win_conditions)

def check_win0(usr: str, pc: str):
    conds = {
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock"
    }
    return conds[usr] == pc

while True:
    usr_pick = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if len(usr_pick) == 0:
        continue
    if usr_pick == "q":
        print("ok, byeeeeeee")
        break

    if usr_pick not in choices:
        print("I didn't understand... try again!")
        continue

    ran_num = random.randomint(0, 2)
    pc_pick = choices[ran_num]

    print("I picked ", pc_pick, "!")

    # won = check_win0(usr_pick, pc_pick)
    # won = check_win1(usr_pick, pc_pick)
    # won = check_win2(usr_pick, pc_pick)
    # if won:
    #   print("You won!")
    #   user_wins += 1
    #   continue
    # else:
    #   print("You lost!")
    #   pc_wins += 1


    if usr_pick == "rock" and pc_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif usr_pick == "scissors" and pc_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    elif usr_pick == "paper" and pc_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        pc_wins += 1

print("Score:")
print("Your score =", user_wins)
print("My score =", pc_wins)
print("Bye!")