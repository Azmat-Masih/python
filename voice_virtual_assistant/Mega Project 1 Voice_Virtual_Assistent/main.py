import speech_recognition as sr # speech recognition library
import webbrowser # to open web pages
import pyttsx3 # text to speech conversion library
import music_library # import the music library
import requests # to make HTTP requests
import google.generativeai as genai # Google Generative AI library


recognizer = sr.Recognizer()  # Initialize speech recognizer
tts_engine = pyttsx3.init()  # Initialize text-to-speech engine


# Text-to-speech function
def speak(text):
    print("Panther:", text) # Print the text to console
    engine = pyttsx3.init(driverName="sapi5")  # try nsss on mac, espeak on linux
    voices = engine.getProperty("voices") # get available voices
    engine.setProperty("voice", voices[0].id) # set voice; change index for different voices
    engine.say(text) # convert text to speech
    engine.runAndWait()# run the speech engine
    engine.stop() # stop the engine


# Function to get AI response from Gemini
def gemini_reply(prompt):
    """Get AI response from Gemini 2.5 Flash"""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash") # load Gemini model
        response = model.generate_content(prompt) # generate content based on prompt
        return response.text.strip() # return the generated text
    except Exception as e: # handle exceptions
        return f"Error talking to Gemini: {e}"


# Function to process user commands
def process_command(c):
    # Process various voice commands
    if "open youtube" in c.lower(): # youtube command
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower(): # google command
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "facebook" in c.lower(): # facebook command
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower(): # linkedin command
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in c.lower(): # github command
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "open chat gpt" in c.lower(): # chatgpt command
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif c.lower().startswith("play"): # play music command
        song = c.lower().split(" ")[1]
        speak(f"Playing {song}")
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c: # news command
        speak("Fetching the latest news headlines")
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
            )
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if not articles:
                    speak("No news found at the moment.")
                else:
                    for i, article in enumerate(articles[:5], start=1):
                        speak(f"Headline {i}: {article['title']}")
                        # time.sleep(0.5)  # short pause between headlines
            else:
                speak(f"Failed to fetch news, error code {r.status_code}.")
        except Exception as e:
            speak(f"An error occurred while fetching news: {e}")

    elif c.startswith("search"): # search command
        query = c.replace("search", "").strip()
        speak(f"Let me check {query}, with the help Gemini.")
        answer = gemini_reply(query)
        speak(answer)
        
    elif "exit" in c or "sleep" in c: # exit command
        speak("Going to sleep, Master.")
        return "exit"


# Main program loop
if __name__ == "__main__":
    speak("Hello Master, I am your voice assistant.")  # Greet the user

    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:  # use the default microphone as the audio source
                print("Say something!")
                audio = r.listen(
                    source, timeout=2, phrase_time_limit=1
                )  # listen for the first phrase and extract it into audio data

            word = r.recognize_google(
                audio
            )  # recognize speech using Google Web Speech API
            print("You said: " + word)
            # print("Google thinks you said " + r.recognize_google(audio)) # print the recognized text

            if word.lower() == "panther":
                speak("Yes Master")

                # listen for further commands
                with sr.Microphone() as source:
                    print("Panther Activate...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command received: " + command)

                    process_command(command)

        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))
