from .base import BaseTokenizer


class CharacterTokenizer(BaseTokenizer):
    def tokenize(self, text: str):
        return list(text)

    def encode(self, text: str):
        tokens = self.tokenize(text)
        return list(range(len(tokens)))