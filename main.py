# A Simple Magic 8 Ball App
# Steven Vandegrift - 05/24/2025
import os
from random import choice

possible_answers = [
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
 __  __    __    ___  ____  ___    ___    ____    __    __    __   
(  \/  )  /__\  / __)(_  _)/ __)  ( _ )  (  _ \  /__\  (  )  (  )  
 )    (  /(__)\( (_-. _)(_( (__   / _ \   ) _ < /(__)\  )(__  )(__ 
(_/\/\_)(__)(__)\___/(____)\___)  \___/  (____/(__)(__)(____)(____)
    ''')
    print(r'''
 .-"""-.
/   _   \
|  (8)  |
\   ^   /
 '-...-'
''')

if __name__ == "__main__":
    clear_screen()
    name = input("What is your name?: ").title()
    print(f"Hi {name if name else 'stranger'}!")
    while True:        
        question = input("What would you like to ask?: ").title()
        answer = choice(possible_answers)
        if question:
            print(f"{name if name else "Your"} question: {question}")
            print(f"Magic 8 Ball's answer: {answer}\n")
            ask_again = input("What to ask another question? (yes/no): ")
            if ask_again.lower() != 'yes':
                print(f"Thanks for playing {name if name else "stranger"}!")
                break
            else:
                clear_screen()
        else:
            print("You gotta ask a question!")
            input("Press Any Key to Continue...")
