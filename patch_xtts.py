try:
    from TTS.tts.layers.xtts.gpt import GPT2InferenceModel
    GPT2InferenceModel._validate_model_class = lambda self: None

    from TTS.tts.layers.xtts import stream_generator
    from TTS.tts.layers.xtts.stream_generator import GenerationConfig

    _orig_generate = stream_generator.StreamGenerator.generate
    def _patched_generate(self, *args, **kwargs):
        if getattr(self, "generation_config", None) is None:
            self.generation_config = GenerationConfig()
        return _orig_generate(self, *args, **kwargs)
    stream_generator.StreamGenerator.generate = _patched_generate
except Exception:
    # If TTS isn't installed or API changed, skip patching
    pass
