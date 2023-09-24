# Import PYTTSX3 for Voice
import pyttsx3
# Import Datetime
import datetime
# Import Speech Recognition for Getting User Speech
import speech_recognition as sr
# Import Wikipedia for Search
import wikipedia
# Import WebBrowser for Open Sites
import webbrowser
# Import Os for Handling Devices Folders
import os
# Import Random for Generating Random Value
import random
# Import SMTPLIB for Sending Email
import smtplib
import pywhatkit as kit

# Get Engine for Voice
engine = pyttsx3.init('sapi5')
# Set Engine Property
voices = engine.getProperty('voices')

# print(voices)

# Voices 0 for Gents Voice
engine.setProperty('voice', voices[0].id)

# Voices 1 for Girls Voice
# engine.setProperty('voice',voices[1].id)

# Speak Func for Speaking


def speak(audio):
    # Saying the Audio
    engine.say(audio)
    engine.runAndWait()

# Wish Me FUnc for Wishing the User


def wishMe():
    # Take Time
    hour = int(datetime.datetime.now().hour)
    # Check the Hour for Greeting the User
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir , I am your assistant!! How can I help you?")

# Take Command Func for Taking Command from User


def takeCommand():
    # Create Recognizer Object
    r = sr.Recognizer()
    # Take Input from Microphone
    with sr.Microphone() as source:
        print("\nListining...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        # Listen the Audio
        audio = r.listen(source)

    # After Listining
    try:
        print("Recognizing...")
        # Recognize the Audio by Google
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        # print(e)

        print("`~` Say that again please `~`")
        return "None"

    # Return that Query
    return query

# SendEmail Func for Sending EMail


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mygmail', 'gmail-password')
    server.sendmail('mygmail', to, content)
    server.close()


# Main
if __name__ == "__main__":
    # Call Wish Me Func
    wishMe()
    while True:
        # Take the User Query
        query = takeCommand().lower()

        try:
            # Searching from Wikipedia
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print("**** According to Wikipedia : ****")
                speak("According to wikipedia")
                print(results)
                speak(results)
            # Open Youtube
            elif 'open youtube' in query:
                print("Opening Youtube ...\n")
                speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com")
            # Open Google
            elif 'open google' in query:
                print("Opening Google ...\n")
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            # Play Song or Video from YouTube
            elif 'play song' in query or 'play video' in query:
                # base_url = "https://www.youtube.com/results?search_query="
                # query_url = base_url+query
                # webbrowser.open(query_url)
                # Play the Song or Video
                print("Opening through Youtube ...\n")
                speak("Opening through Youtube")
                kit.playonyt(query)
            # Play Music from my PC
            elif 'play music from my pc' in query:
                music_dir = "D:\\Music"
                songs = os.listdir(music_dir)
                # print(songs)
                val = random.randint(0, len(songs))
                os.startfile(os.path.join(music_dir, songs[val]))
                print("** Playing", songs[val], "**\n")
                speak(f"Playing{songs[val]}")
            # Check Time
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Sir, The time is : {strTime}")
                speak(f"Sir, The time is : {strTime}")
            # Open VS Code
            elif 'open code' in query:
                path = "C:\\Users\\shila\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
            elif "email to abcd" in query:
                try:
                    speak("What should i say")
                    content = takeCommand()
                    to = 'shilajit.acharjee.ciem.cse@gmail.com'
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir...")
            # Comments
            elif "thanks" in query or "thank you" in query or "welcome" in query or "great answer" in query or "you are very good" in query:
                print("Thanks for Your Response. You're also welcome. If you have any more questions or need further assistance in the future, feel free to ask. Happy coding!")
                speak("Thanks for Your Response You're also welcome If you have any more questions or need further assistance in the future, feel free to ask. Happy coding")
            # Searching Anything in Google
            elif "none" not in query:
                base_url = "https://www.google.com/search?q="
                query_url = base_url+query
                webbrowser.open(query_url)

        except Exception as e:
            print(e)
            print("`~` Sorry Sir ...Please Try Again `~`")
            speak("Sorry Sir ...Please Try Again")