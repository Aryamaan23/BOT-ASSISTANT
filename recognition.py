import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('Hey, I am python bot')

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.6
        audio=r.listen(source)

        try:
            ask=r.recognize_google(audio,language='en-us')
            print(f"You said : {ask}")
        except:
            print("Say that again...")
            return ""
        return ask

if __name__ == "__main__":
    while True:
        query=command().lower()
        print(query)

        try:

            if 'tom' in query:
                query=query.replace('tom','')
                client=wolframalpha.Client("8RWV97-9W8GX44QJJ")
                res=client.query(query)
                ans=next(res.results).text
                print(ans)
                speak(ans)

        except Exception:
            try:
                query=query.replace('tom','')
                results=wikipedia.summary(query,sentences=2)
                print(results)
                speak(results)

            except Exception:
                try:
                    query=query.replace('tom','')
                    webbrowser.open('https://google.com/?#q=' + query)

                except:
                    print("It is weird but I got nothing try re-running the program")
                    speak("It is weird but I got nothing try re-running the program")



