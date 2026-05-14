import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen from microphone
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)

            print("You said:", command)
            return command.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            speak("Internet connection error.")
            return ""

        except:
            return ""

# Main assistant logic
def run_assistant():
    speak("Hello! How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        # Open YouTube
        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Open Google
        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Tell time
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        # Search Google
        elif "search" in command:
            query = command.replace("search", "")
            url = f"https://www.google.com/search?q={query}"

            speak(f"Searching for {query}")
            webbrowser.open(url)

        # Exit assistant
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I did not understand.")

if __name__ == "__main__":
    run_assistant()