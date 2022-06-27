import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import smtplib
import spotify


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12 :
        speak("Good Morning, Sir!")

    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon, Sir!")

    else:
        speak("Good Evening, Sir!")

    speak("I am Jarvis and I work as 100%. Please tell me how may I help you Sir! ")

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}/n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-mail', 'mail-password')
    server.sendmail('your-mail', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'hello' in query:
            speak("Hello Sir! I'm very well. I hope you are well too ")

        elif 'jarvis' in query:
            speak("Yes Sir!")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open twitch' in query:
            webbrowser.open("twitch.tv")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'spotify' in query:
            speak('Searching Spotify...')
            query = query.replace("spotify", "")
            if 'song' in query:
                query = query.replace("song", "")
                spotify.findTrack(query)


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Who do you want me to send?")
                to = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")

        elif 'close yourself' in query:
            speak("Well Sir! I turn myself off. I hope I could serve you well. Goodbye Sir!")
            break


