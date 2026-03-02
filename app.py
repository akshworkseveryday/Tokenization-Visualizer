import streamlit as st
from services.tokenizer_service import TokenizerService
from services.stats import get_stats
from utils.colorizer import colorize_tokens

st.set_page_config(page_title="Tokenization Visualizer", layout="wide")

# ---- Custom Styling ----
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #F8F9FA;
    }

    .main-title {
        font-size: 36px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #2C3E50;
    }

    .section-title {
        font-size: 22px;
        font-weight: 500;
        margin-top: 30px;
        color: #34495E;
    }

    textarea {
        font-size: 16px !important;
    }

    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown('<div class="main-title">Tokenization Visualizer</div>', unsafe_allow_html=True)

text = st.text_area("Enter your sentence", height=120)

service = TokenizerService()

tokenizer_name = st.selectbox(
    "Select Tokenization Method",
    service.list_tokenizers()
)

show_ids = st.checkbox("Show Token IDs")

if text:
    tokenizer = service.get_tokenizer(tokenizer_name)

    tokens = tokenizer.tokenize(text)
    ids = tokenizer.encode(text)

    stats = get_stats(text, tokens)

    st.markdown('<div class="section-title">Statistics</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    col1.metric("Characters", stats["num_characters"])
    col2.metric("Tokens", stats["num_tokens"])

    st.markdown('<div class="section-title">Tokenized Output</div>', unsafe_allow_html=True)
    st.markdown(colorize_tokens(tokens), unsafe_allow_html=True)

    if show_ids:
        st.markdown('<div class="section-title">Token IDs</div>', unsafe_allow_html=True)
        st.write(ids)