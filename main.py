import streamlit as st

# 表示したいPythonファイルのパス
file_path = "sample.py"  # ここに表示したいファイル名を指定

st.title("コード共有")
st.header("ファイル名")
filename="test.py"
st.write(filename)

try:
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    st.code(code, language="python")  # シンタックスハイライト付きで表示
except FileNotFoundError:
    st.error(f"{file_path} が見つかりません")