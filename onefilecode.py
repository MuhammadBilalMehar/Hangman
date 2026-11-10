import random

medium_words = [
    "python", "laptop", "hangman", "teacher", "market",
    "country", "beautiful", "picture", "engineer", "station",
    "hospital", "library", "college", "company", "internet",
    "football", "mountain", "weather", "holiday"
]

choosed = random.choice(medium_words)
print(choosed)
display = []
for _ in range(len(choosed)):
    display += "_"

print(display)