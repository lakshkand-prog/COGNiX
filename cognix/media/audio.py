"""Local speech synthesis helpers powered by pyttsx3."""
import pyttsx3


def speak_text(text):
    """Speak text aloud using the default system voice."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speak_to_file(text, output_path, rate=165):
    """Render speech into a WAV file for playback in the COGNiX media shelf."""
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.save_to_file(text, output_path)
    engine.runAndWait()
