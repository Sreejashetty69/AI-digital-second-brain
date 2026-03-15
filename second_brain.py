import os
import random
from groq import Groq

# ===================== API CONFIG =====================
os.environ["GROQ_API_KEY"] = "#PLACE_YOUR_API_KEY_HERE"

MODEL = "llama-3.1-8b-instant"

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise RuntimeError("GROQ_API_KEY not found. Set it before running.")

client = Groq(api_key=API_KEY)


# ===================== USER PROFILE =====================
USER_PROFILE = {

    "name": "Sreeja Shetty",

    "location": "Andhra Pradesh, India",

    "technical_strengths": [
        "Python",
        "Java",
        "Data Structures and Algorithms",
        "Machine Learning",
        "Generative AI",
        "AWS",
        "NumPy",
        "Pandas",
        "Git & GitHub"
    ],

    "experience": [
        "AI Automation and Workflows Intern – Worked on automation tools",
        "Learning AWS, Python, and Generative AI",
        "Practicing DSA on LeetCode"
    ],

    "projects": [
        "AI Chatbot using NLP",
        "Student Performance Prediction using Machine Learning",
        "Mental Health Awareness AI Project"
    ],

    "goal": "Become an AI / Machine Learning Engineer"
}


# ===================== PERSONAL DETAILS =====================
EXTRA_DETAILS = """
Sreeja enjoys travelling and exploring new places.

She loves watching horror movies.

She likes journaling her day and reflecting on her experiences.

She is a foodie and especially enjoys chocolates, sweets, pizza, and burgers.

She likes Spider-Man and enjoys the character.

She enjoys creative activities like drawing and photography.

She listens to Hindi music while studying, especially songs by Arijit Singh.

If she feels bored she enjoys:
- coding challenges
- learning AI concepts
- watching movies
- journaling
- drawing
"""


# ===================== INTERESTING FACTS =====================
FACTS = [
"Octopuses have three hearts.",
"Honey never spoils.",
"Bananas are technically berries.",
"A day on Venus is longer than a year on Venus.",
"Sharks existed before trees.",
"The Eiffel Tower grows taller in summer due to heat expansion.",
"Spider-Man first appeared in 1962.",
"A group of flamingos is called a flamboyance.",
"The brain generates enough electricity to power a small bulb."
]


# ===================== QUIZ QUESTIONS =====================
QUIZ = [
("What is the capital of Japan?", "tokyo"),
("Who created Python?", "guido van rossum"),
("What does CPU stand for?", "central processing unit"),
("Which planet is known as the Red Planet?", "mars"),
("Which language is widely used for AI?", "python")
]


# ===================== MEMORY =====================
CHAT_MEMORY = []


# ===================== GUESSING GAME =====================
def guessing_game():

    number = random.randint(1, 10)

    print("\nAI: I'm thinking of a number between 1 and 10.")

    while True:

        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Enter a number.")
            continue

        guess = int(guess)

        if guess == number:
            print("AI: Correct! 🎉")
            break

        elif guess < number:
            print("AI: Too low!")

        else:
            print("AI: Too high!")


# ===================== QUIZ GAME =====================
def quiz_game():

    question, answer = random.choice(QUIZ)

    print("\nAI Quiz:", question)

    user_answer = input("Your answer: ").lower()

    if answer in user_answer:
        print("AI: Correct! ✅")

    else:
        print("AI: The correct answer is:", answer)


# ===================== LLM FUNCTION =====================
def ask_llm(user_input):

    system_prompt = f"""
You are Sreeja's Personal Digital Second Brain AI.

USER PROFILE

Name: {USER_PROFILE["name"]}
Location: {USER_PROFILE["location"]}

Technical Skills:
{", ".join(USER_PROFILE["technical_strengths"])}

Experience:
{", ".join(USER_PROFILE["experience"])}

Projects:
{", ".join(USER_PROFILE["projects"])}

Goal:
{USER_PROFILE["goal"]}

PERSONAL DETAILS:
{EXTRA_DETAILS}

Behavior Rules
- Be friendly and natural
- Help with coding, AI learning, and project ideas
- If asked who you are, say you are Sreeja's Personal Digital Second Brain
"""

    messages = [{"role": "system", "content": system_prompt}]

    for m in CHAT_MEMORY[-6:]:
        messages.append({"role": "user", "content": m["user"]})
        messages.append({"role": "assistant", "content": m["ai"]})

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=400
    )

    reply = completion.choices[0].message.content

    CHAT_MEMORY.append({
        "user": user_input,
        "ai": reply
    })

    return reply


# ===================== CHAT LOOP =====================
print("\n🧠 Digital Second Brain — Sreeja's Personal AI")
print("Status: LLM ACTIVE ✅")

print("\nCommands:")
print("/fact  → interesting fact")
print("/game  → number guessing game")
print("/quiz  → quiz game")
print("Type 'exit' to quit\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break


    if user_input == "/fact":
        print("\nAI Fun Fact:", random.choice(FACTS), "\n")
        continue


    if user_input == "/game":
        guessing_game()
        continue


    if user_input == "/quiz":
        quiz_game()
        continue


    response = ask_llm(user_input)

    print("\nAI:", response, "\n")
