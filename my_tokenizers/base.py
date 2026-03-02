class BaseTokenizer:
    def tokenize(self, text: str):
        raise NotImplementedError

    def encode(self, text: str):
        raise NotImplementedError