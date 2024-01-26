from sys import argv

script, user_name, nickname = argv
feedback = '> '

print(f"Hi {user_name} my nickname is {nickname}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print("How old are you?") 
age = input(feedback)
print(f"Do you like me {user_name}?")
likes = input(feedback)

print(f"Where do you live {user_name}?")
lives = input(feedback)

print("What kind of computer do you have?")
computer = input(feedback)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")