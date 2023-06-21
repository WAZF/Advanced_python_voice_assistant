import os
import speech_recognition as sr
import pyttsx3

# initialize text-to-speech engine
engine = pyttsx3.init()

def search_files(search_term, directory_path, file_type=None):
    matching_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if search_term in file and (not file_type or file.endswith(file_type)):
                matching_files.append(os.path.join(root, file))
    return matching_files

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    engine.say("What would you like to search for?")
    engine.runAndWait()
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    search_term = r.recognize_google(audio)
    print(f"You said: {search_term}")
    engine.say(f"Searching for files containing {search_term}.")
    engine.runAndWait()
    # obtain audio from the microphone for directory path
    with sr.Microphone() as source:
        print("Listening...")
        engine.say("In which directory should I search?")
        engine.runAndWait()
        audio = r.listen(source)
    directory_path = r.recognize_google(audio)
    print(f"Directory path: {directory_path}")
    # obtain audio from the microphone for file type
    with sr.Microphone() as source:
        print("Listening...")
        engine.say("Do you want to filter the results by file type?")
        engine.runAndWait()
        audio = r.listen(source)
    response = r.recognize_google(audio)
    if "yes" in response.lower():
        with sr.Microphone() as source:
            print("Listening...")
            engine.say("What file type do you want to filter by?")
            engine.runAndWait()
            audio = r.listen(source)
        file_type = r.recognize_google(audio)
        print(f"Filtering by file type: {file_type}")
    else:
        file_type = None
    matching_files = search_files(search_term, directory_path, file_type)
    if matching_files:
        engine.say(f"I found {len(matching_files)} files.")
        engine.runAndWait()
        print("Matching files:")
        for file_path in matching_files:
            print(file_path)
            engine.say(file_path)
            engine.runAndWait()
    else:
        engine.say("No matching files found.")
        engine.runAndWait()
except sr.UnknownValueError:
    print("Could not understand audio")
    engine.say("Sorry, I didn't catch that.")
    engine.runAndWait()
except sr.RequestError as e:
    print(f"Error: {e}")
    engine.say("Sorry, there was an error with the speech recognition.")
    engine.runAndWait()
