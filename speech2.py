import speech_recognition as sr
import webbrowser as wb
import pyaudio as audio
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
with sr.Microphone() as source:
    print('search google')
    print('speack now')
    audio=r3.listen(source)
if 'search' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://google.com/search?q='
    with sr.Microphone() as source:
        print('search ur query')
        audio=r2.listen(source)
        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('Failed'.format(e))
