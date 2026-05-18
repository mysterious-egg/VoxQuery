# speech_utils.py

import speech_recognition as sr


def recognize_speech():
    """
    Capture microphone audio
    Convert speech -> text

    Returns:
    {
        "success": bool,
        "text": recognized text,
        "error": error message
    }
    """

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            # Show microphone calibration
            print("Adjusting for noise...")

            # Reduce ambient noise impact
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            # -----------------------------
            # Speech tuning
            # -----------------------------

            # Allow slightly longer pauses
            recognizer.pause_threshold = 1.5

            # Minimum speaking duration
            recognizer.phrase_threshold = 0.3

            # Keep a little audio before speech begins
            recognizer.non_speaking_duration = 0.8

            print("Listening...")

            audio = recognizer.listen(

                source,

                # Wait max 5 sec for user to start
                timeout=5,

                # Allow long sentence
                phrase_time_limit=20
            )

        print("Recognizing...")

        text = recognizer.recognize_google(
            audio
        )

        return {

            "success": True,
            "text": text,
            "error": None
        }

    except sr.WaitTimeoutError:

        return {
            "success": False,
            "text": "",
            "error": "No speech detected."
        }

    except sr.UnknownValueError:

        return {
            "success": False,
            "text": "",
            "error": "Could not understand audio."
        }

    except sr.RequestError:

        return {
            "success": False,
            "text": "",
            "error": "Speech service unavailable."
        }

    except OSError:

        return {
            "success": False,
            "text": "",
            "error": "Microphone not detected."
        }

    except Exception as e:

        return {
            "success": False,
            "text": "",
            "error": f"Error: {str(e)}"
        }