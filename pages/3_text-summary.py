import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

st.title("📝 テキスト要約アプリ (sumy版)")

# 入力テキスト
text = st.text_area("要約したい文章を入力してください", height=200)

# 要約する文の数を指定
sent_count = st.slider("要約する文の数", min_value=1, max_value=10, value=3)

# 要約ボタン
if st.button("要約する"):
    if text.strip():
        try:
            parser = PlaintextParser.from_string(text, Tokenizer("japanese"))  # 日本語
            summarizer = LexRankSummarizer()
            summary = summarizer(parser.document, sent_count)

            st.subheader("🔹 要約結果")
            for sentence in summary:
                st.write("-", sentence)

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("文章を入力してください。")