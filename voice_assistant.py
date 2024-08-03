#Voice Assistant:
# Import the required module for text-to-speech conversion
import pyttsx3

try:
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Define the text to be spoken
    text_to_speak = 'Hello sir, how may I help you, sir.'

    # Use the engine to say the text
    engine.say(text_to_speak)

    # Process the speech commands and wait until speaking is finished
    engine.runAndWait()

except Exception as e:
    print(f"An error occurred: {e}")
