from transformers import AutoTokenizer
from .base import BaseTokenizer


class WordPieceTokenizer(BaseTokenizer):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    def tokenize(self, text: str):
        return self.tokenizer.tokenize(text)

    def encode(self, text: str):
        return self.tokenizer.encode(text, add_special_tokens=False)