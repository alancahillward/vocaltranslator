import speech_recognition
import pyttsx3
import goslate

recognizer = speech_recognition.Recognizer()

while True:
    gs = goslate.Goslate()
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            ans = gs.translate(text, "fr")
            print(f"Recognized {ans}")

    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue


