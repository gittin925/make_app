import streamlit as st
from gensim.summarization import summarize

st.title("📝 テキスト要約アプリ")

# 入力テキスト
text = st.text_area("要約したい文章を入力してください", height=200)

# 要約ボタン
if st.button("要約する"):
    if text.strip():
        try:
            summary = summarize(text, ratio=0.3)  # 全体の30%に要約
            if summary:
                st.subheader("🔹 要約結果")
                st.write(summary)
            else:
                st.warning("文章が短すぎるため要約できませんでした。")
        except ValueError:
            st.error("文章が短すぎます。もう少し長い文章を入力してください。")
    else:
        st.warning("文章を入力してください。")