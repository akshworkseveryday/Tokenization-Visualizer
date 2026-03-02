from transformers import AutoTokenizer
from .base import BaseTokenizer


class BPETokenizer(BaseTokenizer):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    def tokenize(self, text: str):
        return self.tokenizer.tokenize(text)

    def encode(self, text: str):
        return self.tokenizer.encode(text, add_special_tokens=False)