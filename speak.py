# speak.py

import typing, typing_extensions
for name in ("ParamSpec", "Concatenate"):
    if not hasattr(typing, name):
        setattr(typing, name, getattr(typing_extensions, name))




# speak.py
import os, multiprocessing, time
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"


def speak_text(text: str, chunk_size: int = 50, delay: float = 0.1):
    """
    Splits `text` into chunks of ~chunk_size characters,
    feeds each to the TTS stream, and plays it immediately.
    """
    for i in range(0, len(text), chunk_size):
        chunk = text[i : i + chunk_size]
        stream.feed(chunk)
        stream.play_async()
        time.sleep(delay)  # give the audio thread time to start

if __name__ == "__main__":
    if os.environ.get("RUN_SPEECH") != "1":
        print("RUN_SPEECH=1 is required to run TTS demo.")
        raise SystemExit(0)
    try:
        import patch_xtts
    except Exception:
        # Skip patching if dependencies are missing
        pass

    multiprocessing.freeze_support()

    try:
        from RealtimeTTS import TextToAudioStream, CoquiEngine
    except ModuleNotFoundError:
        print("RealtimeTTS is not installed.")
        raise SystemExit(1)

    # Use a smaller model to avoid long downloads during tests
    engine = CoquiEngine(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    stream = TextToAudioStream(engine)


    greeting = "Hello, this is a test of the real-time text to speech streaming system."
    print("Speaking:", greeting)
    speak_text(greeting)

    # wait for any remaining audio to finish
    time.sleep(2)
    print("Done.")


  
