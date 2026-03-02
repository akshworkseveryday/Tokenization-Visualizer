from .base import BaseTokenizer


class WordTokenizer(BaseTokenizer):
    def tokenize(self, text: str):
        return text.split()

    def encode(self, text: str):
        tokens = self.tokenize(text)
        return list(range(len(tokens)))