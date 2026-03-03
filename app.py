import streamlit as st
from services.tokenizer_service import TokenizerService
from services.stats import get_stats
from utils.colorizer import colorize_tokens

st.set_page_config(page_title="Tokenization Visualizer", layout="centered")

# ---- Custom Styling ----
st.markdown("""
    <style>
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #2A2D30 0%, #1E2124 100%) !important;
        font-family: 'Source Sans 3', 'Segoe UI', sans-serif !important;
    }
    .main .block-container { padding: 2rem; max-width: 800px; }
    .main-title { font-size: 1.5rem; font-weight: 600; color: #E8EAED; margin-bottom: 1.5rem; }
    .section-title { font-size: 0.9rem; font-weight: 600; color: #9CA3AF; margin-top: 1.5rem; margin-bottom: 0.5rem; }
    .stTextArea textarea { background: rgba(45, 48, 52, 0.9) !important; border: 1px solid rgba(255,255,255,0.1) !important; color: #E8EAED !important; border-radius: 8px !important; }
    [data-testid="stMetric"] { background: rgba(45, 48, 52, 0.9) !important; border: 1px solid rgba(255,255,255,0.08) !important; border-radius: 8px !important; }
    .stCheckbox label { color: #D1D5DB !important; }
    [data-testid="stSelectbox"] { color: #E8EAED !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Tokenization Visualizer</div>', unsafe_allow_html=True)

service = TokenizerService()
text = st.text_area("Input", height=100, placeholder="Enter text to tokenize", label_visibility="collapsed")
tokenizer_name = st.selectbox("Method", service.list_tokenizers())
show_ids = st.checkbox("Show token IDs", value=False)
run = st.button("Tokenize")

if run and text:
    try:
        tokenizer = service.get_tokenizer(tokenizer_name)
        tokens = tokenizer.tokenize(text)
        ids = tokenizer.encode(text)
        stats = get_stats(text, tokens)

        st.markdown('<div class="section-title">Statistics</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.metric("Characters", stats["num_characters"])
        c2.metric("Tokens", stats["num_tokens"])

        st.markdown('<div class="section-title">Output</div>', unsafe_allow_html=True)
        st.markdown(colorize_tokens(tokens), unsafe_allow_html=True)

        if show_ids:
            st.markdown('<div class="section-title">Token IDs</div>', unsafe_allow_html=True)
            st.code(", ".join(map(str, ids)), language=None)

    except Exception as e:
        st.error(f"Tokenization failed: {e}")
