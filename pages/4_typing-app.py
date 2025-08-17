import streamlit as st
import random
import string
import difflib

# --------------------
# 文字列生成関数
# --------------------
def generate_random_string(length=60):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# --------------------
# セッション初期化
# --------------------
if "target" not in st.session_state:
    st.session_state.target = generate_random_string()

# --------------------
# タイトル
# --------------------
st.title("🎯 タイピング練習アプリ")

st.write("出題された文字列と同じ文字を入力してください。")

# 出題文字列
st.subheader("問題:")
st.code(st.session_state.target)

# 入力欄
user_input = st.text_input("入力してください:")

# 一致率の計算
if user_input:
    ratio = difflib.SequenceMatcher(None, st.session_state.target, user_input).ratio()
    st.write(f"✅ 一致率: {ratio:.2%}")
    if user_input == st.session_state.target:
        st.success("完璧に一致しました！🎉")

# 新しい問題を出すボタン
if st.button("次の問題"):
    st.session_state.target = generate_random_string()
    st.rerun()