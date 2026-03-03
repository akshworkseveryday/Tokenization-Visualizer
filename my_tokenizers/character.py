from .base import BaseTokenizer


class CharacterTokenizer(BaseTokenizer):
    def tokenize(self, text: str):
        return list(text)

    def encode(self, text: str):
        """Encode using vocabulary: each unique character maps to a unique ID (industry standard)."""
        tokens = self.tokenize(text)
        vocab = {t: i for i, t in enumerate(sorted(set(tokens)))}
        return [vocab[t] for t in tokens]