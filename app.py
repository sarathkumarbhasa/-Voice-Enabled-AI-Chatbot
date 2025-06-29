import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


genai.configure(api_key="")


model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎙️ Jarvis Activated! Say 'exit' to stop.\n")

while True:
    try:
        with mic as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        prompt = recognizer.recognize_google(audio)
        print("You said:", prompt)

        if prompt.lower() == "exit":
            speak("Goodbye sir!")
            break
        response = model.generate_content(prompt)
        reply = response.text
        print("Jarvis:", reply)
        speak(reply)

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
    except Exception as e:
        print("Error:", e)
        speak("Sorry, there was an error.")
