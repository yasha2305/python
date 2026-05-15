import json
import os
from datetime import datetime

MEMORY_FILE = "chat_memory.json"

# Load previous chat memory
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

# Generate chatbot response
def get_response(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hello! How are you?"

    elif "your name" in text:
        return "I am a Python AI Chatbot."

    elif "time" in text:
        return datetime.now().strftime(
            "Current time is %I:%M %p"
        )

    elif "date" in text:
        return datetime.now().strftime(
            "Today's date is %d-%m-%Y"
        )

    elif "bye" in text or "exit" in text:
        return "Goodbye! Have a nice day."

    else:
        return "I don't fully understand that yet."

# Main chatbot loop
def main():
    memory = load_memory()

    print("=== AI CHATBOT ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)

        print("Bot:", response)

        # Save conversation
        memory.append({
            "user": user_input,
            "bot": response
        })

        save_memory(memory)

        if user_input.lower() == "exit":
            break

if __name__ == "__main__":
    main()