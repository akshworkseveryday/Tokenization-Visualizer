from .base import BaseTokenizer


class WordTokenizer(BaseTokenizer):
    def tokenize(self, text: str):
        return text.split()

    def encode(self, text: str):
        """Encode using vocabulary: each unique token maps to a unique ID (industry standard)."""
        tokens = self.tokenize(text)
        vocab = {t: i for i, t in enumerate(sorted(set(tokens)))}
        return [vocab[t] for t in tokens]