from transformers import AutoTokenizer
from .base import BaseTokenizer


class UnigramTokenizer(BaseTokenizer):
    def __init__(self):
        # T5 uses SentencePiece Unigram model
        self.tokenizer = AutoTokenizer.from_pretrained("t5-small")

    def tokenize(self, text: str):
        return self.tokenizer.tokenize(text)

    def encode(self, text: str):
        return self.tokenizer.encode(text, add_special_tokens=False)