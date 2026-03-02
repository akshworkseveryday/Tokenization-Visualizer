from my_tokenizers.word import WordTokenizer
from my_tokenizers.character import CharacterTokenizer
from my_tokenizers.bpe import BPETokenizer
from my_tokenizers.wordpiece import WordPieceTokenizer
from my_tokenizers.unigram import UnigramTokenizer


class TokenizerService:
    def __init__(self):
        self.tokenizers = {
            "Word": WordTokenizer(),
            "Character": CharacterTokenizer(),
            "BPE (GPT-2)": BPETokenizer(),
            "WordPiece (BERT)": WordPieceTokenizer(),
            "Unigram (T5)": UnigramTokenizer(),
        }

    def list_tokenizers(self):
        return list(self.tokenizers.keys())

    def get_tokenizer(self, name):
        return self.tokenizers.get(name)