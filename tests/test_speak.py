import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import speak

class DummyStream:
    def __init__(self):
        self.chunks = []
    def feed(self, chunk):
        self.chunks.append(chunk)
    def play_async(self):
        pass

def test_speak_text_chunks():
    dummy = DummyStream()
    speak.stream = dummy
    speak.speak_text("abc", chunk_size=2, delay=0)
    assert dummy.chunks == ["ab", "c"]
