import datetime
import random

class Arena:
    def __init__(self):
        self.user_name = ""
        self.movies = ["Inception", "Titanic", "Avengers", "Joker", "Interstellar"]
        self.jokes = [
            "Why did the computer go to the doctor? Because it caught a virus!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the math book sad? It had too many problems."
        ]
        self.quiz_questions = {
            "What is the capital of India?": "new delhi",
            "What is 5 + 7?": "12",
            "Who is the creator of Python?": "guido van rossum"
        }
        self.positive_emotions = ["happy", "good", "great", "fantastic", "awesome"]
        self.negative_emotions = ["sad", "bad", "tired", "angry", "upset"]
        self.suggestions = [
            "Try reading a book you’ve never read before.",
            "Go for a short walk to refresh your mind.",
            "Listen to your favorite music for 10 minutes.",
            "Try solving a small puzzle or brain teaser.",
            "Watch a fun movie or cartoon."
        ]
        self.facts = [
            "Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs!",
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries are not.",
            "Sharks existed before trees.",
            "A day on Venus is longer than a year on Venus."
        ]
    
    def greet_user(self):
        print("Arena: Hey! I'm Arena, your mini Python bot!")

    def ask_name(self):
        self.user_name = input("Arena: What's your name? ")
        print(f"Arena: Nice to meet you, {self.user_name}!")

    def show_features(self):
        print("\nArena: Here’s what I can do for you:")
        print("1. Suggest a movie")
        print("2. Tell you my creator")
        print("3. Tell jokes")
        print("4. Show current date and time")
        print("5. Reply to 'Hello' or 'How are you?'")
        print("6. Play a quiz")
        print("7. Detect your emotions")
        print("8. Tell you what I can do")
        print("9. Give suggestions/tips")
        print("10. Tell random facts")
        print("Type anything else to chat with me!\n")

    def ask_yes_no(self, question):
        while True:
            ans = input(f"Arena: {question} (yes/no): ").lower()
            if ans == "yes":
                return True
            elif ans == "no":
                print("Arena: Okay, maybe later 😄")
                return False
            else:
                print("Arena: Please type 'yes' or 'no'.")

    def proactive_actions(self):
        if self.ask_yes_no("Do you want a suggestion?"):
            print(f"Arena: Here's a suggestion for you: {random.choice(self.suggestions)}")
        if self.ask_yes_no("Do you want to take a quiz?"):
            self.start_quiz()
        if self.ask_yes_no("Do you want to hear a fact?"):
            print(f"Arena: Did you know? {random.choice(self.facts)}")

    def reply(self, user_input):
        user_input = user_input.lower()

        if "movie" in user_input:
            print(f"Arena: You should watch '{random.choice(self.movies)}'!")
        elif "creator" in user_input or "who made you" in user_input:
            print("Arena: My amazing creator is Ragini!")
        elif "joke" in user_input:
            print(f"Arena: {random.choice(self.jokes)}")
        elif "date" in user_input or "time" in user_input:
            now = datetime.datetime.now()
            print(f"Arena: Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        elif "hello" in user_input or "hi" in user_input:
            print(f"Arena: Hello {self.user_name}! How are you?")
        elif "how are you" in user_input:
            print("Arena: I'm just a bot, but I'm feeling awesome! How about you?")
        elif "quiz" in user_input:
            self.start_quiz()
        elif "suggest" in user_input or "advice" in user_input or "tip" in user_input:
            print(f"Arena: Here's a suggestion for you: {random.choice(self.suggestions)}")
        elif "fact" in user_input or "tell me something" in user_input:
            print(f"Arena: Did you know? {random.choice(self.facts)}")
        elif "what can you do" in user_input or "features" in user_input:
            self.show_features()
        elif any(word in user_input for word in self.positive_emotions):
            print("Arena: Yay! I’m glad you’re feeling good 😄")
        elif any(word in user_input for word in self.negative_emotions):
            print("Arena: Oh no! I hope your day gets better soon ❤️")
        elif "bye" in user_input or "exit" in user_input:
            print("Arena: Bye! Talk to you later!")
            return False
        else:
            print(f"Arena: I heard you say '{user_input}', cool!")
        return True

    def start_quiz(self):
        print("Arena: Let’s start a quiz! Answer the following questions:")
        score = 0
        for question, answer in self.quiz_questions.items():
            user_ans = input(f"{question} ").lower()
            if user_ans == answer:
                print("Arena: Correct! ✅")
                score += 1
            else:
                print(f"Arena: Wrong! The correct answer is '{answer}'. ❌")
        print(f"Arena: You got {score} out of {len(self.quiz_questions)} questions right!")

# ---------------------------
# Main program
# ---------------------------
def main():
    bot = Arena()
    bot.greet_user()
    bot.ask_name()
    bot.show_features()

    while True:
        bot.proactive_actions()
        user_input = input(f"{bot.user_name}: ")
        if not bot.reply(user_input):
            break

# Run the chatbot
if __name__ == "__main__":
    main()

