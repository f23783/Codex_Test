# speak.py

import typing, typing_extensions
for name in ("ParamSpec", "Concatenate"):
    if not hasattr(typing, name):
        setattr(typing, name, getattr(typing_extensions, name))




# speak.py
import os, multiprocessing, time
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"
if __name__ == "__main__":
    import patch_xtts

    multiprocessing.freeze_support()

    from RealtimeTTS import TextToAudioStream, CoquiEngine

    # VITS model still works, but we won't stream it chunk-by-chunk:
    engine = CoquiEngine(model_name="tts_models/en/vctk/vits")
    stream = TextToAudioStream(engine)


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




    greeting = "Hello, this is a test of the real-time text to speech streaming system."
    print("Speaking:", greeting)
    speak_text(greeting)

    # wait for any remaining audio to finish
    time.sleep(2)
    print("Done.")


  
