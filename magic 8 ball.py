import random
question = input('Question :       ')
answers= [
    "Yes - definitely.",
    "It is decidely so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good",
    "Very doubtful."
]
random_number = random.randint(0, len(answers)-1)
answer= answers[random_number]
print(f"Magic 8 Ball: {answer}")