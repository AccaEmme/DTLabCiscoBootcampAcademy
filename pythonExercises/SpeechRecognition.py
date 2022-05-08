import speech_recognition as sr

r = sr.Recognizer();
with sr.Microphone() as source:
    print("SPEAK....");
    audio = r.listener(source)
    
print(r.recognize_google(audio));
