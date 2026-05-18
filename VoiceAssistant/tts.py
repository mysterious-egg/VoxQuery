import pyttsx3

def speak(text):

    try:

        if not text:
            return

        # Create fresh engine each call
        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            170
        )

        engine.setProperty(
            "volume",
            1.0
        )

        engine.say(
            str(text)
        )

        engine.runAndWait()

        engine.stop()

    except Exception as e:

        print(
            f"TTS Error: {e}"
        )