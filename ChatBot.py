import json
import random
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        return data
    

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file,  indent = 2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n = 1, cutoff= 0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["Questions"]:
        if q["Question"] == question:
            return q["Answer"]
        

def chat_bot():
    knowledge_base: dict = load_knowledge_base("/Users/judahlomo/Development/VsCode/Python/Knowledge_Base.json")

    random_reponses = ["I can't answer that yet. Can you please teach me?",
                       "Oh! It appears you wrote something I don't understand yet, could you help me out?",
                       "I'm terribly sorry, I didn't quite catch that, help me understand."]
    
    random_reponse_number = random.randint(0, len(random_reponses)-1)


    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "quit":
            break

        best_match: str | None = find_best_match(user_input, [q["Question"]for q in knowledge_base["Questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print(f"Bot: {random_reponses[random_reponse_number]}")
            new_answer: str = input("Type your answer or 'skip' to skip: ")

            if new_answer.lower() != "skip":
                knowledge_base["Questions"].append({"Question": user_input, "Answer": new_answer})  # Fix keys "Question" and "Answer"
                save_knowledge_base("/Users/judahlomo/Development/VsCode/Python/Knowledge_Base.json", knowledge_base)
                print("Bot: Thanks! I learned something new!")

def main():
    chat_bot()  

if __name__ == "__main__":
    main()