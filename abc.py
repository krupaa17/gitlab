import random
import string
import time

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%&?"
    return ''.join(random.choice(chars) for _ in range(length))

def random_joke():
    jokes = [
        "Why do programmers hate nature? Too many bugs!",
        "I told my computer I needed a break… it said 'No problem, I'll go to sleep.'",
        "Why did the function break up with the loop? It needed more space.",
        "Programmer's favorite place in a house? The loop-hole!"
    ]
    return random.choice(jokes)

def lucky_number():
    return random.randint(1, 99)

# Main program
print("\n===== RANDOM PY GENERATOR =====")
print(f"Generated Password 🔐: {generate_password()}")
print(f"Lucky Number 🍀: {lucky_number()}")
print(f"Random Joke 🤣: {random_joke()}")
print("Generated at:", time.strftime("%Y-%m-%d %H:%M:%S"))
print("================================\n")
#i changed krupa file
