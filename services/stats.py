def get_stats(text, tokens):
    """Compute tokenization statistics."""
    return {
        "num_characters": len(text),
        "num_tokens": len(tokens),
    }